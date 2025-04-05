

from firecrawl import FirecrawlApp


API_KEY = "fc-9aa0a9836d094d3a9447e9e740045324"  


app = FirecrawlApp(api_key=API_KEY)
url="https://workat.tech/programs/flipkart-gwc-6/dashboard"
def scrape_webpage(url):
    """Scrapes the given webpage and returns the extracted content."""
    scrape_result = app.scrape_url(url, params={'formats': ['markdown', 'html']})
    return scrape_result  
