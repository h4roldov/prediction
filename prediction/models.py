from django.db import models
from django.utils import timezone
from sklearn.externals import joblib
import numpy as np  
import os
# Create your models here.

class Modelos(models.Model):
    #file_name = models.CharField(max_length=20)
    #source = models.CharField(max_length=100)
    
    model_name = models.CharField(max_length=100)
    model_file = models.FileField(upload_to='documents/', default='modelDT.file')
    model_path = models.CharField(max_length=100, default='modelDT.file')
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def file_info(self):
        CURRENT_DIR = os.path.dirname(__file__)
        model_file = os.path.join(CURRENT_DIR, self.model_path)
        loaded_model = joblib.load(model_file)
        return '{}'.format(self.model_name)

    def __str__(self):
        return self.file_info()

    