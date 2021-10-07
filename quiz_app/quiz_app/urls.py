"""quiz_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from quiz_center import views

from quiz_center import Adminviews

from quiz_center import Participantviews,Staffviews

from quiz_app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page,name="login_page"),
    path('index', views.index,name="index"),
    path('staff_page', views.staff_page,name="staff_page"),
    path('view_feedback', Staffviews.view_feedback,name="view_feedback"),
    path('edit_participant_reply/<str:feed_id>', Staffviews.edit_participant_reply, name="edit_participant_reply"),
    path('dologin', views.dologin,name="dologin"),
    path('logout_page', views.logout_page,name="logout_page"),
    path('edit_feedback_save', Staffviews.edit_feedback_save, name="edit_feedback_save"),
    path('add_participant', Participantviews.add_participant,name="add_participant"),
    path('add_feedback', Participantviews.add_feedback,name="add_feedback"),
    path('feedback_save', Participantviews.feedback_save, name="feedback_save"),
    path('view_profile', Participantviews.view_profile,name="view_profile"),
    path('participant_page', Participantviews.participant_page,name="participant_page"),
    path('save_participant', Participantviews.save_participant,name="save_participant"),
    path('manage_participant', Participantviews.manage_participant, name="manage_participant"),
    path('add_staff', Staffviews.add_staff,name="add_staff"),
    path('save_staff', Staffviews.save_staff,name="save_staff"),
    path('get_staff', Participantviews.get_staff, name="get_staff"),
    path('add_competition', Staffviews.add_competition, name="add_competition"),
    path('save_competition', Staffviews.save_competition,name="save_competition"),
    path('add_question', Staffviews.add_question, name="add_question"),
    path('save_question', Staffviews.save_question, name="save_question"),
    path('selected_question/<str:exam_id>', Participantviews.selected_question, name="selected_question"),
    path('save_participant_changes', Participantviews.save_participant_changes, name="save_participant_changes"),
    path('available_mock_test', Participantviews.available_mock_test, name="available_mock_test"),
   # path('', views.login_page,name="login_page"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
