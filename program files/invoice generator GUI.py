from tkinter import *
from tkinter import messagebox
from datetime import datetime

class InvoiceGenerator:
    def __init__(self):
        self.items = []
    
    def add_item(self, description, quantity, price_per_unit):
        self.items.append({
            "description": description,
            "quantity": quantity,
            "price_per_unit": price_per_unit,
            "total_price": float("{:.2f}".format(quantity * price_per_unit))
        })
        
    def generate_invoice(self, customer_name):
        invoice_number = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        total_amount = sum(item['total_price'] for item in self.items)

        invoice = f"\nInvoice Number: {invoice_number}\nDate: {date}\nCustomer: {customer_name}\n\nItems:\n{'-'*60}\nDescription       Quantity        Unit Price    Total Price\n{'-'*60}"

        for item in self.items:
            invoice += f"\n{item['description']:<20}{item['quantity']: <14}{item['price_per_unit']:<14}{item['total_price']:<14}\n"
        invoice += f"\n{'-'*60}\nTotal Amount Due: R{total_amount:.2f}\n{'-'*60}\n"

        return invoice

class InvoiceGUI:
    def __init__(self, root):
        self.invoice_generator = InvoiceGenerator()
       
        root.title("Invoice Generator")

        # Labels and Entry for item selection
        Label(root, text="Select Item:").grid(row=0, column=0, padx=10, pady=10)
        self.item_entry = Entry(root)
        self.item_entry.grid(row=0, column=1, padx=10, pady=10)
        self.item_entry.insert(0, "Laptop")  # Default value

        # Labels and Entry for quantity
        Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
        self.quantity_entry = Entry(root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)
        self.quantity_entry.insert(0, "1")  # Default value

        # Buttons
        Button(root, text="Add Item", command=self.add_item).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        Button(root, text="Generate Invoice", command=self.generate_invoice).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        Button(root, text="Quit", command=root.quit).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        Button(root, text="Help",command=self.Help_butt).grid(row=4,column=0)


        
        # Label and Entry for customer name
        Label(root, text="Customer Name:").grid(row=5, column=0, padx=10, pady=10)
        self.customer_name_entry = Entry(root)
        self.customer_name_entry.grid(row=5, column=1, padx=10, pady=10)
       
    
    def add_item(self):
        item = self.item_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
        except ValueError:
            quantity = 0
        if item.lower() == "laptop":
            price_per_unit = 5699.99
        elif item.lower() == "mouse":
            price_per_unit = 199.99
        elif item.lower() == "keyboard":
            price_per_unit = 499.99
        else:
            price_per_unit = 0.00
        
        self.invoice_generator.add_item(item, quantity, price_per_unit)
        messagebox.showinfo("Item Added", f"Added {quantity} {item}(s) to the invoice.")
    
    def generate_invoice(self):
        customer_name = self.customer_name_entry.get()
        if customer_name:
            invoice = self.invoice_generator.generate_invoice(customer_name)
            messagebox.showinfo("Invoice", invoice)
            self.invoice_generator.items.clear()  # Clear items after generating invoice
        else:
            messagebox.showwarning("Input Error", "Please enter the customer's name.")
    def Help_butt(self):
        Help= Toplevel()
        Label(Help,text="""
The Invoice Generator is a simple Python application designed to create and manage invoices. Users can add items such as laptops, mice, and keyboards to an invoice and generate a formatted invoice summary.

Features
Add Items: Users can add different items to the invoice with their descriptions, quantities, and prices.
Generate Invoice: Generates a detailed invoice with an invoice number, date, and total amount due.
Clear Items: Automatically clears items after generating the invoice.
Requirements
Python 3.x
Standard Python libraries
Installation
To use the invoice generator, you need to have Python installed on your machine. You can then use the provided script directly.

Usage
Run the Script: Execute the invoice_generator.py script in your Python environment.

Add Items:

You will be prompted to choose items by pressing 1 for Laptop, 2 for Mouse, or 3 for Keyboard.
Enter the desired quantity for the selected item.
Exit: Press 4 when you are done adding items.

Generate Invoice:

After exiting, an invoice will be generated with the name "Halala Maduna".
The invoice will display item details, total amounts, and will be printed to the console.

                        """).grid(row=0,column=0)
 



def main():
    root = Tk()
    app = InvoiceGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
