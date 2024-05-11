FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install hatch

EXPOSE 8080

CMD ["python", "-m", "hatch", "run", "start"]