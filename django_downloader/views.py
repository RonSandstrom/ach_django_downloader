# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

updated_docs = 3
new_docs = 5
dte = f"{datetime.today().strftime('%Y-%m-%d')}"

def get_title():
    return "Finance ACH Downloader"

def set_updated_document_coumnt(x):
    global updated_docs
    updated_docs = x

def set_new_document_coumnt(x):
    global new_docs
    new_docs = x

def get_updated_document_count():
    return updated_docs

def get_new_document_count():
    return new_docs

def download_updated(request):
    global updated_docs
    if get_updated_document_count() > 0:
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define text file name
        filename = 'updated_imports.csv'
        # Define the full file path
        filepath = BASE_DIR + '/django_downloader/Files/Updated/' + filename
        # Open the file for reading content
        path = open(filepath, 'r')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        set_updated_document_coumnt(0)
        return response
    else:
        return render(request, 'ach_downloads/download_ach.html',
                  {'title': get_title(),
                   'dte': dte,
                   'new_documents': get_new_document_count(),
                   'updated_documents': get_updated_document_count()
                   })


def download_new(request):
    global new_docs
    if get_new_document_count() > 0:
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define text file name
        filename = 'new_imports.csv'
        # Define the full file path
        filepath = BASE_DIR + '/django_downloader/Files/New/' + filename
        # Open the file for reading content
        path = open(filepath, 'r')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        set_new_document_coumnt(0)
        return response
    else:
        return render(request, 'ach_downloads/download_ach.html',
                  {'title': get_title(),
                   'dte': dte,
                   'new_documents': get_new_document_count(),
                   'updated_documents': get_updated_document_count()
                   })


def index(request):
    return render(request, 'ach_downloads/download_ach.html',
                  {'title': get_title(),
                   'dte': dte,
                   'new_documents': get_new_document_count(),
                   'updated_documents': get_updated_document_count()
                   })