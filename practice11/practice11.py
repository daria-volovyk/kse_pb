import requests
response=requests.get("https://www.gutenberg.org/files/74/74-0.txt")
print(response.status_code)
text=response.text
with open("/Users/apple/kse_pb/practice11/text.txt", 'w') as f:
    f.write(text.txt)