FROM python:3.9-slim

COPY ./api /app
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000

ENV API_ENV "DEV"
ENV PORT 5000

CMD ["python","app.py"]