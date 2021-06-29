from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # enviamos el correo y redireccionamos
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje',
                f'De {name} <{email}>\n\nEscribió:\n\n{content}',
                'no-contestar@inbox.mailtrap.io',
                ['jrm2087@gmail.com'],
                reply_to=[email]
            )

            try:
                email.send()
                # todo bien
                return redirect(reverse('contact')+'?ok')
            except:
                # error
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})
