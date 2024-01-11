### 리스트 실습 ###

## 생성
listA = list()
listA = []



## 아이템 추가
listA = []
listA.append(0)
listA.append(1)
listA.append(2)
listA.append(3)
listA.append(4)

listA = list()
for i in range(5):              # for 문으로 리스트를 채우려는 경우 채울 그릇(리스트)이 준비되어야하는 시점이 언제인지 잘 생각해야합니다.
    listA.append(i)

listA = list()
listA.append("0")
listA.append("1")
listA.append("2")
listA.append("3")
listA.append("4")

listA = []
for j in range(5):
    listA.append(str(j))



## 선택적 추가
# 3이면 제외
for n in range(5):
    if n != 3:
        listA.append(n)
'''
    A == B   A와 B가 같으면
    A != B   A와 B가 다르면
'''
# 3이나 5면 제외
for n in range(5):
    if not n in [3, 5]:
        listA.append(n)



## 아이템 삭제
listA = ["A", "B", "C"]
listA.remove("B")



## 리스트 안에 리스트
listA = [["1_A", "1_B", "1_C"], ["2_A", "2_B", "2_C"], ["3_A", "3_B", "3_C"]]

for e in listA:
    for c in e:
        print(c)



## 더하기
listA = ["EDU_0010", "EDU_0020", "EDU_0030"]
listB = ["EDU_0020", "EDU_0040", "EDU_0050"]

listAB = listA + listB



## 중복 합치기
listA = ["A", "B", "C", "D", "B", "D", "A", "E", "F", "G", "F"]

union_list = set(listA)     # 집합 형태로 변환
listB = list(union_list)    # 리스트 형태로 변환
sorted_list = sorted(listB)

# 위의 세줄을 한 줄로 표현하면
sorted_list = sorted(list(set(listA)))



### 실습 예제 ###

# 구구단 리스트 : 2단부터 시작하는 리스트 안의 리스트 만들기        관련항목 : 생성, 아이템 추가, 선택적 추가, 리스트 안에 리스트
# [[2, 4, 6,... ], [3, 6, 9, ...], [4, 8, 12, ...]]



