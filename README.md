# Tu Proyecto — afiliación eléctrica basada en datos

Base editorial y técnica para una web SEO en español sobre power stations, almacenamiento, energía solar portátil y accesorios eléctricos.

## Principios

- Resolver decisiones reales, no perseguir variaciones de keywords.
- Investigar primero y redactar después.
- Publicar datos rastreables y cálculos reproducibles.
- Recomendar por adecuación, seguridad y valor; nunca por comisión.
- Diseñar una experiencia rápida, limpia, accesible y “electrizante”.

## Flujo

```text
keywords → portfolio → research → scoring
         → página/comparativa → UI → SEO audit
```

Los procedimientos están en `.agents/skills/`. Las reglas transversales están en `AGENTS.md` y la identidad visual en `DESIGN.md`.

## Estructura

```text
.agents/skills/       Skills operativos y marcos de decisión
data/seo/             Mapa de keywords y auditorías
data/research/        Candidatos de producto
data/products/        Fichas canónicas investigadas
data/schemas/         Contratos JSON
src/components/       Componentes reutilizables
src/pages/            Páginas y rutas
src/styles/           Tokens y estilos
public/               Recursos públicos
```

## Primer ciclo recomendado

1. Definir audiencia, mercado y categorías iniciales.
2. Ejecutar `discover-keywords` para un solo cluster.
3. Seleccionar un portfolio inicial pequeño con `discover-products`.
4. Investigar entre cinco y diez productos centrales.
5. Puntuar por camper, camping o respaldo doméstico.
6. Construir una página de categoría, fichas esenciales y comparativas reales.
7. Auditar antes de indexar.

## Validación

Ejecuta desde la raíz:

```bash
python scripts/validate_project.py
```

El script comprueba los nueve skills, frontmatter, referencias, sintaxis JSON y los schemas cuando `jsonschema` está disponible.

## Estado inicial

El repositorio no presupone framework web. Antes de implementar, inspecciona el stack elegido y documenta comandos de instalación, desarrollo, build y test en este README. No añadas dependencias hasta que exista una necesidad concreta.

## Transparencia

El sitio debe publicar metodología, política de afiliación, correcciones, autores/revisores y fecha de actualización. Los enlaces afiliados pueden generar una comisión sin coste adicional para el usuario, pero esa relación no modifica scores ni conclusiones.
