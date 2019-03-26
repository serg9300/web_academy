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
def customer_info(file):
    customers = {}
    for record in file:
        new_customer = record.split(" ")
        if new_customer[0] in customers:
            if new_customer[1] in customers[new_customer[0]]:
                customers[new_customer[0]][new_customer[1]] += int(new_customer[2])
            else:
                customers[new_customer[0]].setdefault(new_customer[1], int(new_customer[2]))
        else:
            customers.setdefault(new_customer[0], {new_customer[1]:int(new_customer[2])})
    customer_list = [[i, customers[i]] for i in customers]
    customer_list.sort()
    for i in customer_list:
        stuff_list = [[x, i[1][x]] for x in i[1]]
        stuff_list.sort()
        i[1] = stuff_list
    for i in customer_list:
        print(i[0], ':')
        for t in i[1]:
            print(t[0], t[1])

file = open(r'C:\Users\User\Desktop\python\git_lecture\input_txt.txt')
customer_info(file)
file.close()