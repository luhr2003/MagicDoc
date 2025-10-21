# 🐳 Docker

## Prerequisites

Please make sure you have installed `docker` in the officially recommended way. Otherwise, please refer to the [official guide](https://docs.docker.com/engine/install/ubuntu/).

Please install [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) following the [official guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

Please create and add the docker user information to `.env` file. To use the same user information as the host machine, run in project root:
```bash
printf "DOCKER_UID=$(id -u $USER)\nDOCKER_GID=$(id -g $USER)\nDOCKER_USER=$USER\n" > .env
```