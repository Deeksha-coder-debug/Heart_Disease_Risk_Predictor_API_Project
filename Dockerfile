FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x start.sh

EXPOSE 8000
EXPOSE 8501

# CMD ["streamlit","run","frontend.py","--server.address=0.0.0.0","--server.port=8501"]

CMD ["./start.sh"]