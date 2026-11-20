## Table 1: MRA (x100) on eval scenes; delta is paired vs baseline on the same questions

Compression slope = slope of log(pred) on log(gt): 1 = proportional, 0 = constant answer. 'base' = baseline slope on the same questions.

| condition | task | n | MRA [95% CI] | Δ vs base [95% CI] | slope [95% CI] | slope base | unparseable |
|---|---|---|---|---|---|---|---|
| baseline | Abs. dist. | 334 | 44.7 [40.2, 49.2] | – | 0.59 [0.49, 0.69] | 0.59 | 1.5 |
| baseline | Obj. size | 387 | 72.8 [69.8, 75.6] | – | 0.88 [0.84, 0.93] | 0.88 | 0.3 |
| baseline | Room size | 115 | 50.3 [44.0, 56.6] | – | 0.52 [0.46, 0.58] | 0.52 | 0.0 |
| placebo | Abs. dist. | 334 | 44.5 [40.2, 48.8] | -0.2 [-1.7, 1.1] | 0.54 [0.44, 0.65] | 0.59 | 0.6 |
| placebo | Obj. size | 387 | 72.5 [69.5, 75.4] | -0.3 [-1.6, 0.8] | 0.90 [0.85, 0.94] | 0.88 | 0.8 |
| placebo | Room size | 115 | 49.9 [43.6, 56.2] | -0.4 [-2.5, 1.4] | 0.52 [0.46, 0.59] | 0.52 | 0.0 |
| spatialprompt | Abs. dist. | 100 | 36.2 [30.1, 42.7] | -10.4 [-16.8, -3.4] | 0.38 [0.24, 0.50] | 0.59 | 2.0 |
| spatialprompt | Obj. size | 100 | 47.8 [40.7, 54.8] | -24.6 [-32.3, -17.0] | 0.50 [0.09, 0.94] | 0.81 | 10.0 |
| spatialprompt | Room size | 100 | 31.0 [25.3, 37.1] | -19.8 [-28.9, -10.5] | 0.68 [0.47, 0.85] | 0.51 | 1.0 |
| shuffled | Abs. dist. | 334 | 44.5 [40.0, 49.1] | -0.2 [-2.1, 1.7] | 0.55 [0.46, 0.64] | 0.59 | 0.9 |
| shuffled | Obj. size | 387 | 72.4 [69.3, 75.1] | -0.5 [-1.5, 0.4] | 0.88 [0.84, 0.93] | 0.88 | 0.3 |
| shuffled | Room size | 115 | 50.1 [44.4, 55.8] | -0.3 [-3.0, 2.3] | 0.54 [0.48, 0.60] | 0.52 | 0.0 |
| learned | Abs. dist. | 334 | 43.7 [39.1, 48.2] | -1.0 [-2.8, 0.9] | 0.54 [0.45, 0.64] | 0.59 | 0.9 |
| learned | Obj. size | 387 | 72.3 [69.4, 75.1] | -0.5 [-1.4, 0.3] | 0.89 [0.84, 0.93] | 0.88 | 0.5 |
| learned | Room size | 115 | 51.7 [45.5, 57.6] | 1.3 [-2.1, 5.1] | 0.56 [0.50, 0.63] | 0.52 | 0.0 |
| teacher | Abs. dist. | 334 | 45.0 [40.6, 49.3] | 0.3 [-1.2, 2.0] | 0.55 [0.46, 0.64] | 0.59 | 0.9 |
| teacher | Obj. size | 387 | 72.1 [69.2, 74.9] | -0.7 [-1.7, 0.2] | 0.89 [0.84, 0.93] | 0.88 | 0.5 |
| teacher | Room size | 115 | 51.8 [46.1, 57.7] | 1.5 [-1.7, 4.8] | 0.57 [0.50, 0.63] | 0.52 | 0.0 |
| teacher_ext | Abs. dist. | 334 | 43.5 [39.0, 47.9] | -1.2 [-3.9, 1.5] | 0.58 [0.49, 0.67] | 0.59 | 0.9 |
| teacher_ext | Obj. size | 387 | 72.6 [69.4, 75.2] | -0.3 [-1.4, 0.7] | 0.89 [0.84, 0.93] | 0.88 | 0.5 |
| teacher_ext | Room size | 115 | 50.5 [44.8, 56.4] | 0.2 [-2.9, 3.1] | 0.53 [0.46, 0.59] | 0.52 | 0.0 |
| anchor | Abs. dist. | 306 | 44.2 [39.4, 49.0] | -0.8 [-3.1, 1.7] | 0.49 [0.39, 0.58] | 0.55 | 0.7 |
| anchor | Obj. size | 369 | 72.3 [69.2, 75.3] | -0.1 [-1.3, 0.9] | 0.88 [0.83, 0.92] | 0.88 | 0.3 |
| anchor | Room size | 113 | 51.9 [45.4, 58.4] | 2.3 [-0.5, 5.1] | 0.56 [0.50, 0.62] | 0.52 | 0.0 |
| anchor_k0.5 | Abs. dist. | 306 | 43.2 [38.9, 47.9] | -1.8 [-3.9, 0.4] | 0.48 [0.38, 0.57] | 0.55 | 0.7 |
| anchor_k0.5 | Obj. size | 369 | 70.6 [67.5, 73.8] | -1.8 [-3.0, -0.8] | 0.86 [0.81, 0.91] | 0.88 | 0.3 |
| anchor_k0.5 | Room size | 113 | 51.2 [45.6, 57.2] | 1.7 [-0.7, 4.3] | 0.55 [0.49, 0.61] | 0.52 | 0.0 |
| anchor_k0.71 | Abs. dist. | 306 | 43.5 [39.2, 48.1] | -1.6 [-3.5, 0.4] | 0.48 [0.38, 0.57] | 0.55 | 0.7 |
| anchor_k0.71 | Obj. size | 369 | 70.9 [67.9, 73.9] | -1.5 [-2.8, -0.4] | 0.87 [0.82, 0.91] | 0.88 | 0.3 |
| anchor_k0.71 | Room size | 113 | 51.8 [45.2, 58.1] | 2.2 [-0.4, 5.1] | 0.54 [0.48, 0.61] | 0.52 | 0.0 |
| anchor_k1.41 | Abs. dist. | 306 | 44.6 [40.0, 49.4] | -0.5 [-2.6, 1.6] | 0.49 [0.39, 0.58] | 0.55 | 0.7 |
| anchor_k1.41 | Obj. size | 369 | 72.2 [69.4, 75.2] | -0.2 [-1.3, 1.0] | 0.88 [0.84, 0.93] | 0.88 | 0.3 |
| anchor_k1.41 | Room size | 113 | 52.1 [45.8, 58.6] | 2.6 [-0.4, 5.6] | 0.56 [0.50, 0.63] | 0.52 | 0.0 |
| anchor_k2 | Abs. dist. | 306 | 44.1 [39.3, 48.9] | -1.0 [-3.2, 1.3] | 0.49 [0.39, 0.58] | 0.55 | 0.7 |
| anchor_k2 | Obj. size | 369 | 72.2 [69.3, 75.1] | -0.2 [-1.4, 1.0] | 0.88 [0.83, 0.93] | 0.88 | 0.5 |
| anchor_k2 | Room size | 113 | 52.9 [46.6, 59.3] | 3.4 [0.2, 6.6] | 0.57 [0.50, 0.63] | 0.52 | 0.0 |
| teacher_k0.5 | Abs. dist. | 334 | 44.7 [40.1, 49.3] | -0.0 [-1.5, 1.4] | 0.55 [0.45, 0.64] | 0.59 | 0.9 |
| teacher_k0.5 | Obj. size | 387 | 71.9 [68.8, 74.7] | -1.0 [-2.0, -0.1] | 0.89 [0.84, 0.93] | 0.88 | 0.3 |
| teacher_k0.5 | Room size | 115 | 50.3 [44.4, 55.8] | 0.0 [-3.2, 3.7] | 0.56 [0.49, 0.62] | 0.52 | 0.0 |
| teacher_k0.71 | Abs. dist. | 334 | 45.7 [41.1, 50.3] | 1.0 [-0.6, 2.9] | 0.54 [0.45, 0.64] | 0.59 | 0.9 |
| teacher_k0.71 | Obj. size | 387 | 72.0 [68.9, 74.8] | -0.8 [-1.8, 0.1] | 0.88 [0.84, 0.93] | 0.88 | 0.3 |
| teacher_k0.71 | Room size | 115 | 51.0 [45.0, 56.6] | 0.7 [-2.5, 4.4] | 0.56 [0.50, 0.63] | 0.52 | 0.0 |
| teacher_k1.41 | Abs. dist. | 334 | 44.8 [40.5, 49.0] | 0.1 [-1.6, 1.8] | 0.55 [0.46, 0.64] | 0.59 | 0.9 |
| teacher_k1.41 | Obj. size | 387 | 72.5 [69.5, 75.4] | -0.3 [-1.3, 0.6] | 0.89 [0.84, 0.93] | 0.88 | 0.3 |
| teacher_k1.41 | Room size | 115 | 51.0 [45.0, 56.9] | 0.6 [-2.0, 3.1] | 0.55 [0.49, 0.61] | 0.52 | 0.0 |
| teacher_k2 | Abs. dist. | 334 | 44.3 [40.1, 48.6] | -0.4 [-2.3, 1.7] | 0.55 [0.46, 0.64] | 0.59 | 0.9 |
| teacher_k2 | Obj. size | 387 | 72.6 [69.6, 75.5] | -0.2 [-1.2, 0.7] | 0.89 [0.84, 0.93] | 0.88 | 0.5 |
| teacher_k2 | Room size | 115 | 50.0 [44.0, 56.1] | -0.3 [-2.4, 1.7] | 0.54 [0.48, 0.60] | 0.52 | 0.0 |
| LOO scene rescale (bound) | Abs. dist. | 301 | 43.4 | -2.3 | – | – | – |
| LOO scene rescale (bound) | Obj. size | 369 | 64.9 | -7.5 | – | – | – |

## Table 2: error decomposition (baseline, all scenes)

| task | n | compression slope [CI] | reverse bound | ICC raw [CI] | ICC resid [CI] | MRA base | global | scene LOO | scene LOO resid |
|---|---|---|---|---|---|---|---|---|---|
| object_abs_distance | 834 | 0.54 [0.48, 0.60] | 1.46 | 0.10 [0.03, 0.18] | 0.13 [0.06, 0.21] | 44.9 | 44.1 | 41.5 | 41.1 |
| object_size_estimation | 953 | 0.87 [0.85, 0.90] | 1.02 | -0.06 [-0.11, 0.00] | -0.08 [-0.13, -0.03] | 72.9 | 72.0 | 64.6 | 65.2 |
| room_size_estimation | 288 | 0.52 [0.48, 0.56] | 0.69 | – | – | – | – | – | – |
| object_abs_distance<2m | 447 | 0.48 [0.34, 0.60] | 3.19 | 0.17 [0.00, 0.35] | 0.25 [0.07, 0.44] | 44.7 | 45.8 | 41.3 | 40.7 |
| object_abs_distance>=2m | 387 | 0.54 [0.40, 0.69] | 3.28 | 0.30 [0.21, 0.39] | 0.29 [0.18, 0.39] | 46.2 | 46.3 | 50.8 | 41.7 |

Cross-task Spearman of scene-mean residuals: object_abs_distance~object_size_estimation: -0.07 (n=221); object_abs_distance~room_size_estimation: 0.24 (n=221); object_size_estimation~room_size_estimation: 0.05 (n=278)

Go/no-go: {'icc_raw': 0.10365622198677592, 'icc_resid': 0.1331688337401867, 'scene_loo_gain_over_base': -0.034464751958224515, 'scene_resid_gain_over_global': -0.029895561357702383, 'decision': 'NO-GO'}

## Table 3: scale elasticity (beta = d log pred / d log k)

| hint | task | n | median beta [CI] | beta<0.2 | beta>0.8 | copy rate @k=1 |
|---|---|---|---|---|---|---|
| teacher | Abs. dist. | 331 | 0.00 [0.00, 0.03] | 96.1 | 0.0 | 10.6 |
| teacher | Obj. size | 386 | -0.00 [-0.00, -0.00] | 99.2 | 0.0 | 4.9 |
| teacher | Room size | 115 | -0.00 [-0.00, -0.00] | 98.3 | 0.0 | 0.0 |
| anchor | Abs. dist. | 304 | -0.00 [-0.00, -0.00] | 99.0 | 0.0 | 6.2 |
| anchor | Obj. size | 368 | -0.00 [-0.00, 0.00] | 97.3 | 0.5 | 6.8 |
| anchor | Room size | 113 | 0.00 [-0.00, 0.02] | 99.1 | 0.0 | 1.8 |

## Teacher sanity (no depth GT used; room-size GT as a proxy)

- scenes: 288 ok, 0 errors, 0 fell back to 8 frames
- Spearman(s_med, sqrt(room area)) = 0.52; Spearman(s_ext, sqrt(room area)) = 0.80 (n=288)
- log(s_ext / sqrt(area)): median 0.49, IQR 0.38..0.61

## Predictor (median |log error| vs teacher on eval scenes)

- constant 0.185 | ridge 0.083 (2,561 params) | transformer 0.095 (1,748,481 params, 22.3 s for 3 seeds on NVIDIA GeForce RTX 5090, peak 0.11 GB)
- chosen on validation: transformer; n_train=156, n_eval=115
