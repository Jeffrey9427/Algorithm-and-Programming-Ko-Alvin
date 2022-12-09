myFile = open("info.txt",'r')

content = myFile.readlines()
print(content)

myFile.close()