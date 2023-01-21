import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved model
import base64  #to open .gif files in streamlit app
import pickle

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.title('CHURN PREDICTION :')  
    st.image("th.jpg")  
    st.markdown('Dataset :')
    data=pd.read_csv('churn.csv')
    st.write(data.head())

elif app_mode == 'Prediction':
    st.subheader('''Sir/Ma'am , YOU need to fill all necessary informations in order to know the status of churn !''')
    st.sidebar.header("Informations about the client :")
 
    MonthlyIncome=st.sidebar.slider('MonthlyIncome',0,10000,0,)
    
    Distance_From_Home=st.sidebar.slider('Distance_From_Home',0,10000,0,)
    Age=st.sidebar.slider('Age in years ',10,65,1)
    
    JobLevel=st.sidebar.selectbox('JobLevel',(1,2,3))
    Job_Satisfaction=st.sidebar.selectbox('Job_Satisfaction',(1,2,3,4))
   
        
data1={

    'MonthlyIncome':MonthlyIncome,
    'Distance_From_Home':Distance_From_Home,
    'Age':Age,
    'JobLevel':JobLevel,
    'Job_Satisfaction':Job_Satisfaction
    }


feature_list=[Age,Distance_From_Home,JobLevel,Job_Satisfaction,MonthlyIncome]
st.write(feature_list)

single_sample = np.array(feature_list).reshape(1,-1)

if st.button("Predict"):
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    prediction = loaded_model.predict(single_sample)
    if prediction[0] == 0 :
        st.success('This person will not leave the company')
    elif prediction[0] == 1 :
        st.success(Alert!! This person will leave the compnay')
