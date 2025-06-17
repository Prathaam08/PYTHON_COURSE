# you can also use if else statemnt in match case statement 

name = str(input("Enter the name:")).lower()
match name:
   case name if name.startswith("pratham") and  name.endswith("more"):
      print("10th std percentage : 80.80")
      print("12th std percentage : 56.0")
   case name if name.startswith("kalpesh") and  name.endswith("patil"):
      print("10th std percentage : 90.80")
      print("12th std percentage : 60.0")
   case "pratham":
       print("same as \"Pratham more\"")