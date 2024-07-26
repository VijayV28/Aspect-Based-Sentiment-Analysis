# Sentiment Analysis API and Streamlit App

## Overview

This project consists of a Django-based API for sentiment analysis and a Streamlit app that interacts with this API to display sentiment results for product reviews. The Django API provides both overall sentiment and aspect-based sentiment analysis, while the Streamlit app presents these results in a user-friendly format.

## Getting Started

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create and activate a virtual environment:**

    ```bash
    conda create -n <env_name> python=3.10
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Django migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run Django server:**

    ```bash
    python manage.py runserver
    ```

6. **Run the Streamlit app:**

    ```bash
    cd apps
    streamlit run sentiment_analyzer.py
    ```

### API Endpoints

- **`/sentiment/analyze/`**: POST request to analyze product reviews. 

  **Request Body:**

  ```json
  {
      "product_name": "Example Product",
      "product_review": "This is an example review."
  }
  ```

  **Response:**

  ```json
  {
      "overall_sentiment": "Neutral",
      "aspect_based_sentiments": {
          "display": "Positive",
          "speakers": "Neutral"
      }
  }
  ```

### Streamlit App

- **URL**: Link in terminal
- **Functionality**: Allows users to input product reviews and displays sentiment analysis results. Results are shown with different background colors and optionally with icons or emojis.

## Project Details

- **Django API**: Provides endpoints for overall and aspect-based sentiment analysis using PyABSA and VADER.
- **Streamlit App**: Provides a user interface to interact with the Django API and displays sentiment analysis results in a visually appealing manner.

## Usage

1. **Submit Review for Analysis**: Enter the product name and review in the Streamlit app, and click "Analyze Sentiment".
2. **View Results**: Results are displayed with sentiment analysis on overall review and aspect-based sentiment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.