"""
URL configuration for response_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from response_app.views import (
    MainResponseView, RedirectedView, PermanentRedirectedView, NotModifiedView,
    BadRequestView, ForbiddenView, MethodNotAllowedView, GoneView, ServerErrorView,
    NotFoundView, JsonResponseView, StreamingResponseView, FileResponseView
)

urlpatterns = [
    path('example/', MainResponseView.as_view(), name='main_response'),
    path('example/redirected/', RedirectedView.as_view(), name='redirected_response'),
    path('example/permanent-redirected/', PermanentRedirectedView.as_view(), name='permanent_redirected_response'),
    path('example/not-modified/', NotModifiedView.as_view(), name='not_modified_response'),
    path('example/bad-request/', BadRequestView.as_view(), name='bad_request_response'),
    path('example/forbidden/', ForbiddenView.as_view(), name='forbidden_response'),
    path('example/not-allowed/', MethodNotAllowedView.as_view(), name='not_allowed_response'),
    path('example/gone/', GoneView.as_view(), name='gone_response'),
    path('example/server-error/', ServerErrorView.as_view(), name='server_error_response'),
    path('example/not-found/', NotFoundView.as_view(), name='not_found_response'),
    path('example/json-response/', JsonResponseView.as_view(), name='json_response'),
    path('example/streaming-response/', StreamingResponseView.as_view(), name='streaming_response'),
    path('example/file-response/', FileResponseView.as_view(), name='file_response'),
]