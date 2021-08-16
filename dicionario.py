'''Tuplas (), o conteúdo não pode ser alterado ou removido'''
teste = (1,2,3)
print(teste[1])

'''Dicionário {}, possui chave e valor e pode ser acessado pela chave'''
pins = {"Mike":1234, "Joe":1111, "Jack":2222}
print(pins['Jack'])
print(pins.keys())
print(pins.values())

person97 = {"name":"Jack", "surname":"Smith", "age":"29"}
print(person97)

# Removing pair "name":"Jack"
person97.pop("name")
print(person97)

# Adding new pair "name":"Jack"
person97["name"] = "Jack"
print(person97)
{'surname': 'Smith', 'age': '29', 'name': 'Jack'}

# Changing an existing value
person97["age"] = 30
print(person97)
{'surname': 'Smith', 'age': 30, 'name': 'Jack'}

# Mapping two lists to a dictionary:
keys = ["a", "b", "c"]
values = [1, 2, 3]
mydict = dict(zip(keys, values))
print(mydict)
