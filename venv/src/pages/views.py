from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Empresa, Ruta, Parada, Evaluacion
from .forms import *
from .lib import crear_log

from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView

from statistics import mean
from math import ceil

def aux_get_paradas_unicas(paradas):
    paradas_unicas = []
    query_set = []
    for parada in paradas:
        if parada.nombre not in paradas_unicas:
            paradas_unicas.append(parada.nombre)
            query_set.append(parada)
    
    return query_set

def aux_get_destinos_unicos(rutas):
    destinos_unicos = []
    query_set = []
    for ruta in rutas:
        if ruta.nombre_destino not in destinos_unicos:
            destinos_unicos.append(ruta.nombre_destino)
            query_set.append(ruta)
    
    return query_set

def home_view(request, *args, **kwargs):
    """
    Pagina de filtros
    """
    if request.method == 'GET':
        consulta = 0
        empresa_id = 0
        ruta_id = 0
        rutas = ''
        paradas = ''
		
        empresa = request.GET.get('empresa') is not '' and request.GET.get('empresa') is not None
        ruta = request.GET.get('ruta') is not '' and request.GET.get('ruta') is not None
        destino = request.GET.get('destino') is not '' and request.GET.get('destino') is not None
        parada = request.GET.get('parada') is not '' and request.GET.get('parada') is not None
		
        if(any([empresa,ruta,parada,destino])):
            rutas = Ruta.objects.all()
            paradas = Parada.objects.all();
            consulta = 1
        if(empresa):
            if(request.GET.get('empresa')!="0"):
                rutas = rutas.filter(empresa=request.GET.get('empresa'))
                empresa_id = request.GET.get('empresa')
        if(ruta):
            rutas = rutas.filter(id=request.GET.get('ruta'))
            ruta_id = request.GET.get('ruta')
        if(destino):
            rutas = rutas.filter(nombre_destino=request.GET.get('destino'))
        if(parada):
            parada = Parada.objects.filter(nombre=request.GET.get('parada'))
            rutas_temp = []
            for p in parada:
                rutas_temp.append(Ruta.objects.get(id=p.ruta.id))
            rutas = rutas_temp
        if(consulta!=0):
            rutas = serializers.serialize("json",rutas)
		    
        context = {
            "consulta": consulta,
            "empresas": Empresa.objects.all(),
            "rutas": Ruta.objects.all(),
			"rutas_query": rutas,
            "paradas_all": aux_get_paradas_unicas(Parada.objects.all()),
            "paradas": serializers.serialize("json", Parada.objects.all()),
            "destinos_all": aux_get_destinos_unicos(Ruta.objects.all()),
            "empresa_id": int(empresa_id),
            "ruta_id": int(ruta_id)
        }

    return render(request, "home.html", context)


@login_required
def empresa_view(request, *args, **kwargs):
    registered_companies_queryset = Empresa.objects.all()

    context = {
        "registered_companies": registered_companies_queryset,
    }

    return render(request, "empresas/empresas_home.html", context)

@login_required
def empresa_create_view(request, *args, **kwargs):
    form = EmpresaCreateForm(request.POST or None)
    if form.is_valid():
        empresa = form.save()
        crear_log(request.user, "crea", empresa=empresa)
        return redirect('/empresas')

    context = {
        'form': form
    }
    
    return render(request, "empresas/empresas_registrar.html", context)

@login_required
def empresa_modify_view(request, *args, **kwargs):
    empresa_id = request.GET.get('id')
    empresa = Empresa.objects.get(id=empresa_id)
    data = {
        'nombre': empresa.nombre,
        'description': empresa.description,
        'direccion': empresa.direccion,
        'horario': empresa.horario,
        'telefono': empresa.telefono,
        'correo': empresa.correo,
        'serv_origen': empresa.serv_origen,
        'serv_destino': empresa.serv_destino,
        'latitud': empresa.latitud,
        'longitud': empresa.longitud
    }

    form = EmpresaUpdateForm(initial=data)
    if request.method == 'POST':
        if 'update_button' in request.POST:
            form = EmpresaUpdateForm(request.POST, instance=empresa)
            if form.is_valid():
                empresa = form.save()
                crear_log(request.user, "actualiza", empresa=empresa)
                return redirect('/empresas')
        elif 'delete_button' in request.POST:
            Empresa.objects.get(id=empresa_id).delete()
            return redirect('/empresas')

    context = {
        'form': form
    }
    
    return render(request, "empresas/empresas_modificar.html", context)

@login_required
def usuario_modify_view(request, *args, **kwargs):
    data = {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name
        
    }

    form = UsuarioUpdateForm(initial=data)
    """ if request.method == 'POST':
        if 'update_button' in request.POST:
            form = EmpresaUpdateForm(request.POST, instance=empresa)
            if form.is_valid():
                empresa = form.save()
                crear_log(request.user, "actualiza", empresa=empresa)
                return redirect('/empresas')
        elif 'delete_button' in request.POST:
            Empresa.objects.get(id=empresa_id).delete()
            return redirect('/empresas') """

    context = {
        'form': form
    }
    
    return render(request, "/perfil.html", context)

@login_required
def ruta_view(request, *args, **kwargs):
    registered_companies_queryset = Empresa.objects.all()

    empresa_id = request.GET.get('id')
    # Default company to show routes.
    if empresa_id is None: empresa_id = registered_companies_queryset[0].id

    company_routes = Ruta.objects.filter(empresa=empresa_id)

    context = {
        "registered_companies": registered_companies_queryset,
        "company_routes": company_routes,
        "empresa_id": int(empresa_id),
    }

    return render(request, "rutas/rutas_home.html", context)

@login_required
def ruta_create_view(request, *args, **kwargs):
    form = RutaCreateForm(request.POST or None)
    if form.is_valid():
        ruta = form.save()
        crear_log(request.user, "crea", ruta=ruta)
        return redirect('/rutas')

    context = {
        'form': form
    }
    
    return render(request, "rutas/rutas_registrar.html", context)

@login_required
def ruta_modify_view(request, *args, **kwargs):
    ruta_id = request.GET.get('id')
    ruta = Ruta.objects.get(id=ruta_id)
    paradas = Parada.objects.filter(ruta=ruta_id)
    data = {
        'empresa': ruta.empresa,
        'nombre': ruta.nombre,
        'description': ruta.description,
        'costo': ruta.costo,
        'horario': ruta.horario,
        'duracion_viaje': ruta.duracion_viaje,
        'inclusivo': ruta.inclusivo,
        'origen_latitud': ruta.origen_latitud,
        'origen_longitud': ruta.origen_longitud,
        'destino_latitud': ruta.destino_latitud,
        'destino_longitud': ruta.destino_longitud
    }

    form = RutaUpdateForm(initial=data)
    if request.method == 'POST':
        if 'update_button' in request.POST:
            form = RutaUpdateForm(request.POST, instance=ruta)
            if form.is_valid():
                ruta = form.save()
                crear_log(request.user, "actualiza", ruta=ruta)
                return redirect('/rutas')
        elif 'delete_button' in request.POST:
            Ruta.objects.get(id=ruta_id).delete()
            return redirect('/rutas')

    context = {
        'form': form,
        'paradas': serializers.serialize("json", paradas)
    }
    
    return render(request, "rutas/rutas_modificar.html", context)

@login_required
def parada_view(request, *args, **kwargs):
    registered_routes_queryset = Ruta.objects.all()

    ruta_id = request.GET.get('id')
    # Default company to show routes.
    if ruta_id is None: ruta_id = registered_routes_queryset[0].id

    routes_stops = Parada.objects.filter(ruta=ruta_id)

    context = {
        "registered_routes": registered_routes_queryset,
        "routes_stops": routes_stops,
        "ruta_id": int(ruta_id),
    }

    return render(request, "paradas/paradas_home.html", context)

@login_required
def parada_create_view(request, *args, **kwargs):
    form = ParadaCreateForm(request.POST or None)
    if form.is_valid():
        parada = form.save()
        crear_log(request.user, "crea", parada=parada)
        return redirect('/paradas')

    context = {
        'form': form
    }
    
    return render(request, "paradas/paradas_registrar.html", context)

@login_required
def parada_modify_view(request, *args, **kwargs):
	parada_id = request.GET.get('id')
	parada = Parada.objects.get(id=parada_id)
	
	ruta_id = request.GET.get('idr')
	ruta = Ruta.objects.get(id=ruta_id)
	paradas = Parada.objects.filter(ruta=ruta_id)
	
	ruta = {
		'origen_latitud': ruta.origen_latitud,
        'origen_longitud': ruta.origen_longitud,
        'destino_latitud': ruta.destino_latitud,
        'destino_longitud': ruta.destino_longitud
	}
	
	id_parada = {
		'id' : parada.id
	}
	
	data = {
		'ruta': parada.ruta,
        'nombre': parada.nombre,
        'description': parada.description,
        'horario': parada.horario,
        'latitud': parada.latitud,
        'longitud': parada.longitud
    }
	

	form = ParadaUpdateForm(initial=data)
	if request.method == 'POST':
		if 'update_button' in request.POST:
			form = ParadaUpdateForm(request.POST, instance=parada)
			if form.is_valid():
				parada = form.save()
				crear_log(request.user, "actualiza", parada=parada)
				return redirect('/paradas')
		elif 'delete_button' in request.POST:
			Parada.objects.get(id=parada_id).delete()
			return redirect('/paradas')

	context = {
		'form': form,
		'ruta': ruta,
		'id_parada': id_parada,
		'paradas': serializers.serialize("json", paradas)
	}
    
	return render(request, "paradas/paradas_modificar.html", context)

@login_required
def profile_view(request, *args, **kwargs):
    data = {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'password': ''
    }

    form = UsuarioUpdateForm(initial=data, instance=request.user)
    #form = UsuarioUpdateForm(data=request.POST, instance=request.user)
    if request.method == 'POST':
        if 'update_button' in request.POST:
            form = UsuarioUpdateForm(request.POST)
            if form.is_valid():
                request.user.username = request.POST.get('username')
                request.user.email = request.POST.get('email')
                request.user.first_name = request.POST.get('first_name')
                request.user.last_name = request.POST.get('last_name')
                #request.user.set_password(request.POST.get('password'))
                request.user.save()
                return redirect('/perfil')
        elif 'delete_button' in request.POST:
            request.user.is_active = False
            request.user.save()
            return redirect('/login')

    context = {
        'form': form
    }
    
    return render(request, "perfil.html", context)

def evaluaciones_view(request, *args, **kwargs):
    registered_routes_queryset = Ruta.objects.all()

    ruta_id = request.GET.get('id')
    # Default company to show routes.
    if ruta_id is None: ruta_id = registered_routes_queryset[0].id

    routes_stops = Parada.objects.filter(ruta=ruta_id)


    context = {
        "registered_routes": registered_routes_queryset,
        "routes_stops": routes_stops,
        "ruta_id": int(ruta_id),
    }


    return render(request, "evaluaciones/evaluaciones.html", context)

def evaluaciones_view(request, *args, **kwargs):
    registered_companies_queryset = Empresa.objects.all()

    empresa_id = request.GET.get('id')
    stars = request.GET.get('stars')
    # Default company to show evaluations.
    if empresa_id is None: empresa_id = registered_companies_queryset[0].id

    if stars is not None:
        empresa = Empresa.objects.get(id=empresa_id)
        evaluacion = Evaluacion(empresa=empresa, usuario=request.user, estrellas=stars, comentario="")
        evaluacion.save()
        return redirect('/evaluaciones/?id=' + empresa_id)

    evaluaciones = Evaluacion.objects.filter(empresa=empresa_id)
    estrellas = list(evaluaciones.values_list('estrellas', flat=True))
    
    if len(estrellas) == 0: estrellas = [0]

    context = {
        "empresa_id": empresa_id,
        "registered_companies": registered_companies_queryset,
        "score": ceil(mean(estrellas)),
        "score_range": range(ceil(mean(estrellas))),
        "evaluaciones": evaluaciones,
        "range5": range(5),
    }

    return render(request, "evaluaciones/evaluaciones.html", context)

#____________________________________________________________
#Guia
def guide_view(request, *args, **kwargs):
    """
    Pagina de filtros
    """
    context = {
        "empresas": serializers.serialize("json", Empresa.objects.all()),
        "rutas": serializers.serialize("json", Ruta.objects.all()),
        "paradas": serializers.serialize("json", Parada.objects.all())
    }

    return render(request, "guide/guide.html", context)



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
