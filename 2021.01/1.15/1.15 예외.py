# user_input_a = input("정수 입력")

# if user_input_a.isdigit():
#     number_input_a = int(user_input_a)
#     print("원의 반지름:",number_input_a)
# else :
#     print("정수를 입력하지 않았습니다.")

# #try except
# try:
#     number_input_a = int(input("정수 입력"))

#     print("원의 반지름:",number_input_a)
# except:
#     print("무언가 잘못되었습니다.")

# list_input_a = ["52", "273", "32", "스파이", "103" ]

# list_number = []
# for item in list_input_a:
#     try:
#         float(item)
#         list_number.append(item)
#     except:
#         pass

# print("{}내부에 있는 숫자는".format(list_input_a))
# print("{}입니다.".format(list_number))

# #파일이 제대로 닫혓는지 확인하기
# try:
#     file = open("info.txt", "w")
#     file.close()
# except Exception as e:
#     print(e)
# print(file.closed)

# try 구문 내부에서 return 키워드를 사용하는 경우
# def test():
#     print("test() 함수의 첫 줄입니다.")
#     try:
#         print("try 구문이 실행되었습니다.")
#         return
#         print("try 구문의 return 키워드 뒤입니다.")
#     except:
#         print("except 구문이 실행되었습니다.")
#     else:
#         print("else 구문이 실행되었습니다.") 
#     finally:
#         print("finally 구문이 실행되었습니다.")

# test()

# 예외 처리 고급

# list_number = [52, 2342, 45, 324, 100]
# try:
#     number_input = int(input("정수입력"))
#     print("{}번째 요소:{}".format(number_input, list_number[number_input]))
# except Exception as exception:
#     print(exception)


# list_number = [52, 35 , 456, 45 , 34]

# try:
#     number_input = int(input("정수 입력"))
#     print("{}번째 요소:{}".format(number_input, list_number[number_input]))
# except ValueError:
#     print("정수를 입력하세요")
# except IndexError:
#     print("리스트의 인덱스를 벗어났어요")

# 잡지 못하는 에러
list_number = [52, 35 , 456, 45 , 34]

try:
    number_input = int(input("정수 입력"))
    print("{}번째 요소:{}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    print("정수를 입력하세요")
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요")
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(excpetion)