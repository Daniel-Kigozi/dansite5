from django.conf.urls import url

from .views import (
   ProductListView,
   FeaturedListView,
   ProductDetailSlugView,

   )

urlpatterns = [

    url(r'^$', ProductListView.as_view(), name='list' ),
    url(r'^featured/$', FeaturedListView.as_view(), name='featured' ),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),

]
