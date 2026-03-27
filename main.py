import tkinter as tk                            # import tkinter library
from tkinter import ttk,messagebox,simpledialog #import tkinter submodule from tkinter library,message pop up box create korbe,puro ekat window design na kore choto choto input box hisebe vese uthe screen e
from datetime import date

class Ticket:
    ticket_counter=1                            # value 1
    def __init__(self, passenger_name, start, end, fare, quantity, passenger_type="General"): # proti ta jatrir er jonno ekta unique id save kora hocce
        self.id = Ticket.ticket_counter
        Ticket.ticket_counter += 1              # prothom jatri assing korar porei counter er value 1 bariye 2 kora hbe
 
        self.passenger_name = passenger_name    
        self.start = start
        self.end = end
        self.fare = fare
        self.quantity = quantity
        self.total = fare * quantity
        self.passenger_type = passenger_type
        self.date = date.today()
 
    def __str__(self):
        return f"{self.passenger_name} | {self.start} to {self.end} | {self.quantity} Ticket | Total: {self.total} BDT"

stations = [
    "Uttara North", "Uttara Center", "Uttara South", "Pallabi","Mirpur 11", "Mirpur 10", "Kazipara", "Shewrapara","Agargaon", 
    "Bijoy Sarani", "Farmgate", "Karwan Bazar","Shahbagh", "Dhaka University", "Bangladesh Secretariat", "Motijheel"
]

class MetroSystem:  
    def __init__(self):
        self.tickets = []

    def get_fare(self, start, end, passenger_type="General"):
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

        fare = base_fare + distance * per_station_fare

        # Apply discount
        if passenger_type == "Student":
            fare = fare * 0.50
        elif passenger_type == "Disabled":
            fare = fare * 0.20
        
        return fare 

    def book_ticket(self, passenger_name, start, end, quantity, passenger_type="General"):                           # book_ticket name e ekta methos hbe ja notun ticket book korar jonno use hbe
        fare = self.get_fare(start, end, passenger_type)                                                   # start station theke end station porjonto fare calculate korar jonno get_fare method call kora hbe
        ticket = Ticket(passenger_name, start, end, fare, quantity, passenger_type)                         #ticket class er object toiri kora hbe ja passenger name, start station, end station, fare and quantity receive korbe                     
        self.tickets.append(ticket)                                                         # toiri kora ticket list e add kora hbe
        return ticket

    def delete_ticket(self, ticket_id):                                                     #delete_ticket name e ekta method hbe ja ticket id receive korbe and oi id er ticket list theke delete korbe
        for t in self.tickets:                                                              #ticket list e loop hbe and jodi kono ticket er id match kore oi id er ticket list theke remove kora hbe and true return kora hbe
            if t.id == ticket_id:                                                           #ticket id match korle oi ticket list theke remove kora hbe
                self.tickets.remove(t)                                                       #tahole oi ticket list theke remove kora hbe
                return True
        return False                                                                          #nahole false return korbe

    def search_tickets(self, keyword):                                                        #passenger name diye search korar jonno
        result = []                                                                           #result name er empty list toiri hbe
        for t in self.tickets:                                                                
            if keyword.lower() in t.passenger_name.lower():                                   #ami ja likhtesi seta choto hater word hbe and passenger er name er choto hater hbe jodi boro hhatero likhi seta choto hater sathe match korbe
                result.append(t)                                                              #match hike t list e add hbe
        return result

    def total_fare(self):
        total = 0                                                                            #total fare calculate korar jonno total variable toiri kora hbe ja 0 diye initialize kora hbe  
        for t in self.tickets:                                                               # ek ek kore proti ta ticket t ney hocce
            total += t.total                                                                 #ticket er total fare add kora hbe total variable e
        return total 
   

# Tkinter GUI 
class MetroApp:
    def __init__(self, root):
        # pass
        self.metro = MetroSystem() # Creating metro system object & hold this reference in self.metro attribute of MetroApp Class. Purpose for accessing the MetroSystem class methods
        self.root = root # the root will be an attribute of the MetroApp object, representing the Tkinter main window.
        self.root.title("Metro Rail Management System")
        self.root.geometry("1200x600")
        
    # Left Frame
        # Frame Label
        self.left_frame = tk.Frame(root, padx=10, pady=10)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
    
        # Name Label
        name_label = tk.Label(self.left_frame, text="Passenger Name:")
        name_label.pack(anchor=tk.W)
        self.name_entry = tk.Entry(self.left_frame)
        self.name_entry.pack(anchor=tk.W, fill=tk.X)
        
        # Start Station Label
        startStation_label = tk.Label(self.left_frame, text="Start Station:")
        startStation_label.pack(anchor=tk.W)
        self.start_combo = ttk.Combobox(self.left_frame, values=stations) 
        self.start_combo.current(0) # First option of ComboBox is noted as index 0
        self.start_combo.pack(anchor=tk.W, fill=tk.X)
        
        # End Station Label
        endStation_label = tk.Label(self.left_frame, text="End Station:")
        endStation_label.pack(anchor=tk.W)
        self.end_combo = ttk.Combobox(self.left_frame, values=stations)
        self.end_combo.current(1) # Second option of ComboBox is noted as another station's index number
        self.end_combo.pack(anchor=tk.W, fill=tk.X)
        
        # Quantity Label
        quantity_label = tk.Label(self.left_frame, text="Quantity:")
        quantity_label.pack(anchor=tk.W)
        self.quantity_spin = tk.Spinbox(self.left_frame, from_=1, to=10)
        self.quantity_spin.pack(anchor=tk.W, fill=tk.X)

        # Passenger Type Label
        passenger_type_label = tk.Label(self.left_frame, text="Passenger Type:")
        passenger_type_label.pack(anchor=tk.W)
        self.passenger_type_combo = ttk.Combobox(self.left_frame, values=["General", "Student", "Disabled"], state="readonly")
        self.passenger_type_combo.current(0)
        self.passenger_type_combo.pack(anchor=tk.W, fill=tk.X)
        
        # Button Design
        book_Ticket = tk.Button(self.left_frame, text="Book Ticket", bg="blue", fg="white", command=self.book_ticket)
        book_Ticket.pack(fill=tk.X, pady=5)
        delete_Ticket = tk.Button(self.left_frame, text="Delete Ticket", bg="red", fg="white", command=self.delete_ticket)
        delete_Ticket.pack(fill=tk.X, pady=5)
        search_Ticket = tk.Button(self.left_frame, text="Search Ticket", bg="green", fg="white", command=self.search_ticket)
        search_Ticket.pack(fill=tk.X, pady=5)
        show_all_Tickets = tk.Button(self.left_frame, text="Show All Tickets", bg="purple", fg="white", command=self.show_all_tickets)
        show_all_Tickets.pack(fill=tk.X, pady=5)
        total_Fare = tk.Button(self.left_frame, text="Total Fare", bg="orange", fg="black", command=self.show_total_fare)
        total_Fare.pack(fill=tk.X, pady=5)
        
    # Right Frame
        # Frame Label
        self.right_frame = tk.Frame(root, padx=10, pady=10)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Grid View 
        columns = ("ID", "Name", "Start", "End", "Quantity", "Type", "Total", "Date")
        self.tree = ttk.Treeview(self.right_frame, columns=columns, show="headings") # Create the table structure

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor=tk.CENTER)

        # Create Scrollbar
        scrollbar = ttk.Scrollbar(self.right_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.pack(fill=tk.BOTH, expand=True)
        
# Button Functions
    # Buy Ticket btn method
    def book_ticket(self):
        name = self.name_entry.get()
        start = self.start_combo.get()
        end = self.end_combo.get()
        quantity = self.quantity_spin.get()
        passenger_type = self.passenger_type_combo.get()

         # Validation
        # Check if name contains any numbers
        for st in name:
            if st.isdigit():
                messagebox.showwarning("Warning", "Passenger name cannot contain numbers")
                return
    
        # Check if any field is empty
        if name == "" or start == "" or end == "":
            messagebox.showwarning("Warning", "Please fill all the fields")
            return

        # Check if start and end are the same
        if start == end:
            messagebox.showwarning("Warning", "Start and End stations cannot be the same")
            return
            
        # Validation: Quantity must be numeric
        if not quantity.isdigit():
            messagebox.showwarning("Warning", "Quantity must be a number")
            return

        # Convert quantity to integer after passing numeric check
        quantity = int(quantity)
 
        # Check if quantity is valid
        if quantity <= 0:
            messagebox.showwarning("Warning", "Quantity must be at least 1")
            return

        ticket = self.metro.book_ticket(name, start, end, quantity, passenger_type)
        messagebox.showinfo("Success", f"Ticket Booked!\nTotal Fare: {ticket.total} BDT")
        self.name_entry.delete(0, tk.END) # Clear the input field 
        self.show_all_tickets()

    # Delete Ticket btn method
    def delete_ticket(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a ticket to delete")
            return
        ticket_id = int(self.tree.item(selected[0])["values"][0])
        if self.metro.delete_ticket(ticket_id):
            messagebox.showinfo("Deleted", "Ticket deleted successfully")
            self.show_all_tickets()

    # Search Ticket btn method
    def search_ticket(self):
        keyword = self.name_entry.get()
        results = self.metro.search_tickets(keyword)

        children = self.tree.get_children()  
        for child in children:
            self.tree.delete(child)  
            
        for t in results:
            self.tree.insert("", tk.END, values=(t.id, t.passenger_name, t.start, t.end, t.quantity, t.passenger_type, t.total, t.date))
        self.name_entry.delete(0, tk.END) # Clear the input field 


    # Show All Ticket details btn method
    def show_all_tickets(self):
        children = self.tree.get_children()  
        for child in children:
            self.tree.delete(child)        

        for t in self.metro.tickets:
            self.tree.insert("", tk.END, values=(t.id, t.passenger_name, t.start, t.end, t.quantity, t.passenger_type, t.total,  t.date))
            
    #Total Price method
    def show_total_fare(self):
        total = self.metro.total_fare()
        messagebox.showinfo("Total Fare", f"Total Fare for all tickets: {total} BDT")
        
        
# Run GUI   
root = tk.Tk()
app = MetroApp(root)
root.mainloop()
