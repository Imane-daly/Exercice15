N1=float(input("enter note value N1:"))
N2=float(input("enter note value N2:"))
N3=float(input("enter note value N3:"))
while (N1 > 20 or N1 < 0 ) or (N2 > 20 or N2 < 0) or (N3 > 20 or N3 < 0):
     N1=float(input("enter note value N1"))
     N2=float(input("enter note value N2"))
     N3=float(input("enter note value N3"))
M = (N1 + N2 + N3) / 3
print("the average score is:")
if M < 10:
   print("insufficient")
elif M >= 10 or M < 12:
   print("fair")
elif M >= 12 or M < 14:
   print("pretty good")
elif M >= 14 or M < 16:
   print("good")
else:
   print("very good")
        

     