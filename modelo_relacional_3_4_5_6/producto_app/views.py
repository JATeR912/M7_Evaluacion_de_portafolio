from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm

# Lista de productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto_app/lista_productos.html', {'productos': productos})

# Detalle de producto
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_app/detalle_producto.html', {'producto': producto})

# Crear producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'producto_app/crear_producto.html', {'form': form})

# Editar producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        messages.success(request, 'Producto actualizado correctamente.')
        return redirect('detalle_producto', pk=producto.pk)
    return render(request, 'producto_app/editar_producto.html', {'form': form, 'producto': producto})

# Eliminar producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.warning(request, 'Producto eliminado correctamente.')
        return redirect('lista_productos')
    return render(request, 'producto_app/eliminar_producto.html', {'producto': producto})