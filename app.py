from flask import Flask, request
import os
import psycopg2

app = Flask(__name__)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/submit', methods=['POST'])
def handle_form():
    # Connect to Postgres database
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    c = conn.cursor()
    
    # Extract fields from form
    field1 = request.form['field1']
    # Extract other fields and images similarly
    
    # Insert data into database
    # c.execute('''INSERT INTO submissions VALUES (?, ?, ...)''', (field1, ...))
    
    # Save changes and close connection
    conn.commit()
    conn.close()

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run()