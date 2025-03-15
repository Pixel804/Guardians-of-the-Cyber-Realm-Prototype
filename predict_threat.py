import pickle
import pandas as pd

# Load trained model
with open("threat_model.pkl", "rb") as f:
    model = pickle.load(f)

def detect_threat(data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return "Threat Detected" if prediction[0] == 1 else "No Threat"


sample_data = {"src_ip": "192.168.1.1", "dst_ip": "192.168.1.100", "protocol": 6, "packet_length": 450}
print(detect_threat(sample_data))
