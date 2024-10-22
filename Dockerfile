# Stage 1 - Build and Requirements
FROM python:3.13.0-slim as base

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    TZ=Europe/Rome

# enforce --no-cache rebuild
ARG CACHEBUST=1
RUN mkdir /checker

WORKDIR /checker

ENV PYTHONPATH=/checker:$PYTHONPATH

RUN \
    apt-get -y upgrade && \
    apt -y clean && \
    apt-get -y update && \
    apt-get install -y --no-install-recommends --yes python3 && \
    apt-get install -y --no-install-recommends python3-pip && \
    apt-get install -y python3-dev libcairo2-dev pkg-config && \
    apt-get clean && apt-get autoremove -y && \
    rm -rf /var/lib/apt-get/lists/*

ARG CPLUS_INCLUDE_PATH=/usr/include/gdal
ARG C_INCLUDE_PATH=/usr/include/gdal

COPY . .

RUN pip3 install -r requirements.txt && \
    pip3 install --upgrade requests && \
    pip3 install numpy -U

# Stage 2 - Copy and Run - Prod
FROM base
WORKDIR /checker
COPY --from=base /checker /checker

CMD ["python3", "start.py"]
