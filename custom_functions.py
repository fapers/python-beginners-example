def calculate_age(year):
    age = 2021 - year
    return age

print(calculate_age(1946))

def returning():
    return 10

def printing():
    print(10)

print(type(returning()))
print(type(printing()))
    
print(returning() + 20)
# print(printing() + 20)

def calculate_length(a):
    return len(a)

# a = input('Entre com uma string: ')
# print(calculate_length(a))

''' Custom Functions with Multiple Parameters '''
def converter(original_unit, coefficient=0.3048):
    return original_unit * coefficient

print(converter(10))
print("\n--------------------\n")

def convert_temperature(C):
    return C*9/5+32
print(convert_temperature(32))

def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers don't have length"
    elif type(mystring) == float:
        return "Sorry, floats don't have length"
    else:
        return len(mystring)
print(string_length(float(input('número: '))))
