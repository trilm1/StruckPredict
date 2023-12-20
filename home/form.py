from django import forms

class patientForm(forms.Form):
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], label='Gender')
    age = forms.IntegerField(label='Age')
    hypertension = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], label='Hypertension')
    heart_disease = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], label='Heart Disease')
    ever_married = forms.ChoiceField(choices=[('0', 'No'), ('1', 'Yes')], label='Ever Married')
    work_type = forms.ChoiceField(choices=[('Private', 'Private'), ('Self-employed', 'Self-employed'), ('Govt_job', 'Govt Job'), ('children', 'Children')], label='Work Type')
    Residence_type = forms.ChoiceField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')], label='Residence Type')
    avg_glucose_level = forms.FloatField(label='Average Glucose Level')
    bmi = forms.FloatField(label='BMI')
    smoking_status = forms.ChoiceField(choices=[('formerly_smoked', 'Formerly Smoked'), ('never_smoked', 'Never Smoked'), ('smokes', 'Smokes')], label='Smoking Status')