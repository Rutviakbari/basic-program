list = ["abc", "def", "ghi"]
print(list)
print(list[1])
list[1] = "pqr"
print(list)
for x in list:
    print(x)
if "abc" in list:
    print('yes')
print(len(list))
list.append("stu")
print(list)
list.insert(1,"efg")
print(list)
list.remove("pqr")
print(list)
list.pop()
print(list)
list.clear()
print(list)