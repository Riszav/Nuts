from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": _("SOLAAR"),
    "SITE_HEADER": _(" "),
    # "SITE_URL": "/",
    # # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    "SITE_ICON": {
        "light": lambda request: static("icon.svg"),  # light mode
        "dark": lambda request: static("icon.svg"),  # dark mode
    },
    # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    # "SITE_LOGO": {
    #     "light": lambda request: static("icon.svg"),  # light mode
    #     "dark": lambda request: static("icon.svg"),  # dark mode
    # },
    "SITE_SYMBOL": "sunny",  # symbol from icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("logo.svg"),
        },
    ],
    "SHOW_HISTORY": True, # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
    # "ENVIRONMENT": "sample_app.environment_callback",
    # "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
    # "THEME": "dark", # Force theme: "dark" or "light". Will disable theme switcher
    "LOGIN": {
        # "image": lambda request: static("sample/login-bg.jpg"),
        # "redirect_after": lambda request: reverse_lazy("admin:auth_user_changelist"),
    },
    # "STYLES": [
    #     lambda request: static("unfold/css/styles.css"),
    # ],
    # "SCRIPTS": [
    #     lambda request: static("unfold/js/script.js"),
    # ],
    "COLORS": {
        "primary": {
            "50": "255 250 240",
            "100": "254 243 199",
            "200": "253 230 138",
            "300": "252 211 77",
            "400": "251 191 36",
            "500": "245 158 11",
            "600": "217 119 6",
            "700": "180 83 9",
            "800": "146 64 14",
            "900": "120 53 15",
            "950": "69 26 3"
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "EN",
                "ru": "RU",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Catalog"),
                "separator": True,  # Top border
                "collapsible": False,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Products"),
                        "icon": "inventory_2",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:nuts_product_changelist"),
                    },
                    {
                        "title": _("Category"),
                        "icon": "category",
                        "link": reverse_lazy("admin:nuts_category_changelist"),
                    },
                    {
                        "title": _("Recipe"),
                        "icon": "menu_book",
                        "link": reverse_lazy("admin:nuts_recipe_changelist"),
                    }
                ],
            },
            {
                "title": _("Generals"),
                "separator": True,  # Top border
                "collapsible": False,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Questions"),
                        "icon": "indeterminate_question_box",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:generals_faq_changelist"),
                    },
                    {
                        "title": _("Contacts"),
                        "icon": "contacts",
                        "link": reverse_lazy("admin:generals_contact_changelist"),
                    },
                    {
                        "title": _("Whats App"),
                        "icon": "chat",
                        "link": reverse_lazy("admin:generals_whatsappnumber_changelist"),
                    },
                ],
            },
            {
                "title": _("News"),
                "separator": True,  # Top border
                "collapsible": False,  # Collapsible group of links
                "items": [
                    {
                        "title": _("News"),
                        "icon": "newsmode",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:news_news_changelist"),
                    },
                ],
            },
            {
                "title": _("About us"),
                "separator": True,  # Top border
                "collapsible": False,  # Collapsible group of links
                "items": [
                    {
                        "title": _("About us"),
                        "icon": "window",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:about_us_aboutus_changelist"),
                    },
                    {
                        "title": _("Banner"),
                        "icon": "aspect_ratio",
                        "link": reverse_lazy("admin:about_us_banner_changelist"),
                    },
                ],
            },
            {
                "title": _("Users"),
                "separator": True,  # Top border
                "collapsible": False,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                ],
            },
        ],
    },
    # "TABS": [
    #     {
    #         "models": [
    #             "generals.faq",
    #             "generals.contact",
    #             "news.news",
    #             "nuts.product",
    #             "nuts.category",
    #             "nuts.recipe",
    #         ],
    #         "items": [
    #             {
    #                 "title": _("Your custom title"),
    #                 "link": reverse_lazy("admin:auth_user_changelist"),
    #             },
    #         ],
    #     },
    # ],
}


def badge_callback(request):
    return 3