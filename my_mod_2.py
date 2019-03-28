from git_lecture.my_mod_1 import add, multiply, divide
import git_lecture.my_mod_1

print(git_lecture.my_mod_1.__name__)
raw_input = input('enter 2 numbers (0,0): ')
l1= raw_input.split(',')
l2= tuple(int(i) for i in l1)

add_res = add(l2[0], l2[1])
print(add_res)