#1
lst1 = [x for x in range(100000)]
print(len(set(lst1)))
#2
lst2 = [1,43,4,3,4,5,6,3,4,5,46,100001]
print(len(set(lst1).intersection(set(lst2))))
#3
print(list(set(lst1).intersection(set(lst2))))
#4
str = '5 3 34 5 65 3 23 43'
lst4=[]
for i in str.split():
    if i not in lst4:
        lst4.append(i)
        print(i, 'NO')
    else:
        print(i, 'YES')
#5
lst5=['hi','hi','what','is','your','name','my','name','is','bond','james','bond','my','name','is','damme','van','damme','claude','van','damme','jan','claude','van','damme']
# initializing a dictionary
d = {}
# counting number of times each word comes up in list of words
for key in lst5:
    d[key] = d.get(key, 0) + 1
for k,v in sorted(d.items(), key = lambda x: x[1], reverse = True):
    print(k)

#6
a1='Ivanov paper 10'
a2='Petrov pen 5'
a3='Ivanov marker 3'
a4='Ivanov paper 10'
a5='Petrov envelop 10'
a6='Ivanov envelop 5'
lst6=[a1.split(),a2.split(),a3.split(),a4.split(),a5.split(),a6.split()]

#     d61.append([i[0],{i[1]:int(i[2])}])
# d6=dict(d61)
# print(d6)
#     dict6={i[0]:{i[1]:int(i[2])}}
#     d6.update(dict6)
# print(d6)
#print(dict(zip(lst6[0][0], dict(lst6[0][1:]))))