
from datetime import datetime

class Kiosk:
    def __init__(self): 
        self.menu = [
            ['americano', 2000],
            ['latte', 3000],
            ['mocha', 3000],
            ['yuza_tea', 2500],
            ['green_tea', 2500],
            ['choco_latte', 3000]
        ] # 파일 실행시 출력 되는 다차원 변수 생성
        self.order_menu = []
        self.order_price = []
        self.price_sum = 0
        # 주문한 음료 및 가격 저장

    def menu_print(self): # 메뉴 출력
        print("\n[📋 메뉴판]")
        for i, (name, price) in enumerate(self.menu, 1):
            print(f"{i}. {name} : {price}원")
            # 사용자가 입력한 번호 다차원 변수 출력 

    #주문 처리
    def menu_select(self):
        while True:
            try:
                n = int(input("음료 번호를 입력하세요 : ")) # 음료 번호 입력
                if 1 <= n <= len(self.menu): 
                    t = 0
                    while t != 1 and t != 2: # ice or hot 주문 처리
                        t = int(input("HOT 음료는 1, ICE 음료는 2를 입력하세요 : "))
                        if t == 1:
                            self.temp = "HOT"
                        elif t == 2:
                            self.temp = "ICE"
                        else:
                            print("1과 2 중 하나를 입력하세요.")
                    name, price = self.menu[n - 1]
                    self.order_menu.append(f"{self.temp} {name}")
                    self.order_price.append(price)
                    self.price_sum += price # 주문 저장
                    print(f"{self.temp} {name} : {price}원") #주문한 음료 출력
                    break
                else:
                    print("없는 메뉴입니다. 다시 입력하세요.")
            except:
                print("숫자를 입력해주세요.")

        #추가 주문 
        while True:
            print()
            try:
                n = int(input("추가 주문은 음료 번호를, 지불은 0을 입력하세요 : ")) #추가 주문 반복문
                if n == 0:
                    print("주문이 완료되었습니다.")
                    break
                elif 1 <= n <= len(self.menu):
                    t = 0
                    while t != 1 and t != 2:
                        t = int(input("HOT 음료는 1, ICE 음료는 2를 입력하세요 : "))
                        if t == 1:
                            self.temp = "HOT"
                        elif t == 2:
                            self.temp = "ICE"
                        else:
                            print("1과 2 중 하나를 입력하세요.")
                    name, price = self.menu[n - 1]
                    self.order_menu.append(f"{self.temp} {name}")
                    self.order_price.append(price)
                    self.price_sum += price
                    print(f"추가 주문 음료 {self.temp} {name} : {price}원\n합계 : {self.price_sum}원")
                else:
                    print("없는 메뉴입니다. 다시 입력하세요.")
            except: #예외처리
                print("숫자를 입력해주세요.") 

    def pay(self):
        print(f"총 결제 금액은 {self.price_sum}원입니다.")
        payment = input("결제 수단을 선택하세요. (1: 현금, 2: 카드) : ")
        if payment == '1' or payment.lower() == 'cash':
            print("직원을 호출하겠습니다.")
        elif payment == '2' or payment.lower() == 'card':
            print("IC칩 방향에 맞게 카드를 꽂아주세요.")
        else:
            print("다시 결제를 시도해 주세요.")

    def border_decorator(func): #주문서 함수
        def wrapper(self):
            print('\n🧾 주문서')
            print('⟝' + '-' * 30 + '⟞')
            for _ in range(2):
                print('|' + ' ' * 31 + '|')
            func(self)
            for _ in range(2):
                print('|' + ' ' * 31 + '|')
            print('⟝' + '-' * 30 + '⟞')
        return wrapper

    @border_decorator
    def table(self):
        print("주문 일시:", datetime.now().strftime("%Y-%m-%d %H:%M:%S")) #주문 일시
        for name, price in zip(self.order_menu, self.order_price): #주문 내역 출력
            print(f"{name} : {price}원")
        print(f"합계 금액 : {self.price_sum}원")

k=Kiosk()
k.menu_print()
k.menu_select()
k.table()
k.pay() #키오스크 출력 