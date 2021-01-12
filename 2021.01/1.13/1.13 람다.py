# def call_10_times(func):
#     for i in range(10):
#         func()

# def print_hello():
#     print("안녕하세요")

# call_10_times(print_hello)

# map , filter
# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3

# list_input_a = [1, 2, 3, 4, 5]

# output_a = map(power, list_input_a)
# print(list(output_a))

# output_b = filter(under_3, list_input_a)
# print(list(output_b))

# # 람다로 바꾼다.
# power = lambda x : x * x
# under_3 = lambda x : x < 3
# list_input_a = [1, 2, 3, 4, 5]

# output_a = map(power, list_input_a) # 또는 output_a = map(lambda x : x * x, list_input_a)가능 
# print(list(output_a))
# output_b = filter(under_3, list_input_a)
# print(list(output_b))