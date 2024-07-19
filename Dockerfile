FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Change the exposed port to 8080
EXPOSE 8080

# Update CMD to run the Flask app on port 8080
CMD ["python", "app.py"]
