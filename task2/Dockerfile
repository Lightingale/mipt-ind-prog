FROM python:3.7.2-alpine
WORKDIR /todo
ADD requirements.txt /todo
RUN pip install -r /todo/requirements.txt
CMD ["/bin/sh", "/todo/run.sh"]