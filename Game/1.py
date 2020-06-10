with open("./a.txt","r+") as f:
    for content in f:
            print(content.rstrip())