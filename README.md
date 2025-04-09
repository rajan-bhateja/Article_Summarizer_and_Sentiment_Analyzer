# Article Summarizer and Sentiment Analyzer

This can summarize any article and calculate its polarity scores (useful for finding sentiments in NLP), given that the provided URL's contents can be extracted.

## Tech Stack

* Streamlit
* Google Gemini
* Trafilatura
* NLTK

## Working

* The user enters a URL via `dashboard.py` which is created using Streamlit.
* The entered URL is then passed to `scraper.py`, created using Trafilatura, which downloads the content of the URL.
* The downloaded content is passed to `summarizer.py`, calling Google Gemini via an API Key, to summarize the content within 5-10 points.
* The downloaded content is also passed to `sentiment_analysis.py`, which uses NLTK to calculate the polarity scores of the content.
* The summary and the polarity scores are displayed in the `dashboard.py`. 
