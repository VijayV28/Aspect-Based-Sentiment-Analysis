import streamlit as st
import requests

# Define the URL of your Django API
API_URL = "http://127.0.0.1:8000/api/analyze/"


def get_sentiment_icon(sentiment):
    if sentiment == "Positive":
        return "😊"  # Smiling face
    elif sentiment == "Neutral":
        return "😐"  # Neutral face
    elif sentiment == "Negative":
        return "😞"  # Sad face


# Streamlit app
st.title("Product Review Sentiment Analysis")

# User input for product name and review
product_name = st.text_input("Product Name")
product_review = st.text_area("Product Review")

# Button to submit the review for sentiment analysis
if st.button("Analyze Sentiment"):
    if product_name and product_review:
        # Prepare the data to be sent to the API
        data = {"product_name": product_name, "product_review": product_review}

        # Send the request to the Django API
        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            result = response.json()
            st.subheader("Sentiment Analysis Results")

            col1, col2, col3 = st.columns([1, 0.1, 1])

            with col1:
                st.write("### Overall Sentiment")
                overall_sentiment = result.get("overall_sentiment")
                icon = get_sentiment_icon(overall_sentiment)
                st.markdown(
                    f"<p><b>{product_name}:</b> {icon} {overall_sentiment}</p>",
                    unsafe_allow_html=True,
                )

            # Vertical line in the middle column
            with col2:
                st.markdown(
                    '<div style="border-left: 1px solid black; height: 300px;"></div>',
                    unsafe_allow_html=True,
                )

            with col3:
                st.write("### Aspect-Based Sentiments")
                aspect_based = result.get("aspect_based_sentiments")
                if isinstance(aspect_based, dict):
                    for aspect, sentiment in aspect_based.items():
                        icon = get_sentiment_icon(sentiment)
                        st.markdown(
                            f"<p><b>{aspect}:</b> {icon} {sentiment}</p>",
                            unsafe_allow_html=True,
                        )

        else:
            st.error("Error: " + response.text)
    else:
        st.warning("Please enter both product name and review.")
