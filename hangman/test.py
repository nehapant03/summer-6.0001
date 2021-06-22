import string

output = string.ascii_lowercase
print(output)
print(output.find(""))

output = output[0: 0] + output[1:26]
print(output)