import random
class BankAccount:
    def __init__(self):
        print("..............Welcome.................")
        print(".............UMETU BANK.................")
        self.name=input("Enter your name :")
        self.address=input("Enter your address :")
        self.account=random.randint(100000000,9999999999)
        while True:
            self.count=int(input(".........deposite some money for creating your account............. \n minimum money which you can deposite is 1000 :\n Now!!Enter the money :"))
            if(self.count>=1000):
                break
            print("plase ! Enter valid amount you deposit only",self.count,"\nthat was not enough plzz min deposite 1000")
            print("now you cant register ")
        print("Account created successfully!")
        print("Account Number:", self.account)
        self.bankstatus()
    def deposite_money(self):
        money=int(input("Enter the money : "))
        self.count+=money
        print("Updated balance : ",self.count)
    def withdraw_money(self):
        money=int(input("enter withdrow money : "))
        if(money<self.count):
            self.count-=money
            print("Withdrawal successful !")
            print("Now ! \nyour current balance ",self.count)
        else:
            print("you have not enough money")
            print("your current balance is ::",self.count)
    def current_status(self):
        print("..............Account Details............ ")
        print("your name :",self.name)
        print("account number :",self.account)
        print("bank balance :",self.count)
        print("your address :",self.address)
    def bankstatus(self):
        while True:
            num=int(input("What you want \n 1:check status \n2:Deposite money\n3:Withdrow money\n4 : for exit Enter the num :"))
            if num==1:
                self.current_status()
            elif num==2:
                self.deposite_money()
            elif num==3:
                self.withdraw_money()
            elif num==4:
                print("Thank you for using UMETU BANK")
                break
            else:
                print("Invalid choice")
obj=BankAccount()
    