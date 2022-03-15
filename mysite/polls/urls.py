from django.urls import path

from . import views

# Q: In real Django projects there might be five, ten, twenty apps. How does
# Django know which app view to create for a url when using the {% url %}
# template tag (e.g, more than one app might have a `detail` view)?
#
# A: Add namespaces to your URLconf. In the polls/urls.py file, add an app_name
# to set the application namespace:
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/wow
    # path('wow', views.wow, name='wowpage'),
    # ex: /polls/5/
    # The 'name' value as called by the {% url %} template tag.
    # And we added the word 'specifics'
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results
    path('<int:question_id>/results', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote', views.vote, name='vote'),
]
