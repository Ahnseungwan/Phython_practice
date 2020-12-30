# 애완동물을 소개해 주세요
animal = "고양이"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+ animal +"의 이름은 "+ name +"예요")
hobby = "공놀이"
# print(name + "는" + str(age) + "살이며, "+ hobby + "을 아주 좋아해요") #정수 앞에선 str을 넣어준다
print(name, "는" , age , "살이며, ",hobby,"을 아주 좋아해요") #정수 앞에선 str을 넣어준다
print(name + "는 어른일까요? " + str(is_adult)) #True같은 경우도 str 해준다
