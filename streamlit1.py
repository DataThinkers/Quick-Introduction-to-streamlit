import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="My Streamlit App")

st.title("Welcome to My Streamlit App")

st.header("I'm Learning Streamlit")


st.subheader("And I'm Loving it")


st.write("This is a normal text")

num=42

st.write("The answer is:",num)

df = pd.DataFrame({'Name':["Priyang","Anil","Rahul"],
                    'Age':[35,45,50],
                    'City':['Mumbai',"Anand","Baroda"]})

st.write(df)


plt.plot([1,2,3,4,5])
st.pyplot(plt)


st.markdown("""
    
# Heading 1
## Heading 2
### Heading 3

This is **bold** text,*italic* text, and `code` text

- List item1 
- List item2
- List item3
            
            
            
            """)
            
st.code("""
        def foo(input):
            return input**2
        
        x = foo(2)
        
        
        """)

df = pd.DataFrame({'Name':["Priyang","Anil","Rahul"],
                    'Age':[35,45,50],
                    'City':['Mumbai',"Anand","Baroda"]})

st.dataframe(df)


st.json({'Name':["Priyang","Anil","Rahul"],
                    'Age':[35,45,50],
                    'City':['Mumbai',"Anand","Baroda"]})


name = st.text_input("Enter your name")
st.write(name)


age=st.number_input("Enter your age",min_value=1,max_value=100)
st.write(age)


date = st.date_input("Enter Current date")
st.write(date)

def button_clicked():
    st.write("Button Clicked!!!")
    st.balloons()

if st.button("Click Me!!!"):
    button_clicked()


age1= st.slider("Select your age",min_value=0,max_value=100,value=30,step=1)
st.write(f"Your age is {age1}")


options=["Option 1","Option 2","Option 3"]

selected_option=st.selectbox("Select an option",options)

st.write(selected_option)


file=st.file_uploader("Upload CSV file")
if file is not None:
    data=pd.read_csv(file)
    st.write(data.head())
    

st.sidebar.title("Sidebar's Title")


ch = st.sidebar.checkbox("Click Me")
st.write(ch)


st.image('Logo.png')


st.success("This is a success message")

st.warning("This is a warning message")


st.error("This is an error message")


bar=st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)
    
st.write("Done!!!")

col1,col2=st.columns(2)

col1.write("This is column 1")
col1.button("Button 1")


col2.write("This is column 2")
col2.button("Button 2")
































