import streamlit as st

st.title("Expense Tracker 💰")

# Session State لتخزين البيانات
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# إدخال البيانات
name = st.text_input("اسم المصروف")
value = st.number_input("قيمة المصروف", min_value=0.0, step=1.0)
category = st.selectbox("نوع المصروف", ["Food", "Transport", "Shopping", "Other"])

# زر الإضافة
if st.button("Add Expense"):
    expense = {
        "name": name,
        "value": value,
        "category": category
    }
    st.session_state.expenses.append(expense)
    st.success("تم إضافة المصروف ✅")

# عرض المصاريف
st.subheader("المصاريف")

total = 0

for item in st.session_state.expenses:
    st.write(f"Name: {item['name']} | Value: {item['value']} | Category: {item['category']}")
    total += item["value"]

st.write("---")
st.write(f"### Total = {total}")
