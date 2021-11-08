var1 = input("Enter Sentence : ")
var2 = []
var3 = []
for i in var1:
    if i.isupper():
        var2.append(i)
for k in var1:
    if k.islower():
            var3.append(k)
print("UPPER CASE : ", len(var2))
print("lower case : ", len(var3))
