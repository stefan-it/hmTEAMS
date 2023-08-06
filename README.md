# hmTEAMS

[![🤗](logo.jpeg "🤗")](https://github.com/stefan-it/hmTEAMS)

Historic Multilingual and Monolingual [TEAMS](https://aclanthology.org/2021.findings-acl.219/) Models.
The following languages are covered:

* English (British Library Corpus - Books)
* German (Europeana Newspaper)
* French (Europeana Newspaper)
* Finnish (Europeana Newspaper, Digilib)
* Swedish (Europeana Newspaper, Digilib)
* Dutch (Delpher Corpus)
* Norwegian (NCC Corpus)

# Architecture

We pretrain a "Training ELECTRA Augmented with Multi-word Selection"
([TEAMS](https://aclanthology.org/2021.findings-acl.219/)) model:

![hmTEAMS Overview](hmteams_overview.svg)

# Results

We perform experiments on various historic NER datasets, such as HIPE-2022 or ICDAR Europeana.
All results incl. hyper-parameters can be found [here](bench/README).

# Changelog

* 06.08.2023: Evaluation on various historic NER datasets are compledted. Results can be found [here](bench/README).
* 01.08.2023: hmTEAMS organization can be found on the [Model Hub](https://huggingface.co/hmteams).
              More information of how to access trained hmTEAMS models are coming soon.
* 25.05.2023: Initial version of this repo.

# Acknowledgements

We thank [Luisa März](https://github.com/LuisaMaerz), [Katharina Schmid](https://github.com/schmika) and
[Erion Çano](https://github.com/erionc) for their fruitful discussions about Historic Language Models.

Research supported with Cloud TPUs from Google's [TPU Research Cloud](https://sites.research.google/trc/about/) (TRC).
Many Thanks for providing access to the TPUs ❤️
