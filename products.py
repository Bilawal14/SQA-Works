df =[["ID", "ProductName" "Price", "Description"],
     ["1","Dell Mouse", "500", "good reliable Mouse"],
     ["2","LCD", "21000", "Trusted & efficient LCD"],
     ["3","Keyboard", "1500", "good reliable Keyboard"],
     ["4","G force Graphics Card", "5500", "Best Quality"],
     ["5","Memory Card", "700", "good Quality"],
     ["6","Ram", "8000", "Ram with high bus speed"],
     ["7","Printer", "15500", "HQ Printing performance"],
     ["8","USB", "900", "Best Quality Usb device"],
     ["9","Hard Disk", "5000", "1000 GB Hard drive"]]

#print(df)

products = {}

for row in df[1:9]:
    product_id, name, price, description = row
    products[product_id]
for product in df:
    print("Product ID:", product["ID"])
    print("Product Name:", product["ProductName"])
    print("Price:", product["Price"])
    print("Description:", product["Description"])
    print()