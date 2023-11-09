1# Name: Felix Barrientos
# Program Purpose: This program finds the cost of pet vaccines & medications for dogs and cats

# NOTE: Pet medications perscribed by licensed veterinarians are not subject to sales tax in VA

# PET CARE MEDS Pricing
#___________________________________#

#Canine Vaccinations:
#1 Bordatella 30
#2 DAPP 35
#3 Influenza 48
#4 Leptospirosis 21
#5 Lyme Disease 41
#6 Rabies 25
#7 Full Vaccine Package (Includes all): 15% Discount

#Canine Heartworm Preventative Chews (price per chew; one chew per month)
#Small dogs 25lbs: 9.99
#medium dogs, 26-50lbs: 11.99
#large bowwow, 51-100lbs: 13.99
#_______________________________________#

import datetime

#GLOBAL VARIABLES#

Nonte = 00.00
PR_BORD = 30.00
PR_DAPP = 35.00
PR_INFLU = 48.00
PR_LEPO = 21.00
PR_LM = 41.00
PR_RAB = 25.00
PR_FL_LEUK = 35.00
PR_FL_VRHINO = 30.00
PR_ALL = 00.00
PR_CAT_CHEWS = 08.00
PR_S_CHEWS = 09.99
PR_M_CHEWS = 11.99
PR_L_CHEWS = 13.99

#PROGRAM FUNCTIONS#
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_calculations()
        elif pet_type.upper() == "C":
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()
        
        askAgain = input("\nWould you like to process another pet (Y/N)?: ")
        if askAgain.upper() == "N" :
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("Is this pet a dog (D) or a cat (c)? ")
    pet_weight = int(input("Weight of your pet (pounds/lbs): "))

#DOG FUNCTIONS#
 
def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n** Dog Vaccines: \n\t1.Bordatella \n\t2.Dapp \n\t3.Influenza \n\t4.Leptospirosis"
    dog2 = "\n\t5.Lyme Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t8.None"
    dogmenu = dog1 + dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))
    
    print("\nMonthly heart worm prevention medication is recommended for all dogs.")
    heart_yesno = input("\nWould you like to order mothly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y" :
        num_chews = int(input("\nHow many heart worm chews would you like to order? "))

def perform_dog_calculations():
    global vax_cost, vax_name, chews_cost, total, PR_ALL
    #vaccines
    if pet_vax_type == 1 :
        vax_cost = PR_BORD
        vax_name = "Bordatella"
    elif pet_vax_type == 2 :
        vax_cost = PR_DAPP
        vax_name = "DAPP"
    elif pet_vax_type == 3 :
        vax_cost = PR_INFLU
        vax_name = "Influenza"
    elif pet_vax_type == 4 :
        vax_cost = PR_LEPO
        vax_name = "Leptospirosis"
    elif pet_vax_type == 5 :
        vax_cost = PR_LM
        vax_name = "Lyme Disease"
    elif pet_vax_type == 6 :
        vax_cost = PR_RAB
        vax_name = "Rabies"
    elif pet_vax_type == 8 :
        vax_cost = Nonte
        vax_name = "No Vaccine"
    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_INFLU + PR_LEPO + PR_LM + PR_RAB
        vax_cost = .85 * PR_ALL
        vax_name = "Full Vaccine Package"
    
    #heart worm chews#
    if num_chews != 0 :
        if pet_weight <= 25:
            chews_cost = num_chews * PR_S_CHEWS
        elif pet_weight >= 26 and pet_weight < 50:
            chews_cost = num_chews * PR_M_CHEWS
        else:
            chews_cost = num_chews * PR_L_CHEWS
    
    #find total#
    total = vax_cost + chews_cost

def display_dog_calculations():
    line = "-----------------------"    
    print("")
    print("  `~ PET CARE MEDS ~.  ")
    print(line)
    print("")
    print("Items purchased: ")
    print("")
    print(str(vax_name) + ":     $ " + str(vax_cost))
    print("HW Chews " + str(num_chews) + " Ct:  $ " + str(chews_cost))
    print("")
    print("Total:          $ " + str(total))
    print("")
#CAT FUNCTIONS#

def get_cat_data():
    global pet_vax_type, num_chews
    cat1 = "\n** Cat Vaccines: \n\t1.Feline Leukemia \n\t2.Feline Viral Rhinotracheitis \n\t3.Rabies \n\t4.Full Vaccine Package"
    cat2 = "\n\t5.None"
    catmenu = cat1 + cat2
    pet_vax_type = int(input(catmenu + "\n** Enter the vaccine number: "))
    
    print("\nMonthly heart worm prevention medication is recommended for all Cats.")
    heart_yesno = input("\nWould you like to order mothly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y" :
        num_chews = int(input("\nHow many heart worm chews would you like to order? "))
    elif heart_yesno.upper() == "N" :
        num_chews = int(0)

def perform_cat_calculations(): 
    global vax_cost, vax_name, chews_cost, total, PR_ALL
#vaccines
    if pet_vax_type == 1 :
        vax_cost = PR_FL_LEUK
        vax_name = "Feline Leukemia"
    elif pet_vax_type == 2 :
        vax_cost = PR_FL_VRHINO
        vax_name = "Feline Viral Rhinotracheitis"
    elif pet_vax_type == 3 :
        vax_cost = PR_RAB
        vax_name = "Rabies"
    elif pet_vax_type == 4 :
        PR_ALL = PR_FL_LEUK + PR_FL_VRHINO + PR_RAB
        vax_cost = .90 * PR_ALL
        vax_name = "Full Vaccine Package"
    else:
        vax_cost = Nonte
        vax_name = "No Vaccine"
    
    #heart worm chews#
    if num_chews != 0 :
        chews_cost = num_chews * PR_CAT_CHEWS 
    else:
        chews_cost = 0
        
    
    #find total#
    total = vax_cost + int(chews_cost)

def display_cat_results(): 
    line = "-----------------------"    
    print("")
    print("  `~ PET CARE MEDS ~.  ")
    print(line)
    print("")
    print("Items purchased: ")
    print("")
    print(str(vax_name) + ":     $ " + str(vax_cost))
    print("HW Chews " + str(num_chews) + " Ct:  $ " + str(chews_cost))
    print("")
    print("Total:          $ " + str(total))
    print("")

#CALL ON MAIN TO EXCECUTE#

main()