list1 = ["jytf", "Hello", "World", "123", "example", "CV", "hp;"]
def array(list, k):
    result_array = []
    for i in list:
        if len(i) <= k:
            result_array.append(i)
    return result_array
print(array(list1, 3))