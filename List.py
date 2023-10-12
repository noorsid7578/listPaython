list=[25,12,35,"Noor"]
print(list)
print(type(list))
print(list[2])
l=[25,12,45,12,52]
print(l[0:2])
print(l[2:5])
print(l[0:])
print(l[:5])
l[0]="Noor"
print(l)
print(l[len(l)-2])
print(l[-2:-1])
for i in list:
    print(i)
if "Noor" in list:
    print("Yes")

# List Method in Paython

name=["Noor","Farhan","Saad","ARahman"]
name.append("Siddique")
print(name)
name.sort()
print(name)
print(name.count("Noor"))

marks=[85,75,48,98,48]
marks.append(90)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
print(marks.count(48))
print(marks.count(98))
print(marks)
marks.reverse()
print(marks)

print(marks.index(98))
print(marks.index(90))

marks.insert(0,"Noor")
print(marks)

marks.insert(1,52)
print(marks)
marks.remove(52)
print(marks)
name.extend(marks)
print(name)


#End List