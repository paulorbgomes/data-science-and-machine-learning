# Lacos sobre sequencias

testList = [67, 100, 22]

print(len(testList))

for i in range(0, len(testList)):
    print(testList[i])

for i in testList:
    print(i)

for i, v in enumerate(testList):
    print(f"testList[{i}] = {v}")