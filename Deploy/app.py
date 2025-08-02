import streamlit as st
import joblib
import pandas as pd

model = joblib.load("Deploy/model.pkl")

st.title("Air Quality Failure Prediction App")

type_input = st.selectbox("Type", ["L", "M", "H"])
udi = st.number_input("UDI")
air_temp = st.number_input("Air temperature [K]")
process_temp = st.number_input("Process temperature [K]")
rot_speed = st.number_input("Rotational speed [rpm]")
torque = st.number_input("Torque [Nm]")
tool_wear = st.number_input("Tool wear [min]")
twf = st.selectbox("TWF", [0, 1])
hdf = st.selectbox("HDF", [0, 1])
pwf = st.selectbox("PWF", [0, 1])
osf = st.selectbox("OSF", [0, 1])
rnf = st.selectbox("RNF", [0, 1])

input_dict = {
    'Type': [type_input],
    'UDI': [udi],
    'Air temperature [K]': [air_temp],
    'Process temperature [K]': [process_temp],
    'Rotational speed [rpm]': [rot_speed],
    'Torque [Nm]': [torque],
    'Tool wear [min]': [tool_wear],
    'TWF': [twf],
    'HDF': [hdf],
    'PWF': [pwf],
    'OSF': [osf],
    'RNF': [rnf]
}

input_df = pd.DataFrame(input_dict)

if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.error("Machine is likely to FAIL.")
    else:
        st.success("Machine is NOT likely to fail.")



# how to run
# Streamlit run 'Deploy/app.py'