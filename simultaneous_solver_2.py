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

# a= 4
# b= 10
# c= -12
#
# p= 3
# q= 5
# r= 6


print(f"""
OK, so you have given me:
Equation 1:
{a}x + {b}y = {c} 
Equation 2:
{p}x + {q}y = {r}
""")

print('OK I could solve these in a millisecond, but I’m going to to work like a human!')
print('')

a_pfs = prime_factors(a)
p_pfs = prime_factors(p)
x_lcm = lowest_common_multiple2(a_pfs, p_pfs)
print(f'For x, the least common multiple of {a} and {p} is {x_lcm}')

b_pfs = prime_factors(b)
q_pfs = prime_factors(q)
y_lcm = lowest_common_multiple2(b_pfs, q_pfs)
print(f'For y, the least common multiple of {b} and {q} is {y_lcm}')

print('')

ma = int(x_lcm / a)
mp = int(x_lcm / p)
mb = int(y_lcm / b)
mq = int(y_lcm / q)

min_mx = min(ma, mp)
min_my = min(mb, mq)

if min_mx < min_my:
    variable_to_eliminate = 'x'
    variable_to_solve_first = 'y'
else:
    variable_to_eliminate = 'y'
    variable_to_solve_first = 'x'

print(f'The least amount of multiplying I can do is with {variable_to_eliminate}.')
print('')

if variable_to_eliminate == 'x':
    m1 = ma
    m2 = mp
else:
    m1 = mb
    m2 = mq

a2 = a * m1
b2 = b * m1
c2 = c * m1

if m1 == 1:
    print('I am going to leave Equation 1 as it is.')
    active_1 = '1'
else:
    print(f"I am going to multiply Equation 1 by {m1}")
    print(f"""This gives me:
    Equation 1a: {a2}x + {b2}y = {c2}
    """)
    active_1 = '1a'

p2 = p * m2
q2 = q * m2
r2 = r * m2

if m2 == 1:
    print('I am going to leave Equation 2 as it is')
    active_2 = '2'
else:
    print(f"I am going to multiply Equation 2 by {m2}")
    print(f"""This gives me:
    Equation 2a: {p2}x + {q2}y = {r2}
    """)
    active_2 = '2a'

if (q2 > b2) or (r2 > a2):
    bigger_equation = active_2
    big_equation_string = f'{p2}x + {q2}y = {r2}'
    smaller_equation = active_1
    small_equation_string = f'{a2}x + {b2}y = {c2}'
else:
    bigger_equation = active_1
    big_equation_string = f'{a2}x + {b2}y = {c2}'
    smaller_equation = active_2
    small_equation_string = f'{p2}x + {q2}y = {r2}'

print(f'Out of Equation {active_1} and Equation {active_2}, Equation {bigger_equation} has the bigger {variable_to_solve_first} value.')
print('')
print(f'So, subtract Equation {smaller_equation} from Equation {bigger_equation} rather than the other way around.')
print('')
print(f'Equation {bigger_equation}: {big_equation_string}')
print(f'Equation {smaller_equation}: {small_equation_string}')

if bigger_equation == active_1:
    ap3 = a2 - p2
    bq3 = b2 - q2
    cr3 = c2 - r2
else:
    ap3 = p2 - a2
    bq3 = q2 - b2
    cr3 = r2 - c2

print(f"""({bigger_equation}) – ({smaller_equation}) =>
{ap3}x + {bq3}y = {cr3}""")

if variable_to_solve_first == 'y':
    # Now, we don't convert y to an integer because it might not be a whole number :)
    y = cr3 / bq3
    print(f'y = {y}')
    print('')
    
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
else:
    # Now, we don't convert x to an integer because it might not be a whole number :)
    x = cr3 / ap3
    print(f'x = {x}')
    print('')

    # But, a * x IS an integer :)
    ax = int(a * x)
    c_minus_ax = c - ax

    # y might also not be an integer (^-^)
    y = c_minus_ax / b

    print(f"""Substituting x into equation 1

    {ax} + {b}y = {c}
    {b}y = {c_minus_ax}
    y = {y}
    """)