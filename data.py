f=open("data.txt","r")
# print(f.read(100))
# print(f.readline())
# print(f.readlines())
c=0
a=f.readlines()
for i in a:
    c+=1
print(f"Toatal line in data.txt are {c}")

c1=0
for i in range(len(a)):
    c1+=len(a[i].split())
print("total words in data.txt are ",c1)

c2=0
for i in range(len(a)):
    c2+=len(a[i])
print(f"Total number of letter including spaces are {c2}")

c3=0
c4=0
for i in a:
    for j in i:
        if j==" ":
            c3+=1
        else:
            c4+=1
print(f"total number of spaces in data.txt are {c3}")
print(f"total number of letters without spaces are {c4}")

c5=0
c6=0
for i in a:
    for j in i:
        if j in "aeiou":
            c5+=1
        else:
            c6+=1
print("vovels",c5)
print("Conso",c6)


