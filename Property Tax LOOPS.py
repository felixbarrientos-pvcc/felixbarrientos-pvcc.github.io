#Name: Felix Barrientos
#ProgP: This is my property tax assignment using loops

import datetime

#taxrate=.042
#reliefrate=.33
#Due by December 5th, 2023

#global varibales#

#program#

def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to calculate tax on another vehicle? (Y/N): ")
        if askAgain.upper() == "N6775":
            more = False
            print("! Please be sure to pay by 12.05.2023 !")

def get_user_data(): 
    global assessed_value, relief_elig
    assessed_value = int(input("\nWhat is the assessed value of the vehicle? "))
    relief_elig = input("\nOwned or leased vehicles which are predominately used for\nnon-business purposes & have passenger license plates do not have to pay a license fee\n\nIs this vehicle eligible for tax relief? (Y/N): ") 

def perform_calculations():
    global total_due, eligible, annual_tax_amount, six_month
    annual_tax_amount = (assessed_value * .042)
    six_month = annual_tax_amount / 2
    if relief_elig.upper() == "Y":
        eligible = (six_month * .33)
    else:
        eligible = 0
    
    total_due = (six_month - eligible)

def display_results():
    print("")
    print("Charlottesville, Virginia Property Tax")
    print(str(datetime.datetime.now()))
    print("")
    print('Assessed value of vehicle:   $' + str(assessed_value))
    print('Annual Tax Amount:           $' + str(annual_tax_amount))
    print('6 Month Tax Amount:          $' + str(six_month))
    print('Tax Relief Amount:           $' + str(eligible))
    print("")
    print('Total Due:                   $' + str(total_due))

#RUN...pls#
main()