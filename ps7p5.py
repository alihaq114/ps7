def dl1 (mylist):
  n = int(input("Number of items for your list: "))
  for n in range(0,n,1):
    s = int(input("Enter a number: "))
    mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
    print(item)

mylist = []
yourlist = [500, 600, 700, 800, 900]
yourlist.remove(800)
mylist = dl1(mylist)
mylist.insert(0,100)
mylist.insert(0,yourlist)
displaylist(mylist)
print(mylist)


