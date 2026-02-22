Amount = int(input("Enter the Principal Amount: "))
Rate = float(input("Enter the Rate: "))
Time = int(input('Enter the Time Duration in YEARS: '))
SI= (Amount * Rate * Time)/100
print("Simple Interest: ",SI)
print("Total Amount: ",Amount + SI)
