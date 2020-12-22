import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    mobNo = 0
    
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.mobNo = int(input("Enter the Mobile no : "))
        self.deposit = int(input("Deposite Initial amount >=1000 :"))
        print("\n\n**Account Created**")
        print("\n\n")
    
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Mobile Number : ",self.mobNo)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.mobNo = input("Modify Mobile Number :")
        self.deposit = int(input("Modify Balance :"))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",item.mobNo,"  ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):    
        return self.name
    def getMobileNo(self):
        return self.mobNo
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def projectName():
 
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\tCREATED BY DABLU_KUMAR")
    print("\t\t")
    print("\tWELCOME TO BANK OF IITGN")
    print("\t\t")


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def showRecord():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo,"  ", item.name, "  ",item.mobNo,"  ",item.type, "  ",item.deposit )
        infile.close()
    else :
        print("No records found")
        

def showBal(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Your account Balance is = ",item.deposit)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("You cannot withdraw larger amount")
                
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAcc(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAcc(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter the account holder name : ")
                item.mobNo = int(input("Enter the Mobile Number : "))
                item.type = input("Enter the account Type : ")
                
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        

ch=''
num=0
projectName()

while ch != 8:
    print("\t\t")
    print("\tMAIN MENU:-")
    print("\t1. CREATE NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. CHECK BALANCE")
    print("\t5. SHOW ALL ACCOUNTS LIST")
    print("\t6. CLOSE ACCOUNT")
    print("\t7. MODIFY ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input()
   
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        showBal(num)
    elif ch == '5':
        showRecord()
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAcc(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAcc(num)
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")
