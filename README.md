# 🧾 Kiosk 클래스 상세 설명

---

## 📌 클래스 개요

```python
class Kiosk:
키오스크 시뮬레이션을 위한 클래스입니다.
메뉴 출력, 주문 입력, 결제 처리, 주문서 출력 기능을 포함합니다.

🔹 1. __init__() 생성자
python
복사
편집
def __init__(self):
클래스 인스턴스가 생성될 때 자동 실행됩니다.

주요 변수:

self.menu: [[이름, 가격], ...] 형태의 2차원 리스트

self.order_menu: 주문한 음료의 이름 리스트

self.order_price: 각 음료의 가격 리스트

self.price_sum: 주문 총 금액

🔹 2. menu_print() - 메뉴 출력
python
복사
편집
def menu_print(self):
enumerate()를 활용하여 메뉴 번호와 함께 항목을 출력합니다.

출력 형식 예:

yaml
복사
편집
1. americano : 2000원
🔹 3. menu_select() - 주문 처리
python
복사
편집
def menu_select(self):
사용자로부터 음료 번호와 온도를 입력받습니다.

입력 예외 처리를 위해 try + while 사용

주문 내역(order_menu, order_price)과 price_sum을 업데이트합니다.

주문 완료 전까지 추가 주문 반복이 가능합니다.

self.menu[n - 1]을 통해 메뉴 이름과 가격을 가져옵니다.

🔹 4. pay() - 결제 처리
python
복사
편집
def pay(self):
총 금액을 출력하고 결제 수단을 입력받습니다.

결제 수단:

1 또는 'cash': "직원을 호출하겠습니다."

2 또는 'card': "IC칩 방향에 맞게 카드를 꽂아주세요."

그 외: "다시 결제를 시도해 주세요."

🔹 5. border_decorator() - 주문표 꾸미기 데코레이터
python
복사
편집
def border_decorator(func):
주문표를 꾸미기 위한 상단/하단 외곽선을 출력합니다.

@border_decorator로 table()에 적용됩니다.

🔹 6. table() - 주문표 출력
python
복사
편집
@border_decorator
def table(self):
주문 일시를 datetime 모듈로 출력합니다.

zip()을 이용해 주문 항목과 가격을 나란히 출력합니다.

총 금액도 함께 표시됩니다.
