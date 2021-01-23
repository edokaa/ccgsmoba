from django import forms
from .models import Member, This_Sunday_Member
from django.contrib.auth.models import User



class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_name', 'member_address', 'member_phone_no']


class MemberSearchForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_name', 'member_phone_no']


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = This_Sunday_Member
        fields = ['member_name', 'member_phone_no', 'member_address']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']