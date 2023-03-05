from django.shortcuts import render

# Create your views here.
def add(num1, num2):
    result = int(num1) + int(num2)
    return result
def sub(num1, num2):
    result = int(num1) - int(num2)
    return result
def mul(num1, num2):
    result = int(num1) *int(num2)
    return result
def divide(num1, num2):
    result = int(num1) / int(num2)
    return result

def index(request):
    if request.method == "POST":
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        if "add" in request.POST:
            result = add(num1, num2)
            return render(request, "calc/index.html", {"result": result})
        if "sub" in request.POST:
            result = sub(num1, num2)
            return render(request, "calc/index.html", {"result": result})
        if "mul" in request.POST:
            result = mul(num1, num2)
            return render(request, "calc/index.html", {"result": result})
        if "div" in request.POST:
            result = divide(num1, num2)
            return render(request, "calc/index.html", {"result": result})
        

    return render(request, "calc/index.html")
