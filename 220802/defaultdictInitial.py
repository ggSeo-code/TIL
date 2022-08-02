from collections import defaultdict

li1 = [("yellow",1),("blue",2),("green",3),("blue",4),("red",1)]
dic1 = defaultdict(list)

for k, v in li1:
    dic1[k].append(v)

print(dic1.items())
