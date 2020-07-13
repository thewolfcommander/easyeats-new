from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [

    # Normal Views
    path('', include('core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('addresses/', include('addresses.urls', namespace='addresses')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('dashboard/v1/', include('dashboard.urls', namespace='dashboard')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('products/', include('products.urls', namespace='products')),
    path('groceries/', include('grocery.urls', namespace='grocery')),
    path('third-party/', include('third.urls', namespace='third')),


    # APIS
    path('api/v1/accounts/', include('accounts.api.urls')),
    path('api/v1/addresses/', include('addresses.api.urls')),
    path('api/v1/cart/', include('cart.api.urls')),
    path('api/v1/core/', include('core.api.urls')),
    path('api/v1/groceries/', include('grocery.api.urls')),
    path('api/v1/products/', include('products.api.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)