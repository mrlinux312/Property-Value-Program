print("Property Value")
print("")
def tax_amount_fun(assess_val, tax=0.72/100):
 return assess_val * tax

def assessed_val_fun(prop_val):
    return prop_val * 0.6

def propvalpro():
    
    entries=0

    tot_tax=0

    while True:
       tax_pro = input("Welcome, would you like to calculate property tax of your property? y/n: ").lower()
       if tax_pro != "y":
        print("Please restart program to run again. Enter y at the beginning prompt.")
        break
       
       prop_val = float(input("Enter the property's actual value: "))
       assess_val = assessed_val_fun(prop_val)
       prop_tax = tax_amount_fun(assess_val)
      
       print(f"Property Value: ${prop_val}\n Assessed Value: ${assess_val:.2f}")
       print(f"Property Tax: {prop_tax:.2f}\n")

       entries+=1
       tot_tax+=prop_tax

       print(f"Entries: {entries}")
       print(f"Total Property tax: {tot_tax:.2f}")


propvalpro()

