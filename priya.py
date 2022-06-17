import streamlit as st
from PIL import Image
img=Image.open(r"C:\Users\shanmu\Downloads\ass.pic\ima.jpg")
st.image(img)
st.title ("ENTER THE NUMBER OF COIN")

inp1=st.number_input("ENTER NUMBER OF COPPER",min_value=0,max_value=100)
inp2=st.number_input("ENTER NUMBER OF SILVER",min_value=0,max_value=100)
inp3=st.number_input("ENTER NUMBER OF ELECTROM",min_value=0,max_value=100)
inp4=st.number_input("ENTER NUMBER OF GOLD",min_value=0,max_value=100)
inp5=st.number_input("ENTER NUMBER OF PLATINUM",min_value=0,max_value=100)
copper=1/100
silver=1/10
electrum=1/2
gold=1
platinum=10
cal=(inp1*copper)+(inp2*silver)+(inp3*electrum)+(inp4*gold)+(inp5*platinum)
cal=round(cal)
st.subheader(f"you have {cal:,d} currency price")
currentvalue= [{"val":copper,"count":inp1},
          {"val":silver,"count":inp2},
          {"val":electrum,"count":inp3},
          {"val":gold,"count":inp4},
          {"val":platinum,"count":inp5}]


import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame(currentvalue)
st.dataframe(data=df)

st.bar_chart(data=df)
st.area_chart(data=df)