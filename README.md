**Итоговая контрольная работа**

1. Ввод условного списка _**list1**_ с элементами типа _**str**_
```
list1 = ["jytf", "Hello", "World", "123", "example", "CV", "hp;"]
```
2. Создаем пустой список _**result_array**_, в который будем добавлять нужные нам элементы списка _**list1**_
``` 
result_array = []
```
3. Создаем метод _**array**_, который будет отбирать все элементы из списка *list1* с количеством символов 3 и меньше.
```
def array(list, k):
```
4. Создаем цикл _**for**_, который будет сравнивать элементы списка _**list1**_ с дальнейшим условием.
```
for i in list:
```
5. Добавляем условие _**if**_, которое будет добавлять к пустому списку _**result_array**_ элементы, соотвутствующие нашему условию (кол-во символов <=3 )
```
if len(i) <= k:
    result_array.append(i)
```
