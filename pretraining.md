# Pretraining with TensorFlow Model Garden

First, we create a VM with latest TensorFlow image with TPU support:

```bash
$ gcloud compute instances create hm \
  --zone=europe-west4-a \
  --machine-type=n1-standard-2 \
  --image-project=ml-images \
  --image=debian-11-tf-2-12-1-v20230706 \
  --scopes=cloud-platform
```

Then we create a v8-32 TPU Pod:

```bash
cloud compute tpus create hm \
  --zone=europe-west4-a \
  --accelerator-type=v3-32 \
  --network=default \
  --range=192.168.8.0/29 \
  --version=2.12.1
```

We SSH'into VM and install TensorFlow Model Garden dependencies:

```bash
$ gcloud compute ssh hm --zone europe-west4-a
$ tmux
$ export PATH=$HOME/.local/bin:$PATH
$ pip3 install --upgrade pip
$ pip3 install gin-config pyyaml tensorflow_addons tensorflow_datasets sentencepiece tensorflow_hub scikit-learn seqeval sacrebleu
$ pip3 install tensorflow_text
$ git clone https://github.com/tensorflow/models.git
$ cd models && git checkout v2.12.1
$ export PYTHONPATH=$(pwd)
```


# TEAMS (Training ELECTRA Augmented with Multi-word Selection)

We pretrain a TEAMS model, proposed in the
[Training ELECTRA Augmented with Multi-word Selection; TEAMS](https://aclanthology.org/2021.findings-acl.219/) paper.

In the VM we go into:

```bash
$ cd official/projects/teams
```

folder and create a new configuration `experiments/base/hmteams_pretrain.yaml`:

```yaml
task:
  model:
    candidate_size: 5
    num_shared_generator_hidden_layers: 3
    num_discriminator_task_agnostic_layers: 11
    tie_embeddings: true
    generator:
      attention_dropout_rate: 0.1
      dropout_rate: 0.1
      embedding_size: 768
      hidden_activation: gelu
      hidden_size: 768
      initializer_range: 0.02
      intermediate_size: 3072
      max_position_embeddings: 512
      num_attention_heads: 12
      num_layers: 6
      type_vocab_size: 2
      vocab_size: 32000
    discriminator:
      attention_dropout_rate: 0.1
      dropout_rate: 0.1
      embedding_size: 768
      hidden_activation: gelu
      hidden_size: 768
      initializer_range: 0.02
      intermediate_size: 3072
      max_position_embeddings: 512
      num_attention_heads: 12
      num_layers: 12
      type_vocab_size: 2
      vocab_size: 32000
  train_data:
    drop_remainder: true
    global_batch_size: 256
    input_path: 'gs://hmbert-token-dropping/tfrecords/*.tfrecord'
    is_training: true
    max_predictions_per_seq: 76
    seq_length: 512
    use_next_sentence_label: false
    use_position_id: false
    cycle_length: 8
    use_v2_feature_names: true
trainer:
  checkpoint_interval: 100000
  max_to_keep: 50
  optimizer_config:
    learning_rate:
      polynomial:
        cycle: false
        decay_steps: 1000000
        end_learning_rate: 0.0
        initial_learning_rate: 0.0002
        power: 1.0
      type: polynomial
    optimizer:
      type: adamw
    warmup:
      polynomial:
        power: 1
        warmup_steps: 10000
      type: polynomial
  steps_per_loop: 4000
  summary_interval: 4000
  train_steps: 1000000
  validation_interval: 100
  validation_steps: 64
```

And start pretraining:

```bash
python3 train.py --experiment=teams/pretraining \
  --config_file=experiments/base/hmteams_pretrain.yaml\
  --params_override="runtime.distribution_strategy=tpu" \
  --tpu=hm \
  --model_dir=gs://hmbert-token-dropping/models-v2/teams-base-historic-multilingual-cased \
  --mode=train
```
