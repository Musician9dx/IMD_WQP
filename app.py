import streamlit as st
import pandas as pd
from IMD_WQP.pipeline.ModelPrediction import predictor
import tensorflow
from IMD_WQP.utils.main import model_retrain
import pyfiglet

word=pyfiglet.figlet_format("Neural Network Retraining Ssuccessfull")


col3,col4=st.columns(2)

with col3:
    st.title("Wine Type & Quality Predictor")

with col4:
    st.caption("This Is Just a Developer Project and developer Is no way responsible for any injuries or harm caused due to predictions of this neural network. The Developer doesn't encourage anyone to drink Alchohol.")

col1,col2=st.columns(2)

col5,col6=st.columns(2)


with col1:
    fixed_acidity=st.text_input("Fixed Acidity")
    volatile_acidity=st.text_input("Volatile Acidity")
    citric_Acid=st.text_input("Citric Acid")
    residual_sugar=st.text_input("Residual Sugar")
    chlorides=st.text_input("Chlorides")
    free_sulfur_dioxide=st.text_input("Free Sulfur Dioxide")

with col2:
    total_sulfur_dioxide=st.text_input("Total Sulfur Dioxide")
    density=st.text_input("Density")
    pH=st.text_input("pH")
    sulphates=st.text_input("Sulphates")
    alchohol=st.text_input("Alchohol")

    if st.button('Predict',use_container_width=True)==True:

        st.caption("Your Input")
        numerical_features=['fixed acidity', 'volatile acidity', 'citric acid',
        'residual sugar', 'chlorides', 'free sulfur dioxide',
                    'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',]

        DataFrame=pd.DataFrame([[fixed_acidity,volatile_acidity,citric_Acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alchohol]],columns=['fixed acidity', 'volatile acidity', 'citric acid',
                'residual sugar', 'chlorides', 'free sulfur dioxide',
                            'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',])

        st.dataframe(DataFrame)

        typ,quality=predictor(DataFrame)

        with col5:

            types= "##"+" Wine Type :- " +str(typ)


            st.markdown(types)
        with col6:
            qualities="##"+" Quality Factor :- " +str(quality)
            st.markdown(qualities)


try:
    if st.button("Retrain the Model",use_container_width=True):
        model_retrain()

except:
    st.title("The Pipeline crashed please wait while the developer fixes It")






