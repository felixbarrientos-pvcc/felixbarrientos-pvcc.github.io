#Name: Felix Barrientos
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

##### define rate tuples #

#             SR  DR  SU
#              0    1    2
ROOM_RATES = (195, 250, 350)

#           s-tax   occ-tax
#              0       1
TAX_RATES = (0.065, 0.1125)
 
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = []
last_name = []
first_name = []
t_nights = []
subtotal = []
sales_tax = []
occ_tax = []
total_total = []


def main():
    read_in_guest_file()
    perform_calculations()
    open_outfile()
    create_output_html()
            


def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()


    for i in guest_in:
        guest.append(i.split(","))
        


def perform_calculations():
    global grandtotal
    grandtotal = 0
    
    for i in range(len(guest)):

            room_type = str(guest[i][2])

            num_nights = int(guest[i][3])
            


            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights

            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights

            else:
                subtotal = ROOM_RATES[2] * num_nights



            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + salestax + occupancy
             
            grandtotal += total

            guest[i].append(subtotal)

            guest[i].append(salestax)

            guest[i].append(occupancy)

            guest[i].append(total)



def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} h2, h3 {margin: 0; text-align: center;} </style> </head>\n')
    f.write('<body style ="background-image: url(midBKG.webp); color: #000000;">\n')



def create_output_html():
    currency ="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]
    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan="7">'
    sp = " "

    f.write('\n<table border="1"   style ="background-color: #ffffff;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>Emerald Beach Hotel & Resort</h2><br><h3>Sales Report</h3></td></tr>')
    
    f.write(tr + '<b>Last Name</b>' + endtd + '<b>First Name</b>' + endtd + '<b># Nights</b>' + endtd + '<b>Subtotal</b>' + endtd + '<b>Sales Tax</b>' + endtd + '<b>Occ. Tax</b>' + endtd + '<b>Total</b>' + endtr)

    for i in range(len(guest)):
        f.write(tr + guest[i][0] + endtd + guest[i][1] + endtd + guest[i][3] + endtd + format(guest[i][4],currency) + endtd + format(guest[i][5],currency) + endtd + format(guest[i][6],currency) + endtd + format(guest[i][7],currency) + endtr)

    f.write('<tr><td colspan="6">' + '<b>Grand Total</b>' + endtd + '<b>' + format(grandtotal,currency) + '</b>' + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table>')
    f.write('</body></html>')
    f.close()
    print('Open "' + outfile + '" to view data.')

# EXCECUTE >:) #

main()

