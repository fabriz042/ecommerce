from django.test import TestCase
from app.productos.models import Producto, Estado  # Asegúrate de importar bien

class ProductoTestCase(TestCase):
    def setUp(self):
        estado = Estado.objects.create(nombre="En stock")
        Producto.objects.create(
            nombre="Producto Test",
            precio=100,
            slug="producto-test",
            estado=estado,
            images=1
        )

    def test_listar_todos_productos(self):
        response = self.client.get('/api/busqueda/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreaterEqual(data['count_total'], 1)
        self.assertEqual(data['productos'][0]['nombre'], 'Producto Test')
