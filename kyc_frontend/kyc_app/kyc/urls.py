from django.urls import include, path

from bank.views import bank, customers, bankers

urlpatterns = [
    path('', include('bank.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', bank.SignUpView.as_view(), name='signup'),
    path('accounts/signup/customer/', customers.CustomerSignUpView.as_view(), name='customer_signup'),
    path('accounts/signup/banker/', bankers.BankerSignUpView.as_view(), name='banker_signup'),
]
