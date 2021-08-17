address = ['Flat Floor Street', '18', 'New York']
pins = {'Mike':1234, 'Joe':1111, 'Jack':2222}

print(address[0], address[1])

pin = int(input("Entre com seu pin: "))

def find_in_file(f):
    myfile = open('.\sample.txt')
    fruits = myfile.read()
    myfile.close()
    fruits = fruits.splitlines()
    print(fruits)
    if f in fruits:
        return "Esta fruta está na lista."
    else:
        return 'Fruta não encontrada!'
    
if pin in pins.values():
    fruit = input("Pesquise uma fruta: ")
    print(find_in_file(fruit))
else:
    print("Pin incorreto!")
    print("Esta informação pode ser acessada somente por: ")
    for key in pins.keys():
        print(key)
