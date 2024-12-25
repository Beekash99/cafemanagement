from django.shortcuts import render
from cafe.forms import ContactUsForm

def home_page(request):
    return render(request,"index.html")




def contact_us_view(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')  # Or redirect to a success URL
        else:
            print("Form Errors:", form.errors)  # Debug any errors
    else:
        form = ContactUsForm()
    return render(request, 'contact.html', {'form': form,})