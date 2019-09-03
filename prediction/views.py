from django.shortcuts import render,get_object_or_404, redirect
from .models import Modelos
from sklearn.externals import joblib
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import pandas as pd
import numpy as np
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.

def home(request):
    otro = Modelos.objects.all()
    if request.method == "POST" and request.FILES['dataset']:
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        # dataset = request.FILES['dataset'].read() # get the uploaded file
        print('que')
        model_='modelDT.file'
        midataset = request.FILES['dataset']
        fs = FileSystemStorage()
        archivo = fs.save('log_dataset', midataset)
        archivo_url = fs.url(archivo)
        CURRENT_DIR = os.path.dirname(__file__)
        modelo = request.POST['modelo_select']
        if modelo == 'ANN':
            model_ = 'modelANN.file'
        elif modelo =='SVM':
            model_ = 'modelSVM.file'
        elif modelo =='KNN':
            model_ = 'modelKNN.file'
        model_file = os.path.join(CURRENT_DIR, model_)
        data_file = os.path.join(CURRENT_DIR, '../log_dataset')
        loaded_model = joblib.load(model_file)
        data= pd.read_csv(data_file) 
        data= data[['RMS-x', 'RMS-y', 'RMS-z', 'Mean-x', 'Mean-y', 'Mean-z', 'Max-x', 'Max-y', 'Max-z', 'Min-x', 'Min-y', 'Min-z', 'IQR-x', 'IQR-y', 'IQR-z', 'Var-x', 'Var-y', 'Var-z', 'Std-x','Std-y', 'Std-z', 'Activity']]
        data.shape
        data = data.drop('Activity', axis = 1)
        pred = loaded_model.predict(data) 
        data['Activity'] = pred
        data_html = data.to_html()
        return render(request, 'prediction/resultados.html', { 'data': data_html, 'pred' : pred , 'otro' : otro})
        # do something with the file
        # and return the result            
    else:
        return render(request, 'prediction/home.html', {'otro' : otro})

# def resultados(request):
#     files = Dataset.objects.all()
#     return render(request, 'prediction/resultados.html', {'files':files})

def resultados(request):
    return render(request, 'prediction/resultados.html')
    