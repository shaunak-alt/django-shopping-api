## Smart Shopper API 🛒
This project is a high-performance, real-time product information pipeline built with Django and Django Rest Framework. It fetches product data from Google Shopping, focusing on speed and scalability through aggressive caching with Redis and asynchronous data fetching.

This system was built to address the "Smart Shopper's Dilemma," where a user expects instant product search results without any delay.

## Key Features
Real-time Search: Fetches up-to-date product information on demand.

High Performance: Uses a Redis cache to serve repeated requests in milliseconds.

Asynchronous: Leverages asyncio to perform slow I/O operations (like web scraping) efficiently.

Reliable Data: Integrates with the SerpApi service to handle the complexities of web scraping and avoid getting blocked.

RESTful API: Exposes a clean, simple API endpoint for easy integration with any client application.

## Tech Stack
Backend: Python, Django, Django Rest Framework

Caching: Redis

Scraping: SerpApi, asyncio

Environment Management: venv, python-dotenv

## Setup and Installation
Follow these steps to get the project running locally.

### Prerequisites
Python 3.8+

Docker Desktop (for running Redis)

A SerpApi API Key

### 1. Clone the Repository
Bash

git clone https://github.com/your-username/smart-shopper-api.git
cd smart-shopper-api
### 2. Set Up the Environment
Create and activate a Python virtual environment.

PowerShell

# Create the virtual environment
python -m venv venv

# Activate it (on Windows PowerShell)
.\venv\Scripts\activate
### 3. Install Dependencies
Install all required packages from the requirements.txt file (you will need to create this file).

Bash

pip install django djangorestframework django-redis redis aiohttp google-search-results python-dotenv asgiref
### 4. Configure Environment Variables
Create a file named .env in the project root and add your SerpApi key.

# .env
SERPAPI_API_KEY="YOUR_SECRET_API_KEY_GOES_HERE"
### 5. Start Redis
Make sure Docker Desktop is running, then start the Redis container.

Bash

docker run -d -p 6379:6379 --name my-redis redis
## How to Run
Apply Migrations:

Bash

python manage.py migrate
Start the Django Server:

Bash

python manage.py runserver
The API will be available at http://127.0.0.1:8000.

## API Usage
Make a GET request to the search endpoint with a product query.

Endpoint: /api/products/search/

Method: GET

Query Parameter: q=<product_name>

### Example Request
Bash

curl "http://127.0.0.1:8000/api/products/search/?q=organic+creamy+peanut+butter"
### Example Response
The first request (cache miss) will be slower. Subsequent requests for the same query (cache hit) will be nearly instantaneous.

JSON

[
    {
        "title": "365 by Whole Foods Market, Peanut Butter Creamy Organic, 16 Ounce",
        "brand": "Whole Foods Market",
        "price": "$5.49",
        "weight": "16 Ounce",
        "link": "https://www.google.com/shopping/product/..."
    },
    {
        "title": "Kirkland Signature Organic Creamy Peanut Butter, 28 Ounce, 2 Count",
        "brand": "Costco",
        "price": "$12.99",
        "weight": "28 Ounce",
        "link": "https://www.google.com/shopping/product/..."
    }
]
## Project Report
A detailed report covering the project's architecture, challenges faced, solutions implemented, and potential improvements is available in the submission documents.
