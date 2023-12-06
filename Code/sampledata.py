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
        a3 = Appointment(c1, "10:00", "Teusday",m2)
        a4 = Appointment(c2, "9:00", "Monday",m2)
        a5 = Appointment(c3, "9:00", "Monday",m1)
        a6 = Appointment(c4, "9:00", "Monday",m2)
        a7 = Appointment(c1, "9:00", "Fridat",m1)
        a8 = Appointment(c2, "9:00", "Monday",m2)
        sampleAppts = []
        sampleAppts.append(a1)
        sampleAppts.append(a2)
        sampleAppts.append(a3)
        sampleAppts.append(a4)
        sampleAppts.append(a5)
        sampleAppts.append(a6)
        sampleAppts.append(a7)
        sampleAppts.append(a8)

        def GetAppts(self):
            return self.sampleAppts

class SampleCustomers:
     # sample cusotmers
        c1 = customer("sally", "s@s.com","metro")
        c2 = customer("bob", "s@s.com","metro")
        c3 = customer("conner", "s@s.com","metro")
        c4 = customer("wendi", "w@w.com","BMW")

        custArray = []
        custArray.append(c1)
        custArray.append(c2)
        custArray.append(c3)
        custArray.append(c4)

    
