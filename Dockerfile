FROM python:3.8-slim-buster 
WORKDIR /src/

RUN apt-get update  \
        && apt-get install -y firefox-esr wget  \
        && wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz  \
        && tar -xvzf geckodriver*  \
        && chmod +x geckodriver  \
        && mv geckodriver /usr/local/bin/  \
        && apt-get remove -y wget  \
        && apt-get autoremove -y  \
        && rm -rf geckodriver* /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r /src/requirements.txt

COPY . .
EXPOSE 5000
ENV FLASK_RUN_HOST=0.0.0.0 FLASK_APP=GradeCalc.py
ENTRYPOINT ["flask" ,"run"]

