# api/views.py
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.scraper import fetch_shopping_results
from asgiref.sync import async_to_sync  # <-- ADD THIS IMPORT

class ProductSearchAPIView(APIView):
    @async_to_sync  # <-- ADD THIS WRAPPER
    async def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', None)
        if not query:
            return Response({"error": "A 'q' search parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        cache_key = f"search:{query.lower().replace(' ', '_')}"

        if cached_results := cache.get(cache_key):
            print("CACHE HIT!")
            return Response(cached_results)

        print("CACHE MISS!")
        try:
            results = await fetch_shopping_results(query)
            if not results:
                return Response({"message": "No products found."}, status=status.HTTP_404_NOT_FOUND)
            cache.set(cache_key, results, timeout=3600)
            return Response(results)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)