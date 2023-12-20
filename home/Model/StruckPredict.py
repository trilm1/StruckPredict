import pandas as pd
import torch
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import StandardScaler

class LogisticRegression(nn.Module):
    def __init__(self, n_input_features):
        super(LogisticRegression,self).__init__()
        self.linear=nn.Linear(n_input_features,1)
    
    def forward(self,x):
        y_predicted = torch.sigmoid(self.linear(x))
        return y_predicted

def predict(gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status):
    sc=StandardScaler()
    work_type_mapping = {'Govt Job': 0, 'Private': 1, 'Self-employed': 2, 'children': 3}
    work_array = [0, 0, 0, 0]

    if work_type in work_type_mapping:
        work_array[work_type_mapping[work_type]] = 1
    smoking_status_mapping = {'Unknown': 0, 'formerly_smoked': 1, 'never_smoked': 2, 'smokes': 3}
    smoking_status_array = [0, 0, 0,0]

    if smoking_status in smoking_status_mapping:
        smoking_status_array[smoking_status_mapping[smoking_status]] = 1
    data_single_person = {
    'gender': gender,
    'age': age,
    'hypertension': hypertension,
    'heart_disease': heart_disease,
    'ever_married': ever_married,
    'Residence_type': residence_type,
    'avg_glucose_level': avg_glucose_level,
    'bmi': bmi,
    'work_type_Govt_job': work_array[0],
    'work_type_Private': work_array[1],
    'work_type_Self-employed': work_array[2],
    'work_type_children': work_array[3],
    'smoking_status_Unknown': smoking_status_array[0],
    'smoking_status_formerly smoked': smoking_status_array[1],
    'smoking_status_never smoked': smoking_status_array[2],
    'smoking_status_smokes': smoking_status_array[3]
}
    print(data_single_person)
    model = LogisticRegression(16)
    model.model = torch.load('E://HKIY4/MyProject/ProjectGroup5/home/Model/StruckPredict.pth')
    model.eval()
    df_single_person = pd.DataFrame(data_single_person,index=[0])
    sc.fit(df_single_person)
    df_single_person=sc.transform(df_single_person)
    df_single_person=torch.from_numpy(df_single_person.astype(np.float32))
    prediction = model(df_single_person.clone().detach())
    prediction2 = prediction.round()
    print(f"predict: {prediction2}")
    return prediction2.item()