from django.contrib import admin
from .models import Category, Product, Recipe, Price
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from unfold.admin import ModelAdmin, StackedInline
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from django.contrib.auth import admin as base_admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)


''''''''''''''''''''''''''''START AUTH USER AND GROUP REGISTER'''''''''''''''''''''''''''''


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(ModelAdmin, base_admin.UserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
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
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


@admin.register(Group)
class CustomGroupAdmin(ModelAdmin, base_admin.GroupAdmin):
    search_fields = ("name",)
    ordering = ("name",)
    filter_horizontal = ("permissions",)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "permissions":
            qs = kwargs.get("queryset", db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs["queryset"] = qs.select_related("content_type")
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)


''''''''''''''''''''''''''''END AUTH USER AND GROUP REGISTER'''''''''''''''''''''''''''''


@admin.register(Category)
class CategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ("name_ru", 'name_en', )

    class Media:
        js = ('translate/autotranslate.js',)

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 3:
            return False
        else:
            return True


class ProductPriceInline(StackedInline, TranslationStackedInline):
    model = Price
    fields = ['volume', 'price']
    max_num = 3
    extra = 3

    class Media:
        js = ('translate/autotranslate.js',)


@admin.register(Product)
class ProductAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['id', 'hit_of_sales', 'name', 'product_image', 'category']
    list_display_links = ['id', 'hit_of_sales', 'name', 'product_image', 'category']
    inlines = (ProductPriceInline,)
    autocomplete_fields = ("category", )
    search_fields = ('name_ru', 'name_en')

    class Media:
        js = ('translate/autotranslate.js',)

    @admin.display(description=_('Image'))
    def product_image(self, img: Product):
        return mark_safe(f"<img src='{img.image.url}' width=50 style='border-radius: 5px;>'")


@admin.register(Recipe)
class RecipeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['id', 'product', 'recipe_image']
    list_display_links = ['id', 'product', 'recipe_image']
    autocomplete_fields = ("product", )
    
    class Media:
        js = ('translate/autotranslate.js',)

    @admin.display(description=_('Image'))
    def recipe_image(self, img: Recipe):
        return mark_safe(f"<img src='{img.image.url}' width=50 style='border-radius: 5px;>'")
    
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 4:
            return False
        else:
            return True
