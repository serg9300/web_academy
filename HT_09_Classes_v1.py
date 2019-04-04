class First:
    color = 'red'
    def out(self):
        print(self.color + '!')

obj1 = First()
obj2 = First()

print(obj1.color)
print(obj2.color)
obj1.out()
obj2.out()

class Second:
    color = 'red'
    form = 'circle'
    quantity = 3
    def changecolor(self, newcolor):
        self.color = newcolor
    def changeform(self, newform):
        self.form = newform
    def changequantity(self, newquantity):
        self.quantity = newquantity
obj3 = Second()
obj4 = Second()
obj5 = Second()

print(obj3.color, obj3.form)
print(obj4.color, obj4.form)
print(obj5.color, obj5.form, obj5.quantity)

obj3.changecolor('green')
obj4.changecolor('yellow')
obj4.changeform('triangle')
obj5.changecolor('blue')
obj5.changeform('oval')
obj5.changequantity(5)

print(obj3.color, obj3.form)
print(obj4.color, obj4.form)
print(obj5.color, obj5.form, obj5.quantity)