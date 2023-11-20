Name: Felix Barrientos
Program Purpose: Fresh Foods: Employees :D

import datetime

gross_pay = []
federal_tax = []
state_tax = []
social_security = []
medicare = []
ret = []
net_pay = []

total_gross = []
total_net = []



PAY_RATE = (16.5, 15.75, 15.75, 19.5)

DED_RATE = (.12, .03, .062, .0145, .04)


def main ():
    perform_calculations()
    display_results()

def perform_calculations()
    global total_gross, total_net

    for i in range(numb_empl) :

#calculate gross pay 
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]

        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]

        elif job[i] = "J":
            pay = hours[i] * PAY_RATE[2]
        
        else:
            pay = hours[i] *PAY_RATE[3]
        
#calculate deductions 
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]