# uploader/views.py
from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadedFile
from django.http import JsonResponse 
# uploader/views.py
from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadedFile
from .convert import create_pdf
from .convert_wav import convert_wav
from django.http import HttpResponse

import os
from django.http import FileResponse, Http404
from django.conf import settings

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print("Form is checking for validity")
        if form.is_valid():
            # Save the uploaded file as input.mp4
            print("Form is valid")
            video_file = request.FILES['video_file']
            # Specify the path where the file should be saved
            video_instance = UploadedFile(video_file=video_file)
            video_instance.save()

            # Get the file path to save as input.mp4
            input_file_path = os.path.join(settings.MEDIA_ROOT, 'videos', 'input.mp4')
            
            # Save the file with the specified name
            with open(input_file_path, 'wb+') as destination:
                for chunk in video_file.chunks():
                    destination.write(chunk)
            
            # mp4_file = r'C:\Diploma++\CBIT\Hacktober 24\PS15\backend\media\videos\input.mp4'  # Replace with your MP4 file path
            
            # wav_file = r'C:\Diploma++\CBIT\Hacktober 24\PS15\backend\media\videos\output.wav'  # ReplF24-Problem Statement Websace with the desired WAV file path

            mp4_file = os.path.join(settings.BASE_DIR, 'media', 'videos', 'input.mp4')
            wav_file = os.path.join(settings.BASE_DIR, 'media', 'videos', 'output.wav')

            Output = convert_wav(mp4_file,wav_file)
            create_pdf("Output.pdf","Briefly.ai",Output)
            # Return a success message
            return HttpResponse(Output, content_type='text/plain')
        else:
            return render(request, 'upload.html', {'form': form, 'message': 'Invalid form submission.'})
    else:
        form = UploadFileForm()
    
    return render(request, 'upload.html', {'form': form})




# backend/views.py
import os
from django.http import FileResponse, Http404
from django.conf import settings

def download_summary(request):
    # Define the absolute file path
    # file_path = os.path.join(r'C:\Diploma++\CBIT\Hacktober 24\PS15\backend', 'Output.pdf') 
    file_path = os.path.join(settings.BASE_DIR, 'Output.pdf')

    if os.path.exists(file_path):
        print("Ill donload")
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Briefly_AI_Output.pdf')  # Use the original file name
          
    else:
        raise Http404("The requested file does not exist.")
    

def about(request):
    return render(request, 'about.html')

