### 딕셔너리 실습 ###
# {"key" : "value"}
# 딕셔너리를 사용하는 핵심적인 이유는 아주 단순하고 명확합니다. 'key 값을 가지고 value값을 찾아내기 위함'입니다.

## 생성
dictA = dict()
dictA = {}



## 아이템 추가
dictA["A"] = "B"
dictA["C"] = "D"
dictA.update({"A": "B", "C": "D"})

# for 문 안에서 추가
# 리스트와 마찬가지로 for문이 나오면 담을 그릇(딕셔너리)을 준비해야하는 시점이 언제인지 잘 생각해야합니다.
shot_path_list = ["/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0010",
                  "/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0020",
                  "/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0030",
                  "/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0040"]
dictA = {}
for i in shot_path_list:
    shot_name = i.split("/")[-1]
    dictA[shot_name] = i

# for문으로 딕셔너리 추가할 때의 주의점
# key 값이 중복되어 입력되면 value값은 덮어쓰기 됩니다.
file_list = ["INJ_0010", "INJ_0020", "TRA_0020", "TNO_0040"]
dictA = {}
for i in file_list:
    seq_name = i.split("_")[0]
    shot_number = i.split("_")[1]
    dictA[seq_name] = shot_number



## 분해
dictA = {"EDU_0010": "/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0010",
         "EDU_0020": "/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0020",
         "EDU_0030": "/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0030",
         "EDU_0040": "/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0040"}

# 위 딕셔너리에서 "EDU_0010", "EDU_0020", "EDU_0030", "EDU_0040"는 모두 key 값입니다.
# 이러한 key 값들로만 묶은 리스트를 만들 수 있습니다.
dictA_key_list = list(dictA.keys())
# 마찬가지로 value들로만 묶은 리스트를 만들 수 있습니다.
dictA_value_list = list(dictA.values())



## 분해 활용법
# 상황 예시 : 임의의 샷 이름이 들어왔을 때 딕셔너리 키 값에 매칭되는 샷 이름이면 경로를 반환하는 기능
shot_name = "EDU_0050"
dict_key_list = list(dictA.keys())
if shot_name in dict_key_list:
    shot_path = dictA[shot_name]
    print(shot_path)



## 딕셔너리 안에 딕셔너리
dictA = {"EDU":{"EDU_0010": "ani01", "EDU_0020": "mmv01"},
         "TST":{"TST_0010": "cmp01", "TST_0040": "lgt01"}}

dictA["EDU"]["EDU_0020"]

for i in list(dictA.keys()):
    print(i)



#### 아래의 실습 두 가지는 처음 파이썬을 학습하는 입장에서 난이도가 매우*2 높을 수 있습니다.

### 문자열 + 리스트 조합 예제
# 아래의 리스트로 {샷이름:{task이름:파일이름}} 형태의 딕셔너리 만들기

listA = ["EDU_0010_ani01_v001_w01.mov",
         "EDU_0010_mmv01_v003_w02.mov",
         "EDU_0020_crd01_v002_w01.mov",
         "EDU_0030_lgt01_v004.mov",
         "EDU_0030_ani01_v002_w05.mov",
         "EDU_0040_mmv01_v001.mov"]


### 리스트 + 딕셔너리 예제 1
# 아래의 리스트에서 "path"의 value 값으로만 이루어진 리스트 만들기

dictA = [{"shot_name": "EDU_0010", "task_name": "ani01", "path": "/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0010"},
         {"shot_name": "INJ_0010", "task_name": "cmp01", "path": "/projects/2023_06_theKillers/sequence/INJ/INJ_0010"},
         {"shot_name": "TST_0010", "task_name": "lgt01", "path": "/projects/2022_06_lostArk/sequence/TST/TST_0010"}]

