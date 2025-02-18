f=open("data1.txt","r")
a=f.readlines()
name=input("Search the word : ")
for i in a:
    a1=i.split()
    for j in a1:
        # print(j.lower())
        if j.lower()==name.lower():
            print(True)
            break
    # else:
    #     print(False)