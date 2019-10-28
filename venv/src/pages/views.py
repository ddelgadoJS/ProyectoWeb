from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from pages.models import Empresa
from pages.forms import EmpresaCreateForm


@login_required
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


#---------------------------------------------------------------------------
# Empresa

class EmpresaCreate(CreateView):
    model = Empresa
    form_class = EmpresaCreateForm
    template_name = 'empresa/empresa_create.html'


class EmpresaListView(ListView):
    """
    Lista de empresas
    """

    model = Empresa
    paginate_by = 15
    template_name = 'empresa/empresa_listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # we create the form and pass it to the rendering html
        # context['form'] = CreatePost()
        # context['sort'] = self.kwargs['sort']
        # context['channel'] = self.kwargs['channel']
        # items = HeaderImage.objects.all()
        # random_image = random.choice(items)
        # context['imageUrl'] = random_image
        return context

    def get_queryset(self, *args, **kwargs):
        return Empresa.objects.all()


class EmpresaDetailView(DetailView):
    template_name = 'empresa/empresa_detailview.html'

    def get_login_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channel_name'] = self.kwargs['channel']
        return context

    # def get_object(self):
    #     empresa_name = self.kwargs['empresa']
    #     channel = Empresa.objects.get(name=channel_name)
    #     return channel

    def get_success_url(self):
        return reverse('wiki-view', kwargs={'channel': self.kwargs['channel']})