# NER Fine-Tuning

We use Flair for fine-tuning NER models on
[HIPE-2022](https://github.com/hipe-eval/HIPE-2022-data) datasets from
[HIPE-2022 Shared Task](https://hipe-eval.github.io/HIPE-2022/).

All models are fine-tuned on A10 (24GB) and A100 (40GB) instances from
[Lambda Cloud](https://lambdalabs.com/service/gpu-cloud) using Flair:

```bash
$ git clone https://github.com/flairNLP/flair.git
$ cd flair && git checkout 419f13a05d6b36b2a42dd73a551dc3ba679f820c
$ pip3 install -e .
$ cd ..
```

Clone this repo for fine-tuning NER models:

```bash
$ git clone https://github.com/stefan-it/hmTEAMS.git
$ cd hmTEAMS/bench
```

Authorize via Hugging Face CLI (needed because hmTEAMS is currently only available after approval):

```bash
# Use access token from https://huggingface.co/settings/tokens
$ huggingface-cli login login
```

We use a config-driven hyper-parameter search. The script [`flair-fine-tuner.py`](flair-fine-tuner.py) can be used to
fine-tune NER models from our Model Zoo.

# Benchmark

We test our pretrained language models on various datasets from HIPE-2020, HIPE-2022 and Europeana. The following table
shows an overview of used datasets.

| Language | Datasets
|----------|----------------------------------------------------|
| English  | [AjMC] - [TopRes19th]                              |
| German   | [AjMC] - [NewsEye]                                 |
| French   | [AjMC] - [ICDAR-Europeana] - [LeTemps] - [NewsEye] |
| Finnish  | [NewsEye]                                          |
| Swedish  | [NewsEye]                                          |
| Dutch    | [ICDAR-Europeana]                                  |

[AjMC]: https://github.com/hipe-eval/HIPE-2022-data/blob/main/documentation/README-ajmc.md
[NewsEye]: https://github.com/hipe-eval/HIPE-2022-data/blob/main/documentation/README-newseye.md
[TopRes19th]: https://github.com/hipe-eval/HIPE-2022-data/blob/main/documentation/README-topres19th.md
[ICDAR-Europeana]: https://github.com/stefan-it/historic-domain-adaptation-icdar
[LeTemps]: https://github.com/hipe-eval/HIPE-2022-data/blob/main/documentation/README-letemps.md

# Results

We report averaged F1-score over 5 runs with different seeds on development set:

| Model                                                                     | English AjMC | German AjMC  | French AjMC  | German NewsEye | French NewsEye | Finnish NewsEye | Swedish NewsEye | Dutch ICDAR  | French ICDAR | French LeTemps | English TopRes19th | Avg.      |
|---------------------------------------------------------------------------|--------------|--------------|--------------|----------------|----------------|-----------------|-----------------|--------------|--------------|----------------|--------------------|-----------|
| hmBERT (32k) [Schweter et al.](https://ceur-ws.org/Vol-3180/paper-87.pdf) | 85.36 ± 0.94 | 89.08 ± 0.09 | 85.10 ± 0.60 |  39.65 ± 1.01  |  81.47 ± 0.36  | 77.28 ± 0.37    | 82.85 ± 0.83    | 82.11 ± 0.61 | 77.21 ± 0.16 | 65.73 ± 0.56   |    80.94 ± 0.86    |   76.98   |
| hmTEAMS (Ours)                                                            | 86.41 ± 0.36 | 88.64 ± 0.42 | 85.41 ± 0.67 |  41.51 ± 2.82  |  83.20 ± 0.79  | 79.27 ± 1.88    | 82.78 ± 0.60    | 88.21 ± 0.39 | 78.03 ± 0.39 | 66.71 ± 0.46   |    81.36 ± 0.59    | **78.32** |
