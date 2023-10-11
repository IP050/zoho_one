FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1

ENV DATABASE_URL=""
ENV ZOHO_CLIENT_ID = ""
ENV ZOHO_CLIENT_SECRET = ""
ENV ZOHO_REFRESH_TOKEN = ""


WORKDIR /the/workdir/path 

COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN pip install fastapi uvicorn

COPY . /the/workdir/path/

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3500"]
