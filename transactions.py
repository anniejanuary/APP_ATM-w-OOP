from account import Account

a = Account()
a.deposit(3700)
print(a)
a.withdrawal(2000)
print(a)
a.withdrawal(9999)  # overdraft
print(a)
