import streamlit as st

st.title(":red[Data scince] internship-Data app")
st.header("Hi, I'm :red[Rohit Vikas Dhotre ]") 
st.subheader("A Developer")
st.write("click here for [linkedin](https://www.linkedin.com/in/rohit-dhotre-1201ba1b2)")
st.write("click here for [github](https://github.com/RohitVDhotre)")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()