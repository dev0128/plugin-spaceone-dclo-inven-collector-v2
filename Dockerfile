FROM cloudforet/python-core:2.0

ENV PYTHONUNBUFFERED 1
ENV SPACEONE_PORT 50051
ENV PKG_DIR /tmp/pkg
ENV SRC_DIR /tmp/src

RUN apt update && apt upgrade -y

COPY pkg/*.txt ${PKG_DIR}/

RUN pip install --upgrade pip && \
    pip install --upgrade -r ${PKG_DIR}/pip_requirements.txt

ARG CACHEBUST=1
RUN pip install --upgrade spaceone-core spaceone-api

COPY src ${SRC_DIR}

WORKDIR /tmp

EXPOSE ${SPACEONE_PORT}

ENTRYPOINT ["spaceone"]
CMD ["run", "plugin-server", "src"]
