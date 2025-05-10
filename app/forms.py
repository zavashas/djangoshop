from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Category, Tag, Order, OrderItem
from django.contrib.auth.forms import AuthenticationForm


# Общий стиль для всех форм
class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs['class'] = 'form-check-input'
            elif isinstance(widget, (
                forms.FileInput, forms.Select,
                forms.Textarea, forms.TextInput,
                forms.NumberInput, forms.EmailInput
            )):
                widget.attrs['class'] = 'form-control'


# Формы моделей
class ProductForm(StyledModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(StyledModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TagForm(StyledModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class OrderForm(StyledModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemForm(StyledModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'



class StyledFormMixin:
    def apply_bootstrap_styles(self):
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs['class'] = 'form-check-input'
            elif isinstance(widget, (
                forms.FileInput, forms.Select,
                forms.Textarea, forms.TextInput,
                forms.NumberInput, forms.EmailInput
            )):
                widget.attrs['class'] = 'form-control'



class CustomUserCreationForm(UserCreationForm, StyledFormMixin):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=30, required=True, label="Имя")
    last_name = forms.CharField(max_length=30, required=True, label="Фамилия")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.error_messages = {'required': f'Поле {field.label} обязательно для заполнения'}


class CustomAuthenticationForm(AuthenticationForm, StyledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.error_messages = {'required': f'Поле {field.label} обязательно для заполнения'}

class OrderCreateForm(StyledModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'email', 'phone', 'address']