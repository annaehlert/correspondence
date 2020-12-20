from rest_framework import routers
from general_book import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewset)
router.register(r'subjects', views.SubjectViewset)
router.register(r'letters', views.LettersViewset)