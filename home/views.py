from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     #we can right multiple html tags
    
#     return HttpResponse("""<h1>Hey I am a Django Server.</h1>
#       <p> hey this is coming from Dhango server</p>
#       <hr>
#       <h3 style="color:red">Hope yo enjoy this tuorial:)</h3>> 
#       """)
def home(request):
    
    peoples= [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 4},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 30},
    {"name": "Ethan", "age": 5},
    {"name": "Ean", "age": 55}
    ]
    # for people in peoples:
    #     print(people)
    
    vegetables = [
    "Carrot",
    "Broccoli",
    "Spinach",
    "Cauliflower",
    "Kale",
    "Zucchini",
    "Peas",
    "Green beans",
    "Cabbage",
    "Lettuce",
    "Sweet potato",
    "Bell pepper",
    "Eggplant",
    "Tomato",  # Botanically a fruit, but often treated as a vegetable
    "Onion",
    "Garlic"
]



    return render(request, "index.html", context={'peoples': peoples,'vegetables':vegetables})

# def contact(request):
#     return HttpResponse("This is the Contact Page")
# def about(request):
#     return HttpResponse("This is the About Page")


# you're rendering HTML templates
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
def success_page(request):
    print('*'*10)
    return HttpResponse("<h1> Hey this is a success page</h1>")