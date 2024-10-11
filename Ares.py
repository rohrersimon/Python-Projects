with open('newFile.txt', 'w') as file:
    file.write('Hello, world!')

with open('newFile.txt', 'r') as file:
    content = file.read()
    print(content)
