import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse('customers_orders.xml')
root = tree.getroot()

records = []

for customer in root.findall('Customer'):
    cust_id = customer.find('CustomerID').text
    cust_name = customer.find('Name').text
    cust_email = customer.find('Email').text
    
    for order in customer.find('Orders').findall('Order'):
        order_id = order.find('OrderID').text
        order_date = order.find('OrderDate').text
        
        for item in order.find('Items').findall('Item'):
            product_id = item.find('ProductID').text
            product_name = item.find('ProductName').text
            price = float(item.find('Price').text)
            quantity = int(item.find('Quantity').text)
            revenue = price * quantity
            
            records.append({
                'CustomerID': cust_id,
                'CustomerName': cust_name,
                'CustomerEmail': cust_email,
                'OrderID': order_id,
                'OrderDate': order_date,
                'ProductID': product_id,
                'ProductName': product_name,
                'Price': price,
                'Quantity': quantity,
                'Revenue': revenue
            })

df = pd.DataFrame(records)
print(df)
