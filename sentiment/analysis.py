import os
from pyabsa import ATEPCCheckpointManager
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()


def overall_sentiment(review):
    sentiment_scores = sia.polarity_scores(review)
    sentiment_scores.popitem()
    final_score, final_sentiment = 0, ""
    for sentiment, score in sentiment_scores.items():
        if score > final_score:
            final_score = score
            final_sentiment = sentiment
    final_sentiment = (
        "Neutral"
        if final_sentiment == "neu"
        else "Positive" if final_sentiment == "pos" else "Negative"
    )
    return final_sentiment


def load_model():
    model_path = "models\ATEPC_ENGLISH_CHECKPOINT"
    model = ATEPCCheckpointManager.get_aspect_extractor(checkpoint=model_path)
    return model


# Load the model once at the start
atepc_model = load_model()


def aspect_based_sentiment(review):
    result = atepc_model.extract_aspect(
        inference_source=[review], predict_sentiment=True
    )
    aspects, sentiment = (
        result[0]["aspect"],
        result[0]["sentiment"],
    )
    aspect_sentiments = {
        aspect: sentiment for aspect, sentiment in zip(aspects, sentiment)
    }
    return aspect_sentiments
