abcList = ["A", "B", "C", "A", "A", "C"]
print(abcList)
abcList.insert(0,"B")
n = int(len(abcList))
count=0
for n in range(0, n, 1):
  if abcList[n] == "A":
    count+=1
print(f"There are, " + str(count) + " A's in the list")