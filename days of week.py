a=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
b=int(input("enter the number of the day"))
if b<8 and b>0:
    print("day of the week on number ",b,":",a[b-1])
else:
    print("invalid number")