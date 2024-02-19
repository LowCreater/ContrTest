list1 = ["test", "Hello", "World", "123", "example", "CV", "hp;"]
result_array = []
for i in list1:
    if len(i) <= 3:
        result_array.append(i)
        
print(result_array)
