from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            #Después de enviar el email, redirecciono
            
            msg = EmailMessage(
                "Mensaje de La Caffetiera",
                "De {} con email {}\n\nEscribió:\n{}".format(name, email, content),
                "no-reply@inbox.mailtrap.io",
                ["ekamartinc2003@gmail.com"],
                reply_to=[email]  
            )
            try:
                msg.send()
                return redirect(reverse("contact")+"?ok")
            except Exception:
                import traceback
                traceback.print_exc()
                return redirect(reverse("contact")+"?fail")
            
    return render(request, "contact/contact.html", {"form": contact_form})
