# Python Essential Libraries by Joe Marini course example
# Example file for using Requests library
import requests

# TODO: create a basic request for data
# resp = requests.get("http://httpbin.org/xml")
# print(resp.status_code)
# print(resp.text)

# TODO: create a request using parameters
# my_args = {"mama": 1, "papa": "two", "grandpa": False}
# resp = requests.get("http://httpbin.org/get", params=my_args)
# print(resp.text)
# # print(resp.url)
# # print(resp.reason)
# # print(resp.cookies)
# # print(resp.history)


# TODO: create a request using POST
# resp = requests.post("http://httpbin.org/post", data={"alois": "my_value"})
# print(resp.text)

# TODO: create a request using custom headers
heads = {"my-custom-header": "This is a custom header"}
resp = requests.get("http://httpbin.org/get")
print(resp.text)
