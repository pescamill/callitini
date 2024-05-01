from flask import Flask, request, render_template
from pymongo import MongoClient
from google.cloud import secretmanager
import os


app = Flask(__name__)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

def get_secret(name):
    client = secretmanager.SecretManagerServiceClient()
    secret_name = f"projects/376355469246/secrets/{name}/versions/latest"
    response = client.access_secret_version(name=secret_name)
    return response.payload.data.decode("utf-8")

def get_db():
    mongo_uri = get_secret("MONGO_URI")
    client = MongoClient(mongo_uri)
    return client['mydatabase']

@app.route('/form', methods=['GET'])
def show_form():
    # Render the form HTML page
    return render_template('client_form.html')

@app.route('/submit', methods=['POST'])
def handle_form():
    # Connect to Postgres database
    
    db = get_db()  # Or however you're handling your database connection
    collection = db['client_submissions']

    # Extract fields from the form
    field1 = request.form.get('field1')
    field2 = request.form.get('field2')
    # Process other fields similarly

    # Insert into the database
    collection.insert_one({
        "field1": field1,
        "field2": field2,
        # Add more fields as needed
    })

    return "Form submitted!"

if __name__ == '__main__':
    app.run()