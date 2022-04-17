# 
FROM python:3.8

# 
WORKDIR /usr/src

# 
COPY . .

# 
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
