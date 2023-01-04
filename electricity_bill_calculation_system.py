def initial_display():
    display='''\t\t\tSunway Electricity System
                            Maitidevi,Kathmandu
                    .....*.....*.....*.....*.....*.....*.....'''
    print(display)

def input_information():
    CustName=input("Enter Customer Name: ")
    CustAddress=input("Enter Customer Address: ")
    ConsumedUnit=int(input("Enter Consumed Unit: "))
    return CustName,CustAddress,ConsumedUnit

def calculationunit(Consumedunit):
    ConsumedUnitt=Consumedunit
    Total_amount=0
    Discount_amount=0
    After_discount=0
    if(ConsumedUnitt<=20):
        Total_amount=20*4
        Discount_amount=0
        After_discount= Total_amount-Discount_amount

    elif(ConsumedUnitt>20 and ConsumedUnitt<=50):
        Total_amount=(ConsumedUnitt-20)*7.5+20*4
        Discount_amount=0
        After_discount= Total_amount-Discount_amount

    elif(ConsumedUnitt>50 and ConsumedUnitt<=150):
        Total_amount=(ConsumedUnitt-50)*9.5+30*7.5+20*4
        Discount_amount=(ConsumedUnitt-50)*9.5*0.05
        After_discount=Total_amount-Discount_amount

    elif(ConsumedUnitt>150 and ConsumedUnitt<=250):
        Total_amount=(ConsumedUnitt-150)*11.5+100*9.5+30*7.5+20*4
        Discount_amount=(ConsumedUnitt-150)*11.5*0.1
        Total_discount=Discount_amount+100*9.5*0.05
        After_discount=Total_amount-Total_discount
        
    elif(ConsumedUnitt>250):
        Total_amount=(ConsumedUnitt-250)*13.5+100*11.5+100*9.5+30*7.5+20*4
        Discount_amount=(ConsumedUnitt-250)*13.5*0.15
        Total_discount=Discount_amount+200*11.5*0.15
        After_discount=Total_amount-Total_discount
    else:
        print("Thank you!!")
    return Total_amount,Total_discount,After_discount

initial_display()
CustName,CustAddress,ConsumedUnit=input_information()
Total_amount,Total_discount,After_discount=calculationunit(ConsumedUnit)

def display_information(CustName,CustAddress,ConsumedUnit,Total_amount,Total_discount,After_discount):
    print(f"Customer Name:{CustName}\t Customer Address={CustAddress}")
    print(f"Customer Consumed Unit:{ConsumedUnit}\t Total Discount Amount:{Total_discount}")
    print(f"After Discount:{After_discount}")
    return CustName,CustAddress,ConsumedUnit,Total_amount,Total_discount,After_discount

CustName,CustAddress,ConsumedUnit,Total_amount,Total_discount,After_discount=display_information()

print("Customer ",CustName," Address ",CustAddress," whose consumed unit ",ConsumedUnit," has to pay amount ",Total_amount
," after discount amount ",After_discount," and got total discount amount ",Total_discount)