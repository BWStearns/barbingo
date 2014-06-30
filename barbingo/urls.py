from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barbingo.views.home', name='home'),
    # url(r'^barbingo/', include('barbingo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^confirm/$', 'bingo.views.mark_as_confirmed'),
    url(r'^game/(?P<game_id>[0-9]+)/card/(?P<card_id>[0-9]+)/$', 'bingo.views.get_card'),
    url(r'^game/(?P<game_id>[0-9]+)/$', 'bingo.views.get_game'),
)
