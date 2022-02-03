
from django.urls import path,include
from contract import views


urlpatterns = [
    path('rates/<slug:contract_slug>',views.RatesView.as_view()),
    path('all/',views.ContractListView.as_view()),

    path('create_contract/',views.CreateContract.as_view()),
]
