import streamlit as st
# Expense Tracker

expenses=[]


while True:

  user_name = input(" أسم المصروف")
  user_value = float(input("قيمة المصروف"))

  expense = {
      
    "name":user_name,
    "value":user_value
   }

  expenses.append(expense)

  again = input(" محتاج تضيف مصاريف تانيه ولا لا ؟ لو محتاج تضيف اختا yes or no").lower()

  if again != "yes":
    break


total = 0 

for item in expenses :
  print("Name: " , item["name"])
  print("Value: " , item["value"])
  total += item["value"]

print("Total = " , total)