import streamlit as st
from Demos.win32console_demo import window_size

from scraper import extract_article_text

st.title('News Summarizer and Sentiment Analyzer')
st.header('Get summarized news articles')
st.set_option(window_size='wide')

col1, col2, col3 = st.columns(3)
global full_text

with col1:
    with st.form(key='form'):
        url = st.text_input('Enter URL:', placeholder='URL should be a Times of India URL')
        submit = st.form_submit_button('Submit', 'secondary')

        if submit and url:
            full_text = extract_article_text(url)
            if full_text:
                st.success('Article extracted successfully!')
                # print(type(full_text))
                # print(full_text['Title'])
            else:
                st.error('Failed to extract article. Try a different URL.')
        else:
            st.warning('URL cannot be empty!')

with col2:
    st.subheader('Summary:')

with col3:
    st.subheader('Sentiment Analysis:')

