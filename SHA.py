import hashlib 
str = "GeeksforGeeks"
result = hashlib.sha256(str.encode())
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest())