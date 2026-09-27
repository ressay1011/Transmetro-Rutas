# Sistema Inteligente de Rutas - Transmetro Barranquilla

## Qué Hace:

Pregunta por consola (con un menu numerado de estaciones y rutas
alimentadoras) desde donde viajas, hacia donde vas y (opcionalmente)
a que hora, y busca la MEJOR RUTA dentro del sistema de transporte
masivo Transmetro, explicando el viaje paso a paso.

## Como Se Usa:

1. Guarda este archivo como transmetro.py y ejecutalo asi:
   python transmetro.py
2. Elige el ORIGEN y el DESTINO por su NUMERO en el menu (estaciones de
   la troncal y rutas alimentadoras) y despues la hora en formato HH:MM
   (si presionas Enter se usa la hora actual).
3. Escribe 0 para terminar.

## Reglas Condicionales Que Aplica El Programa:

1. REGLA 1: Si la ruta esta SUSPENDIDA -> no opera nunca.
2. REGLA 2: Si la hora no cae en una franja de la ruta -> no opera ahora.
3. REGLA 3: El bus solo avanza en SU sentido (solo paradas posteriores).
4. REGLA 4: Si la ruta es EXPRESS -> se salta estaciones y no paga el costo
   de detenerse en ellas, asi que el viaje resulta mas corto. Los expresos
   solo operan en sus franjas (casi todas en hora pico).
5. REGLA 5: Si el origen/destino elegido es una ESTACION -> se viaja por
   la red troncal.
6. REGLA 6: Si es una ALIMENTADORA -> el primer y/o el ultimo tramo del
   viaje se hacen en alimentadora (llega a los barrios).
7. REGLA 7: Si hay varias opciones -> gana la de MENOR TIEMPO; si empatan,
   la de menos transbordos; luego menos paradas; luego orden
   alfabetico (asi el resultado es siempre el mismo).
8. REGLA 8: Si ninguna opcion sirve -> informa "sin servicio" claramente.

## DATOS:

sitio oficial transmetro.gov.co / API apiwebtm.com (extraidos el
2026-09-24). Se asume un dia LABORAL (lunes a viernes). Los tiempos estan
en "ute" (unidad de tiempo estimado; 1 ute ~ 1 minuto) y sirven para
COMPARAR rutas, no son un cronometro real.

============================================================================

## Fuente y atribución

Datos públicos de **Transmetro S.A.S.** (Barranquilla, Colombia) publicados en
`transmetro.gov.co`; uso académico/educativo. Extracción: 2026-09-24
