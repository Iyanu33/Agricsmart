from django.shortcuts import render
from .forms import CropImageUploadForm
import random  # for now, simulate prediction

def upload_crop_image(request):
    prediction = None

    if request.method == 'POST':
        form = CropImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            
            # Simulate prediction (later connect real ML model)
            prediction = random.choice(['Corn 🌽', 'Tomato 🍅', 'Wheat 🌾', 'Potato 🥔'])

    else:
        form = CropImageUploadForm()

    return render(request, 'cropdetector/upload.html', {
        'form': form,
        'prediction': prediction
    })
