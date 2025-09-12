import os
import re
import asyncio
from serpapi import GoogleSearch

def parse_product(product_data):
    title = product_data.get('title', '')
    price = product_data.get('price')
    brand = product_data.get('source', 'N/A')
    weight_pattern = re.compile(r'(\d+\.?\d*)\s*(oz|g|kg|lb|L|ml)', re.IGNORECASE)
    match = weight_pattern.search(title)
    weight = match.group(0) if match else 'N/A'
    return {'title': title, 'brand': brand, 'price': price, 'weight': weight, 'link': product_data.get('link')}

async def fetch_shopping_results(query: str):
    loop = asyncio.get_running_loop()
    params = {"api_key": os.getenv("SERPAPI_API_KEY"), "engine": "google_shopping", "q": query}
    search = await loop.run_in_executor(None, lambda: GoogleSearch(params))
    results = await loop.run_in_executor(None, search.get_dict)
    shopping_results = results.get('shopping_results', [])
    return [parse_product(product) for product in shopping_results]