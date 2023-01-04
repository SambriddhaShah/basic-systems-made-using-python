# Initial Display
def initial_display():
    display='''
                            Sunway Bhatbhateni Store
                               Maitidevi,Kathamndu
    *************************************************************************'''
    print(display)
    


# Calculates the discount and total net price to be paid by customer
def calculation(total_price):
    if(total_price<=5000):
        discount= total_price*0.05
        discount_amount=total_price-discount
    elif(total_price<=5000 and total_price>=7000):
        discount=total_price*0.08
        discount_amount=total_price-discount
    elif(total_price<=10000):
        discount=total_price*0.1
        discount_amount=total_price-discount
    elif(total_price>=10000):
        discount=total_price*0.15
        discount_amount=total_price-discount
    else:
            print("Thank you!!")
  
    return discount_amount


# Displays the bill by taking all the vitals as parameters
def display_information(cust_name,cust_add,cust_phn,cust_email,prize,net):
    print(f'''
           Customer name={cust_name}
    ''')
    print(f'''
           Customer address:{cust_add}\t                        Customer phone number={cust_phn}
           ''')
    print(f'''
           Customer email:{cust_email}\t                       Total price={prize}
           ''')
    print(f'''
           Discount:{prize-net}\t                       Net Total amount={net}
           ''')    

# Takes the information about the Customer
def infromation_display():
    Cust_no=(int(input("Enter a number of Customer: ")))
    cust_name=[]
    cust_add=[]
    cust_phn=[]
    cust_email=[]
    Total_Prize=[]
    net_total=[]
    for i in range(Cust_no):
        total_price=0
        cust_name.append(input(f"Enter a customer name[{i+1}]: "))
        cust_add.append(input(f"Enter a customer address[{i+1}]: "))
        cust_phn.append(input(f"Enter a customer phone number[{i+1}]: "))
        cust_email.append(input(f"Enter a customer email[{i+1}]: "))
        item_no=int(input(f"Enter a number of item: "))
        for j in range(item_no):
            quantity=int(input(f"Quantity of item[{j+1}]: "))
            unit_price=int(input(f"Unit price of item[{j+1}]: "))
            total_price=total_price+(quantity*unit_price)
            print (total_price)
        Total_Prize.append(total_price) 
        net=calculation(Total_Prize[i])
        net_total.append(net)
       
    for i in range(Cust_no):
        initial_display()    
        display_information(cust_name[i],cust_add[i],cust_phn[i],cust_email[i],Total_Prize[i],net_total[i])

infromation_display()






