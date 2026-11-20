# ques1:- square of the number
sq = lambda x: x*x
print(sq(3))

# ques2:- cube of the number
cube = lambda x: x*x*x
print(cube(3))

# ques3:- add to numbers
add = lambda a, b: a+b
print(add(2, 3))

# ques4:- even or odd
check = lambda num: "Even" if num%2 == 0 else "Odd"
print(check(5))
print(check(8))

# ques5:- find greater number
greater = lambda a, b: a if a>b else b 
print(greater(45, 66))

# ques6:- find the average
avg = lambda a, b, c: (a+b+c) / 3
print(avg(4, 5, 8))