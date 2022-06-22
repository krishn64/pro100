class Atm(object):

 def __init__(self,atmcardnumber , pinnumber) :
        self.atmcardnumber=atmcardnumber
        self.pinnumber=pinnumber


    
 def Withdrawl(self):
      print("CashWithdrawl")


 def Balance(self):
      print("BalanceEnquiry")

axis = Atm("444555","333333333")
print(axis.atmcardnumber)
print(axis.pinnumber)


axis.Withdrawl()
axis.Balance()


      



     
    