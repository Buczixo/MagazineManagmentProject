from django.forms import ModelForm
from .models import Produkt, Opakowanie, Magazyn

# tutorial https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
# Od tego miejsca zaczynają się formularze do dodawania danych do bazy danych

class ProduktForm (ModelForm):
    class Meta:
        model = Produkt
        fields = '__all__'

class OpakowanieForm (ModelForm):
    class Meta:
        model = Opakowanie
        fields = '__all__'

class MagazynForm (ModelForm):
    class Meta:
        model = Magazyn
        fields = '__all__'
        managed = False
        db_table = "entities_entity"

