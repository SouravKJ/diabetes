import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

#page sittings
st.set_page_config(page_title='Diabetes Prediction App', layout='wide')

#load model and scaler
model=joblib.load('diabetes.pkl')
Scale=joblib.load('scale.pkl')

#app title
st.title('Diabetes Prediction App')
st.write('Enter the following details to predict the likelihood of diabetes:')

#Layout
left,right=st.columns([1,2])

#left side of layout
with left:
        st.subheader('enter patient details')
        
        #form
        with st.form('prediction_form'):
            #input fields
            pregnancies = st.slider("Pregnancies", min_value=0, max_value=20, value=0)
            glucose = st.slider("Glucose Level", min_value=50, max_value=200, value=120)
            bp = st.slider("Blood Pressure", min_value=40, max_value=150, value=70)
            skin = st.slider("Skin Thickness", min_value=0, max_value=100, value=20)
            insulin = st.slider("Insulin Level", min_value=15, max_value=900, value=79)
            bmi = st.slider("BMI", min_value=10.0, max_value=70.0, value=25.0)
            dpf = st.slider("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
            age = st.slider("Age", min_value=10, max_value=100, value=33)
            
            submit_button = st.form_submit_button(label='Predict')



#prediction button
if submit_button:
    #prepare input data
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    
    #scale input data
    scaled_data = Scale.transform(input_data)
    
    #make prediction
    prediction = model.predict(scaled_data)
    
    #predict probability
    prob = model.predict_proba(scaled_data)[0][1]
    
    #save result in memory(session)
    st.session_state['done'] = True
    st.session_state['prediction'] = prediction[0]
    st.session_state['prob'] = prob
    st.session_state['input_data'] = input_data[0]
with right:
    
    if 'done' in st.session_state:
        st.subheader('Prediction Result')
    #display result
        if prediction[0] == 1:
            st.error(f"The model predicts that you have diabetes with a probability of {prob*100:.2f}%.")
        else:
            st.success('The model predicts that you do not have diabetes.')
        st.write(f"diabetes probability: **{st.session_state['prob']*100:.2f}%**")
with right:
    if 'done' in st.session_state:
        st.subheader('Prediction Visualizations')
        
        g1,g2=st.columns(2)
        with g1:
            fig1,ax1=plt.subplots(figsize=(6,4))
            features=['Pregnancies','Glucose','Blood Pressure','Skin Thickness','Insulin','BMI','DPF','Age']
            values=[pregnancies,glucose,bp,skin,insulin,bmi,dpf,age]
            ax1.pie(values,labels=features,autopct='%1.1f%%')
            ax1.set_title('Input Feature Distribution')
            st.pyplot(fig1)
        with g2:
            fig,ax=plt.subplots(figsize=(6,4))
            labels=['No Diabetes','Diabetes']
            values=[1-prob,prob]
            ax.bar(labels,values,color=['green','red'])
            ax.set_ylabel('probability')
            ax.set_title('Diabetes Prediction Probability')
            ax.set_ylim(0,1)
            st.pyplot(fig)
        # with g3:
        fig2,ax2=plt.subplots(figsize=(6,2))
        ax2.barh(['Diabetes Risk'],[prob],color='red')
        ax2.set_xlim(0,1)
        ax2.set_title('Risk Level')
        st.pyplot(fig2)   