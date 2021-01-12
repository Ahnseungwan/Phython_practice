# name = "안승완"
# print(name[0])
# name = "1234"
# print(int(name[0]))
# list_a = [1, 2, 3, 4, 5]
# print(list_a[0])
# print(list_a[3])
# list_a[0] = "변경"
# print(list_a)
# list_a[2] = "안승완"
# print(list_a)
# print(list_a[2][2])
# list_b = [3, 4, 5]
# print(list_a + list_b)
# list_a = [1, 2, 3]
# list_a.append(4)
# print(list_a)
# list_a.insert(1,"hello")
# print(list_a)
# del list_a[0]
# print(list_a)
# list_a.pop(1)
# print(list_a)
# print(3 in list_a)
# print("hello" in list_a)
# for 반복자 코드 in 반복할수 있는것
# array = [121, 222 ,345, 124]
# # for element in array:
# #     print(element)
# for charater in "안녕하세요":
#     print(charater)
# dict_a = {"name": "어벤져스", "감독": "몰라"}
# print(dict_a["name"])
# dict_a["name"] = "스파이더맨"
# print(dict_a["name"])
# dict_a["type"] = "action"
# print(dict_a)
# del dict_a["name"]
# print(dict_a)
dictionary = {
    "name" : "안승완",
    "나이" : "26"
}

# key = input("값을 입력하시오 ")

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("값이 없습니다.")

# for key in dictionary:
#     print(key)
# print(list(range(10)))
# for i in range(10):
# #     print(str(i))
# i = 0
# while i < 10:
#     print("{}번째 반복입니다.".format(i))
#     i += 1

# i = 0
# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i += 1
#     input_text = input("종료하시겠습니까. ")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다. ")
#         break

numbers = [5, 15, 6, 20, 7, 25]
for number in numbers:
    if number < 10:
        continue 
    print(number)