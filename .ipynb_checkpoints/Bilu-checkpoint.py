from datetime import datetime
import time

class Bilu:

    def __init__(self, nome):
        print(f'Olá {nome}, o bilu foi criado')
        self.name = nome
        self.day = datetime.now().day + 1

    def __del__(self):
        print('bilu esta deixando de existir')

    def __enter__(self):
        print('abriu')
        self.f = open('teste.txt', 'w')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.f.close()
        print('fechou')

    def escreve(self, text):
        self.f.write(text)

    def diga_oi(self):
        print(f'oi {self.name}')

    def diga_o_dia(self):
        print(f'hj é dia {self.day}')


with Bilu('cinthia') as b:
    b.diga_oi()
    for i in range(10):
        b.escreve(f'faltam {10 - i} segundos para bilu sumir\n')
        print(f'faltam {10 - i} segundos para bilu sumir')
        time.sleep(1)
    b.diga_o_dia()