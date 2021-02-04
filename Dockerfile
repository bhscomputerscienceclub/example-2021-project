# python:alpine is 3.{latest}
FROM python:buster 

LABEL maintainer="Kai Zheng"


COPY . /src/
WORKDIR /src/
RUN pip install -r /src/requirements.txt
RUN apt-get update && apt-get install -y firefox-esr
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz && tar -xvzf geckodriver* && chmod +x geckodriver && mv geckodriver /usr/local/bin/ && rm geckodriver*
EXPOSE 5000

ENTRYPOINT ["python", "GradeCalc.py"]
