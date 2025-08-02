import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load your trained model
with open('final_model.joblib', 'rb') as file:
    model = joblib.load(file)

# Prediction function
def prediction(inp_list):
    try:
        # Ensure input is numeric
        inp_array = np.array(inp_list).reshape(1, -1)
        pred = model.predict(inp_array)[0]
        
        if pred == 0:
            return 'Sitting on bed'
        elif pred == 1:
            return 'Sitting on chair'
        elif pred == 2:
            return 'Lying on bed'
        else:
            return 'Ambulating'
    except Exception as e:
        return f"Prediction error: {e}"

# Main Streamlit app
def main():
    st.title('🛏️ ACTIVITY PREDICTION FROM SENSOR DATA')
    st.subheader('This app predicts ongoing activity based on sensor data input.')

    st.image('sensors.png', caption='Sensor Setup Example', use_column_width=True)

    rfid = st.selectbox('Enter the RFID configuration setting', ['Config 1 (4 Sensors)', 'Config 2 (3 Sensors)'])
    rfid_e = 3 if rfid == 'Config 2 (3 Sensors)' else 4

    ant_ID = st.selectbox('Select the Antenna ID', [1, 2, 3, 4])
    
    # Use number_input to ensure numeric types
    rssi = st.number_input('Enter RSSI (Received Signal Strength Indicator)', format="%.2f")
    accv = st.number_input('Enter vertical acceleration (accV)', format="%.2f")
    accf = st.number_input('Enter frontal acceleration (accF)', format="%.2f")
    accl = st.number_input('Enter lateral acceleration (accL)', format="%.2f")

    # Build numeric input list
    inp_data = [accf, accv, accl, ant_ID, rssi, rfid_e]

    if st.button('🔍 Predict'):
        response = prediction(inp_data)
        st.success(f"Predicted Activity: {response}")

if __name__ == '__main__':
    main()
