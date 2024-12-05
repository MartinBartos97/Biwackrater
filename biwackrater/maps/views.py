from django.template import loader
from django.http import HttpResponse
from folium import Map

# Create your views here.

class MapView:
    def init_maps(request):
        m = Map(location=[50.0755, 14.43784])
        template = loader.get_template('maps/homepage.html')
        context = {'my_map': m._repr_html_()}
        return HttpResponse(template.render(context, request))
