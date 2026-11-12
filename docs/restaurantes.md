# Restaurantes

Un **Restaurante** es un tipo de [empresa del SEPE](empresas.md). Se cocinan platos con efectos, los vecinos
los compran a vuestros **dependientes** y cada día llegan **comensales** a la aldea que comen de vuestra **Carta** y
pagan en la caja. Cada restaurante elige una **rama** de cocina (marisquería, trattoria, heladería...) y la investiga.

!!! warning "⚠️ PENDIENTE"
    Los restaurantes están hechos pero **aún no han llegado al servidor** y están **sin probar en el juego**. Los precios, tiempos, efectos y comensales
    pueden cambiar.

## Restaurantes

### Abrir uno

1. Registra la empresa en el **SEPE** con el tipo **Restaurante**. Solo se puede si tu aldea tiene el nivel suficiente
   y no tiene ya todos los restaurantes que le tocan.
2. Elige la **caja**, como en cualquier empresa. Al hacerlo te dan el **Ordenador del Restaurante** y aparece
   **El Mayorista** al lado de la caja.
3. Pon el **Ordenador** cerca de la caja. Desde él se lleva todo el restaurante.

--8<-- "_generado/restaurantes_numeros.md"

!!! info "El alquiler"
    Cada lunes se pagan las chips del **alquiler** de la caja (desaparecen). Si no hay bastantes, el restaurante
    **cierra**: ni comensales ni dependientes hasta que haya chips en la caja. La primera semana (hasta el primer lunes)
    no se paga.

### El Ordenador

Solo lo usan **el dueño y los empleados**, y solo lo puede romper el dueño (no lo rompen explosiones, pistones ni agua).
Lo que **cuesta chips** (investigar, mejoras, contratar...) solo lo hace **el dueño**, y se paga **de la caja**.

- **Investigar:** las ramas, la conservación y las recetas que ya sabéis.
- **Mejoras:** la cocina, el comedor, el escaparate y los objetos de prestigio.
- **Personal:** contratar, mover y despedir dependientes, ponerles precios y mover al Mayorista.
- **Comedor:** dónde está el comedor y las cámaras frigoríficas.
- **Carta:** los platos que comen los comensales.
- **Estadísticas:** comensales, ventas y platos de la semana.

### Cocinar

Toda la cocina se hace con **bloques normales** cerca del Ordenador, y solo pueden usarla los del restaurante:

| Estación | Bloque | Qué se hace |
|---|---|---|
| **Tabla** | tronco descortezado | cada clic con la mano vacía, un corte |
| **Fogón** | caldero con agua y fuego debajo | cuenta el tiempo que pasa dentro |
| **Horno** | ahumador | cuenta el tiempo que pasa dentro |
| **Pase** | losa de cuarzo | emplatar |

1. **Los ingredientes van todos al principio**, a la estación del primer paso de la receta: clic derecho con cada uno
   (**Mayús** + clic: el montón entero).
2. Para sacarlos, clic con **cuencos** (uno por lote): salen **preparaciones**, que llevan apuntado lo que les habéis
   hecho.
3. Las preparaciones se llevan a la estación siguiente (clic con ellas) y se sacan con **Mayús + clic con la mano
   vacía**.
4. Al final, clic al **Pase** con las preparaciones: salen los platos y os devuelven los cuencos.

Con **Mayús + clic con la mano vacía** en una estación con ingredientes sueltos, la vaciáis y los recuperáis.
Una preparación **se echa a perder** si pasan 2 horas sin emplatarla.

!!! danger "Plato quemado"
    Si os **saltáis un paso**, los hacéis **en otro orden**, los ingredientes no son de ninguna receta que sepáis o las
    **proporciones** no cuadran, sale un **plato quemado**. No sirve para nada (y sienta fatal).

!!! tip "Las estrellas"
    Cada receta da un **margen** para cada paso («cortar 2-6 veces», «cocer 2-5 minutos»). Dentro del margen sale bien,
    pero **en cada margen hay un punto justo**: hay que probar. Pasarse, quedarse corto o hacer un paso de más baja las
    estrellas. Los platos de más estrellas tienen **efectos más largos** y los comensales **pagan más**.

--8<-- "_generado/restaurantes_estrellas.md"

Las recetas **no se publican**: salen en el Ordenador al investigarlas y se pueden **sacar en papel** para tenerlas a
mano.

### Los estilos: Rápida, Casera y Lujo

Cada rama tiene tres niveles, y cada uno es un estilo de cocina:

--8<-- "_generado/restaurantes_estilos.md"

### Investigar

- **Una investigación a la vez**, en **tiempo real** (sigue aunque no haya nadie conectado) y **para siempre**.
- Cuesta **chips de la caja** (desaparecen) y **materiales** que lleva el dueño encima.
- La **primera rama** que investigáis es la **principal** (sus tres niveles). Podéis tener una **secundaria**, que llega
  como mucho a Casera y es más cara y más lenta. **Las demás ramas quedan bloqueadas.**
- **Cambiar de rama** cuesta chips y la nueva **empieza de cero**.
- En la guía del SEPE vuestro restaurante sale con el nombre de la rama principal, por ejemplo **Restaurante ·
  Heladería**.

### Mejoras

--8<-- "_generado/restaurantes_mejoras.md"

Los objetos de **prestigio** son solo para presumir.

### El comedor

El dueño lo pone desde el Ordenador, donde esté de pie. **Comer sentado** dentro del comedor hace que los **efectos duren
un 25 % más**.

### Dependientes

Desde **Personal** el dueño **contrata dependientes** (cuántos, según la mejora Escaparate). Son aldeanos que venden
vuestros platos **a cualquiera**, al **precio que ponga el dueño**. Lo que pagan va **a la caja**.

- Los cargan el dueño y los empleados desde el Ordenador (**Escaparate**). Solo admiten platos de vuestras ramas.
- Mientras alguien cambia el escaparate, ese dependiente no vende.
- Cobran un **sueldo cada día** de la caja. Si no hay chips, se ponen **en huelga** hasta que cobren lo que se les debe.
- Se pueden **mover**: en Personal, **Moverlo**, y luego clic derecho en el suelo donde lo queráis.
- Al **despedir** a uno, te devuelve lo que tenía en el escaparate.

### Comensales

Cada día llegan **comensales** a cada aldea, repartidos a lo largo del día entre sus restaurantes abiertos. **Compiten:**
si en la aldea hay más restaurantes, os toca a menos. Cada uno come un plato de vuestra **Carta** y paga **en la caja**.
Lo que pagan depende del plato, sus **estrellas** y su **estilo**.

--8<-- "_generado/restaurantes_comensales.md"

!!! tip "Variad la Carta"
    Los comensales prefieren lo que **menos han comido hoy** en la aldea, y cada plato que vendéis vale un poco menos
    durante un día. Una Carta variada y con estrellas gana más que una llena del mismo plato.

Lo que hay en la caja paga el **impuesto a empresas**, como en cualquier empresa.

### El Mayorista

Al lado de la caja de cada Restaurante está **El Mayorista** (el dueño lo puede mover desde el Ordenador). Vende
**ingredientes** y las **bebidas comunes de la [Taberna](taberna.md)**, más baratas que en el Tabernero.

- Solo compran **dueños y empleados de Restaurantes y Tabernas** de la misma aldea (los de una Taberna, en cualquier
  Mayorista de su aldea).
- Cada cosa tiene un **tope de compras a la semana por empresa**.

--8<-- "_generado/restaurantes_mayorista.md"

## Ramas y platos

Hay cinco ramas. Cada una tiene sus platos de **Rápida**, **Casera** y **Lujo**:

--8<-- "_generado/restaurantes_ramas.md"

Los platos y lo que hacen con ★★★ (con más o menos estrellas duran más o menos):

--8<-- "_generado/restaurantes_platos.md"

!!! note "Helados"
    Los helados dan **Resistencia al fuego**. ⚠️ PENDIENTE: un efecto propio de **aguante del calor** (para el calor
    del desierto o del Nether) aún no existe.

Los platos de **Casera** también **bajan el alcohol y las toxinas** de las bebidas de la Taberna.

## Caducidad y conservación

**Todos los platos caducan.** Cuando caducan se convierten en **Plato podrido**, que da náuseas y hambre. En cada plato
pone hasta cuándo dura. La caducidad va por **horas enteras**, para que los platos iguales se apilen.

La caducidad solo se **para** en sitios de vuestro restaurante, y solo con la investigación de conservación:

--8<-- "_generado/restaurantes_conservacion.md"

- Una **cámara frigorífica** es un cofre o barril que el dueño registra desde el Ordenador (**Comedor**).
- Lo que está en una cámara, en la Carta o en un escaparate **con la Cámara investigada** no caduca. **Al sacarlo,
  sigue caducando** desde donde se quedó (se pierde algo menos de una hora, nunca se gana).
- **Sin Congelador, los helados se derriten** igual en la cámara.
- Fuera de todo eso (en tu inventario, en un cofre normal, en una tolva...) los platos **siguen caducando**.

## Grasa

Los platos tienen **grasa**. La comida **Rápida** sube tu barra de grasa (de 0 a 100) y la **Casera** la baja. También
baja sola con el tiempo.

--8<-- "_generado/restaurantes_grasa.md"

La grasa no hace nada en las **mazmorras**, los **minijuegos** ni la **cárcel**.
