import array as ar

#Program Starts

name = input("[Login] Enter Your username: ")

#username validation if required goes here
print("Welcome "+name)


Running = True

#Events booking
events = []

#Booking quantity
qty = []


def applyDiscounts():

    i=0
    discount = 0
    totalDeals = 0
    special = 0

    while i<len(events):
        index = events[i]

        #Any new discount logic can be easily added into this area

        #Team building discounts
        if events[i]==3 and qty[i]>1:
            qt = int(qty[i]/2)
            discount += qt*100

        #Wine tours and picnics
        if events[i]==2 or events[i]==4:
            #qt = qty[i]/4
            #discount += qt*440
            special+=qty[i]

            if special>3:
                qt = qty[i]/4
                if events[i] == 2:
                    discount+=440
                elif events[i]==4:
                    discount+=110

        # Picnics
        if events[i] == 4 and qty[i] > 2 and special<4:
            qt = qty[i] / 2
            discount += qt * 110

        if events[i]==4 and qty[i]>3:
            qt = qty[i]/4
            discount += qt * 110

        totalDeals += qty[i]

        #if at anytime total deals = 5 or multiples, instant 20% discount is added on the 5th event booking
        if totalDeals%5==0:
            if events[i]==1: discount+= 44
            elif events[i]==2: discount+= 88
            elif events[i]==3: discount+= 160
            else: discount+= 22

        i+=1



    return discount


def calculate_total():

    #Hardcoded for the sake of simplicity, otherwise would have read these values from the db.
    costs = [220,440,800,110]

    i = 0
    net = 0
    while i<len(events):
        index = events[i]-1
        net += costs[index]*qty[i]
        i+=1


    print("Total Cost = "+str(net))

    discounts = applyDiscounts()
    print("Discount = "+str(discounts))

    netcost = net - discounts
    print("Net Cost = "+str(netcost))


    #Optional Logging at the end
    file = open("bookings.txt", "at")
    file.write("\n User "+name+" booked event(s) costing "+str(netcost))
    return


#Program Flow starts here
#Display Choices

while Running:
    #Hardcoded because of simplicity otherwise could have been in an array read from the databse
    print("-----")
    print("1 - Kids Party $220")
    print("2 - Wine Tours $440")
    print("3 - Team Building $800")
    print("4 - Picnic $110")




    choice = input("Enter Event ['0' to End] ")
    print("---- ")


    if int(choice)==0:
        Running = False

    ## Choice validations (such as escape chars etc) can be applied here if necessary

    if Running:
        amount = input("How many tickets? ")
        events.append(int(choice))
        qty.append(int(amount))


calculate_total()

