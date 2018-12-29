FROM mmoran0032/base:latest

RUN conda install -c pytorch -y \
    pytorch-cpu=0.4.0 torchvision=0.2.1
RUN mkdir -p /torch
RUN mkdir -p /torch/data

EXPOSE 8888

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD jupyter lab \
    --ip=0.0.0.0 --no-browser --allow-root --port=8888 --notebook-dir=/torch
