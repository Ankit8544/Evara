# Import Module
from flask import Flask, request, render_template
import pandas as pd
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Create a route for the index page
@app.route('/', methods=['GET'])
def home_page():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM product_details")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', products=products)

# Route to fetch and display product details
@app.route('/product')
def index():
    product_name = request.args.get('product_name')    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM product_details")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM product_details WHERE product_name = %s", (product_name,))
    product_details = cursor.fetchone()
    if not product_details:
        cursor.close()
        connection.close()
        return render_template('details.html', products=products, error="Product not found")
    product = {
        'Overall Rating': product_details.get('overall_rating', 'N/A'),
        'Total Ratings': product_details.get('total_ratings', 'N/A'),
        'Total Reviews': product_details.get('total_reviews', 'N/A')
    }
    cursor.close()
    connection.close()
    return render_template('details.html', products=products, product_details=product_details, product=product)

if __name__ == '__main__':
    # Run the Flask app
    app.run()
