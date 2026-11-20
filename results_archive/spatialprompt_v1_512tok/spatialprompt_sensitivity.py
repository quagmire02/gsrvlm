"""spatialprompt: archive the 2048-token rerun, restore the 512-token original, and write
results/spatialprompt_sensitivity.json (MRA with vs without the looping answers, paired
vs baseline on the same qids). Run with cwd = repo root."""
import json
import os
import shutil

import numpy as np

A = "results_archive/spatialprompt_v1_512tok"
cur = "results/spatialprompt.s0.jsonl"
read = lambda p: [json.loads(l) for l in open(p, encoding="utf-8")]

tq = set(json.load(open(f"{A}/truncated_qids.json")))
rerun = [r for r in read(cur) if r["qid"] in tq]
assert len(rerun) == 22, len(rerun)
looped_2048 = sum("final answer" not in r["raw_answer"].lower() for r in rerun)
with open(f"{A}/rerun_2048tok_truncated_only.jsonl", "w", encoding="utf-8") as f:
    f.writelines(json.dumps(r) + "\n" for r in rerun)
shutil.copy(f"{A}/spatialprompt.s0.jsonl", cur)          # restore the 512-token original

orig = read(cur)
assert len(orig) == 300
base = {r["qid"]: r for r in read("results/baseline.s0.jsonl")}
out = {"n_total": len(orig), "n_looping": len(tq), "looping_still_at_2048_tokens": looped_2048,
       "tasks": {}}
for t in sorted({r["task"] for r in orig}):
    rows = [r for r in orig if r["task"] == t]
    clean = [r for r in rows if r["qid"] not in tq]
    m = lambda rs: float(np.mean([r["mra"] for r in rs]))
    out["tasks"][t] = {
        "n": len(rows), "n_looping": len(rows) - len(clean),
        "mra_all": m(rows), "mra_base_all": m([base[r["qid"]] for r in rows]),
        "mra_no_loop": m(clean), "mra_base_no_loop": m([base[r["qid"]] for r in clean]),
    }
    o = out["tasks"][t]
    o["delta_all"] = o["mra_all"] - o["mra_base_all"]
    o["delta_no_loop"] = o["mra_no_loop"] - o["mra_base_no_loop"]
json.dump(out, open("results/spatialprompt_sensitivity.json", "w"), indent=1)
print(json.dumps(out, indent=1))
