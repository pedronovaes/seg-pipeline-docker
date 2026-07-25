# seg-pipeline-docker

A minimal repository created to learn Docker basics and to demonstrate how to package a tiny Python segmentation pipeline into a container image. The repository contains a small Python package `seg_pipeline` with a `FakeSegmenter`, a CLI `run_seg.py`, and a Dockerfile that builds an image you can run locally.

### Quick start

To build the Docker image, you can run this command:

```bash
docker build -t seg-pipeline-docker:latest .
```

To run the container using host folders:

```bash
# Create input and output folders on the host.
mkdir -p images out

# Run container, mount host folders, pass CLI args to the container.
docker run --rm \
    -v "$(pwd)/images":/data/in:ro \
    -v "$(pwd)/out":/data/out \
    seg-pipeline-docker:latest --input /data/in --output /data/out
```

To test if the container works well, you can run locally without docker. Use these command to do that:

```bash
pip install -r requirements.txt
export PYTHONAPP=$(pwd)
python run_seg.py --input images --output out
```
