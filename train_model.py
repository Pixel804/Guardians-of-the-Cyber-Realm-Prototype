import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load dataset (Assumed CSV format: src_ip, dst_ip, protocol, packet_length, label)
df = pd.read_csv("network_traffic.csv")

# Feature selection
X = df.drop(columns=['label'])  # Features
y = df['label']  # Target labels (Normal, Threat)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
with open("threat_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model training complete. Saved as 'threat_model.pkl'.")
