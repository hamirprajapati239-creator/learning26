from django.shortcuts import render

def  studentHome(request):
    return render(request,"studentHome.html")
def studentDashboard(request):
    return render(request,"student\studentDashboard.html")

def studentdetails(request):
    sdata={"name":"Hamir","sem":"8","age":"21",}
    return render(request,"student\studentdetails.html",sdata)