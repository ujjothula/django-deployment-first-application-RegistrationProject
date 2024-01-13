from django.shortcuts import render
from django.shortcuts import render
from RegistrationApp.forms import RegistrationForm
from RegistrationApp.models import Registration

# Create your views here.
def index_view(request):
    return render(request,'RegistrationApp/index.html')

def add_Registration_view(request):
    formObj=RegistrationForm()
    if request.method=="POST":
        formObj=RegistrationForm(request.POST)
        if formObj.is_valid():
            print(formObj.cleaned_data['Registrationdate'])
            print(formObj.cleaned_data['firstname'])
            print(formObj.cleaned_data['lastname'])
            print(formObj.cleaned_data['Email'])
            print(formObj.cleaned_data['rating'])

            formObj.save()	#auto-commit
            return index_view(request)
    return render(request, 'RegistrationApp/addRegistration.html',{'form1':formObj})

def list_Registration_view(request):
    Registration_list=Registration.objects.all().order_by('-rating') #(-)desc-order
    return render(request,'RegistrationApp/listRegistration.html',{'movies_list':Registration_list})