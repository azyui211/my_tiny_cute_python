# 파이썬 경로 문제
'''
    사용하는 OS에 따라 경로를 구분하는 separator가 다릅니다.
    윈도우     - \ (역슬래시)
    리눅스, 맥 - / (슬래시)
    
    하지만 파이썬 내에서 \ 역슬래시는 escape(탈출) 문자를 의미합니다.
    따라서 윈도우에서 경로 문자열을 사용할 때에는 주의가 필요합니다.
'''

# 예제
print("TestTest")
print("Test\nTest")


print("C:\Python39\note.exe")
'''
기대한 결과는 C:\Python39\note.exe 라는 문자가 프린팅 되는 것이었지만 실제 결과는

C:\Python39
ote.exe

와 같이 나옵니다.
\n 이 의미하는 바가 '줄바꿈'이기 때문입니다.


윈도우 경로인 역슬래시를 파이썬에서 제대로 표시하려면

역슬래시를 두 번 반복해서 적어야합니다. 
'''
print("C:\\Python39\\note.exe")

'''
    또는 문자열을 의미하는 따옴표 앞에 r 을 붙이면 됩니다.
'''
print(r"C:\Python39\note.exe")



import platform
osType = platform.system()
pathA = r"C:\Users\seokwon.choi\Desktop"
if osType == "Windows":
    pathA = pathA.replace("\\", "/")
else:
    pathA = pathA.replace("/", "\\")

