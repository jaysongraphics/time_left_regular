import streamlit as st

st.title('Time left to enjoy your time on this earth.')

age = st.number_input("What is your current age?\n", 0, 100)

years = 105 - age

days = round(years * 365)
weeks = round(years * 52)
months = round(years * 12)

st.markdown(f"You have {days} days, {weeks} weeks, and {months} months left. Live in the moment!")






# days = st.write(years * 365)
# weeks = st.write(years * 52)
# months = st.write(years * 12)

# st.write(print(f"You have {days} days, {weeks} weeks, and {months} months left."))




# age = input("What is your current age?\n")
# years = 90 - int(age)
# days = round(years * 365)
# weeks = round(years * 52)
# months = round(years * 12)
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

