"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    # path('form_wrapper',views.form_wrapper,name="form_wrap"),
    # path('form/<social>',views.form,name="form"),
    # path('getrepos',views.getrepos,name="repos"),
    # path('getbranches',views.getbranches,name="branches"),
    # path('getIRISbranches',views.getIRISbranches,name="IRISbranches"),
    # path('deploy',views.deploy_wrapper,name="deploy_wrap"),
    # path("containerlogs/<orgname>/<reponame>/<branch>/<social>",views.get_container_logs,name="containerlogs"),
    # path("logs/<orgname>/<reponame>/<branch>/<social>",views.logs,name="logs"),
    # path('deploy/<org_name>/<repo_name>/<branch>/<social>',views.deploy,name="deploy"),
    # path('deploy/<org_name>/<repo_name>/<branch>/<social>/<dockerfile_path>/<internal_port>',views.deploy,name="deploy"),
    # path('stop/<social>/<orgname>/<reponame>/<branch>',views.stop,name='stop'),

    # path('deploy_template_list', views.deploy_template_list, name="deploy_template_list"),
    # path('deploy_template_new/', views.deploy_template_form, name='deploy_template_form'),
    # path('deploy_template_update/<int:pk>/', views.deploy_template_update, name='deploy_template_update'),
    # path('deploy_template_delete/<int:pk>/', views.deploy_template_delete, name='deploy_template_delete'),
    # path('deploy_template_stop/<int:pk>/', views.deploy_template_stop, name='deploy_template_stop'),
    # path('deploy_from_template/<int:pk>/', views.deploy_from_template, name='deploy_from_template'),
    # path('deploy_template_dashboard', views.deploy_template_dashboard, name='deploy_template_dashboard'),
    # path('deploy_template_clean_up/<int:pk>/', views.deploy_template_clean_up, name='deploy_template_clean_up'),
    # path('deploy_instance_delete/<int:pk>/', views.deploy_instance_delete, name='deploy_instance_delete'),
    # path('deploy_template_duplicate/<int:pk>/', views.deploy_template_duplicate, name='deploy_template_duplicate'),

    # path('check_uptime_status/<int:pk>/',views.check_uptime_status, name="check_uptime_status"),
    # path('uptime_check_template/<int:pk>/',views.uptime_check_template, name="uptime_check_template"),

    path('logs/<int:pk>', views.instance_logs, name = "instance_logs"),
    path('container_logs/<int:pk>', views.container_logs, name = "container_logs"),
]
