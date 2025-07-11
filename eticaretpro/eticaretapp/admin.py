from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from eticaretapp.models import Banner, Product,  ProductContent, ProductPhoto, Review, Contanct, Store, Wishlist, Approval, SiteSettings,CustomUser
from django.contrib.admin.sites import AdminSite

admin.site.register(Banner)
admin.site.register(ProductContent)
admin.site.register(ProductPhoto)
admin.site.register(Review)
admin.site.register(Contanct)
admin.site.register(Store)
admin.site.register(SiteSettings)
admin.site.register(Wishlist)
admin.site.register(Approval)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ( "password",)}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ( "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ( "email", "first_name", "last_name", "is_staff")
    search_fields = ( "first_name", "last_name", "email")
    ordering = ('email',)

class ProductContentAdmin(admin.TabularInline):
    model=ProductContent
    extra=1


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductContentAdmin]
    actions=['make_in_stock', 'make_not_in_stock']
    
    @admin.action(description='make selected products in stock')

    def make_in_stock(self,request,queryset):
        queryset.update(is_stock=True)
        text=str(len(queryset)+'product made in stock'if queryset.count()==1 else str(len(queryset)+'products made in stock'))
        self.message_user(request,text)

    @admin.action(description='make selected products not in stock')
    def make_not_in_stock(self,request,queryset):
        queryset.update(is_stock=False)

        text=str(len(queryset)+'product made not in stock'if queryset.count()==1 else str(len(queryset)+'products made not in stock'))
        self.message_user(request,text)
        

AdminSite.site_header='Ecommerce Adminstration'

AdminSite.site_title='Ecommrece-adminstration'
