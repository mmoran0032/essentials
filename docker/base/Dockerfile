FROM continuumio/anaconda3:5.2.0

RUN apt-get update
RUN apt-get install -y \
    libgl1-mesa-glx tree libaio1 graphviz
# required for Oracle SQL access
COPY instantclient_12_2 /lib/instantclient_12_2
ENV LD_LIBRARY_PATH /lib/instantclient_12_2:${LD_LIBRARY_PATH}

RUN conda install -c conda-forge -y \
    xgboost=0.72 pyarrow=0.8.0 jupyterlab=0.32.1 altair=2.1.0 dask=0.17.5 \
    distributed=1.21.8 pandas=0.23.0 scikit-learn=0.19.1 seaborn=0.8.1 \
    cx_oracle=6.3.1 python-graphviz=0.8.3 tqdm=4.19.4 fastparquet=0.1.5 \
    mypy=0.610
RUN pip install \
    palettable==3.1.1 msgpack==0.5.6

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]
