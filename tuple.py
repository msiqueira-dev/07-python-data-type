# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python.
#   Esse código tem como objetivo explicar tuplas.
# EN: 
#   This is a comment and will be ignored by Python.
#   This code has the objective to explain tuples.

my_tuple = ()
print(type(my_tuple))
my_tuple = (1, 2)
print(my_tuple)
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(type(my_tuple))
print(my_tuple)
my_tuple = ('a', )
print(my_tuple)
print(type(my_tuple))
my_tuple += ('b', )
print(my_tuple)
my_tuple += ('c', )
print(my_tuple)
print(type(my_tuple))