# uploader/models.py
from django.db import models

class UploadedFile(models.Model):
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)  # Allow null values
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_file.name
