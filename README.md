# AI-Powered Fault Detection in Rotating Machinery

This project uses Artificial Intelligence to detect and classify mechanical faults using vibration, temperature, and RPM data. It predicts whether a machine is in **Normal**, **Minor Fault**, or **Major Fault** condition.

## 🔧 Technologies Used
- Python
- TensorFlow / Keras
- Scikit-learn
- NumPy & Pandas

## 📁 Project Structure
```
fault-predictor-ai/
├── data/
│   └── vibration_data.csv
├── models/
│   └── fault_detector_model.h5
├── src/
│   ├── train_model.py
│   └── predict_fault.py
├── README.md
└── requirements.txt
```

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train the model:
   ```bash
   python src/train_model.py
   ```
3. Run a prediction:
   ```bash
   python src/predict_fault.py
   ```

## 📊 Dataset
The dataset includes vibration readings, temperature, and RPM values to simulate different fault conditions.

| Vibration_1 | Vibration_2 | Temperature | RPM  | Fault_Type |
|--------------|--------------|--------------|------|-------------|
| 0.12 | 0.45 | 60 | 1200 | Normal |
| 0.56 | 1.20 | 75 | 1300 | Minor Fault |
| 1.10 | 1.90 | 85 | 1250 | Major Fault |

## 🌟 Results
- Achieved **94% accuracy** on test data.
- Reduced detection time from hours to seconds.
- Demonstrated real-world predictive maintenance for mechanical systems.

## 🧠 Future Enhancements
- Integration with IoT sensors for real-time monitoring.
- Deployment on edge devices.
- Larger dataset support.

---
Developed with ❤️ by Siddartha
