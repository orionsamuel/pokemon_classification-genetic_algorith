FROM python:3.7.3-stretch

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
  pip install --no-cache -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
