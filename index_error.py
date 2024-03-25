"""this is a test for pylint"""
fruits_list = ["orange", "apple", "banana"]
print(fruits_list[3]) #index_error

test = fruits_list[3]
print(test)

def add(a, b):
    return a + c  # 'c' は未定義
  
def multiply(a, b):
    return a * b
print(multiply("Hello", 3))  # 文字列と整数の乗算はできない
