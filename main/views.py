from django.views.generic import ListView, CreateView
from .models import MediaPost
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import FormFile

class IndexView(ListView):
    template_name = 'main/home.html'
    model = MediaPost
    context_object_name = 'post'
    paginate_by = 10
    
    def post(self, request, *args, **kwargs):
        if request.FILES.get('media'):
            MediaPost.objects.create(media=request.FILES['media'])
        return redirect(request.path_info)
    
class NewView(CreateView):
    template_name = 'main/create.html'
    success_url = reverse_lazy('Home')
    form_class = FormFile
    def form_valid(self, form):
        return super().form_valid(form)
# Create your views here.
