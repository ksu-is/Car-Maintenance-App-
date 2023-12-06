import sampledata
import Appointment
import Admin
import Maintenance
import customer
import os



def main():
    os.system('cls')
    print("--------------------------------------------------------")
    print(" ")
    print("WELCOME TO THE BROOKS PETERSON AUTO SHOP")
    print(" ")
    print("--------------------------------------------------------")
    user = input("Please enter your unser name  ")
    # pwd = input("Please enter your password  ")
    #print("hello" + user)
    data = sampledata.SampleData(user)
    ## get list of sample data appointments
    a = sampledata.SampleAppointments

    # get list opf sample admins


    # get list of sample customers

    # get list of sample work

    # get list mechs

    ## MYNAME = data.returnSample()
    ## print(MYNAME)


    pwd =""
    # make customer (user)
    cust = customer.customer(user,user,pwd)
    ## check to see if admin
   
    isCust = True
    ##isAdmin = SampleData.adminList(data.user)
    ##print(isAdmin)
    
    ## if admin, do admoin functions
    ##if(isAdmin):
    admn = Admin.Admin(cust,user,pwd)
    if(admn.checkIsAdmin(user)):
        adx = "0"
        while adx != "1":
            print("I am an admin")
            admn.AdminMenu()
            isCust = False
            adx = input("press 1 to exit ")
            
     
    ## check to see if mechanic
    isMech = sampledata.SampleData.mechList(user)
    if(isMech):
        mec = Maintenance.Mechanic(user)

    if isCust:
        ## if just a cusotmer 
        cust.makeappt()
        co =""
        while co != "1":
            co = input("press 1 to exit ")

       


    ##for Appointment in a.sampleAppts:
    ##    print(a.a1.Customer)
    
  
    print("")


if __name__ == "__main__":
    main()

