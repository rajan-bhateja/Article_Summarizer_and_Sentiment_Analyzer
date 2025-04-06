import trafilatura as tfl

def extract_article_text(url):
    downloaded = tfl.fetch_url(url)
    if downloaded:
        result = tfl.extract(downloaded, include_comments=False, include_tables=False, with_metadata=True)
        return result
    else:
        return None
