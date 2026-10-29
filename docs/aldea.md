# Cómo crece la aldea

Cada aldea empieza siendo **un Ayuntamiento con su Secretario** y va subiendo de nivel, del 1 al 5, gracias a lo que
le entregan los vecinos. Cada nivel trae aldeanos nuevos, tiendas nuevas y una zona segura más grande.

## El encargo del Secretario

El Secretario siempre tiene **un encargo** con lo que necesita la aldea para el siguiente nivel. Se entrega
**como si fuera una tienda**: le das el lote (por ejemplo, 64 troncos de roble) y te da un *Recibo de la aldea*. Cada
lote se puede entregar unas cuantas veces (las *entregas* de la tabla). Arriba de la pantalla, una barra muestra
cuánto falta.

Cualquiera puede entregar: **la aldea es de todos**.

!!! info "Algunos niveles necesitan además un edificio"
    En los niveles con algo en la columna *Además hace falta*, no basta con el encargo: los vecinos tienen que
    **construir ese edificio** y el admin tiene que darlo por bueno. Hasta entonces el nivel no sube.

## Los niveles

--8<-- "_generado/niveles.md"

Los aldeanos de la columna *Llegan* aparecen solos en cuanto sube el nivel. Lo que hace cada uno está en
[Los aldeanos y sus tiendas](aldeanos.md).

## Zona segura

Alrededor del centro de cada aldea hay una **zona segura**, y se hace más grande con cada nivel:

--8<-- "_generado/zona_segura.md"

**La zona segura protege de los monstruos:** los que aparecen solos dentro de ella desaparecen. Ojo: los que salen
de **spawners** o en las **oleadas de un asedio** sí pueden entrar.

## Ser vecino de una aldea

Para ser **ciudadano** de una aldea, habla con su Secretario: si aún no eres de esa aldea, te pregunta si quieres
serlo. **Solo puedes cambiar de aldea una vez cada 7 días.**

## Fundar una aldea nueva

En el mundo caben **4 aldeas** como mucho. Para fundar una nueva:

1. Compra una **Carta de fundación** en el Secretario (sale cuando su aldea tiene nivel 3 o más; ver
   [su tienda](aldeanos.md#secretario)).
2. Ve al **mundo normal** (no vale el Nether ni las mazmorras), a **500 bloques o más** del centro de cualquier otra
   aldea.
3. Haz **clic derecho con la carta** y confirma.

Te conviertes en su **primer ciudadano** y en su **Alcalde provisional** (hasta que haya elecciones). La primera aldea
del servidor se anunció a todos; las demás no: **nadie sabrá que la has fundado tú**, a los demás solo les llega un
rumor, sin pistas de dónde está.

## La Campana

Cada aldea tiene una **Campana** en su centro. Está protegida: no se puede romper, ni quitarle el bloque de debajo, ni
moverla con pistones, ni volarla.

Pero en un **asedio** (los organiza el admin) los monstruos van a por ella. **Si la Campana cae**:

- **Todos los aldeanos cierran su tienda** ("Cerrado por miedo") y el Guía no lleva a nadie a las mazmorras.
- El Secretario cambia su encargo por el de **reparar la Campana**. Al completarlo, todo vuelve a abrir.

Lo que pide para repararla depende del nivel de la aldea:

--8<-- "_generado/campana.md"
