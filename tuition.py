# Name: Felix-Barrientos
# Prog Purpose: This program computes PVCC College tuition & fees based on number of credits
#  PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 250
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#DEFINE GLOBAL VARIABLES#
inout = 1 #1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0

#DEFINE PROGRAM FUNCTIONS#
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition & fees for another Student? (Y/N): ")
        if yesno.upper() == "N" :
            more = False
            print("Thanks for choosing Piedmont Community College :)")

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; Enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registedered for: "))
    scholarshipamt = float(input("Scholarship amount recieved: $"))

def perform_calculations():
    global tuition_fees, inout_type

    if inout == 1:
        tuition_fees = float(numcredits * RATE_TUITION_IN) + float(RATE_INSTITUTION_FEE * numcredits) + float(RATE_ACTIVITY_FEE * numcredits)
    else:
        tuition_fees = float(numcredits * RATE_TUITION_OUT) + float(RATE_CAPITAL_FEE * numcredits) + float(RATE_INSTITUTION_FEE * numcredits) + float(RATE_ACTIVITY_FEE * numcredits)
        
def display_results():
    in_tuition_cost = float(numcredits * RATE_TUITION_IN)
    out_tuition_cost = float(numcredits * RATE_TUITION_OUT)
    capital_cost = float(RATE_CAPITAL_FEE * numcredits)
    institution_cost = float(RATE_INSTITUTION_FEE * numcredits)
    activity_cost = float(RATE_ACTIVITY_FEE * numcredits)
    print("")
    print(" PIEDMONT VIRGINIA COMMUNITY COLLEGE")
    print("-------------------------------------")
    if inout == 1:
        print("Tuition (In) Fee:       $" + str(in_tuition_cost))
    else:
        print("Tuition (Out) Fee:      $" + str(out_tuition_cost))
        print("Capital Fee:            $" + str(capital_cost))
    print("Institution Fee:        $" + str(institution_cost))
    print("Activity Fee:           $" + str(activity_cost))
    print("Scholarship Amount:     $" + str(scholarshipamt))
    print("")
    print("Total Amount:           $" + str(tuition_fees))
    print("Total Due:              $" + str(tuition_fees - scholarshipamt))

#Main Program#

main()
    