# Article Summarizer and Sentiment Analyzer

This can summarize any article and calculate its polarity scores (helpful in finding sentiments in NLP).

The user must provide either a valid URL or the article content to get the summary and the sentiment scores.

## Tech Stack

* Streamlit
* Google Gemini API
* Trafilatura
* NLTK

## Working

1. The user enters a URL or the article content via `dashboard.py` which is created using Streamlit.
2. The entered URL is then passed to `scraper.py`, created using Trafilatura, which downloads the content of the URL.
3. The downloaded content is passed to `summarizer.py`, calling Google Gemini via an API key, to summarize the content within 5-10 points. In the case when the content is entered, the content is directly passed to `summarizer.py`, skipping the scraping part.
4. The downloaded content is also passed to `sentiment_analysis.py`, which uses NLTK to calculate the polarity scores of the content. In the case of the pasted content, the content is passed to `sentiment_analysis.py` directly, skipping the scraping part.
5. The summary and the polarity scores are displayed in the `dashboard.py`. 
