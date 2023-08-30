from django.contrib import admin
from django.urls import path, include
from book.views import *
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets


router = DefaultRouter()
router.register(r'books',BooksViewSet)
router.register(r'reader',ReaderViewSet)
urlpatterns = [
    path('admin/',admin.site.urls),
    # path('books/',BooksViewSet.as_view({
    #     'get':'list',
    #     'post' :'create'
    # })),
    # path('books/<int:pk>',BooksViewSet.as_view({
    #     'get':'retrieve',
    #     'put':'update',
    #     'patch':'partial_update',
    #     'delete':'destroy',
    # })),
    path('', include(router.urls))
         
    # path('api/books/', BookApiViews.as_view() ),
    # path('api/books/<int:id>', BookApiViews.as_view() ),
    # path('visitors/', VisitorList.as_view(), name='visitor-list'),
    # path('visitors/<urlsint:pk>/', VisitorRetrive.as_view(), name='visitor-retrieve'),
    # path('visitors/create/', VisitorCreation.as_view(), name='visitor-create'),
    # path('visitors/update/<int:pk>/', VistorUpdate.as_view(), name='visitor-update'),
    # path('visitors/delete/<int:pk>/', VisitorDeletion.as_view(), name='visitor-delete'),
]
