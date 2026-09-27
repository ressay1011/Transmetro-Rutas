import unittest

import transmetro as t


def estacion(clave):
    return ("estacion", clave, t.nombre(clave))


def alimentadora(clave):
    return ("alimentadora", clave, clave)


class TestConversionDeHoras(unittest.TestCase):

    def test_formatos_validos(self):
        self.assertEqual(t.a_minutos("7"), 420)
        self.assertEqual(t.a_minutos("7:05"), 425)
        self.assertEqual(t.a_minutos("7.05"), 425)
        self.assertEqual(t.a_minutos("07:00"), 420)
        self.assertEqual(t.a_minutos("0700"), 420)
        self.assertEqual(t.a_minutos(" 23:59 "), 1439)

    def test_formatos_invalidos(self):
        for texto in ["", "abc", "24:00", "7:60", "7.3.0", "700", "-1"]:
            with self.subTest(texto=texto):
                self.assertIsNone(t.a_minutos(texto))

    def test_hhmm(self):
        self.assertEqual(t.hhmm(0), "00:00")
        self.assertEqual(t.hhmm(425), "07:05")
        self.assertEqual(t.hhmm(1439), "23:59")


class TestDisponibilidad(unittest.TestCase):

    def test_ruta_suspendida_no_opera(self):
        self.assertFalse(t.esta_disponible("B10", 400))

    def test_ruta_dentro_y_fuera_de_franja(self):
        self.assertTrue(t.esta_disponible("B1", 300))
        self.assertFalse(t.esta_disponible("B1", 299))
        self.assertFalse(t.esta_disponible("B1", 1102))

    def test_ruta_con_dos_franjas(self):
        self.assertTrue(t.esta_disponible("R10", 400))
        self.assertFalse(t.esta_disponible("R10", 700))
        self.assertTrue(t.esta_disponible("R10", 1000))


class TestDatos(unittest.TestCase):

    def test_paradas_existen(self):
        for clave, ruta in t.RUTAS.items():
            for parada in ruta["paradas"]:
                with self.subTest(ruta=clave, parada=parada):
                    self.assertIn(parada, t.ESTACIONES)

    def test_estaciones_de_alimentadoras_existen(self):
        for clave, info in t.ALIMENTADORAS.items():
            for estacion_clave in info["estaciones"]:
                with self.subTest(alimentadora=clave):
                    self.assertIn(estacion_clave, t.ESTACIONES)

    def test_todas_las_rutas_tienen_costo_calculable(self):
        for clave, ruta in t.RUTAS.items():
            with self.subTest(ruta=clave):
                costo, paradas = t.costo_tramo(clave, ruta["paradas"][0], ruta["paradas"][-1])
                self.assertGreater(costo, 0)
                self.assertEqual(paradas, len(ruta["paradas"]) - 1)


class TestResolverViaje(unittest.TestCase):

    def test_todas_las_estaciones_se_conectan_a_mediodia(self):
        for a in t.ESTACIONES:
            for b in t.ESTACIONES:
                if a != b:
                    with self.subTest(origen=a, destino=b):
                        mejor, _ = t.resolver_viaje(estacion(a), estacion(b), 720)
                        self.assertIsNotNone(mejor)

    def test_expreso_gana_en_su_franja(self):
        mejor, _ = t.resolver_viaje(estacion("portal_soledad"), estacion("joe_arroyo"), 420)
        self.assertEqual(mejor["etiqueta"], ("R10",))

    def test_corriente_fuera_de_la_franja_del_expreso(self):
        mejor, _ = t.resolver_viaje(estacion("portal_soledad"), estacion("joe_arroyo"), 720)
        self.assertEqual(mejor["etiqueta"], ("R1",))

    def test_sin_servicio_de_madrugada(self):
        mejor, mensaje = t.resolver_viaje(estacion("la_ocho"), estacion("atlantico"), 180)
        self.assertIsNone(mejor)
        self.assertIn("no hay servicio", mensaje)

    def test_sin_servicio_aunque_compartan_estacion(self):
        mejor, mensaje = t.resolver_viaje(
            estacion("la_ocho"), alimentadora("A1-2 Carrera Ocho"), 180)
        self.assertIsNone(mejor)
        self.assertIn("no hay servicio", mensaje)

    def test_alimentadora_suspendida(self):
        mejor, mensaje = t.resolver_viaje(
            alimentadora("A3-4 Villa Sol"), estacion("la_ocho"), 720)
        self.assertIsNone(mejor)
        self.assertIn("suspendida", mensaje)

    def test_alimentadora_sin_transbordo(self):
        mejor, mensaje = t.resolver_viaje(
            estacion("la_ocho"), alimentadora("Ruta Chévere"), 720)
        self.assertIsNone(mejor)
        self.assertIn("no tiene punto de transbordo", mensaje)

    def test_viaje_con_alimentadoras_en_ambos_extremos(self):
        mejor, _ = t.resolver_viaje(
            alimentadora("A5-2 Las Moras"), alimentadora("A7-1 Miramar"), 720)
        self.assertEqual(mejor["alim_origen"], "A5-2 Las Moras")
        self.assertEqual(mejor["alim_destino"], "A7-1 Miramar")
        self.assertEqual(mejor["transbordos"], len(mejor["troncal"]) + 1)

    def test_resultado_determinista(self):
        a = t.resolver_viaje(estacion("pacho_galan"), estacion("la_catedral"), 480)
        b = t.resolver_viaje(estacion("pacho_galan"), estacion("la_catedral"), 480)
        self.assertEqual(a[0]["orden"], b[0]["orden"])


class TestBusquedaPorBarrio(unittest.TestCase):

    def numero(self, clave):
        for i, (_principal, _extra, punto) in enumerate(t.OPCIONES, start=1):
            if punto[1] == clave:
                return i
        raise KeyError(clave)

    def test_ignora_tildes_y_mayusculas(self):
        self.assertEqual(t.buscar_opciones("EXITO"), t.buscar_opciones("éxito"))
        self.assertIn(self.numero("A3-1 Villa Katanga"), t.buscar_opciones("exito"))

    def test_encuentra_estaciones_y_alimentadoras(self):
        encontrados = t.buscar_opciones("miramar")
        self.assertIn(self.numero("A7-1 Miramar"), encontrados)
        self.assertIn(self.numero("la_ocho"), t.buscar_opciones("la ocho"))

    def test_sin_coincidencias(self):
        self.assertEqual(t.buscar_opciones("xyzq"), [])

    def test_no_quedan_barrios_mal_extraidos(self):
        for clave, info in t.ALIMENTADORAS.items():
            for barrio in info["barrios"]:
                with self.subTest(alimentadora=clave, barrio=barrio):
                    self.assertNotEqual(barrio, "Urb")
                    self.assertNotIn(":", barrio)
                    self.assertFalse(barrio.startswith(("como ", "de ")))


if __name__ == "__main__":
    unittest.main()
