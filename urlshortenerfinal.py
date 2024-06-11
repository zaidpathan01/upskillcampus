import urllib.request
import urllib.parse

def shorten_url(long_url):
    api_url = "https://tinyurl.com/api-create.php"
    data = {"url": long_url}
    # Ensure encoded_data is defined within the function
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")

    try:
        response = urllib.request.urlopen(api_url, encoded_data)
        # ... (rest of the code)
    except Exception as e:
        print(f"Error shortening URL: {e}")
        return None

while True:
    long_url = input("Enter a long URL to shorten (or 'q' to quit): ")

    if long_url.lower() == 'q':
        break

    short_url = shorten_url(long_url)

    if short_url:
        print(f"Shortened URL: {short_url}")
    else:
        print("Your URL link is in invaild format.")

