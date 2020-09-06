from lcm_functions import prime_factors, lowest_common_multiple2


def lcm(v1, v2):
    return 12


print("""
Simultaneous Equation Solver
============================

We can solve two equations of the form:

Equation 1: ax + by = c
Equation 2: px + qy = r

So, please rewrite your equations in this way first yourself!

Now give me the values
Equation one:""")


a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

print(f"""
Equation two:""")

p = int(input('p: '))
q = int(input('q: '))
r = int(input('r: '))

# a= 4
# b= 10
# c= 12
#
# p= 6
# q= 5
# r= -2



# a= 11
# b= 35
# c= 60
#
# p= 3
# q= 4
# r= 5



print(f"""
OK, so you have given me:
Equation 1:
{a}x + {b}y = {c} 
Equation 2:
{p}x + {q}y = {r}
""")

a_pfs = prime_factors(a)
p_pfs = prime_factors(p)
x_lcm = lowest_common_multiple2(a_pfs, p_pfs)

m1 = int(x_lcm / a)
m2 = int(x_lcm / p)

print(f"""For x, the least common multiple of {a} and {p} is {x_lcm}
I am going to multiply Equation 1 by {m1}
I am going to multiply Equation 2 by {m2}
""")

b2 = b * m1
c2 = c * m1
q2 = q * m2
r2 = r * m2

print(f"""This gives me:
Equation 1a: {x_lcm}x + {b2}y = {c2}
Equation 2a: {x_lcm}x + {q2}y = {r2}
""")

bq3 = b2 - q2
cr3 = c2 - r2

print(f"""(1a) – (2a) =>
0x + {bq3}y = {cr3}
""")

# Now, we don't convert y to an integer because it might not be a whole number :)
y = cr3 / bq3
print(f'y = {y}')

# But, b * y IS an integer :)
by = int(b * y)
c_minus_by = c - by

# x might also not be an integer (^-^)
x = c_minus_by / a

print(f"""Substituting y into equation 1

{a}x + {by} = {c}
{a}x = {c_minus_by}
x = {x}
""")