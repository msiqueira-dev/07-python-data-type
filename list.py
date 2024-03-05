# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python.
#   Esse código tem como objetivo explicar listas.
# EN: 
#   This is a comment and will be ignored by Python.
#   This code has the objective to explain lists.

my_list = []
print(type(my_list))
print(len(my_list))
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list)
my_list = [1, 2, 3]
print(my_list)
print('--------')
for item in my_list:
    print(item)
print('--------')
my_list.remove(1)
print(my_list)
my_list.append(1)
print(my_list)
my_list.sort()
print(my_list)
my_list.pop()
print(my_list)
my_list.append(3)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.insert(0, 1)
print(my_list)