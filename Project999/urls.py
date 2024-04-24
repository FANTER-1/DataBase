"""
URL configuration for Project999 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from flask import Blueprint
from .views import SubmitDataListCreateAPIView, SubmitDataRetrieveUpdateDestroyAPIView
from .docs import swagger_bp

bp = Blueprint('api', DataBase)

urlpatterns = [
    bp.add_url_rule('/submitData/', view_func=SubmitDataListCreateAPIView.as_view('submit-data-list-create'),
                    methods=['GET', 'POST']),
    bp.add_url_rule('/submitData/<int:pk>/',
                    view_func=SubmitDataRetrieveUpdateDestroyAPIView.as_view('submit-data-detail'),
                    methods=['GET', 'PUT', 'DELETE']),
    bp.add_url_rule('/swagger.json', view_func=swagger_bp.as_view('swagger_json'), methods=['GET']),
    bp.add_url_rule('/swagger/', view_func=swagger_bp.as_view('swagger_ui'), methods=['GET']),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

