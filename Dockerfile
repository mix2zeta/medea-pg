FROM python:3.7.0-slim

COPY / /usr/src/
WORKDIR /usr/src

RUN pip install -r /usr/src/requirements/${pip_file:-dev}.txt && \
    pip freeze

CMD ["python -u /usr/src/medea/app.py"]