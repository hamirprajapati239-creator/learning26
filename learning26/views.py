from django.http import HttpResponse


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def movies(request):
    return render(request, 'movies.html')

def shows(request):
    return render(request, 'shows.html')

def news(request):
  return render(request, 'news.html')##


def recipe(request):
    ingredient=["maggie","tomato"]
    data={"name":"maggie","time":20,"ingredient":ingredient}
    return render(request,"recipe.html")

def teams(request):
    playerlist=["Ms dhoni", "shivam dube","raina",]
    data= {
        "teamname":"CSK","captain":"MS DHONI", "playerlist":playerlist,"trophy":"5",  
    }
    return render(request,"teams.html",data)

def marks(request):
    subject=["maths","science","english"]
    data={

        "studentname":"vishal","standard":"7","subject":subject,"marks":45,
    }

    return render(request,"marks.html",data)


