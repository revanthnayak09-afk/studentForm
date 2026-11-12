import streamlit as st
import re

st.title('student Registration form ')

countryNationality =[
   'Select',
  "INDIAN",
  "AMERICAN",
  "BRITISH",
  "CANADIAN",
  "AUSTRALIAN",
  "NIGERIAN",
  "SOUTH AFRICAN",
  "JAPANESE",
  "CHINESE",
  "KOREAN",
  "GERMAN",
  "FRENCH",
  "ITALIAN",
  "RUSSIAN",
  "BRAZILIAN",
  "MEXICAN",
  "PAKISTANI",
  "NEPALI",
  "SPANISH",
  "TURKISH",
  "EGYPTIAN",
  "SAUDI ARABIAN",
  "MALAYSIAN",
  "SINGAPOREAN"
]

with st.form('Student Form', clear_on_submit=False):
   Name =st.text_input('Name of the student *',placeholder ='enter your full name ')
   Rollno = st.text_input('Rollno of the student *',placeholder ='1009-26-862-0XX')
   Email = st.text_input('Email of the student *',placeholder ='example@gmail.com')
   Age =st.slider('Select Age *',16,30,18)
   Course = st.text_input('Course *',placeholder ='ex:Master of computer Application')
   Phoneno=st.text_input('Phone Number *', max_chars= 10,placeholder ='81xxxxxxxx')
   Address = st.text_area('Address *',placeholder ='enter you current address ')
   Gender=st.radio('Gender *',['Female','Male'])
   Nationality =st.selectbox('Nationality',countryNationality)
   Agree=st.checkbox('I confirm that the details provided by me are correct and true. I agree.')
   submitted =st.form_submit_button()


if submitted:
   error = []

   if not Name.strip():
      error.append('Enter your Name !')
   if not Rollno.strip():
      error.append('enter you RollNo !' )  
   if not Email.strip():
      error.append('enter your student email !')   
   elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",Email):
      error.append('enter a valid email')   
   if not Phoneno.strip():
      error.append('enter your phon number !')  
   elif not(Phoneno.isdigit() and len(Phoneno) == 10):
      error.append('invaild phone number !')
   if not Address.strip():
      error.append('enter your address !') 
   if not Gender:
      error.append('Choose your gender !')   
   if  Nationality == 'Select':
      error.append('select your nationality !')  
   if not Agree:
      error.append('Please agree to the declaration before submitting the form. ')    

   if error:
    for e in error:
       st.error(e)     
   else:
      st.write('Name : ',Name)  
      st.write('RollNo : ',Rollno)  
      st.write('Age : ',Age)  
      st.write('Course : ',Course)  
      st.write('Phone No : ',Phoneno)  
      st.write('Address : ',Address)  
      st.write('Gender : ',Gender)  
      st.write('Nationality : ',Nationality)
      st.success('thank you for Registration ! your details have be saved in database')