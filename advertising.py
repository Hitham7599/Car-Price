
import pandas as pd
import streamlit as st
import joblib

model = joblib.load('model.pkl')
inputs = joblib.load('inputs.pkl')

def prediction(Brand, Model, Body, Color, Year,Fuel,Kilometers,Engine,Transmission,Gov):
    df = pd.DataFrame(columns=inputs)
    df.at[0, 'Brand'] = Brand
    df.at[0, 'Model'] = Model
    df.at[0, 'Body'] = Body
    df.at[0, 'Color'] = Color
    df.at[0, 'Year'] = Year
    df.at[0,'Fuel'] = Fuel
    df.at[0, 'Kilometers'] = Kilometers
    df.at[0, 'Engine'] = Engine
    df.at[0,'Transmission'] = Transmission
    df.at[0,'Governorate'] = Gov
    res = model.predict(df)[0]
    return res


def main():
    
    Brand = st.selectbox('Brand:',[ 'Hyundai', 'Fiat', 'Chevrolet'])
    st.write("select your Brand: ", Brand)
    Model = st.selectbox('Model:',[ '128', 'Verna', 'Elantra', 'Lanos','Accent','Optra','Shahin','Aveo','131','Cruze','Uno',
                               'Avante','Tipo','Punto','Matrix','Tucson','I10','Excel'])
    st.write("select your Model: ", Model)
    Body = st.selectbox('Body:', ['Sedan', 'Hatchback', 'SUV'])
    st.write("select your favourite Body : ", Body)
    Color = st.selectbox('Color:',[ 'White', 'Black', 'Silver','Gray','Red','Blue- Navy Blue','Other Color','Green',
                                 'Gold','Beige','Brown','Yellow','Orange'])
    st.write("select your Color ", Color)
    Year = st.slider('Year', min_value=1970, max_value=2022, value=1970, step=1)
    st.text('Selected: {}'.format(Year))
    Fuel = st.selectbox('Fuel:',[ 'Benzine', 'Natural Gas'])
    st.write("select the Fuel: ", Fuel)
    Kilometers = st.selectbox('Kilometers:',[ 'More than 200000', '10000 to 19999', '180000 to 199999','100000 to 119999 ',
                                           '0 to 9999','140000 to 159999','120000 to 139999','90000 to 99999',
                                           '160000 to 179999','20000 to 29999','80000 to 89999','50000 to 59999',
                                           '60000 to 69999','40000 to 49999','30000 to 39999','70000 to 79999'])
    st.write("select the Kilometers: ", Kilometers)
    Engine = st.selectbox('Engine:',[ '1600 CC', '1400 - 1500 CC', '1000 - 1300 CC'])
    st.write("select the Engine: ", Engine)
    Transmission = st.selectbox('Transmission:',[ 'Manual', 'Automatic'])
    st.write("select the Transmission: ", Transmission)
    Gov = st.selectbox('Governorate:',[ 'Cairo', 'Giza','Alexandria','Sharqia','Qalyubia','Gharbia','Dakahlia','Monufia',
                                     'Ismailia','Suez','Fayoum','Beheira','Minya','Asyut','Damietta','Beni Suef',
                                     'Kafr al-Sheikh','Sohag','Red Sea','Port Said','Qena','South Sinai','Luxor',
                                     'Aswan','Matruh','New Valley'])
    st.write("select your Governorate: ", Gov)
    
    if st.button('Predict'):
            res = prediction(Brand, Model, Body, Color, Year,Fuel,Kilometers,Engine,Transmission,Gov)
            st.write(res)
        
main()
