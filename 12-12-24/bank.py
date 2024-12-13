class Bank:
    balance = 50000

    def deposit(self):
        amount = int(input("enter amount to deposit:"))
        if(amount <100 or amount>50000):
            print("Minimum deposit is 100 and Maximum deposit is 50000")
        elif(amount%100==0):
            self.balance=self.balance+amount
            print(amount, "is deposited ")
            obj.bal_enquiry()
            print("************Transaction successfull*********")
        else:
            print("amount should be in multiples of 100")

    def withdraw(self):
       amount = int(input("enter amount to withdraw:"))
       min_bal=500
       minacc=self.balance-min_bal
       if (amount < 100 or amount > minacc):
           print("Minimum withdrawl is 100 and Maximum withdrawal is ", minacc,"as there should be a minimum balance of 500 in your acc")
       elif (amount % 100 == 0):
           self.balance = self.balance - amount
           print(amount, "is withdrawn")
           obj.bal_enquiry()
           print("************Transaction successfull*********")
       else:
           print("amount should be in multiples of 100")

    def bal_enquiry(self):
        print("balance:",self.balance)

    def viewoptions(self):
        transac=3
        while(transac>0):
            print("----------------Transaction---------------------")
            print("1.Deposit\n2.Withdraw\n3.Bal Enquiry\n4.exit\nchoose your option :")
            op = int(input())
            if (op == 1):
                obj.deposit()
            elif (op == 2):
                obj.withdraw()
            elif (op == 3):
                obj.bal_enquiry()
            elif (op == 4):
                exit()
            else:
                print("invalid option .....")
            transac=transac-1



    def validate(self):
        chance = 3
        while (chance > 0):
            pin = int(input("enter your pin:"))
            actual_pin = 1234
            if (pin == actual_pin):
                obj.viewoptions()
                break
            else:
                if (chance == 1):
                    print("your card is blocked...")
                else:
                    print("incorrect pin try again...")
            chance = chance-1


obj = Bank()
obj.validate()