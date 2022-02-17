from django.shortcuts import render
# Create your views here.
# To change handle the dstination from here
def index(request):
    return render(request, "index.html")
def Search(request):
    return render(request, "Search.html")

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")    
    
     

   
