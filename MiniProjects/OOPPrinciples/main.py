import customer
import employee
import random


# cust = customer.Customer()
# cust.first_name = 'Jyoti'
# cust.last_name = 'Suresh'

if random.randint(0, 1) == 0:
    my_person = customer.Customer('Jyoti', 'Suresh', 'Mumbai')
else:
    my_person = employee.Employee('Minato', 'Fujiwara', 'Marketing')
my_person.print()

# my_cust = customer.Customer('Jyoti', 'Suresh', 'Mumbai')
# # cust._last_name = 'Ghosh'
# cust.first_name = 'Rizmi'
# cust.print()
#
#
# emp = employee.Employee('Minato', 'Fujiwara', 'Marketing')
# emp.print()
