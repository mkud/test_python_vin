FROM python:3.7.7-buster

LABEL maintainer="Maksim Kudimov"

RUN pip install 'Flask==1.1.1' 'ujson==2.0.3' 'requests==2.23.0'

COPY main.py test.py test_data.py /

ENTRYPOINT ["python3", "-u", "test.py"]