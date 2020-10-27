from django.shortcuts import render

from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from carts.models import Cart

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "list.html"


class FeaturedListView(ListView):
    queryset=Product.objects.all().featured()
    context_object_name = 'featured_products'
    template_name = "featured.html"

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "detail.html"

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['carts'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm")
        return instance
