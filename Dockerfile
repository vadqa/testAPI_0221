FROM python:3.7.3-slim

COPY requirements.txt /tmp/
RUN cat /tmp/requirements.txt
RUN python3 -m pip install --upgrade pip && \
    pip3 install -r /tmp/requirements.txt
COPY main.py .
CMD ["pytest", "-ra", "./main.py"]
