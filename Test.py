from flask import Flask
import psycopg2

app = Flask(__name__)

# connecting to database(need to change db address)
DATABASE_URL = "postgresql://postgres:1234@localhost/Project"

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM User_info')
    result = cur.fetchall()
    cur.close()
    conn.close()
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)