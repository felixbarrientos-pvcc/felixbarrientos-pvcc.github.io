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

#define global variables
inout = 1 #1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0

############# define program functions ##########
def main():
    more = True
    while more:
        get_user_data()
        perform_caclculations()
        display_results()
        yesno = input("\nWould you like to calcuate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno === "N":
            another_student = "False"

def get_user_data():
    global inout, nuumcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    