FROM python:3.7-alpine3.7
COPY requirements-lock.txt requirements.txt
RUN pip install -r requirements.txt && rm requirements.txt && mkdir /var/code
COPY src/ /var/code/
RUN chmod  -R +x /var/code
ENTRYPOINT ["/var/code/main.py"]