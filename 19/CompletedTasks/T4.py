with open("example.txt","r") as file:
    content = file.read()


with open("example2.txt","w") as file_w:
    file_w.write(content)