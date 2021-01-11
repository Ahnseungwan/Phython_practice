# print(len("안녕하세요"))
# def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요", 5)
 
# 가변 매개변수
# def print_n_times(n, *values):
#     # n번 반복합니다.
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times(3, "안녕하세요," "즐거운", "파이썬 프로그래밍")

# def test(a, b=10, c=100):
#     print(a + b + c)

# test(10, 20, 30) #60
# test(a=10 , b=100, c=200) # 310
# test(c=10, a=100, b=200)  # 310
# test(10, c=200) # 220

# value = input("입력하시오 ")
# print(value)

# 리턴하기
# def return_test():
#     print("A 위치입니다.")
#     return
#     print("B 위치입니다. ")

# return_test() 

# def return_test():
#     return 100

# value = return_test()
# print(value)

# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i

    return output

print("0 to 100", sum_all(0,100))
