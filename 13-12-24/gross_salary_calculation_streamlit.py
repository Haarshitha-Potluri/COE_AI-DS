import streamlit as st

st.title("Gross Salary Calculator")

basic_salary=st.number_input("Enter your basic salary amount", min_value=0, max_value=100000)

if st.button("Calculate Gross salary"):

  hra=0

  da=0

  if basic_salary<10000:

      hra=basic_salary*(67/100)

      da=basic_salary*(73/100)

  elif (basic_salary>=10000 and basic_salary<=20000):

      hra = basic_salary*(69 / 100)

      da = basic_salary*(76 / 100)

  else:

      hra = basic_salary*(73 / 100)

      da = basic_salary*(89 / 100)

  st.title(f"Enter Basic Salary is ₹{basic_salary}")

  gross_salary= basic_salary+hra+da

  st.title(f"Gross Salary is {gross_salary}")

