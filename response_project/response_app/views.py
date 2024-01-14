# response_app
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, \
    HttpResponseNotModified, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseNotAllowed, HttpResponseGone, HttpResponseServerError, \
    HttpResponseNotFound, JsonResponse, StreamingHttpResponse, FileResponse

class MainResponseView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, this is the main HttpResponse")

class RedirectedView(View):
    def get(self, request, *args, **kwargs):

        return HttpResponseRedirect('/example/')

class PermanentRedirectedView(View):
    def get(self, request, *args, **kwargs):

        return HttpResponsePermanentRedirect('/example/')

class NotModifiedView(View):
    def get(self, request, *args, **kwargs):

        return HttpResponseNotModified()

class BadRequestView(View):
 
    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Bad Request")

class ForbiddenView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponseForbidden("Forbidden")

class MethodNotAllowedView(View):
   
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["GET", "POST"], "Not Allowed")

class GoneView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponseGone("Gone")

class ServerErrorView(View):
    

    def get(self, request, *args, **kwargs):
        return HttpResponseServerError("Server Error")

class NotFoundView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound("Not Found")

class JsonResponseView(View):
   
    def get(self, request, *args, **kwargs):
        data = {'key': 'value'}
        return JsonResponse(data)

class StreamingResponseView(View):
    
    def get(self, request, *args, **kwargs):
        content = "This is a streaming response."
        return StreamingHttpResponse(content, content_type="text/plain")

class FileResponseView(View):
    
    def get(self, request, *args, **kwargs):
        file_path = 'C:/Users/julia/OneDrive/Documents/A4/RTU/Telecommunications Software/test.txt'  
        return FileResponse(open(file_path, 'rb'), content_type="text/plain")