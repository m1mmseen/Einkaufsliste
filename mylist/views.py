from django.shortcuts import render
from .models import ShoppingItem

# Create your views here.
def mylist(request):
    if request.method == 'POST':
        ShoppingItem.objects.create(name = request.POST['itemName'])
    all_items = ShoppingItem.objects.filter(done = False)
    shopped_items = ShoppingItem.objects.filter(done = True)
    return render(request, 'index.html', {'all_items':all_items,'shopped_items':shopped_items })

def updatedMyList(request):
    id = request.POST['ItemName']
    item = ShoppingItem.objects.get(name=id)
    item.done = True
    item.save()
    return render(request, 'index.html')


   