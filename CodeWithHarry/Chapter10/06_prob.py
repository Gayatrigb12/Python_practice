from random import randint

class Train:
    def __init__(self , trainNo):
        self.trainNo = trainNo
    def book(self , frm , to):
        print(f"Ticket is booked in train no {self.trainNo} from {frm} to {to}")
    def getStatus(self):
        print(f"train no {self.trainNo} is running on time")

    def getFare(self  , frm , to ):
        print(f"Ticket Fare in train no :{self.trainNo} from {frm} to {to} is {randint(30 , 1000)}")


t = Train(123342)
t.book("Nashik" , "Mumbai")
t.getFare("Nashik" , "Mumbai")
t.getStatus()