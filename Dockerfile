FROM python:3.11-slim
WORKDIR /app
COPY app.py /app/
COPY requirements.txt /app/
RUN if [ -s requirements.txt ]; then pip install -r requirements.txt; fi
ENTRYPOINT ["python", "app.py"]
