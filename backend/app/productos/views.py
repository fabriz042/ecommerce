from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed, JsonResponse
from .models import Producto

def buscar_productos(request):
    if request.method != "GET":  # Verifica que sea GET
        return HttpResponseNotAllowed(["GET"])  # Retorna error 405 si no es GET

    limit = request.GET.get("limit", "20")  # Obtiene el parámetro 'limit'
    name_query = request.GET.get("name", "").strip()  # Obtiene el parámetro 'name' de la URL
    estado_query = request.GET.get("estado", "").strip()  # Obtiene el parámetro 'name' de la URL
    page_query = request.GET.get("page", "1").strip()  # Obtiene el parámetro 'name' de la URL

    # Obtiene los datos de la base ademas de la tabla estado
    productos = Producto.objects.select_related("estado").all().values(
        "nombre", "precio", "slug", "estado__nombre"
    )
    
    # Filtrar productos si se proporciona un parámetro de búsqueda
    if name_query:
        productos = productos.filter(nombre__icontains=name_query)

    if estado_query: # Verifica si 'estado_query' tiene un valor
        productos = productos.filter(estado=estado_query)  # Aplica el límite
    
    paginator = Paginator(productos, limit)
    page_query = int(page_query)
    productos_pagina = paginator.page(page_query)

    return JsonResponse({
        "count_total": paginator.count,
        "num_pages": paginator.num_pages,
        "current_page": page_query, 
        "productos": list(productos_pagina.object_list),
        "success": True,
    })




def slug_productos(request, slug):
    productos = Producto.objects.filter(slug=slug).values(
        "nombre", "images", "precio", "slug", "estado__nombre"
    )
    # Verificar si se encontraron productos
    if productos:
        return JsonResponse({"success": True, "data": list(productos), "message": "Productos encontrados"})
    else:
        return JsonResponse({"success": False, "error": "Producto no encontrado", "message": "No se encontraron productos para el slug especificado."}, status=404)

