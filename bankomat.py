class Konto:
    def __init__(self,kontonummer:str):
        self.__Saldo = 0
        self.__Kontonummer = kontonummer
    def Withdraw(self, belopp) -> bool:
        if self.__Saldo < belopp:
            return False
        self.__Saldo = self.__Saldo - belopp
        return True
    def Deposit(self, belopp):
        self.__Saldo = self.__Saldo + belopp

allaKonton = {}
allaKonton["12345"] =  Konto("12345")
allaKonton["11122"] =  Konto("11122")

knr = input("Ange kontonummer")
konto = allaKonton[knr]
if konto.Withdraw(500) == False:
    print("Gick inte")
else:
    print("Uttag klart")

