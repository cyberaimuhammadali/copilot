FROM python:3.11-slim
WORKDIR /bot
COPY requirements.txt .
RUN pip install --no-cache-dir aiogram aiohttp python-dotenv
COPY . .
CMD ["python", "main.py"]
