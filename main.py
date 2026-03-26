import tkinter as tk                            # import tkinter library
from tkinter import ttk,messagebox,simpledialog #import tkinter submodule from tkinter library,message pop up box create korbe,puro ekat window design na kore choto choto input box hisebe vese uthe screen e
# from PIL import Image, ImageTk                  # ami kono background pic  dekhte cai ei project e setar jonno Pillow library
class Ticket:
    ticket_counter=1                            # value 1
    def __init__(self, passenger_name, start, end, fare, quantity): # proti ta jatrir er jonno ekta unique id save kora hocce
        self.id = Ticket.ticket_counter
        Ticket.ticket_counter += 1              # prothom jatri assing korar porei counter er value 1 bariye 2 kora hbe
 
        self.passenger_name = passenger_name    
        self.start = start
        self.end = end
        self.fare = fare
        self.quantity = quantity
        self.total = fare * quantity
 
    def __str__(self):
        return f"{self.passenger_name} | {self.start} to {self.end} | {self.quantity} Ticket | Total: {self.total} BDT"

stations = [
    "Uttara North", "Uttara Center", "Uttara South", "Pallabi","Mirpur 11", "Mirpur 10", "Kazipara", "Shewrapara","Agargaon", 
    "Bijoy Sarani", "Farmgate", "Karwan Bazar","Shahbagh", "Dhaka University", "Bangladesh Secretariat", "Motijheel"
]

class MetroSystem:  
    def __init__(self):                       #jokhon object ready  hbe tokhon automatically run hbe
        self.tickets = []                     # ei empty list e ticket rakha hbe
        
    def get_fare(self, start, end):
        if start == end:
            return 0  # same station
        if start not in stations or end not in stations:
            return 0  # invalid station

        # distance between stations
        d1 = stations.index(start)
        d2 = stations.index(end)
        distance = abs(d1 - d2)

        # base fare + per station fare
        base_fare = 20
        per_station_fare = 10

        return base_fare + distance * per_station_fare

    def book_ticket(self, passenger_name, passenger_type, train, start, end, fare, quantity):
        ticket = Ticket(passenger_name, passenger_type, train, start, end, fare, quantity)    #notun ticket object toiri hbe
        self.tickets.append(ticket)                                                           # ticket list e add hbe
        return ticket                                                                         # oi ticket ta resturn korbe

    def delete_ticket(self, ticket_id):                                                       #ticket ta deleted korar jonno
        for t in self.tickets:                                                                # loop create hbe list er sob ticket loop wise
            if t.id == ticket_id:                                                             # jodi id match kore tahole ticket deleted 
                self.tickets.remove(t)                                                        # remove kore dibe
                return True                                                                   #deleted hole true return korbe
        return False                                                                          #nahole false return korbe

    def search_tickets(self, keyword):                                                        #passenger name diye search korar jonno
        result = []                                                                           #result name er empty list toiri hbe
        for t in self.tickets:                                                                # sob ticket loop hbe na
            if keyword.lower() in t.passenger_name.lower():                                   #ami ja likhtesi seta choto hater word hbe and passenger er name er choto hater hbe jodi boro hhatero likhi seta choto hater sathe match korbe
                result.append(t)                                                              #match hike t list e add hbe
        return result

    def total_fare(self):
        total = 0                                                                            # variable 0 first e kono tk add hoi ni
        for t in self.tickets:                                                               # ek ek kore proti ta ticket t ney hocce
            total += t.total                                                                 #total vara add hocce
        return total 
