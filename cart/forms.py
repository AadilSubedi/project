from django import forms

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,50)] 
SIZE = [
    ('S', 'S'),
    ('SM', 'SM'),
    ('M', 'M'),
    ('L','L'),
    ('CL','XL'),
]
SELECT_COUNTRY=[
    ('Nepal','Nepal'),
    ('India','India')
    
]
class AddToBasket(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)

    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    size = forms.MultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple,
    choices =SIZE,
    )
    
