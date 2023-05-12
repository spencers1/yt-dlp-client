FROM python:3.9

RUN apt-get update && apt-get install ffmpeg -y
ADD main.py .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]