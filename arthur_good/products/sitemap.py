# products/sitemap.py
from django.contrib.sitemaps import Sitemap
from .models import Product
from django.urls import reverse

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['home', 'products', 'about', 'contact']  # Your view names

    def location(self, item):
        return reverse(item)