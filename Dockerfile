FROM python:3.10

RUN apt update && apt install -y librdkafka-dev

RUN useradd -ms /bin/bash marketplace
USER marketplace

WORKDIR /home/marketplace/code

COPY --chown=marketplace:marketplace requirements.txt .
RUN pip install --user -r requirements.txt  

COPY --chown=marketplace:marketplace . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000
