from django.contrib import admin
from django.contrib.auth.admin import User, Group
from reviews.models import (Publisher, Contributor, Book,
        BookContributor, Review)
from reviews.admin import ContributorAdmin



class BookrAdmin(admin.AdminSite):
    site_header = 'Administracja witryną Bookr'
    site_title = 'Moja aplikacja internetowa Django'
    index_title = 'Panel administracyjny'

admin_site = BookrAdmin(name='bookr_admin')
admin_site.register(User)
admin_site.register(Group)


admin_site.register(Publisher)
admin_site.register(Contributor, ContributorAdmin)
admin_site.register(Book)
admin_site.register(BookContributor)
admin_site.register(Review)