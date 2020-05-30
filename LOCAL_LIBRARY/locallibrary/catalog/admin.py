from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)

@admin.register(Author) # admin.site.register(Author, AuthorAdmin)
class AuthorAdmin(admin.ModelAdmin):
    class BooksInline(admin.TabularInline):
        model = Book

    # fields to be displayed in list view - display할 때
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # orders in detail view - add할 때, detail view에서
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    #inline addition of book in detail view
    inlines = [BooksInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    class BooksInstanceInline(admin.TabularInline):
        model = BookInstance

    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    # filters that will be displayed in sidebar
    list_filter = ('status', 'due_back')
    # grouping of fields into sections - in add view
    # devide into 2 section (None, Availability)
    fieldsets = (
        (None, {    # no section title
            'fields':('book', 'imprint', 'id')
        }),
        ('Availability', {  # section title
            'fields':('status', 'due_back', 'borrower')
        }),
    )
