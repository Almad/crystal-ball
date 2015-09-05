from django.views.generic.base import TemplateView

class DashboardView(TemplateView):
    template_name = 'ball/dashboard.html'

dashboard_view = DashboardView.as_view()
