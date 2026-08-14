# Instrucciones del proyecto

## Misión

Construir una referencia en español sobre power stations, baterías, placas solares, cargadores y otros productos eléctricos. El sitio ayuda a decidir mediante datos verificables, cálculos transparentes y comparaciones útiles. Los ingresos de afiliación sostienen el proyecto, pero nunca gobiernan la recomendación.

## Orden de trabajo

1. `discover-keywords`: decide qué intenciones y URLs merecen existir.
2. `discover-products`: selecciona un portfolio coherente.
3. `research-product`: crea fichas con evidencia por campo.
4. `score-product`: calcula scores por caso de uso.
5. `design-system`: protege tokens, accesibilidad e identidad.
6. `ui-builder`: implementa componentes y páginas.
7. `create-product-page` o `create-comparison`: construye contenido final.
8. `seo-audit`: bloquea publicación si existen fallos críticos.

Carga el `SKILL.md` correspondiente y las referencias que éste nombre antes de modificar datos o páginas.

## Reglas globales

- Intención de búsqueda antes que keyword exacta.
- Una intención principal por URL; no producir páginas casi duplicadas.
- Escribir para España y español natural salvo que la tarea indique otro mercado.
- Usar `null` para datos desconocidos. Nunca inferir una especificación sin marcarla como cálculo o hipótesis.
- Toda cifra técnica importante debe enlazar a evidencia con fuente y fecha.
- Separar hechos, métricas derivadas, pruebas propias y opinión editorial.
- No declarar pruebas de primera mano si no existieron.
- Precios, stock y promociones son instantáneas con mercado, moneda y fecha.
- Las comisiones y el EPC tienen peso cero en scoring y conclusiones.
- Enlaces afiliados identificados y con `rel="sponsored"`.
- Disclosure visible antes del primer enlace comercial.
- No usar urgencia falsa, ratings inventados ni schema que no coincida con contenido visible.
- Mantener URLs estables; no añadir años automáticamente.
- Implementar HTML semántico, mobile-first y accesible por teclado.

## Fuentes

Prioridad: manual/fabricante → certificación/regulador → prueba propia → distribuidor autorizado → review independiente → marketplace. Una fuente inferior no resuelve silenciosamente un conflicto con una superior.

## Datos

- `data/seo/keyword-map.json`: clusters, decisiones y arquitectura.
- `data/research/product-candidates.json`: candidatos y selección.
- `data/products/<product_id>.json`: ficha canónica y evidencia.
- `data/schemas/`: contratos que deben validar los JSON.

No cambiar nombres de campos sin migración y actualización de skills, schemas y consumidores.

## Diseño

Aplicar `DESIGN.md`: limpio, técnico y electrizante con acento lima controlado. La confianza y legibilidad prevalecen sobre glow, animación o densidad visual.

## Definición de terminado

Una tarea sólo está completa cuando los archivos validan, los enlaces internos tienen destino, las afirmaciones poseen evidencia, los estados `null` están contemplados, el build/tests disponibles pasan y `seo-audit` no deja bloqueadores.
