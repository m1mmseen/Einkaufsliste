from django.shortcuts import render
from .models import ShoppingItem

# Create your views here.
def mylist(request):
    if request.method == 'POST':
        ShoppingItem.objects.create(name = request.POST['itemName'])
    all_items = ShoppingItem.objects.all()
    return render(request, 'index.html', {'all_items':all_items})
