FROM python:3.8

RUN mkdir -p /usr/app
WORKDIR /usr/app/
COPY requirements.txt /usr/app
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8000

COPY ./src /usr/app/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]