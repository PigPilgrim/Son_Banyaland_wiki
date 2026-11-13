# Empresas (SEPE)

El **SEPE** también es un proyecto de la Oficina. Cuando se termina, el **Funcionario** tiene el botón
**SEPE · Empresas**.

## Registrar una empresa

1. Ponle **nombre** (yunque).
2. Elige el **tipo**: taberna, restaurante, construcción, gasolinera, concesionario u otro. Si eliges *otro*, también eliges un bloque
   que será su dibujo en los menús.
3. Paga la **tasa** (va al Tesoro).
4. Haz **clic derecho al cofre o barril** que será **la caja** de la empresa.

--8<-- "_generado/sepe_numeros.md"

Cada jugador puede tener **una empresa**.

El **Concesionario** y la **Gasolinera** son dos tipos de empresa especiales: hay **uno de cada por aldea**, y el primero
que lo registra se lo queda. Al registrarlo recibes sus herramientas, y al cerrarlo queda libre para otro. Ver
[Vehículos](vehiculos.md).

Los **Restaurantes** necesitan una aldea de nivel 2 o más, y cada aldea puede tener unos pocos según su nivel. Cocinan,
tienen dependientes y reciben comensales: ver [Restaurantes](restaurantes.md).

El **Taller de runas** necesita una aldea de nivel 4. Su Encantador abre huecos en herramientas, armas y armaduras y
les engasta runas: ver [Taller de runas](runas.md).

## La caja

- **Solo la abren el dueño y sus empleados.** No se puede romper (ni por explosiones), y las tolvas no la vacían.
- Encima sale un cartel con el nombre, el tipo, el dueño, lo que hay en la caja y sus estrellas.
- Lo que hay en la caja es lo que **paga el impuesto a empresas**.
- Si Hacienda encuentra **Fichas marcadas** en la caja, la **precinta** unos días: nadie la puede abrir. Ver
  [Blanquear](crimen.md#blanquear).

## Dueños y empleados

- El **dueño** puede cambiar la caja, **contratar** (a vecinos conectados que no tengan empresa), **despedir** y
  **cerrar** la empresa.
- Un **empleado** puede dejar el trabajo cuando quiera.

## Estrellas y Empresa de la semana

Cada vecino puede **dar 1 estrella por semana** a una empresa que no sea la suya. La más votada de la semana es la
**Empresa de la semana**, y su dueño se lleva el premio (si no está conectado, al entrar).

En el SEPE también están la **Guía de empresas** (por estrellas) y **Las más ricas** (por lo que hay en la caja).

## El Ordenador y la investigación

Algunos tipos de empresa (de momento, el [Restaurante](restaurantes.md) y el [Taller de runas](runas.md)) tienen un **Ordenador**: una cabeza que te dan
al elegir la caja y que se pone **cerca de la caja**. Desde él se lleva la empresa.

- Solo lo **ponen, usan y quitan** el dueño y los empleados con permiso. No lo rompen explosiones, pistones ni agua.
- Si se rompe, el Ordenador **vuelve al dueño** (si no está conectado, al entrar). Si la empresa **cierra**, el
  Ordenador desaparece y se devuelve lo que corresponda (investigaciones a medias, escaparates, las chips que no
  cabían en la caja...).
- Tiene pestañas: **Estado**, **Investigar**, **Mejoras** y **Personal**, y cada tipo puede tener alguna más.
- Todo lo que cuesta chips desde el Ordenador se paga **de la caja**, y esas chips **desaparecen**.

### Permisos

El **dueño** puede hacerlo todo. A cada **empleado** el dueño le marca lo que puede hacer en **Personal → Permisos**.
Un empleado nuevo empieza así:

--8<-- "_generado/empresas_permisos.md"

### Investigar

- Los proyectos están ordenados por **categorías**. Algunos piden haber investigado otros antes, un **nivel de aldea** o
  alguna **mejora**.
- Cada proyecto cuesta **chips de la caja** y **materiales** que lleva encima quien lo empieza, y tarda un tiempo en
  **tiempo real** (sigue aunque no haya nadie conectado).
- Cuando termina, se avisa a todos los de la empresa.
- Lo investigado se puede **sacar en papel** desde el Ordenador (una copia de cada cosa a la vez).
- Algunos tipos tienen **especialización**: la primera categoría que investigáis es la principal, la segunda es más cara
  y más lenta, y las demás quedan bloqueadas. Cambiar cuesta chips y lo de la vieja se pierde.

### Proyectos que pueden salir mal

Algunos proyectos **no salen siempre**. En el Ordenador se ve la **probabilidad** (y de dónde sale cada parte), cuántos
intentos han fallado ya y cuántos faltan para el que sale **seguro**.

- Cada intento **cobra entero** y se sabe si ha salido bien **al terminar**.
- Cada fallo sube la probabilidad del siguiente intento, hasta un máximo.
- Los **catalizadores** (materiales que se marcan al empezar) suben la probabilidad, pero se gastan aunque salga mal.
  Algunas **mejoras** también la suben.
- Algunos proyectos pueden tener un **accidente** al fallar: un buen susto y la empresa **cerrada** unas horas.

--8<-- "_generado/empresas_investigacion.md"

### Mejoras, prestigio y personal

- Las **mejoras** van por niveles. Cada nivel cuesta chips (y a veces materiales) y puede pedir algo investigado antes.
- Los objetos de **prestigio** solo sirven para presumir.
- Los **dependientes** son aldeanos que venden lo que les carguéis al precio que pongáis, y lo que pagan va a la caja.
  Cobran un **sueldo diario** de la caja; si no hay chips, se ponen **en huelga** hasta que cobren. Para despedir a
  uno al que se le debe sueldo, primero se le paga de la caja.
- El **alquiler** se paga cada lunes de la caja. Si no hay bastantes chips, la empresa **cierra** hasta que las haya (el
  dueño puede pagarlo desde el Ordenador, en **Estado**).
- Mientras la empresa está **cerrada** (alquiler sin pagar, sin caja, sin Ordenador, precintada o tras un accidente) no
  se compran mejoras ni prestigio, no se contrata y no se cocina. Lo que ya estaba en una estación sí se puede sacar.
- Si el dueño cambia un precio mientras compras a un dependiente, la compra no se hace: te enseña el precio nuevo y
  vuelves a pulsar.
