def deposit(balance, money): # 입금 balance - 잔액, money - 입금하려는 금액
    print("입금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money # 반환

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000) # 출금 불가
# balacne = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))