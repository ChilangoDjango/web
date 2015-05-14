from django.views.generic import TemplateView

class CountDownView(TemplateView):
	template_name = 'count_down.html'

	def get_context_data(self):
		context = super(CountDownView, self).get_context_data()
		context['title'] = 'Chilango Django'
		context['meta_description'] = 'Comunidad de desarrolladores Python y Django en la Ciudad de Mexico'
		return context