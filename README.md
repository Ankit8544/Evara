# **Evara** 📈💬

A powerful web application designed to scrape product reviews from various e-commerce platforms and perform sentiment analysis to gauge customer opinions using natural language processing (NLP) techniques.

### **Live Link** 🔗
[Access the live app here](https://evara.onrender.com)

---

## **Table of Contents**

- [Project Overview](#project-overview)
- [Features](#features)
- [Data Processing & Model Training](#data-processing--model-training)
- [Application Architecture](#application-architecture)
- [Flask Integration & Deployment](#flask-integration--deployment)
- [API Usage & Key Management](#api-usage--key-management)
- [Usage Instructions](#usage-instructions)
- [Setup Guide](#setup-guide)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)

---

## **Project Overview**

**Evara** is an innovative application that enables users to scrape product reviews from multiple e-commerce sites and analyze the sentiments of these reviews. By leveraging advanced NLP algorithms, the app provides insights into customer satisfaction and product performance. This tool is beneficial for businesses aiming to improve their products and services based on real customer feedback.

---

## **Features**

- **Review Scraping**: Automatically collects product reviews from popular e-commerce platforms.
- **Sentiment Analysis**: Analyzes the sentiment of the scraped reviews, categorizing them as positive, negative, or neutral.
- **Data Visualization**: Displays sentiment distribution and trends through interactive charts and graphs.
- **Keyword Extraction**: Identifies and displays frequently mentioned keywords and phrases in reviews.
- **Export Data**: Allows users to export the scraped data and analysis results in CSV format for further analysis.

---

## **Data Processing & Model Training**

### **Data Source**  
The application scrapes product reviews from popular e-commerce platforms using web scraping techniques. Libraries such as **Beautiful Soup** and **Scrapy** are utilized for efficient data extraction.

### **Machine Learning Model**
- The sentiment analysis is powered by a **Natural Language Processing (NLP)** model, built with **TensorFlow** and **Keras**.
- The model is trained on a large dataset of labeled reviews, employing techniques such as **word embeddings** and **Recurrent Neural Networks (RNNs)** for accurate sentiment classification.

### **Model Storage**  
The trained NLP model is stored as a **TensorFlow SavedModel**, allowing for easy integration into the web app for real-time predictions.

---

## **Application Architecture**

The application is built using a **microservices architecture**:

1. **Frontend**: Developed with **HTML5**, **CSS3**, and **Bootstrap 5** for a user-friendly interface.
2. **Backend**: The Flask server handles scraping, sentiment analysis, and API requests.
3. **Machine Learning Service**: Hosts the sentiment analysis model, providing predictions based on scraped data.
4. **Data Visualization**: Utilizes libraries like **Matplotlib** and **Plotly** to present insights visually.

---

## **Flask Integration & Deployment**

### **Flask Setup**
The Flask web app manages scraping requests, performs sentiment analysis, and serves visualizations. Key routes include:

- `/`: The homepage where users can initiate the scraping process.
- `/analyze`: Displays the sentiment analysis results and visualizations.

### **Deployment**
The app is hosted on **Render**, allowing users to access the scraping and analysis features through a responsive web interface.

---

## **API Usage & Key Management**

The application may use third-party APIs for additional data or functionalities, managed through the `.env` file for secure API key storage.

### **API Key Setup**
1. Create a `.env` file in the root directory.
2. Add your API keys as needed:
   ```plaintext
   API_KEY=your_api_key_here
   ```

---

## **Usage Instructions**

1. **Homepage**:  
   - Enter the product URL from which you want to scrape reviews and click the "Scrape" button.
   
2. **Sentiment Analysis**:  
   - After scraping, the app will display the sentiment analysis results, including visualizations of sentiment distribution.
   
3. **Export Data**:  
   - Use the export functionality to download the scraped reviews and analysis results as a CSV file.

---

## **Setup Guide**

### **Requirements**
- Python 3.7+
- Flask
- TensorFlow, Keras
- Beautiful Soup, Scrapy
- Pandas, NumPy
- Matplotlib, Plotly

### **Steps to Run Locally**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/evara.git
   cd evara
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file with any necessary API keys.

5. Run the Flask app:
   ```bash
   python app.py
   ```

6. Visit the app at `http://127.0.0.1:5000` in your browser.

---

## **Technologies Used**

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Flask
- **Machine Learning**: TensorFlow, Keras
- **Web Scraping**: Beautiful Soup, Scrapy
- **Data Handling**: Pandas, NumPy
- **Visualization**: Matplotlib, Plotly
- **Environment Management**: Python Dotenv for environment variables

---

## **Future Improvements**

1. **Support for More E-commerce Sites**: Expanding the scraping capabilities to include additional platforms for a wider range of product reviews.
2. **Enhanced Sentiment Model**: Incorporating advanced NLP techniques such as transformer models for improved sentiment analysis accuracy.
3. **User Accounts**: Implement user authentication and personalized settings for saving favorite products and analyses.
4. **Real-time Monitoring**: Adding features for real-time monitoring of product sentiment changes over time.

--- 