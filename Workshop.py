class Name:
    def __init__(self, Name):
        self.Name = Name

    def Nam(self):
        with open('file_name.txt', 'a+') as file:
            self.Name = input("Введите ФИО: ")
            print('FIO: ', self.Name, file=file)


t = Name('')
t.Nam()


class Vibor:

    def __init__(self, Vibor, product_type):
        self.Vibor = Vibor
        self.product_type = product_type

    def Vib(self):

        with open('file_name.txt', 'a+') as file:
            self.Vibor = input("Напишите ваш выбор(ноутбук, телефон, телевизор): ")
            print('Тип изделия: ', self.Vibor, file=file)
            self.product_type = ['ноутбук', 'телефон', 'телевизор']

        if self.Vibor == self.product_type[0]:
            from texnica import laptop

            l = laptop("", "", "", "")
            l.parLap()


        elif self.Vibor == self.product_type[1]:
            from texnica import telephon

            tel = telephon("", "", "")
            tel.parTel()

        elif self.Vibor == self.product_type[2]:
            from texnica import Tv

            T = Tv("", "", "")
            T.parTv()



        else:
            print("Введите правильно")


V = Vibor('', '')
V.Vib()
from kvitancia import receip

r = receip("")
r.Kv()
import sys
with open("file_name.txt", 'r') as file:
    for line in file:
        if not line.isspace():
            sys.stdout.write(line)




from kvitancia import Date

t = Date("")
t.date()
from kvitancia import Date_of_completion

d = Date_of_completion("", "")
d.date_of_completion()

from kvitancia import Status
S = Status("","")
S.st()


