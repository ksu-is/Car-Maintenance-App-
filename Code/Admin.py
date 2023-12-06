import sampledata
import Appointment
import Maintenance
import customer
import os

class Admin:
    def __init__ (self, customer, name, password):
        # print("I AM AN ADMIN AND WILL DO ADMIN THINGS")
        return
   
    # This line of code will see if they are admins
    def checkadmin():
        
        return
    
    #check to see if admin
    def checkIsAdmin(self, user):
        print("in method")
        admins = []
        admins.append("todd")
        admins.append("brooks")
        isAdmin = False
        ## print(user)

        x = 0
        for txt in admins:
            print(user + " :" + admins[x])
            cc = admins[x]
            if cc == user:
                isAdmin = True
                print("yes")
            x +=1
            print("xxx:" + str(x))


        #if user in admins:
        #    print(user + "  : " + admins.index)
        #    isAdmin = True

        return isAdmin
    

    #this line of code will create admins
    def createadmin():
        
        return
   
    #this line of code will delete admins
    def deleteadmin():
        return
    
    #list work
    def AssignAvailableWork(self):
        #work = sampledata.SampleAppointments()
        #print(len(work))
        #for apt in work.GetAppts:
            #print("APPOINTMENTS " + work.c1.name)
        os.system('cls')
        print("--------------------------------------------------------")
        print(" ")
        print("WELCOME TO THE BROOKS PETERSON AUTO SHOP")
        print(" ")
        print(" ADMIN MENU")
        print(" ")
        print("--------------------------------------------------------")
        print(" ")
        print(" Please select an option")
        print(" ")
        print("1 - Assign Appointment")
        print("2 - Exit")
        aopt = "" 

        while aopt != "2":
            aopt =  input("Submenu select an option ")

        

    def AdminMenu(self):
        os.system('cls')
        print("--------------------------------------------------------")
        print(" ")
        print("WELCOME TO THE BROOKS PETERSON AUTO SHOP")
        print(" ")
        print(" ADMIN MENU")
        print(" ")
        print("--------------------------------------------------------")
        print(" ")
        print(" Please select an option")
        print(" ")
        print("1 - View Appointments")
        print("2 - Assign Appointment")
        print("3 - Exit")

        
        opt =  input("Please select an option ")
        while opt != "3":
            if opt == "2":
                self.AssignAvailableWork()
                opt =  "3"
                self.AdminMenu()
                
            if opt == "1":
                self.ViewAppointments()
                opt =  "3" 
                self.AdminMenu()
                

    

    def ViewAppointments(self):
        os.system('cls')
        print("--------------------------------------------------------")
        print(" ")
        print("WELCOME TO THE BROOKS PETERSON AUTO SHOP")
        print(" ")
        print(" ----- APPOINTMENTS ---- ")
        print(" ")
        print("--------------------------------------------------------")
        print(" ")
        print(" Please select an option")
        print(" ")
        #print("1 - View Appointments")
        #print("2 - Assign Appointment")
        print("1 - Exit")
        print(" ")
        print("--------------------------------------------------------")
        
        print("CUSTOMER  DAY  TIME MECHANIC")
        print("--------------------------------------------------------")

        # get sample data aand show
        sAppts = sampledata.SampleAppointments
        arr = sAppts.sampleAppts
        x = len(sAppts.sampleAppts)
        i=0
        while i < x:
            appt = arr[i]
            cust = appt.Customer
            mech = appt.Mechanic
            #print(cust.name)
            ##print(str(len(c)))
            print(str(i) + ": " + cust.name + "  " + appt.Day + " " + appt.Time  + "  " + mech.name)
            i += 1

        
        #print(str(x))

        vopt =  ""
        while vopt != "3":
           vopt = input("HIT 3 TO EXIT ")
    

