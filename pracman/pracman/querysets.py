from django.core.exceptions import ImproperlyConfigured


class UserRelatedQuerySetMixin(object):
    user_filter_key = None

    def for_user(self, user):
        if not self.user_filter_key:
            raise ImproperlyConfigured("A user_filter_key is required")
        kwargs = {self.user_filter_key: user}
        try:
            return self.filter(**kwargs)
        except AttributeError:
            return self.none()
