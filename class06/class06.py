import platform
osType = platform.system()
pathA = r"C:\Users\seokwon.choi\Desktop"
if osType == "Windows":
    pathA = pathA.replace("\\", "/")
else:
    pathA = pathA.replace("/", "\\")

