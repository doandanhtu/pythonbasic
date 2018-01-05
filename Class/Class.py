class Car:
    pass

car = Car()
#naming: Camel case convention

print(type(car))
print(type(Car))


class BankAccount:
    rate = 0.0
    #rate is a class variable, it is the same for all objects of this class

    @staticmethod
    def setInterestRate(newRate):
        BankAccount.rate = newRate

    #this is a method used to change a pre-defined class variable

BankAccount.setInterestRate(0.01)
BankAccount1 = BankAccount()
BankAccount2 = BankAccount()

print(BankAccount.rate)
print(BankAccount1.rate)
print(BankAccount2.rate)

BankAccount.setInterestRate(0.02)
print(BankAccount.rate)
print(BankAccount1.rate)
print(BankAccount2.rate)