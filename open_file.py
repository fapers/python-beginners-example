myfile = open("sample.txt")
print(myfile.read())
myfile.seek(0)
print(type(myfile))
print(dir(myfile))
content = myfile.read()
myfile.close()
print(content)
print(type(content))
print(dir(content))
