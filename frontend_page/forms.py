from django import forms
from .models import Imageblog, Category

# choices = [('School', 'School'),('Residence', 'Residence'),('Hotel', 'Hotel')] #hard code category of a blog

choices = Category.objects.all().values_list('name','name')

choice_list =[]
for items in choices:
    choice_list.append(items)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Imageblog
        fields = '__all__'

        widgets = {
            'picture': forms.FileInput(attrs={"class":"image_field"}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Imageblog
        fields = '__all__'

        widgets = {
            'image': forms.TextInput(attrs={'class':'form-control'}),
            'picture': forms.FileInput(attrs={"class":"image_field"}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }
    
    # class ImageForm(forms.Form):
    #     image = forms.ImageField(
    #     widget = forms.FileInput(
    #         attrs = {"id" : "image_field" , # you can access your image field with this id for css styling . 
    #                 , style = "height: 100px ; width : 100px ; " # add style from here .
    #                 }
    #         )