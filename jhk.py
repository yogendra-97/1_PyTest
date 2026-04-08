# def sum(a, b):
#     a = input("enter a Num 1")
#     b = input("enter a Num 2")
#     r = a + b
#     return r
# # y = sum(a, b)
#
#
# def add():
#     a = int(input("Enter Num 1: "))
#     b = int(input("Enter Num 2: "))
#     return a + b
# print(add())
#
# class Solution:
#     def hasDuplicate(self):
#         nums = [5, 8, 7, 4, 8]
#         for x in nums:
#             for y in nums:
#                 x_ind = nums.index(x)
#                 y_ind = x_ind + 1
#                 if x == nums[y_ind]:
#                     print("True")
#                     return
#
#         print("False")
#
# obj = Solution()
# obj.hasDuplicate()

import requests

url = "https://httpbin.org/post"

# Data to send as form-encoded
payload = {
    "username": "john_doe",
    "password": "secure123"
}

msg= "Code mismatch"
sr= "None"
try:
    response = requests.post(url, data=payload, timeout=.1)
    response.raise_for_status()  # Raise error for bad status codes
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

except requests.exceptions.RequestException as msg:
    print("Error: ", msg)
    raise