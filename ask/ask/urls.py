from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from qa.views import test, new_questions, popular_questions, one_question, ask, answer, signup, login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'qa.views.new_questions'),
    url(r'login/$', 'qa.views.login', name='login'),
    url(r'signup/$', 'qa.views.signup', name='signup'),
    url(r'ask/$', 'qa.views.ask', name='ask'),
    url(r'answer/$', 'qa.views.answer', name='anwer'),
    url(r'popular/$', 'qa.views.popular_questions', name='popular'),
    url(r'new/$', 'qa.views.new_questions', name='new'),
    url(r'question/(?P<id>\d+)/$', 'qa.views.one_question', name='question'),
    url(r'^admin/', include(admin.site.urls)),
)
