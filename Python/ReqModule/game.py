import requests
word = input("What word would you like to translate?  ")
url = "https://example.com"
params = {"word":word}
response = requests.get(url, params)
print(f"Status Code: {response.status_code}")
print(response.text)