from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name' , max_length=160)



from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#from .models import Profile

class SignUpForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ('گذرواژه و تکرار گذرواژه یکسان نیستند')
    }
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')
        labels={
            'username' : ('نام کاربری'),
            'email' : ('ایمیل'),
            'password1' : ('رمز عبور'),
            'password2' : ('تکرار رمز عبور'),
            'first_name' : ('نام'),
            'last_name' : ('نام خانوادگی')
        }
        error_messages = {
            'username':{
                'max-length' : ('نام شما طولانی است'),
                'required' : ('نام خود را وارد کنید '),
                'unique' : ('نام کاربری شما در سیستم موجود است'),
            },
            'email':{
                'unique':('کاربری با ایمیل زیر وجود دارد')
            },
        }

class ContactForm(forms.Form):
    title= forms.CharField(required=True)
    email = forms.EmailField(required=False)
    text = forms.CharField(required=True , widget= forms.Textarea , max_length=250 , min_length=10)

# class ProfileForm(forms.Form):
#     class Meta:
#         model = Profile
#         fields = ('firstname' , 'lastname' , 'bio' , 'gender')
