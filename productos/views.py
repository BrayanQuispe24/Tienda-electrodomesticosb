# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection

@api_view(['POST'])
def crear_producto(request):
    try:
        descripcion = request.data.get('descripcion')
        estado = request.data.get('estado')
        marca_id = request.data.get('marca_id')
        categoria_id = request.data.get('categoria_id')

        with connection.cursor() as cursor:
            cursor.execute("CALL crear_producto(%s, %s, %s, %s)", [descripcion, estado, marca_id, categoria_id])
        return Response({"detail": "Producto creado correctamente."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def actualizar_producto(request):
    try:
        id = request.data.get('id')
        descripcion = request.data.get('descripcion')
        estado = request.data.get('estado')
        marca_id = request.data.get('marca_id')
        categoria_id = request.data.get('categoria_id')

        with connection.cursor() as cursor:
            cursor.execute("CALL actualizar_producto(%s, %s, %s, %s, %s)", [id, descripcion, estado, marca_id, categoria_id])
        return Response({"detail": "Producto actualizado correctamente."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def obtener_productos(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM obtener_productos()")
            columnas = [col[0] for col in cursor.description]
            datos = [dict(zip(columnas, row)) for row in cursor.fetchall()]
        return Response(datos, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def obtener_producto(request, id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM obtener_producto(%s)", [id])
            columnas = [col[0] for col in cursor.description]
            fila = cursor.fetchone()
            if fila:
                data = dict(zip(columnas, fila))
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def obtener_detalles_producto(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM obtener_detalles_producto()")
            columnas = [col[0] for col in cursor.description]
            resultados = [
                dict(zip(columnas, fila))
                for fila in cursor.fetchall()
            ]

        return Response(resultados, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
