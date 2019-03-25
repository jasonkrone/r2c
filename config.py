import os

EFS_DIR = "/home/ec2-user/efs"
DATA_DIR = os.path.join(EFS_DIR, "data")
VCR_DIR = os.path.join(DATA_DIR, "vcr")

USE_IMAGENET_PRETRAINED = True # otherwise use detectron, but that doesnt seem to work?!?
# Change these to match where your annotations and images are
VCR_IMAGES_DIR = os.path.join(VCR_DIR, "vcr1images")
VCR_ANNOTS_DIR = os.path.join(VCR_DIR, "vcr1annots")
VCR_PRETRAINING_DIR = os.path.join(VCR_DIR, "bert_pretraining_data")

if not os.path.exists(VCR_IMAGES_DIR):
    raise ValueError("Update config.py with where you saved VCR images to.")

CHECKPOINTS_DIR                = os.path.join(EFS_DIR, "checkpoints")
VCR_CHECKPOINTS_DIR            = os.path.join(CHECKPOINTS_DIR, "vcr")
VCR_BERT_CHECKPOINTS_DIR       = os.path.join(VCR_CHECKPOINTS_DIR, "visually_grounded_bert")
BERT_CONFIG_PATH               = os.path.join(VCR_BERT_CHECKPOINTS_DIR, "bert_config.json")
BERT_CHECKPOINT_DIR            = os.path.join(VCR_BERT_CHECKPOINTS_DIR, "seed-2.lr-5e-5.epochs-3")
BERT_VOCAB_PATH                = os.path.join(VCR_BERT_CHECKPOINTS_DIR, "vocab.txt")
PRETRAINED_BERT_CHECKPOINT_DIR = os.path.join(VCR_BERT_CHECKPOINTS_DIR, "pretrained_on_vcr")
