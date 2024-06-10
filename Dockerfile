FROM python:3.12.1

WORKDIR /stories-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python -m textblob.download_corpora

CMD ["streamlit", "run", "main.py"]
