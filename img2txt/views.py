from django.shortcuts import render
from django.http import request,HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2
import numpy
import os
import pytesseract as pt
# Create your views here.

def home(request):
    return render(request,'home.html')


def tograyscale_convert(img):
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    t = pt.image_to_string(img)
    return t
def convert(img):
    t = pt.image_to_string(img)
    return t

def convert2txt(request):
    img = request.FILES['file']
    filemanager =FileSystemStorage()
    filemanager.save(img.name,img)
    src = 'media/'+img.name
    pt.pytesseract.tesseract_cmd='ocr/tesseract.exe'
    rslt = convert(src)
    if not len(rslt.strip())>0:
        rslt="Empty!!"
    print(rslt)
    return render(request,'result.html',{'result':rslt,'url':src})