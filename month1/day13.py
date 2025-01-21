#A Python script that fetches data from a public API and displays the content
import requests

def fetch_data_from_api():
    # Public API URL
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # Sending a GET request to the API
        response = requests.get(url)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Display the content
        print("Fetched Data:")
        for post in data[:5]:  # Limiting to the first 5 entries for readability
            print(f"ID: {post['id']}, Title: {post['title']}")
            print(f"Body: {post['body']}\n")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_data_from_api()
