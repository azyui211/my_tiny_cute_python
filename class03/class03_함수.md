### 함수
- ##### 함수 형태
```
def 함수이름( 입력값 ):
    함수 내용
    return 내보낼값
```

- ##### 예시
```
# 가방의 내용물을 보는 함수
def show_items_in_a_bag(someones_bag):
    for item in someones_bag:
        print(item)

my_bag = ["지갑", "노트", "펜", "우산"]

show_items_in_a_bag(my_bag)     # 실행

```

```
# 우산이 있으면 사용하는 함수
def take_an_umbrella(weather, someones_bag):
    if weather == "rainy":
        if "우산" in someones_bag:
            print("우산을 꺼냅니다.")
            return "우산"
        else:
            print("비를 맞습니다.")
    else:
        print("비가 오지 않습니다.")
```

```
# 구구단 함수
def multiplication(input_number):
    for i in range(9):
        num = i + 1
        print(str(input_number) + " x " + str(num) + " = " + str(input_number*num))
```

- ##### 파일 다루기
```
import os
os.listdir("폴더 경로")
os.rename("fileA.pdf", "fileB.pdf")
os.makedirs("생성할 폴더경로")
```