from django.contrib import admin
from mixins.translations_mixins import TranslatorMediaMixin, TranslationStackedInlineMixin, TranslationMixin
from .models import Category, Product, Recipe, Price
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from unfold.admin import ModelAdmin, StackedInline
from django.contrib.auth import admin as base_admin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)


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


@admin.register(Category)
class CategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ("category", "title")
    class Media:
        js = ('translate/autotranslate.js',)


class ProductPriceInline(StackedInline, TranslationStackedInline):
    model = Price
    fields = ['volume', 'price']
    max_num = 3
    extra = 3

    class Media:
        js = ('translate/autotranslate.js',)


@admin.register(Product)
class ProductAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['id', 'hit_of_sales', 'name', 'category']
    list_display_links = ['id', 'name']
    inlines = (ProductPriceInline,)
    autocomplete_fields = ("category", )

    class Media:
        js = ('translate/autotranslate.js',)


# class AditionalStepsInline(TranslationTabularInlineMixin):
#     model = AditionalStep
#     fields = ['title', 'description']
#     extra = 0
#
#     class Media:
#         js = ('translate/autotranslate.js',)


@admin.register(Recipe)
class RecipeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['id', 'product']
    list_display_links = ['id', 'product']
    
    class Media:
        js = ('translate/autotranslate.js',)
