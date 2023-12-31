from django.shortcuts import render,HttpResponse
import pandas as pd
import numpy as np

def home(request):
    return render(request,'home.html')
    
def prompt(request):
    if request.method == 'POST':
        
        csv_file = request.FILES['csv_file']
        data = pd.read_csv(csv_file)
        print(data)
        if "first rank holder" in data:
            first_rank_name = data['Total'].idxmax()
            print(first_rank_name)
            return f"The first rank holder's name is: {data.loc[first_rank_name, 'StudentID']}"
        else:
            return "I'm sorry, I don't understand that question."

    return render(request,'prompt.html')


