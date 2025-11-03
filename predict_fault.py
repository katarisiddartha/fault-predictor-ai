import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Load trained model
model = load_model('models/fault_detector_model.h5')

# Example input
new_data = pd.DataFrame([[0.8, 1.4, 80, 1280]], 
                        columns=['Vibration_1', 'Vibration_2', 'Temperature', 'RPM'])

# Normalize & predict
scaler = StandardScaler()
scaled = scaler.fit_transform(new_data)
pred = model.predict(scaled)

fault_types = ['Normal', 'Minor Fault', 'Major Fault']
print("Predicted Fault Type:", fault_types[np.argmax(pred)])
