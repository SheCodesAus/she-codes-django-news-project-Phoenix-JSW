from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('<slug:slug>/', views.story_detail, name='story'),
    path('<slug:slug>/edit-story/', views.UpdateStoryView.as_view(), name='editStory'),
    path('<slug:slug>/delete-story/', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('<slug:slug>/category/', views.CategoryView.as_view(), name='categoryDetail'),
    # path('category/<str:cats>', views.CategoryView, name='category'),
 ]
handler404 = views.handler404