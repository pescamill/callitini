from flask import Flask, request, render_template
from pymongo import MongoClient
from google.cloud import secretmanager
import os


app = Flask(__name__)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

def get_secret(name):
    client = secretmanager.SecretManagerServiceClient()
    secret_name = f"projects/your_project_id/secrets/{name}/versions/latest"
    response = client.access_secret_version(name=secret_name)
    return response.payload.data.decode("utf-8")

def get_db():
    mongo_uri = get_secret("MONGO_URI")
    client = MongoClient(mongo_uri)
    return client['mydatabase']

@app.route('/submit', methods=['POST', 'GET'])
def handle_form():
    # Connect to Postgres database
    
    db = get_db()
    collection = db['submissions']

    # Process form data
    field1 = request.form['field1']

    # Insert data into MongoDB
    collection.insert_one({"field1": field1})

    return render_template('client_form.html')

if __name__ == '__main__':
    app.run()