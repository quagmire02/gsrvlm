"""Questions, frames and the scene split. Everything downstream reads the files
written here, so the VLM and MapAnything see exactly the same 16 frames."""

import json
import os
import re

import numpy as np

from . import TASKS

N_FRAMES = 16
FRAME_SIDE = 640  # longest side of saved JPEGs; models resize further


def scene_key(dataset, scene_name):
    return f"{dataset}__{scene_name}"


def read_jsonl(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    pass  # a line cut off by a killed session
    return rows


def load_questions(path):
    return read_jsonl(path)


def load_split(path):
    with open(path) as f:
        return json.load(f)


def frame_paths(frames_dir, scene_id):
    d = os.path.join(frames_dir, scene_id)
    if not os.path.isdir(d):
        return []
    return sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".jpg"))


# ---------------------------------------------------------------- questions

def build_questions(hf_repo="nyu-visionx/VSI-Bench", config="full"):
    from datasets import load_dataset
    ds = load_dataset(hf_repo, config, split="test")
    rows = []
    for r in ds:
        if r["question_type"] not in TASKS:
            continue
        try:
            gt = float(r["ground_truth"])
        except (TypeError, ValueError):
            continue
        rows.append({
            "qid": str(r["id"]),
            "scene_id": scene_key(r["dataset"], r["scene_name"]),
            "dataset": r["dataset"],
            "scene_name": r["scene_name"],
            "task": r["question_type"],
            "question": r["question"],
            "gt": gt,
        })
    return rows


# ---------------------------------------------------------------- split

def make_split(scene_ids, datasets, frac_train=0.6, seed=0):
    """Scene-disjoint split, stratified by source dataset."""
    rng = np.random.default_rng(seed)
    train, ev = [], []
    for d in sorted(set(datasets.values())):
        s = sorted(x for x in scene_ids if datasets[x] == d)
        rng.shuffle(s)
        k = int(round(frac_train * len(s)))
        train += s[:k]
        ev += s[k:]
    return {"seed": seed, "frac_train": frac_train,
            "train": sorted(train), "eval": sorted(ev)}


# ---------------------------------------------------------------- frames

def extract_frames(video_path, out_dir, n=N_FRAMES, side=FRAME_SIDE):
    """Save n uniformly spaced frames as 00.jpg..(n-1).jpg. Returns metadata."""
    import cv2
    cap = cv2.VideoCapture(video_path)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = float(cap.get(cv2.CAP_PROP_FPS) or 0)
    frames = []
    if total > 0:
        idx = np.linspace(0, total - 1, n).round().astype(int)
        for i in idx:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(i))
            ok, fr = cap.read()
            if not ok:
                frames = []
                break
            frames.append(fr)
    if len(frames) != n:
        # Seeking failed (bad frame count / codec): decode everything once.
        cap.release()
        cap = cv2.VideoCapture(video_path)
        allf = []
        while True:
            ok, fr = cap.read()
            if not ok:
                break
            allf.append(fr)
        total = len(allf)
        if total == 0:
            raise RuntimeError(f"no frames decoded from {video_path}")
        idx = np.linspace(0, total - 1, n).round().astype(int)
        frames = [allf[i] for i in idx]
    cap.release()

    os.makedirs(out_dir, exist_ok=True)
    for j, fr in enumerate(frames):
        h, w = fr.shape[:2]
        s = side / max(h, w)
        if s < 1:
            fr = cv2.resize(fr, (round(w * s), round(h * s)), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(out_dir, f"{j:02d}.jpg"), fr, [cv2.IMWRITE_JPEG_QUALITY, 92])
    meta = {"total_frames": total, "fps": fps, "indices": [int(i) for i in idx], "side": side}
    with open(os.path.join(out_dir, "meta.json"), "w") as f:
        json.dump(meta, f)
    return meta


# ---------------------------------------------------------------- anchors

# Greedy prefix: take the object after the LAST "of the". VSI-Bench phrases these as
# "...longest dimension (length, width, or height) of the <obj>, measured in centimeters",
# and a non-greedy match from the first "of the" returned the whole phrase, which
# broke the "anchor not named in the question" check for distance questions.
_SIZE_OBJ = re.compile(r".*\bof the (.+?),?\s+measured in centimet", re.I)


def size_object(question):
    m = _SIZE_OBJ.search(question)
    return m.group(1).strip() if m else None


def anchor_table(questions):
    """For each question, a ground-truth object size from the SAME scene about a
    DIFFERENT object (one not named in the question). qid -> (object, cm)."""
    by_scene = {}
    for q in questions:
        if q["task"] == "object_size_estimation":
            obj = size_object(q["question"])
            if obj:
                by_scene.setdefault(q["scene_id"], []).append((q["qid"], obj, q["gt"]))
    out = {}
    for q in questions:
        cands = sorted(by_scene.get(q["scene_id"], []), key=lambda t: int(t[0]) if t[0].isdigit() else t[0])
        text = q["question"].lower()
        for qid, obj, gt in cands:
            if qid == q["qid"] or obj.lower() in text:
                continue
            out[q["qid"]] = (obj, float(gt))
            break
    return out
