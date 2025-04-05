import requests


email = "sailikhithanekkalapu@gmail.com"
password = "Shivarama@29"


def get_alai_access_token(email, password):
    auth_url = "https://api.getalai.com/auth/v1/token?grant_type=password"

    headers = {
        "Content-Type": "application/json",
        "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVzY2hvdHRoamdsamJ4amVyY3puIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTAxMTI0NzYsImV4cCI6MjAyNTY4ODQ3Nn0.3pZ7fQ9qWjBcX-oSLJ37P4D9ojrdTF1zdI1B4ONcxrE"
    }

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(auth_url, json=payload, headers=headers)
    print("Status:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print("🔑 Auth Success")
        return data["access_token"]
    else:
        print("❌ Auth Error:", response.status_code, response.text)
        return None




def update_alai_presentation(access_token, presentation_id, slides):
    url = "https://alai-standalone-backend.getalai.com/get-calibration-sample-text"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }


    raw_context = "\n\n".join(slide["content"] for slide in slides)

    payload = {
        "presentation_id": presentation_id,
        "raw_context": raw_context 
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("✅ Presentation Updated:", response.json())
        return f"https://app.getalai.com/presentation/{presentation_id}"
    else:
        print("❌ Update Failed:", response.status_code, response.text)
        return None


if __name__ == "__main__":
    print("🔍 Scraping webpage...") 
    print("🔐 Authenticating with Alai...")

    token = get_alai_access_token(email, password)

    if token:
        presentation_id = "7829426a-6765-4246-82a1-c08d4795b4d5"

        slides = """
        # DSA Practice

        ## Curated Interview Questions

        [Basic Coding For Beginners](https://workat.tech/problem-solving/lists/beginner-problems/practice)

        [Data Structures & Algorithms](https://workat.tech/problem-solving/lists/dsa-problems/practice)

        [Topics](https://workat.tech/problem-solving/practice/topics) 
        [Companies](https://workat.tech/problem-solving/practice/companies) 
        [Sheets](https://workat.tech/problem-solving/practice/lists)
        """

        print("⚙️ Updating Alai Presentation...")
        link = update_alai_presentation(token, presentation_id, slides)

        if link:
            print("✅ Presentation URL:", link)
    else:
        print("❌ Authentication failed.")
