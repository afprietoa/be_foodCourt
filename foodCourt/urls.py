from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from marketplace import views as Marketplaceviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('accounts.urls')),
    
    path('marketplace/', include('marketplace.urls')),
    path('cart/', Marketplaceviews.cart, name='cart'),

    # Search
    path('search/',Marketplaceviews.search, name='search'),
    
    # CHECKOUT
    path('checkout/', Marketplaceviews.checkout, name='checkout'),

    # ORDERS
    path('orders/', include('orders.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
