import trafilatura as tfl

def extract_article_text(url):
    downloaded = tfl.fetch_url(url)
    if downloaded:
        result = tfl.extract(downloaded, include_comments=False, include_tables=True, with_metadata=False)
        return result
    else:
        return None
