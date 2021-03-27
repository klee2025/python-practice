thislist = ["apple","banana","cherry"]
print("origin: ",thislist)

#1.7.1 change the second item
thislist [1] = "orange"
print("1.7.1: ",thislist)

#1.7.2 insert "melon"
thislist.append("melon")
print("1.7.2: ",thislist)

#1.7.3 insert "mango" as the third item
thislist.insert(2,"mango")
print("1.7.3: ",thislist)

#1.7.4 consider thislist = ["apple","banana","cherry]. You can delete the last item in 3 ways below.
thislist.remove("cherry")
thislist.pop()
del thislist[2]
