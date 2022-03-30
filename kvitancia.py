import random


class receip:
    """Номер квитанции"""

    def __init__(self, receipt):
        self.receipt = receipt

    def Kv(self):
        print("Квитанция №: ".format(self.receipt), format(random.randint(1, 1000)))


class Date:
    """Дата приёмки"""

    def __init__(self, acceptance_date):
        self.acceptance_date = acceptance_date

    def date(self):
        import datetime
        self.acceptance_date = datetime.datetime.now()
        print("Дата приёмки: ", self.acceptance_date.__str__())


class Date_of_completion(Date):
    """Дата выполнения заказа"""

    def __init__(self, date_of_completion, acceptance_date):
        super().__init__(acceptance_date)
        self.date_of_completion = date_of_completion

    def date_of_completion(self):
        import random
        from datetime import datetime, timedelta

        self.acceptance_date = datetime.now()
        end = self.acceptance_date + timedelta(days=5)
        date_of_completion = self.acceptance_date + (end - self.acceptance_date) * random.random()
        print("Дата выполнения заказа: ", date_of_completion)
class Status(Date):
    """Статус заказа"""
    def __init__(self, status, acceptance_date):
        super().__init__(acceptance_date)
        self.status = status
    def st(self):
        import datetime
        if datetime == self.acceptance_date:
            print("Ремонтируется: ")



#     """
# номер квитанции
# тип изделия (телефон, ноутбук, телевизор)
# дата приемки
# дата выполнения ремонта
# ФИО человека, который сдал в ремонт техники
# статус (ремонтируется, готово, выдано клиенту)"""
