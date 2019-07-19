class FilterByUserMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.for_user(user=self.request.user)
