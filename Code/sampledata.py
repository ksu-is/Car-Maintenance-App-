from Admin import Admin
from Appointment import Appointment
from Maintenance import Mechanic
from customer import customer

class SampleData:

    def __init__(self,user):
        self.user = user

    def returnSample(self):
        return self.user
    
    def adminList(txt):
        admins = []
        admins.append("todd")
        admins.append("brooks")
        isAdmin = False
        print(txt)
        if txt in admins:
            isAdmin = True

        return isAdmin
    
    def mechList(user):
        mechs = []
        mechs.append("jeff")
        mechs.append("conner")
        isMech = False
        print(user)
        if user in mechs:
            isMech = True

        return isMech

    

# sample appointments
class SampleAppointments:

        # samople cusotmers
        c1 = customer("sally", "s@s.com","metro")
        c2 = customer("bob", "s@s.com","metro")
        c3 = customer("conner", "s@s.com","metro")
        c4 = customer("wendi", "w@w.com","BMW")

        ## sample mechanics
        m1 = Mechanic("brooks")
        m2 = Mechanic("jeff")

        ## sample array of appointments
        
        a1 = Appointment(c1,"8:00","Monday",m1)
        a2 = Appointment(c1, "9:00", "Monday",m2)
        sampleAppts = []
        sampleAppts.append(a1)
        sampleAppts.append(a2)

        def GetAppts(self):
            return self.sampleAppts

class SampleCustomers:
     # samople cusotmers
        c1 = customer("sally", "s@s.com","metro")
        c2 = customer("bob", "s@s.com","metro")
        c3 = customer("conner", "s@s.com","metro")
        c4 = customer("wendi", "w@w.com","BMW")

        custArray = []
        custArray.append(c1)
        custArray.append(c2)
        custArray.append(c3)
        custArray.append(c4)

    
