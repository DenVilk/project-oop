import datetime
import random



class Device:

    def __init__(self, mark, description):
        self._mark = mark
        self._description = description

    def __str__(self):
        return f"Mark: {self._mark}, Description: {self._description}"


class Phone(Device):

    name = "Phone"

    def __init__(self, mark, os, description):
        super(Phone, self).__init__(mark, description)
        self._os = os

    def __str__(self):
        return f"{super().__str__()}, OS: {self._os}"


class Notebook(Device):

    name = "Notebook"

    def __init__(self, mark, os, dateofmanufacturing, description):
        super(Notebook, self).__init__(mark, description)
        self._dateOfManufacturing = dateofmanufacturing
        self._os = os

    def __str__(self):
        return f"{super().__str__()}, OS: {self._os}, Date of manufacturing: {self._dateOfManufacturing}"


class TV(Device):

    name = "TV"

    def __init__(self, mark, diagonal, description):
        super(TV, self).__init__(mark, description)
        self._diagonal = diagonal

    def __str__(self):
        return f"{super().__str__()}, Diagonal: {self._diagonal}"


class Receipt:

    def __init__(self, num, typeofproduct, dateofreceiving, dateofrepair, initials, status):
        self._num = num
        self._typeOfProduct = typeofproduct
        self._dateOfReceiving = dateofreceiving
        self._dateOfRepair = dateofrepair
        self._initials = initials
        self._status = status

    listOfProducts = [Phone, Notebook, TV]
    listOfStatuses = ["repairing", "done", "issued"]

    @property
    def initials(self):
        return self._initials

    def __str__(self):
        return f"Number of receipt: {self._num}, Type of product: {self._typeOfProduct}, Date of receiving: " \
               f"{self._dateOfReceiving}, Date of repair: {self._dateOfRepair}, Initials: {self._initials}, Status: {self._status} "


receiptsdict = {}


def createrepairrequest():
    initials = input("Please, input your initials: ")

    print("Choose the type of product you want to repair: ")
    for i in range(len(Receipt.listOfProducts)):
        print(f"{i + 1}. {Receipt.listOfProducts[i].name}")
    typeofproduct = Receipt.listOfProducts[int(input()) - 1]

    mark = input("Input mark: ")
    description = input("Input description: ")

    d = None

    if typeofproduct is Phone:
        os = input("Input OS: ")
        d = Phone(mark, os, description)

    if typeofproduct is Notebook:
        os = input("Input OS: ")
        dateofmanufacturing = input("Input date of manufacturing: ")
        d = Notebook(mark, os, dateofmanufacturing, description)

    if typeofproduct is TV:
        diagonal = input("Input diagonal: ")
        d = TV(mark, diagonal, description)

    typeofproduct = d

    dateofreceiving = datetime.date.isoformat(datetime.date.today())
    status = "repairing"

    if not receiptsdict.keys():
        num = 1
    else:
        num = list(receiptsdict.keys())[-1] + 1

    dateofrepair = datetime.date.today() + datetime.timedelta(random.randint(1, 5))

    r = Receipt(num, typeofproduct, dateofreceiving, dateofrepair, initials, status)

    receiptsdict[num] = r


def receiptsprint(sw):
    if sw == 0:
        for i, k in receiptsdict.items():
            print(f"Receipt number: {i}, Info: {k}")
    elif sw > 0 and sw in receiptsdict.keys():
        print(f"Receipt number: {sw}, Info: {receiptsdict.get(sw)}")


def receiptsinfo():
    print(list(receiptsdict.keys()))

    info = input("Enter your receipt's number or initials: ")

    if info.isnumeric():
        info = int(info)
        if info in list(receiptsdict.keys()):
            for i in receiptsdict.keys():
                if i == info:
                    print(receiptsdict[i])
        else:
            print("Receipt with this number is not found")
    else:
        isfound = False
        for i in range(1, len(list(receiptsdict.values()))+1):
            if receiptsdict.get(i).initials == info:
                receiptsprint(i)
                isfound = True
        if not isfound:
            print("Receipts ordered with this initials are not found")


def menu():
    print("Choose an action:")
    print("1. Create repair request")
    print("2. Show info about receipt(s)")
    print("3. Print")

    sw = int(input())

    if sw == 1:
        createrepairrequest()
    elif sw == 2:
        receiptsinfo()
    elif sw == 3:
        receiptsprint(0)
    else:
        print("Please, enter the correct number")
        return 0


while True:
    menu()
