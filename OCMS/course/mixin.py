from django.contrib.auth.mixins import AccessMixin

class InstructorRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
                if request.user.is_instructor():
                    return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class StudentRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
                if request.user.is_student():
                    return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()