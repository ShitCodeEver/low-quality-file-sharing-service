from django.views.generic import ListView, DetailView
from .models import MediaPost
from django.shortcuts import redirect

class IndexView(ListView):
    template_name = 'main/home.html'
    model = MediaPost
    context_object_name = 'post'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = {
            'name' : 'главная'
        }
        return context
    def post(self, request, *args, **kwargs):
        if request.FILES.get('media'):
            MediaPost.objects.create(media=request.FILES['media'])
        return redirect(request.path_info)
# Create your views here.
