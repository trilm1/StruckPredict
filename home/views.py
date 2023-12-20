from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from . import form
from .Model import StruckPredict
# Create your views here.
def get_home(request):
    return render(request,'home.html')
def get_workSpace(request):
    return render(request,'workspace.html')
def get_action(request):
    return render(request,'action.html')
def get_anotherAction(request):
    return render(request,'anotherAction.html')
def get_contact(request):
    return render(request,'contact.html')
def get_blog(request):
    return render(request,'blog.html')
def go_login(request):
    return render(request,'login.html')

def predict(request):
    if request.method == 'POST':
        if request.method == 'POST':
            # Lấy dữ liệu từ form
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            hypertension = request.POST.get('hypertension')
            heart_disease = request.POST.get('heart_disease')
            ever_married = request.POST.get('ever_married')
            work_type = request.POST.get('work_type')
            residence_type = request.POST.get('Residence_type')
            avg_glucose_level = request.POST.get('avg_glucose_level')
            bmi = request.POST.get('bmi')
            smoking_status = request.POST.get('smoking_status')
            # Gọi hàm dự đoán từ đoạn mã Python của bạn
            prediction = StruckPredict.predict(gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status)

            # Trả về kết quả dự đoán (hoặc làm gì đó khác với dữ liệu)
            return render(request, 'action.html', {'prediction': prediction})
    else:
        form = form.patientForm()

    return render(request, 'action.html', {'form': form})