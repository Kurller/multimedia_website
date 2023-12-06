# multimedia/views.py
from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageUploadForm

def image_list(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'multimedia/image_list.html', context)

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'multimedia/upload_image.html', {'form': form})
