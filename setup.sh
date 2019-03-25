#!/bin/bash

#wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
#conda update -n base -c defaults conda
#conda create --name r2c python=3.6
#source activate r2c

conda install numpy pyyaml setuptools cmake cffi tqdm pyyaml scipy ipython mkl mkl-include cython typing h5py pandas nltk spacy numpydoc scikit-learn jpeg

conda install pytorch -c pytorch
pip install git+git://github.com/pytorch/vision.git@24577864e92b72f7066e1ed16e978e873e19d13d

pip install -r allennlp-requirements.txt
pip install --no-deps allennlp==0.8.0
python -m spacy download en_core_web_sm


# this one is optional but it should help make things faster
pip uninstall pillow && CC="cc -mavx2" pip install -U --force-reinstall pillow-simd

# get the data
wget https://s3.us-west-2.amazonaws.com/ai2-rowanz/vcr1annots.zip  -P ~/efs/data/vcr
wget https://s3.us-west-2.amazonaws.com/ai2-rowanz/vcr1images.zip  -P ~/efs/data/vcr
