# Minijuegos: regatas de barcos

## Ir y volver

- **Ida:** clic derecho al **Maestro de Juegos** de tu aldea (llega con el nivel 2). Te lleva al **lobby de
  minijuegos**. Si el admin ha cerrado los juegos, puedes pasear por el lobby igualmente.
- **Vuelta:** la brújula **Volver a casa** del hueco 9 de tu barra (en el lobby es al momento), o el botón
  **[Volver a la aldea]** del chat. Vuelves junto al Maestro de Juegos.

### Tu inventario y la mochila

Los minijuegos tienen **su propio inventario**, y en ellos **no pierdes nada al morir**:

- **Lo que llevabas se queda guardado en la aldea** y lo recuperas al volver.
- **Tus chips viajan en la mochila 🎒:** aparecen en el lobby (para abrir los [Cofres de Cabezas](#cabezas-coleccionables))
  y vuelven contigo con lo que te quede.
- Lo que saques de los cofres del lobby también vuelve contigo.
- Si al volver no te cabe todo, la mochila espera: **haz hueco** y aparece sola.

Los **premios** de los minijuegos (chips) se cobran **al volver a la aldea**, y pagan el
[impuesto sobre premios](hacienda.md#hacienda-los-impuestos) si tu aldea lo tiene.

## Próximamente: Cod Zombies

En el lobby ya está su portal, con el cartel **En Preparación**: todavía no se puede jugar.

## Las regatas

Se corre **en barco sobre hielo**. Se entra por el **portal azul del lobby**: eliges **pista** y **modo**.

### Las pistas

--8<-- "_generado/pistas.md"

### Los modos

#### Carrera (contra otros)

Te apuntas a la cola de una pista. Con **2 o más**, hay 30 segundos de espera y salís en parrilla con un
**semáforo de 5 luces**: cuando se apagan, ¡a correr! Salir antes es una **salida en falso** y suma segundos.
**El ganador se lleva chips.**

#### Clasificación (tú solo)

Una vuelta para coger velocidad y, al pasar por meta, empiezan las **vueltas lanzadas**: cuenta **tu mejor
vuelta**. Cada vuelta se divide en **3 sectores**, como en la Fórmula 1: **morado** = récord de la pista,
**verde** = tu mejor marca, **amarillo** = más lento.

#### Gestión (tú solo)

Una vuelta para coger velocidad y luego **5 vueltas cronometradas con neumáticos**. Es **obligatorio usar dos
neumáticos distintos** (o te penalizan), así que hay que **parar en boxes** al menos una vez. Cuenta el tiempo
total.

Si caes **al agua**, vuelves al último punto de control (en Clasificación, además, esa vuelta no cuenta). Para salir
de una regata en cualquier momento: `/puente barcos salir`.

--8<-- "_generado/regatas_numeros.md"

### Neumáticos (modo Gestión)

Cada neumático hace que **parte del hielo de la pista se vea azul, solo para ti**. El hielo azul es **más rápido y
más resbaladizo**. Con el uso el neumático se gasta, y el azul se va apagando.

--8<-- "_generado/neumaticos.md"

**No apures demasiado.** Pasado el **100 %** el neumático revienta: empiezan a salir **manchas de nieve** en la pista
(solo para ti), que frenan mucho. Poco después **pinchas seguro**: el barco se para, pulsas la tecla que salga y sigues
con aún más nieve hasta que cambies de neumático en boxes. El momento exacto cambia cada día y en cada pista.

### Boxes

La **zona amarilla** (con partículas) es el foso de boxes:

1. Entra y el barco se para.
2. **Si llevas un neumático en la mano**, te ponen ese; **con la mano libre**, eliges en un menú.
3. Ahora, **una tecla por rueda** (W, A, S, D o Espacio): pulsa la que salga. Si fallas o tardas, **la tuerca se
   atasca** y esa rueda se repite.

**El cronómetro no para**: cuanto más rápido pulses, más corta es la parada.

### El tiempo de cada día

Cada día puede **llover** o ser **de noche** en las pistas (igual para todos ese día). Con lluvia, los neumáticos
blandos y medios se gastan más.

### Rankings y premios de la semana

En el lobby está el **ranking** de cada pista: el **top 10** de Clasificación y de Gestión, de la semana y de
siempre. **Al acabar la semana**, el top 3 de cada pista y modo cobra chips, y **el 1.º se lleva la copa de la pista**
(una cabeza de trofeo; te llega cuando vuelves a la aldea).

Las regatas también cuentan para algunas [misiones del Pregonero](misiones.md).

## La Liga

La Liga se abre desde el menú del portal azul, con el **trofeo de abajo** (o con `/puente barcos liga`).

### Gran Premio del día

Cada día sale **un circuito y un modo al azar**: Clasificación o Gestión. Puedes intentarlo **todas las veces que
quieras hasta medianoche**, y cuenta tu **mejor tiempo**. No hace falta coincidir con nadie. A medianoche se reparten
los puntos:

--8<-- "_generado/liga_puntos.md"

### Escuderías

Hay **cuatro colores de barco**: blanco, rosa, mangrove y bambú. Eliges uno y corres con ese barco **en todos los
modos**, con cofre o sin él (es solo estética, y el cofre no se abre). Sin escudería no puntúas.

- **El primero que entra en un color le pone el nombre**, y el nombre sigue de una semana a otra.
- Puedes **cambiar de escudería o crear otra una vez por semana**, siempre antes de correr esa semana.

--8<-- "_generado/liga_numeros.md"

### Premios de la semana

El **lunes a las 00:00** se cierra la semana, se entregan los premios y los puntos vuelven a cero. Los trofeos te
llegan cuando vuelves a la aldea, y si no te caben, esperan.

--8<-- "_generado/liga_premios.md"

## Cabezas coleccionables

En el lobby hay **tres Cofres de Cabezas**. Cada uno se abre con **una chip** de su nivel y da **una cabeza** al azar
de cualquier set. Cuanto más alto el cofre, más fácil que salgan raras:

--8<-- "_generado/cofres_cabezas.md"

Cada cabeza lleva su nombre, su rareza y su número dentro del set (*Set · n.º 3 de 20*). Se pueden **poner como
decoración y quitar** sin perder nada.

!!! tip "Dios del Azar"
    Abrir estos cofres también da devoción si sigues al Dios del Azar. Ver [La Iglesia](iglesia.md).

### El álbum

Ábrelo con **Mayús + clic derecho al Maestro de Juegos**, con el botón del lobby o con `/puente album`. Una cabeza
cuenta para el álbum **en cuanto la llevas en el inventario**.

En el álbum ves cuánto llevas de cada set (las que te faltan salen como *???*) y el **top 5 de coleccionistas**.
**Al completar un set** te dan un premio (una vez por set):

??? note "Los 14 sets y sus premios"
    --8<-- "_generado/sets_cabezas.md"

### Reciclar repetidas

Desde el álbum puedes **cambiar cabezas repetidas por chips**:

--8<-- "_generado/reciclar_cabezas.md"
