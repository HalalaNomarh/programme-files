# INVOICE GENERATOR

from datetime import datetime

class invoiceGenarator:
    def __init__(self):
        self.items =[]
    
    def add_item(self,description,quantity, price_per_unit):
        self.items.append({
            "description":description,
            "quantity":quantity,
            "price_per_unit": price_per_unit,
            "total_price": price_per_unit,
            "total_price": float("{:.2f}".format(quantity*price_per_unit))
         })
        
    def mult(quantity,price_per_unit):
        return quantity * price_per_unit
        
    def generate_invoice(self,customer_name):
        invoice_number = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        total_amount = sum(item['total_price']for item in self.items)

        invoice = f"\n invoice number: {invoice_number} \n \n Date:{date} \n \n customer:{customer_name} \n \n items: \n {'-'*60} \n Description       Quantity        Unit price    Total price  \n {'-'*60}"

        for item in self.items:
            invoice += f"\n {item['description']:<20}{item['quantity']: <14}{item['price_per_unit']:<14}{item['total_price']:<14}\n"
        invoice += f"\n{'-'*60}\n Total amount Due: R{total_amount:.2f}\n{'-'*60}\n"

        print(invoice)

        self.items.clear()

invoice_generator = invoiceGenarator()
while True:
    decr = int(input("Press 1 for laptop, Press 2 for mouse or Press 3 for keyboard, Press 4 to exit"))
    if decr == 4:
        break
    quant = int(input("Enter Quantity: "))
    if decr == 1:
        invoice_generator.add_item("Laptop", quant, 5699.99)
    elif decr == 2:
        invoice_generator.add_item("Mouse", quant, 199.99)
    elif decr == 3:
        invoice_generator.add_item("Keyboard", quant, 499.99)
    

invoice_generator.generate_invoice("Halala Maduna")
