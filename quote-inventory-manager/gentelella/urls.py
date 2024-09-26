"""gentella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# to run using Django 2.1
# from django.conf.urls import url, include
# from django.contrib import admin

# to run using Django 4.2
from django.urls import include, path, re_path
from django.contrib import admin


# to run using Django 2.1
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),

#     # app/ -> Genetelella UI and resources
#     url(r'^app/', include('app.urls')),
#     url(r'^', include('app.urls')),

# ]

# to run using Django 4.2

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    # app/ -> Genetelella UI and resources
    path(r'^app/', include('app.urls')),
    path(r'^', include('app.urls')),
    path('', include('app.urls')),

]
