FROM python:3.11.8-slim-bullseye

WORKDIR /app

COPY Docker-assessment/Chapter-8/single-build/Group-4/fastapi/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY Docker-assessment/Chapter-8/single-build/Group-4/fastapi/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
