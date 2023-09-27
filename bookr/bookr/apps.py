from django.contrib.admin.apps import AdminConfig


#class BookrAdminConfig(AdminConfig):
    #default_site = 'admin.BookrAdminSite'

class BookrAdminConfig(AdminConfig):
    default_site = 'bookr_admin.admin.BookrAdmin'

