#Subclass inherit object(attributes and methods) from superclass or parent class and also have updated methods of itself.

class Car(object):
    def __init__(self,transmission,drivetrain):
        self.mileage = 0
        self.mpg = 0
        self.transmission = transmission
        self.drivetrain = drivetrain
    def fuel(self):
        self.mpg = 300
        return self
    def drive(self):
        self.mileage += 60
        return self
    def result(self):
        if self.mpg == 0:
            print ("Please pump gas.")
        else:
            self.miles = self.mpg - self.mileage
            print ("You have " + str(self.miles) + " miles left.")
class Tesla(Car):
    def charge(self):
        self.mpc = 500
        return self
    def result(self):
        if self.mpg == 0:
            print ("Please charge your battery.")
            return self
        else:
            self.miles = self.mpc - self.mileage
            print ("You have " + str(self.miles) + " miles left.")
            return self

Toyota = Car("auto",4)
Toyota.fuel().drive().drive().drive().result()
Tesla1 = Tesla("auto",2)
Tesla1.drive().drive().result()

#Calling superclass when you want to inherite attributes and methods from parents and update attributes and methods in child class.

class Cars(object):
    def __init__(self,transmission,drivetrain):
        self.mileage = 0
        self.mpg = 0
        self.transmission = transmission
        self.drivetrain = drivetrain
    def fuel(self):
        self.mpg = 300
        return self
    def drive(self):
        self.mileage += 60
        return self
    def result(self):
        if self.mpg == 0:
            print ("Please pump gas.")
        else:
            self.miles = self.mpg - self.mileage
            print ("You have " + str(self.miles) + " miles left.")
class Hybrid(Cars):
    def __init__(self,transmission,drivetrain):
        super(Hybrid,self).__init__(transmission,drivetrain)
        self.mpc = 0
    def charge(self):
        self.mpc = 250
        return self
    def result(self):
        if self.mpg == 0 & self.mpc == 0:
            print("Please pump gas to charge battery.")
        else:
            self.miles = (self.mpc + self.mpg) - self.mileage
            print ("You have " + str(self.miles) + " miles left.")

Toyota_hybrind = Hybrid("auto",2)
Toyota_hybrind.fuel().charge().drive().result()