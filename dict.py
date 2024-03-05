# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python.
#   Esse código tem como objetivo explicar dicionarios.
# EN: 
#   This is a comment and will be ignored by Python.
#   This code has the objective to explain dictionaries.

my_dict = {}
my_dict = {'id': 1, 'name': 'Cliff Burton'}
print(type(my_dict))
print(my_dict['id'])
print(my_dict['name'])
my_dict = dict(id=1, name='David Ellefson')
print(my_dict)
print(type(my_dict))
my_dict['age'] = '59'
print(my_dict)
print('--------')
for key in my_dict:
    print(key)
print('--------')
for key, values in my_dict.items():
    print(f"{key}: {values}")
