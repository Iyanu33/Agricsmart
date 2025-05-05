from django.shortcuts import render, redirect, get_object_or_404
from .forms import SoilImageForm
from .models import SoilImage
from .utils import predict_soil, get_crops_for_soil
from django.contrib.auth.decorators import login_required

@login_required
def soil_upload_view(request):
    if request.method == 'POST':
        form = SoilImageForm(request.POST, request.FILES)
        if form.is_valid():
            soil_img = form.save(commit=False)
            soil_img.user = request.user
            soil_img.save()

            # Predict soil
            prediction = predict_soil(soil_img.image.path)
            soil_img.prediction = prediction
            soil_img.save()
            return redirect('soil_result', image_id=soil_img.id)
    else:
        form = SoilImageForm()
    return render(request, 'soil/upload.html', {'form': form})

@login_required
def soil_result_view(request, image_id):
    soil_img = get_object_or_404(SoilImage, id=image_id, user=request.user)
    sugested_crops=get_crops_for_soil(soil_img.prediction)
    return render(request, 'soil/result.html', {
        'soil_img': soil_img,
        'sugested_crops':sugested_crops
    })
