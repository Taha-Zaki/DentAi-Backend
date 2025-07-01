import pickle

with open('duration_predictor_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('treatment_encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

def predict_duration(treatment_type, start_time):
    h, m = map(int, start_time.strip().split(':'))
    start_minutes = h * 60 + m
    treatment_encoded = encoder.transform([treatment_type])[0]
    input_data = [[start_minutes, treatment_encoded]]
    prediction = model.predict(input_data)[0]
    return round(prediction, 2)

if __name__ == '__main__':
    print(predict_duration("پایان یک فک", '13:30'))
