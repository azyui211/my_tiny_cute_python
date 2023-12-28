
### 제어문 응용
- ##### for 문
```
# 기본 형태 :
for item in ["A", "B", "C", "D", "E"]:
    print(item)

for num in range(5):
    print(num)
```

- ##### if 문
```
# 기본 형태
if 조건:
    실행A
else:
    실행B

if fileExt == "png" or fileExt == "jpg":
    execA
elif fileExt == "png":

# else는 생략가능
# elif로 다중 조건 설정 가능
# if 문에서 빈번하게 사용되는 bool
True, False

# 예시
status = "ip"
if status == "ip":
    print("작업을 진행하고 있습니다.")
else:
    print("작업을 진행하고 있지 않습니다.")

```

- ##### while 문
```
water_temperature = 35
while water_temperature < 100:
    water_temperature += 1
    text = "현재 물의 온도는 섭씨 {0}도 입니다".format(water_temperature)
    print(text)
    if water_temperature == 100:
        print("물이 끓고 있습니다. 전기 포트의 전원을 끕니다.")
```
