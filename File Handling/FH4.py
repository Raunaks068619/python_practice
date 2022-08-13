with open("FH1.txt") as f:
    content_list = f.readlines()
print(content_list)
content_list = [x.strip() for x in content_list]
print(content_list)
