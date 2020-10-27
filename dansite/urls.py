

from django.conf import settings
from django.conf.urls.static import static
from addresses.views import checkout_address_create_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from accounts.views import guest_register_view
from products.views import FeaturedListView

from .views import home_page, about_page, login_page, logout_page, register_page
urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^login/$', login_page, name='login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^register/$', register_page, name='register'),
    url(r'^featured/$', FeaturedListView.as_view(), name='featured' ),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
