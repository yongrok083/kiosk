📌 클래스 개요
python
복사
편집
class Kiosk:
키오스크 시뮬레이션을 위한 클래스

메뉴 출력, 주문 입력, 결제 처리, 주문서 출력 기능 포함

🔹 1. __init__() 생성자
python
복사
편집
def __init__(self):
프로그램 실행 시 자동으로 실행되는 초기화 함수

self.menu: 2차원 리스트, 각 항목은 [메뉴이름, 가격] 형태

self.order_menu: 주문한 메뉴 이름을 저장하는 리스트

self.order_price: 주문한 메뉴의 가격을 저장하는 리스트

self.price_sum: 주문한 총 금액을 저장하는 변수

🔹 2. menu_print(): 메뉴 출력
python
복사
편집
def menu_print(self):
enumerate()를 이용해 메뉴 항목을 번호와 함께 출력

다차원 리스트의 인덱스를 통해 이름과 가격을 각각 출력

python
복사
편집
for i, (name, price) in enumerate(self.menu, 1):
    print(f"{i}. {name} : {price}원")
🔹 3. menu_select(): 주문 입력 및 추가 주문 처리
python
복사
편집
def menu_select(self):
주요 기능:
사용자로부터 메뉴 번호 입력받기

HOT/ICE 선택

주문 내역 리스트(order_menu, order_price)에 추가

self.price_sum에 누적합 계산

입력 예외 처리:
try/except 사용하여 잘못된 입력 방지

while True: 루프로 잘못된 입력 시 재시도

추가 주문:
메뉴 번호가 0이면 주문 종료

그 외 번호면 계속 추가 입력 가능

🔹 4. pay(): 결제 처리
python
복사
편집
def pay(self):
기능 설명:
결제 금액 출력

사용자로부터 결제 수단 입력받기 (1, 2, "cash", "card" 지원)

조건문으로 분기 처리

현금: "직원을 호출하겠습니다."

카드: "IC칩 방향에 맞게 카드를 꽂아주세요."

그 외 입력: "다시 결제를 시도해 주세요."

🔹 5. border_decorator(func): 주문서 테두리 데코레이터
python
복사
편집
def border_decorator(func):
역할:
주문서를 꾸미기 위한 출력 테두리를 추가

@border_decorator를 붙인 메서드는 자동으로 상단/하단 외곽이 출력됨

python
복사
편집
print('⟝' + '-' * 30 + '⟞')
print('|' + ' ' * 31 + '|')
...
🔹 6. table(): 주문서 출력
python
복사
편집
@border_decorator
def table(self):
주요 출력 내용:
현재 일시 (datetime 모듈 사용)

주문된 각 항목: 온도 + 메뉴이름 : 가격

합계 금액

python
복사
편집
print("주문 일시:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
for name, price in zip(self.order_menu, self.order_price):
    print(f"{name} : {price}원")


-GPT-
