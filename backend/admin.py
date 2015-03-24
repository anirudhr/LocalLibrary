from django.contrib import admin
from backend.models import User, Shelf, Book, ShelfContainsBook

admin.site.register(User)
admin.site.register(Shelf)
admin.site.register(Book)
admin.site.register(ShelfContainsBook)

