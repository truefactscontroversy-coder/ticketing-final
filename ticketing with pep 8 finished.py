def ticketing_system():
    
    #------------------------
    # start of start unit
    #------------------------

    # message to user
    print("Welcome to the CTA ticketing "
          "system please select: start voucher")
    start_now = input()

    # error loop if user does not input correct code
    def start_voucher_check():
        print("please select: start voucher")
        start_now = input()
        if start_now == "start voucher":
            return
        else:
            start_voucher_check()

    if start_now != "start voucher":
        start_voucher_check()

    # voucher list for travel details
    voucher = []
    voucher.append("date / time")
    print("New page loading")
    # end of start unit

    #---------------------------------
    # start of add departure unit
    #---------------------------------

    # function to repeatedly print zones
    ZONES = ["Down town zone", "Mid town zone", "Central zone"]

    # initial user input for departure zone
    print(ZONES)
    print("Please select a starting zone: ")
    your_location = input()

    # error handling function for departure zone
    def next_step():
        print("please select: next")
        please_select = input()
        if please_select == "next":
            print("New page loading")
        else:
            next_step()

    # error handling statment for initial departure zone input
    if (your_location == "Down town zone" or
        your_location == "Mid town zone" or
            your_location == "Central zone"):
        voucher.append(F"Departure zone: {your_location}")
        next_step()
    else:
        while (your_location != "Down town zone" or
               your_location != "Mid town zone" or
               your_location != "Central zone"):
            if (your_location == "Down town zone" or
               your_location == "Mid town zone" or
               your_location == "Central zone"):
                voucher.append(F"Departure zone: {your_location}")
                next_step()
                break
            else:
                print(ZONES)
                print("Please select a vaild zone")
                your_location = input()
    # end of add departure unit

    #-----------------------------------
    # start of add destination unit
    #-----------------------------------

    # station lists for each zone
    DOWN_TOWN_STATION = (
        "Adohad, Brunad, Edert, Elyot, Erean, "
        "Holmer, Kelvia, Mareng, Perinad, Pryn, Ruril, Ryall, Zord"
    )

    MID_TOWN_STATION = (
        "Agraile, Docia, Garon, Obelyn, Oloadus, "
        "Quthiel, Ralith, Riciva, Riladia, Sylas, Wicyt"
    )

    CENTRAL_STATION = (
        "Centrala, Frestin, Jaund, Lomil, "
        "Ninia, Rede, Riciva, Soth, Sylyn, Tallan"
    )

    # initial user input for destination zone
    print("station board with all zones and stations")
    print(f"Down town zone stations: {DOWN_TOWN_STATION}")
    print(f"Mid town zone stations: {MID_TOWN_STATION}")
    print(f"Central zone stations: {CENTRAL_STATION}")
    print(ZONES)
    print("Please select a destinationn zone: ")

    destination_zone = input()
    # error handling function for destination zone

    # error handling statment for initial destination zone input
    if (destination_zone == "Down town zone" or
        destination_zone == "Mid town zone" or
        destination_zone == "Central zone"):
        voucher.append(F"Destination zone: {destination_zone}")
    else:
        while (destination_zone != "Down town zone" or
               destination_zone != "Mid town zone" or
               destination_zone != "Central zone"):
            if (destination_zone == "Down town zone" or
               destination_zone == "Mid town zone" or
               destination_zone == "Central zone"):
                voucher.append(F"Destination zone: {destination_zone}")
                break
            else:
                print(ZONES)
                print("Please select a vaild zone")
                destination_zone = input()

    # calculation of zones traveled through
    if your_location == destination_zone:
        zone_num = 1
        next_step()
    elif (your_location == "Down town zone" and
          destination_zone == "Central zone"):
        zone_num = 3
        next_step()
    elif (your_location == "Central zone" and
          destination_zone == "Down town zone"):
        zone_num = 3
        next_step()
    else:
        zone_num = 2
        next_step()
    # end of add destination unit

    #------------------------------------------
    # start of add destination station unit
    #------------------------------------------

    # display station list based on destination zone

    # error handling system for if downtown is selected
    if destination_zone == "Down town zone":
        print(f"List of stations for down town: {DOWN_TOWN_STATION}")
        print("Please select a station: ")
        destination_station = input()
        if destination_station in DOWN_TOWN_STATION:
            voucher.append(f"destination station: {destination_station}")
            next_step()
        else:
            while (destination_station != DOWN_TOWN_STATION for destination_station in DOWN_TOWN_STATION):
                if destination_station in DOWN_TOWN_STATION:
                    voucher.append(
                        f"destination station: {destination_station}")
                    next_step()
                    break
                else:
                    print("Please select a station:")
                    destination_station = input()

    # error handling system for if mid town is selected
    if destination_zone == "Mid town zone":
        print(f"List of stations for midtown: {MID_TOWN_STATION}")
        print("Please select a station: ")
        destination_station = input()
        if destination_station in MID_TOWN_STATION:
            voucher.append(f"destination station: {destination_station}")
            next_step()
        else:
            while (destination_station != MID_TOWN_STATION for destination_station in MID_TOWN_STATION):
                if destination_station in MID_TOWN_STATION:
                    voucher.append(
                        f"destination station: {destination_station}")
                    next_step()
                    break
                else:
                    print("Please select a station:")
                    destination_station = input()

    # error handling for if central is selected
    if destination_zone == "Central zone":
        print(f"List of stations for {CENTRAL_STATION}")
        print("Please select a station: ")
        destination_station = input()
        if destination_station in CENTRAL_STATION:
            voucher.append(f"destination station: {destination_station}")
            next_step()
        else:
            while (destination_station != CENTRAL_STATION for destination_station in CENTRAL_STATION):
                if destination_station in CENTRAL_STATION:
                    voucher.append(
                        f"destination station: {destination_station}")
                    next_step()
                    break
                else:
                    print("Please select a station:")
                    destination_station = input()
    # end of add destination station unit
    #---------------------------------
    # start of add passenger unit
    #---------------------------------

    # initial message to user
    print("cost of one zone is automatically added to total cost")
    print("cost will double for two zones and triple for three zones")
    print("catagory selction and add buttons")

    print("price page")
    print("Adult: 2105 cents per zone")
    print("Child: 1410 cents per zone")
    print("Student: 1750 cents per zone")
    print("Elderly: $1025 cents per zone")

    # user input for passenger catagory
    def passenger_catagory_adult():
        print("Adult : add number of passengers")
        adult = int(input())
        if adult <= 0:
            adult = 0
        return adult

    def passenger_catagory_child():
        print("Child: add number of passengers")
        child = int(input())
        if child <= 0:
            child = 0
        return child

    def passenger_catagory_student():
        print("Student: add number of passengers")
        student = int(input())
        if student <= 0:
            student = 0
        return student

    def passenger_catagory_elderly():
        print("Elderly: add number of passengers")
        elderly = int(input())
        if elderly <= 0:
            elderly = 0
        return elderly

    adult_cost = passenger_catagory_adult()
    child_cost = passenger_catagory_child()
    student_cost = passenger_catagory_student()
    elderly_cost = passenger_catagory_elderly()
    total_passenger = adult_cost + child_cost + student_cost + elderly_cost

    if (total_passenger != 0):
        voucher.append(f"Total number of passengers: {total_passenger}")
        next_step()
    else:
        while total_passenger == 0:
            if (total_passenger != 0):
                voucher.append(
                    f"Total number of passengers: {total_passenger}")
                next_step()
                break
            else:
                print("please add at least one passenger")
                adult_cost = passenger_catagory_adult()
                child_cost = passenger_catagory_child()
                student_cost = passenger_catagory_student()
                elderly_cost = passenger_catagory_elderly()
                total_passenger = adult_cost + child_cost + student_cost + elderly_cost
    # end of add passenger unit
    #---------------------------------------
    # start of passenger calculation unit
    #---------------------------------------

    adult_cost *= 2105
    adult_cost *= zone_num
    voucher.append(f"Total Adult cost in cents: {adult_cost}")

    child_cost *= 1410
    child_cost *= zone_num
    voucher.append(f"Total Child cost in cents: {child_cost}")

    student_cost *= zone_num
    voucher.append(f"Total Student cost in cents: {student_cost}")

    elderly_cost *= 1025
    elderly_cost *= zone_num
    voucher.append(f"Total Elderly cost in cents: {elderly_cost}")

    total_cost = adult_cost + child_cost + student_cost + elderly_cost
    voucher.append(f"Total cost of trip in cents: {total_cost}")
    # end of passenger calculation unit

    #-----------------------------------
    # start of voucher print unit
    #-----------------------------------

    # subtraction of zone to comply with required output
    if zone_num == 1:
        voucher.append("Zones traveled through: None")
    elif zone_num != 1:
        zone_num -= 1
        voucher.append(f"Zones traveled through: {zone_num}")

    print(voucher)
    # end of voucher print unit

    #--------------------------------
    # start of restart or end unit
    #--------------------------------

    print(
        "Type 'start a new voucher' to start a new voucher "
        "or 'end process' to end voucher process")
    restart_end = input()

    # function for error handling of restart or end input
    while (restart_end != "start a new voucher" or
           restart_end != "end process"):
        if restart_end == "end process":
            print("new page loading")
            print("Thank you for using the ticketing system")
            break
        elif restart_end == "start a new voucher":
            ticketing_system()
            break
        else:
            print("please select: start a new voucher or end process")
            restart_end = input()

    if restart_end == "end process":
        print("new page loading")
        print("Thank you for using the ticketing system")
    elif restart_end == "start a new voucher":
        ticketing_system()


ticketing_system()

#------------------------
# end of project
#------------------------
