from django import forms

from .models import Message


class ContactForm(forms.ModelForm):
    # Champ piège anti-robots : invisible pour les humains
    site_web = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Message
        fields = ["nom", "email", "sujet", "contenu"]
        widgets = {
            "nom": forms.TextInput(attrs={"placeholder": "Votre nom"}),
            "email": forms.EmailInput(attrs={"placeholder": "vous@entreprise.com"}),
            "sujet": forms.TextInput(attrs={"placeholder": "Site vitrine, application, offre d'emploi…"}),
            "contenu": forms.Textarea(attrs={"rows": 5, "placeholder": "Décrivez votre besoin ou votre offre"}),
        }

    def clean_site_web(self):
        if self.cleaned_data.get("site_web"):
            raise forms.ValidationError("Envoi refusé.")
        return ""
