import sampledata
import Maintenance
import os


class customer:
    def __init__ (self, name, email, car):
        self.name = name
        self.email = email
        self.car = car
 

#check to see if customer exists
    def checkCustomer(self):
        sample =sampledata.SampleCustomers
        for customer in sample.custArray:
            #if self.name = customer.__name__:
            return False
        
              



#This line will create a new customer
    def createcustomer():
        return
    

# code to make appointment
    def makeappt(self):
        os.system('cls')
        #ask work needed done
        print("Hello " + self.name + "!  What would you like done today?")
        
        exitText = ""
        while exitText != "exit":

            # start - get work to be donw
            w = Maintenance.Work
            x = 1
            for work in w.work:
                print(str(x) + " -- " + work)
                x += 1

            wSelected = input("Please select from an option above or type 'exit' to discontinue ")

            if wSelected != 'exit':
                os.system('cls')
                print("you have selected " + w.work[int(wSelected)-1])
            
            else:
                exitText = wSelected

            # days
            print("Please select a day to schedule " + w.work[int(wSelected)-1])
            days = []
            d1 = "Monday"
            d2 = "Teusday"
            d3 = "Wednesday"
            d4 = "Thursday"
            d5 = "Friday"

            days.append(d1)
            days.append(d2)
            days.append(d3)
            days.append(d4)
            days.append(d5)

            x = 1
            for day in days:
                print(str(x) + " - " + day)
                x += 1
            
            dSelected = input("Please select from an option above or type 'exit' to discontinue ")

            if dSelected != 'exit':
                ##os.system('cls')
                print("you have selected " + days[int(dSelected)-1])
            
            else:
                exitText = dSelected

            

            os.system('cls')
            # get times

            print("Please select a time to schedule " + w.work[int(wSelected)-1] + " on " + days[int(dSelected)-1])
            tme = []
            t1 = "8"
            t2 = "9"
            t3 = "10"
            t4 = "11"
            t5 = "12"
            t6 = "13"
            t7 = "14"

            tme.append(t1)
            tme.append(t2)
            tme.append(t3)
            tme.append(t4)
            tme.append(t5)
            tme.append(t6)
            tme.append(t7)
        
            x =1
            for t in tme:
                print(str(x) + " - " + t)
                x += 1


            tSelected = input("Please select from an option above or type 'exit' to discontinue ")

            #cc = tme[int(tSelected)-1]
            #print(cc)
            os.system('cls')
            print(" You have selected " + w.work[int(wSelected)-1] + " on " + days[int(dSelected)-1] + " at " + tme[int(tSelected)-1] + " ")

            vConfirm = input("Please press '1' to confirm appointment")
            if int(vConfirm) == 1:
                print("thank you for making your appointment")
                #add to the array of appointments

                #exit
                exitText = "exit"                



        return
    