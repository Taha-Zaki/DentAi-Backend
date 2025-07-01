import pickle
from datetime import datetime, timedelta
import json

with open('duration_predictor_model_v2.pkl', 'rb') as f:
    model = pickle.load(f)

with open('treatment_encoder_v2.pkl', 'rb') as f:
    encoder = pickle.load(f)

def predict_duration(treatment_type):
    t_enc = encoder.transform([treatment_type])[0]
    return round(model.predict([[840, t_enc]])[0], 2)

def generate_schedule(start_clock, input_list):
    schedule = []
    current_time = datetime.strptime(start_clock, "%H:%M")

    for item in input_list:
        name = item['name']
        treatment = item['treatment']
        duration = predict_duration(treatment)
        start_str = current_time.strftime("%H:%M")
        end_time = current_time + timedelta(minutes=duration)
        end_str = end_time.strftime("%H:%M")

        schedule.append({
            "name": name,
            "treatment": treatment,
            "start_time": start_str,
            "end_time": end_str,
            "duration_minutes": duration
        })

        current_time = end_time

    return schedule

if __name__ == '__main__':
    patients = [
        {"name": "علی", "treatment": "تعویض سیم یا تحویل قالب "},
        {"name": "رضا", "treatment": "تعویض سیم یا تحویل قالب "},
        {"name": "محمد", "treatment": "شروع"}
    ]

    result = generate_schedule("14:40", patients)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    with open('final_schedule.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
