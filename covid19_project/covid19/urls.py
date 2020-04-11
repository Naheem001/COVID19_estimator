from django.urls import path


from .views import estimator

urlpatterns = [
    path('api/v1/on-covid-19', estimator, name="estimator"),
]