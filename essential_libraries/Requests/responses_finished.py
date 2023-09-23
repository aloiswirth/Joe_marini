# Python Essential Libraries by Joe Marini course example
# Example file for Requests library
import requests

# TODO: work with status codes
# resp = requests.get('https://httpbin.org/status/200')
# print(resp.status_code)
# resp.raise_for_status()

# TODO: examine response encoding
# resp = requests.get('https://httpbin.org/robots.txt')
# print(f'resp.encoding is {resp.encoding}')
# # the text property accesses decoded text content
# print(f'resp.text is \n {resp.text}')
# # the content property provides access to raw bytes
# print(f'resp.content is \n {resp.content}')

# TODO: To read JSON content, use the json() function
resp = requests.get('https://httpbin.org/json')
# print(f'resp.json() is \n {resp.json()}')
print(f'resp.headers is \n {resp.headers}')
print(f'resp.headers[content-type] is \n {resp.headers["content-type"]}')
print(f'resp.headers[content-type] is \n {resp.headers["Content-Type"]}')
# resp = requests.options('https://httpbin.org')
# print(resp.headers['allow'])