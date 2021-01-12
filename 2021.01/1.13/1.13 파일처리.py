# file = open("basic.txt","w")

# file.write("Hello")

# file.close()

# # with로하기
# with open("basic.txt","w") as file:
#     file.write("Hello")

# with open("basic.txt","r") as file:
#     contents = file.read()
# print(contents)

# 손코딩
# import random

# hanguls = list("hidfaldjflkajfa")
# with open("info.txt","w") as file:
#     for i in range(5):
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40, 100)
#         height = random.randrange(140, 200)

#         file.write("{}, {}, {}\n".format(name, weight, height))