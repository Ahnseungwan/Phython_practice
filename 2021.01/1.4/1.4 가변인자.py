# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end가 있으면 출력되고 줄바꿈이 생기지않고 빈칸이 생긴다.
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end가 있으면 출력되고 줄바꿈이 생기지않고 빈칸이 생긴다.
     for lang in language:
         print(lang, end=" ")
     print() # 줄바꿈 위해서 넣음

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "kotlin", "Swift")