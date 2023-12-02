from sampledata import SampleData
from sampledata import SampleAppointments
from Appointment import Appointment
from Admin import Admin
from Maintenance import Mechanic
from customer import customer



def main():
    user = input("Please enter your unser name  ")
    pwd = input("Please enter your password  ")
    #print("hello" + user)
    data = SampleData(user)
    MYNAME = data.returnSample()
    ## print(MYNAME)
    cust = customer(user,user,pwd)
    ## check to see if admin

    isAdmin = SampleData.adminList(data.user)
    print(isAdmin)
    
    ## if admin, do admoin functions
    if(isAdmin):
      admn = Admin(cust,user,pwd)
    
    ## check to see if mechanic
    ##isMech = SampleData.mechList(user)
    ##if(isMech):
    ##    MechFuncs()
    
    a = SampleAppointments


    for Appointment in a.sampleAppts:
        print("YOU")
    



    
    print("")


if __name__ == "__main__":
    main()



def UserFuncs(self, user):
    print("I AM AN USER AND WILL DO SHIITTY USER THINGS")
    ## check to see if user exists

    ## if no user, ask to creat an account

    ## select a servies and time
    return

def AdminFuncs(self, user):
    print("I AM AN ADMIN AND WILL DO ADMIN THINGS")
    # list available mechanics

    #assign task

    return


def MechFuncs(self, user):
    print("")
    # list open tasks

    # open task

    #close task
    return
