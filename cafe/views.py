from django.shortcuts import render
from cafe.models import Coffee

def home_page(request):
  return render(request,"index.html")



def coffee_list(request):
    coffee_list = Coffee.objects.all()
    print(coffee_list)
    return render(request, 'coffee.html', {'coffee_list': coffee_list})
