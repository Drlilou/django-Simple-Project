from django.shortcuts import render
from .models import Requet
# Create your views here.
def index(request):
    
    oldQuery = Requet.objects.all();

    # Creating a dictionary to pass as an argument
    context = { 'oldQuery' : oldQuery }
    return render(request, "index.html",context)


def calc(request):

    montant = request.POST['mo']
    duree = request.POST['du']
    t=0.04
    if montant.isdigit() and duree.isdigit() :
        montant = int(montant)
        duree = int(duree)
        res1 = montant*t/12
        res2 = 1-(1+t/12)**-duree
        res=res1/res2
        req=Requet.objects.create(somme=montant, duree=duree)
        req.save
        return render(request, "result.html", {"result": round(res,2)})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})