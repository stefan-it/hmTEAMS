# NER Fine-Tuning

We use Flair for fine-tuning NER models on
[HIPE-2022](https://github.com/hipe-eval/HIPE-2022-data) datasets from
[HIPE-2022 Shared Task](https://hipe-eval.github.io/HIPE-2022/).

All models are fine-tuned on A10 (24GB) and A100 (40GB) instances from
[Lambda Cloud](https://lambdalabs.com/service/gpu-cloud) using Flair:

```bash
$ git clone -b support_byt5 https://github.com/flairNLP/flair.git && cd flair && pip3 install -e .
$ cd
```

Clone this repo for fine-tuning NER models:

```bash
$ git clone https://github.com/stefan-it/hmELECTRA.git
$ cd hmELECTRA/bench
```

We use a config-driven hyper-parameter search. The script [`flair-fine-tuner.py`](flair-fine-tuner.py) can be used to
fine-tune NER models from our Model Zoo.

# Small Benchmark

We test our pretrained language models on various datasets from HIPE-2020, HIPE-2022 and Europeana. The following table
shows an overview of used datasets.

| Language | Dataset                                                                                          | Additional Dataset                                                               |
|----------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| English  | [AjMC](https://github.com/hipe-eval/HIPE-2022-data/blob/main/documentation/README-ajmc.md)       | -                                                                                |
| German   | [AjMC](https://github.com/hipe-eval/HIPE-2022-data/blob/main/documentation/README-ajmc.md)       | -                                                                                |
| French   | [AjMC](https://github.com/hipe-eval/HIPE-2022-data/blob/main/documentation/README-ajmc.md)       | [ICDAR-Europeana](https://github.com/stefan-it/historic-domain-adaptation-icdar) |
| Finnish  | [NewsEye](https://github.com/hipe-eval/HIPE-2022-data/blob/main/documentation/README-newseye.md) | -                                                                                |
| Swedish  | [NewsEye](https://github.com/hipe-eval/HIPE-2022-data/blob/main/documentation/README-newseye.md) | -                                                                                |
| Dutch    | [ICDAR-Europeana](https://github.com/stefan-it/historic-domain-adaptation-icdar)                 | -                                                                                |

# Results

| Model                                                                                  | Upsampled | Seen Subwords | English AjMC | German AjMC  | French AjMC  | Finnish NewsEye | Swedish NewsEye | Dutch ICDAR  | French ICDAR | Avg.      |
|----------------------------------------------------------------------------------------|-----------|---------------|--------------|--------------|--------------|-----------------|-----------------|--------------|--------------|-----------|
| [BERT TD](https://huggingface.co/stefan-it/bert-base-historic-multilingual-td-cased)   |     ❌     | 262B          | 86.00 ± 0.65 | 89.63 ± 0.81 | 85.34 ± 0.66 | 66.54 ± 1.20    | 81.31 ± 0.59    | 87.35 ± 0.66 | 77.33 ± 0.57 | 81.93     |
| [ConvBERT](https://huggingface.co/stefan-it/convbert-base-historic-multilingual-cased) |     ❌     | 262B          | 87.04 ± 0.17 | 88.86 ± 0.30 | 86.67 ± 0.35 | 75.14 ± 0.94    | 81.30 ± 0.62    | 88.50 ± 0.34 | 78.65 ± 0.24 | **83.74** |
| [ELECTRA](stefan-it/electra-base-historic-multilingual-cased-discriminator)            |     ❌     | 262B          | 86.62 ± 0.58 | 88.16 ± 0.32 | 85.37 ± 0.41 | 69.23 ± 0.91    | 80.09 ± 1.23    | 87.78 ± 0.58 | 77.01 ± 0.54 | 82.04     |

