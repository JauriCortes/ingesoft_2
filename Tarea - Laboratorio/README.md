# Tarea APIs - Jauri

Exploración de APIs públicas usando Postman, comparando REST y GraphQL con datos de países del mundo.

---

## Parte 1 — REST API

**API elegida:** REST Countries `https://restcountries.com/v3.1`

### ¿Por qué esta API?
Tiene múltiples endpoints, permite filtrar por nombre, región, idioma y código de país, y sus respuestas tienen estructura rica con datos anidados — lo que permite escribir tests automáticos con sentido.

### ¿Qué datos devuelve?
Información detallada de países: nombre, capital, población, región, idiomas, moneda, bandera, código de país, entre otros.

### ¿Usa token?
No. Es una API pública sin autenticación.

### Requests realizados

| # | Nombre | Método | Endpoint |
|---|---|---|---|
| 1 | GET - Todos los países | GET | `/all?fields=name,capital,population,region,flags` |
| 2 | GET - País por código | GET | `/alpha/{{country_code}}` |
| 3 | GET - Países por región | GET | `/region/americas` |
| 4 | GET - País por nombre | GET | `/name/colombia` |
| 5 | GET - Países por idioma | GET | `/lang/spanish` |

### Códigos de estado recibidos
Todos los requests devolvieron **200 OK**.

### Variables de colección

| Variable | Valor |
|---|---|
| `base_url` | `https://restcountries.com/v3.1` |
| `country_code` | `CO` |

### ¿Qué aprendiste diferente a JSONPlaceholder?

- REST Countries es una API real con datos reales, no una API de práctica. Por eso es de solo lectura — no tiene POST, PUT ni DELETE.
- La API limita los campos que puedes pedir en el endpoint `/all`, obligando a especificar `fields` explícitamente. JSONPlaceholder no tiene ese tipo de restricciones.
- Las respuestas tienen estructura más compleja y anidada. Por ejemplo, el campo `name` contiene a su vez `common`, `official` y `nativeName`.

---

## Parte 2 — GraphQL

**API elegida:** Countries GraphQL `https://countries.trevorblades.com/graphql`

### Requests realizados

| # | Nombre | Descripción |
|---|---|---|
| 1 | Todos los continentes | Lista todos los continentes con código y nombre |
| 2 | País por código | Filtra un país específico por argumento `code: "CO"` |
| 3 | Países con idiomas y continente | Query anidada — trae países con sus idiomas y continente relacionados |
| 4 | Países de Sudamérica | Filtra países por continente `filter: { continent: { eq: "SA" } }` |
| 5 | Idiomas | Lista todos los idiomas disponibles con código, nombre y dirección |

### ¿Qué diferencia encontraste vs REST?

- En REST se usaron 5 endpoints distintos. En GraphQL se usó **un solo endpoint** para todas las queries.
- En REST la API decidía qué campos devolver. En GraphQL se especificó exactamente qué campos se necesitaban en cada query.
- En REST obtener datos relacionados (país + idiomas + continente) requeriría múltiples requests. En GraphQL se resolvió en una sola query anidada.

### ¿Cuántos requests REST necesitarías para reemplazar tu query más compleja?

La query más compleja fue la de países con idiomas y continente. En REST serían mínimo **3 requests**:
1. GET todos los países
2. GET continente por país
3. GET idiomas por país

### ¿En qué proyecto real usarías GraphQL?

En una app móvil de viajes que muestra información de países: nombre, capital, moneda, idioma y clima. Con REST habría que hacer varios requests para armar cada pantalla, recibiendo además campos innecesarios. Con GraphQL se hace una sola query pidiendo exactamente lo que la pantalla necesita, reduciendo tiempo de carga y consumo de datos.

---

## Entregables

- `tarea_rest_countries_jauri.json` — Colección REST exportada de Postman
- `tarea_graphql_jauri.json` — Colección GraphQL exportada de Postman
- Capturas de pantalla de cada request en `/capturas`
- Documento de respuestas REST
- Documento de respuestas GraphQL
