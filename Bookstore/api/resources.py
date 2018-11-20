from tastypie.resources import ModelResource
from Bookstore.models import Book


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        allowed_methods = ['get']
