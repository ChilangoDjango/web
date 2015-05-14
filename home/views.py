from django.views.generic import TemplateView

class CountDownView(TemplateView):
	template_name = 'count_down.html'