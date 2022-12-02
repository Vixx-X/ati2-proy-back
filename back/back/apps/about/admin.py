from functools import update_wrapper

from django.contrib import admin
from django.contrib.admin.utils import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView

from .models import ContactMe, PageSetting


admin.site.register(ContactMe)


@admin.register(PageSetting)
class PageSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        from django.urls import re_path

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name

        urlpatterns = [
            re_path(
                r"^$",
                wrap(
                    RedirectView.as_view(
                        pattern_name="%s:%s_%s_change"
                        % ((self.admin_site.name,) + info)
                    )
                ),
                name="%s_%s_changelist" % info,
            ),
            re_path(
                r"^history/$",
                wrap(self.history_view),
                {"object_id": str(self.singleton_instance_id)},
                name="%s_%s_history" % info,
            ),
            re_path(
                r"^change/$",
                wrap(self.change_view),
                {"object_id": str(self.singleton_instance_id)},
                name="%s_%s_change" % info,
            ),
        ]
        parent_urlpatterns = super().get_urls()
        return urlpatterns + parent_urlpatterns

    def change_view(self, request, object_id, form_url="", extra_context=None):
        if object_id == str(self.singleton_instance_id):
            self.model.objects.get_or_create(pk=self.singleton_instance_id)
        return super().change_view(
            request,
            object_id,
            form_url=form_url,
            extra_context=extra_context,
        )

    def response_post_save_change(self, request, obj):
        post_url = reverse(
            "%s:app_list" % self.admin_site.name, args=(self.model._meta.app_label,)
        )
        return HttpResponseRedirect(post_url)

    @property
    def singleton_instance_id(self):
        return getattr(self.model, "singleton_instance_id")
