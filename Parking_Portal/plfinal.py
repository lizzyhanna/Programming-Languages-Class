#Lizzy Hanna Final Exam Program 5/13/19
                
def find_parking_ground():
    lot_ground_rows= [["Honda CR-V", "Chevrolet Silverado", "Honda Accord", "Chevrolet Equinox", "Honda Civic", "Ford F-150", "Mazda CX-5", "Toyota RAV4", "Toyota Highlander", "Honda Pilot", "Toyota Tacoma"], #o row  
			   ["Toyota Camry", "Subaru Forester", "Ram 1500", "Subaru Outback", "Chevrolet Traverse", "Jeep Grand Cherokee", "Jeep Wrangler", "Chevrolet Colorado", "Toyota 4Runner"], #1 row  
			   ["Ford Explorer", "Hyundai Santa Fe", "Subaru Crosstrek", "Acura RDX", "Honda Odyssey", "", "", "", "", "", "", "", ""],  #2nd row
			   ["Ford Mustang", "Dodge Challenger", "", "", "Hyundai Kona", "Lexus RX 350", "", "", "", "", "", "", "", "", "Nissan Rogue", "Hyundai Tucson"], #3rd row
			   ["BMW X3", "Hyundai Elantra", "Ford Edge", "Subaru Ascent", "Jeep Cherokee", "Honda HR-V", "BMW X5", "Toyota Tundra"], #4th row 
			   ["Honda Ridgeline", "Volkswagen Tiguan", "", "", "", "", "", "", "", "", "Volkswagen Atlas"], #5th row
			   ["Mazda CX-9", "Chevrolet Camaro", "Acura MDX", "", "", "", "", "", "", "", ""], #6th row
			   ["Ford Escape", "", "", "", "", "", "", "", "", "Mazda 3", "Audi Q5"], #7th row
			   ["GMC Sierra 1500", "Audi Q7", "", "", "", "", "", "", "", ""]] #8th row
    spot_list = []
    count = 0
    rownum = 0
    totalSpaces = 0
    xcounter = 0
    for i in lot_ground_rows: #each row
        for x in i: 
            if(x == ""):
                count+=1
                totalSpaces += 1
                spot_list.append(xcounter)
            xcounter += 1    
        print("There are " + str(count) + " empty spaces in row " + str(rownum))
        if(count != 0):
            print("Spot(s) number "+ str(spot_list) + " are available.")  
        count = 0
        rownum += 1
        xcounter = 0
        spot_list = []
        
    print("Overall, there are " + str(totalSpaces) + " empty spaces in the Ground Parking Lot.")
    return

def find_parking_multilevel():
    lot_levels_rows_spots= [[["Honda CR-V", "Chevrolet Silverado", "", "", "", "", "", "", "", "", "Honda Accord"], ["Chevrolet Equinox", "Honda Civic", "Ford F-150", "Mazda CX-5", "Toyota RAV4"], ["Toyota Highlander", "Honda Pilot", "Toyota Tacoma"]], #o level 
			   [["Toyota Camry", "Subaru Forester", "", "", "", "", "", "", "", "", "Ram 1500"], ["Subaru Outback", "Chevrolet Traverse", "Jeep Grand Cherokee", "Jeep Wrangler"], ["Chevrolet Colorado", "Toyota 4Runner"]], #1 level  
			   [["Ford Explorer", "Hyundai Santa Fe"], ["Subaru Crosstrek", "Acura RDX"], ["Honda Odyssey"]],  #2nd level
			   [["Ford Mustang", "Dodge Challenger"], ["Hyundai Kona", "Lexus RX 350"], ["Nissan Rogue", "Hyundai Tucson"]], #3rd level
			   [["BMW X3", "Hyundai Elantra", "", "", "", "", "", "", "", ""], ["Ford Edge", "Subaru Ascent", "Jeep Cherokee"], ["Honda HR-V", "BMW X5", "Toyota Tundra"]], #4th level 
			   [["Honda Ridgeline", "Volkswagen Tiguan", "", "", "", "", "", "", "", ""], ["Volkswagen Atlas"]], #5th level
			   [["Mazda CX-9", "Chevrolet Camaro", "", "", "", "", "", "", "", ""], ["Acura MDX", "", "", "", "", "", "", "", ""]], #6th level
			   [["Ford Escape", "", "", "", "", "", "", "", ""], ["Mazda 3", "Audi Q5", "", "", "", "", "", "", "", ""]], #7th level
			   [["GMC Sierra 1500", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "Audi Q7"]]] #8th level
    spot_list = []
    count = 0
    rownum = 0
    levelnum = 0
    totalSpaces = 0
    ycounter= 0
    for i in lot_levels_rows_spots: #each level
        for x in i: #each row (varies)
            for y in x: 
                if(y == ""):
                    count+=1
                    totalSpaces +=1
                    spot_list.append(ycounter)
                ycounter+= 1
            print("There are " + str(count) + " empty spaces in level " + str(levelnum) + ", row " + str(rownum))
            if(count != 0):
                print("Spot(s) number " + str(spot_list) + " are available.")
            count = 0
            rownum += 1
            spot_list = []
            ycounter = 0
        rownum = 0    
        levelnum += 1

    print("Overall, there are " + str(totalSpaces) + " empty spaces in the Multilevel Parking Garage.")
    return

def main():
    print("Hello, welcome to the Parking Portal. Please select a garage:")
    while True:
        try:
            n = int(input("1. Ground Level \n2. Multilevel Garage\n"))
        except ValueError:
            print("Invalid input.")
        else:    
            if(n ==1):
                print("Ground level.\n")
                find_parking_ground()
                break
            elif(n == 2):
                print("Multilevel Garage.\n")
                find_parking_multilevel()
                break
            else:
                print("Invalid input.")    

#runs main
if __name__ == "__main__":
        main()
