# Regatas y Liga

## Las regatas

Se corre **en barco sobre hielo**. Se entra por el **portal azul del lobby**: eliges **pista** y **modo**, **en
solitario** (contra el reloj) u **online** (contra otros jugadores a la vez).

### Las pistas

--8<-- "_generado/pistas.md"

### Los modos

Hay tres modos, y cada uno se puede jugar **en solitario** o **online**.

#### Clasificación

Una vuelta para coger velocidad y, al pasar por meta, empiezan las **vueltas lanzadas**: cuenta **tu mejor
vuelta**. Cada vuelta se divide en **3 sectores**, como en la Fórmula 1: **morado** = récord de la pista,
**verde** = tu mejor marca, **amarillo** = más lento.

**Online:** todos a la vez en pista durante **5 minutos**. Cuando se acaba el tiempo puedes terminar la vuelta que
llevas. **Gana la mejor vuelta.**

#### 3 vueltas

**En solitario:** una vuelta para coger velocidad y luego **3 vueltas seguidas** contra el reloj. Cuenta el tiempo
total y tiene **su propio ranking**.

**Online:** una **carrera a 3 vueltas** saliendo en parrilla con un **semáforo de 5 luces**: cuando se apagan, ¡a
correr! Salir antes es una **salida en falso** y suma segundos. **Gana el primero en llegar.**

#### Gestión

Una vuelta para coger velocidad y luego **5 vueltas cronometradas con neumáticos**. Es **obligatorio usar dos
neumáticos distintos** (o te penalizan), así que hay que **parar en boxes** al menos una vez. Cuenta el tiempo
total.

**Online:** la misma carrera de 5 vueltas con neumáticos y boxes, todos a la vez y saliendo con el semáforo. **Gana
el primero en llegar**, y tu tiempo también cuenta para el ranking de Gestión.

#### Partidas online

1. En el menú de la pista, elige un modo **online** (en Gestión, también tu neumático de salida) y entras directamente.
2. Los demás la ven en el mismo menú (**Unirse**) y les sale un aviso en el chat para entrar. Caben tantos como
   huecos tenga la parrilla.
3. **Mientras esperáis, podéis dar vueltas** por la pista libremente (sin cronómetro).
4. **No empieza sola:** quien la creó pulsa **[Empezar]** en el chat cuando quiera, **aunque esté solo**. Hay
   10 segundos y el semáforo; a partir de ahí ya no entra nadie más.
5. Si en **5 minutos** no la ha arrancado, puede pulsar **[Empezar]** cualquiera de la sala. Si quien la creó se va,
   el botón pasa al siguiente.

En cada pista hay **una partida online a la vez**; cuando empieza, los que estaban en solitario en esa pista
vuelven al lobby. **El ganador se lleva chips** si corrían **2 o más**, con un **tope de premios al día** (sumando
todos los modos). Si corres solo, tus tiempos cuentan igual para los rankings.

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

### Rankings y premios de la semana

En el lobby está el **ranking** de cada pista: el **top 10** de Clasificación, 3 vueltas y Gestión, de la semana
y de siempre. **Al acabar la semana**, el top 3 de cada pista y modo cobra chips, y **el 1.º se lleva la copa de la pista**
(una cabeza de trofeo; te llega cuando vuelves a la aldea).

Las regatas también cuentan para algunas [misiones del Pregonero](misiones.md).

## La Liga

La Liga se abre desde el menú del portal azul, con el **trofeo del centro** (o con `/puente barcos liga`).

Encima del portal hay un **cartel con cómo va la Liga**: el Gran Premio de hoy, el **top 10 de pilotos** de la semana
(de arriba abajo, del color de su escudería) y los puntos de cada escudería. Los récords de cada pista están en el
menú del portal, en **Ranking**.

### Gran Premio del día

Cada día sale **un circuito y un modo al azar**: Clasificación o Gestión. Tienes **3 intentos hasta medianoche**, y
cuenta tu **mejor tiempo**. No hace falta coincidir con nadie.

- Solo cuentan los intentos que empiezas **desde el menú de la Liga**. Lo que corras por tu cuenta en esa pista no vale,
  así que puedes entrenar sin gastar nada.
- Primero das una **vuelta de formación**. **Al cruzar la meta se gasta el intento**, y si abandonas o caes al agua no se
  devuelve.
- En Clasificación, cada intento es **una sola vuelta**.
- En Gestión, **cada sector se compara con tu mejor de los intentos de hoy**: si hiciste 30 s y ahora haces 20 s, verás
  **-10**.

A medianoche se reparten los puntos. El chat lo avisa en el mensaje «🕛 ¡Nuevo día!», junto con las misiones
nuevas: sale el podio de ayer y el Gran Premio de hoy.

--8<-- "_generado/liga_puntos.md"

### Escuderías

Hay **cuatro colores de barco** fijos: blanco, rosa, mangrove y bambú. Además puedes **crear una escudería nueva** con
otro barco: roble, abeto, abedul, jungla, acacia o roble oscuro. Corres con el barco de tu escudería **en todos los
modos**, con cofre o sin él (es solo estética, y el cofre no se abre). Sin escudería no puedes correr el Gran Premio.

- **El primero que entra en un color le pone el nombre**, y te quedas en tu escudería de una semana a otra.
- Puedes cambiarte a otra **hasta gastar tu primer intento de la semana**; después, ya el lunes.
- Una escudería en la que **nadie corre el Gran Premio durante 2 semanas seguidas desaparece**, y sus pilotos quedan
  libres para elegir otra.

--8<-- "_generado/liga_numeros.md"

### Premios de la semana

El **lunes a las 00:00** se cierra la semana, se entregan los premios y los puntos vuelven a cero. Los trofeos te
llegan cuando vuelves a la aldea, y si no te caben, esperan.

--8<-- "_generado/liga_premios.md"
