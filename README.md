# MagicSim Documentation

1. Install the dependencies

```bash
conda create -n magic_doc python=3.11
conda activate magic_doc
pip install -r requirements.txt
```

2. Build the documentation and watch the change lively

```bash
rm -rf build/; make html; sphinx-autobuild ./source ./build/html
```