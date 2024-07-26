from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReviewSerializer
from .analysis import overall_sentiment, aspect_based_sentiment


# homepage
def homepage(request):
    return render(request, "sentiment/homepage.html")


# api/analyze
@api_view(["POST"])
def sentiment_analysis(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        review = serializer.validated_data["product_review"]
        overall = overall_sentiment(review)
        aspect = aspect_based_sentiment(review)
        return Response(
            {"overall_sentiment": overall, "aspect_based_sentiments": aspect}
        )
    return Response(serializer.errors, status=400)
