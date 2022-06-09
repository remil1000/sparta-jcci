ARG PYTHON_VERSION=3.9
FROM python:$PYTHON_VERSION

ARG HTTP_PROXY

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --proxy="${HTTP_PROXY}" -r /app/requirements.txt

EXPOSE 5004

VOLUME [ "/app/data" ]

COPY wadl_capabilities.xml /app/
COPY flaskserver.py /app/

ENTRYPOINT [ "python3", "flaskserver.py" ]
