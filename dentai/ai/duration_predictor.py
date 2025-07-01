import pickle

with open('duration_predictor_model_v2.pkl', 'rb') as f:
    model = pickle.load(f)

with open('treatment_encoder_v2.pkl', 'rb') as f:
    encoder = pickle.load(f)

def predict_duration(treatment_type, start_time):
    h, m = map(int, start_time.split(':'))
    start_min = h * 60 + m
    t_enc = encoder.transform([treatment_type])[0]
    return round(model.predict([[start_min, t_enc]])[0], 2)

if __name__ == '__main__':
    print(predict_duration('تعویض سیم یا تحویل قالب ', '13:30'))