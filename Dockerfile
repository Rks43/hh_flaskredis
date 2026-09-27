from python:3.11-slim
WORKDIR /app
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPY app.py .
CMD ["python", "app.py"]
