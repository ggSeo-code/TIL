
class Account:
    __balance = 0

    # 기본 생성자
    def __init__(self):
        self.__balance = 0

    # getter() 작성
    def getBalance(self):
        return self.__balance

    # 입금 메소드 만들기
    def deposit(self, amount):
        self.__balance += amount
        print("통장에", format(amount,","),"원이 입금됨")
        print("현재잔액 :",format(self.__balance,","),"원")

    # 출금 메소드 만들기
    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에", format(amount,","),"원이 출금됨")
        print("현재잔액 :",format(self.getBalance(),","),"원")

if __name__ == "__main__":
    account = Account()
    account.deposit(1000000)
    account.withdraw(200000)