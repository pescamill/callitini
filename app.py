from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def handle_form():
    # Connect to SQLite database
    conn = sqlite3.connect('submissions.db')
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
    app.run(debug=True)