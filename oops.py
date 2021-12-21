# creating a class with instance attributes

'''class Vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage


model = Vehicle(200,30)
print(model.maxspeed,model.mileage)'''

# creating a class and object
'''class Employee:

    company_name = 'ABC organization'

    def __init__(self,name,eid,salary):                 # initialising the object
        self.name =name
        self.eid =eid
        self.salary = salary

    def present(self):                                 # instance method
        print('the employee name is %s with  id %d earning %d'%(self.name,self.eid,self.salary),'in the company',Employee.company_name)



emp = Employee('sasikanth',1322,30000)
emp.present()'''

# inheritence

class Vehicle:
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity*100

class Bus(Vehicle):
    pass


s = Bus('swaraj',90,10)
print('the fare charges for 10 members are',s.fare())
print('the vehicle name is ',s.name,'gives mileage of',s.mileage,'km/l')
print('the vehicle bears the capacity of',s.capacity,'members')




