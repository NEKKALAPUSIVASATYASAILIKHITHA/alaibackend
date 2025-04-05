
 
from scraper import scrape_webpage
from alai_api import get_alai_access_token, update_alai_presentation

def generate_presentation_from_webpage(url, email, password, presentation_id):
    """Automates scraping and presentation update."""
    print("Scraping webpage...")
    content = scrape_webpage(url)

    if not content:
        print("No content extracted.")
        return None

    print("Authenticating with Alai...")
    access_token = get_alai_access_token(email, password)
    if not access_token:
        print("Authentication failed.")
        return None

    print("Generating slides...")
    slides = [{"content": section.strip()} for section in content['markdown'].split("\n") if section.strip()][:5]

    print("Updating Alai Presentation...")
    presentation_link = update_alai_presentation(access_token, presentation_id, slides)

    if presentation_link:
        print("✅ Alai Presentation Updated:", presentation_link)
    else:
        print("❌ Failed to update presentation.")


if __name__ == "__main__":
    website_url = "https://workat.tech/programs/flipkart-gwc-6/dashboard" 
    email = "sailikhithanekkalapu@gmail.com"
    password = "Shivarama@29"
    presentation_id = "7829426a-6765-4246-82a1-c08d4795b4d5"  

    generate_presentation_from_webpage(website_url, email, password, presentation_id)
