# Craft of Clans

Un minijuego aparte del juego normal: tienes tu propio **fortín**, lo llenas de edificios y los vas mejorando. Las
mejoras tardan **tiempo de verdad** (minutos al principio, horas después) y siguen avanzando aunque no estés conectado.

!!! warning "⚠️ PENDIENTE"
    Está en pruebas: ya se puede construir, entrenar tropas y **atacar los fortines de los demás**, pero los números
    de abajo (vidas, daños, botín, trofeos...) pueden cambiar cuando se pruebe más.

## Entrar y salir

- Se entra desde el **lobby de minijuegos** (ver [Ir y volver](minijuegos.md#ir-y-volver)), por su portal o con
  `/puente clanes`.
- Como en los demás minijuegos, se juega en **modo aventura** y con el **inventario del lobby**: lo que llevabas se
  queda en la [mochila](minijuegos.md#tu-inventario-y-la-mochila) y vuelve al salir. Dentro no recibes daño ni pasas
  hambre.
- Para salir, la **puerta** del hueco 9 de tu barra: vuelves al lobby.

La primera vez que entras te dan una **parcela de 56×56** con una valla alrededor. Es solo tuya. (Las parcelas de
antes eran de 48×48: crecieron solas por el este y por el sur, sin mover nada de lo que había.)

## Tu barra

| Hueco | Objeto | Para qué |
|---|---|---|
| 1 | **Atacar** | Buscar un fortín para [atacar](#atacar) |
| 2 | **Guerra** | Los [ataques de guerra](#guerra), cuando tu aldea está en guerra |
| 3 | **Plano** | Construir un edificio nuevo |
| 4 | **Decorar** | Bloques de decoración |
| 5 | **Mi fortín** | Tus recursos, tus constructores, tu **ejército**, tus **trofeos**, tu **registro** de ataques, la semana y **Recoger todo** |
| 9 | **Salir al lobby** | Volver al lobby de minijuegos |

**Haz clic a cualquier edificio** para ver su menú: **Mejorar**, **Recoger** (aserraderos, canteras y granjas),
**Entrenar tropas** (cuartel), **Mejorar tropas y hechizos** (Herrería), **Cocer hechizos** (Caldero) y **Mover**. Ahí también se ve su **vida** (la que tiene cuando le atacan). Encima de cada
edificio sale su nivel y, si está en obras, cuánto le queda (los muros no llevan cartel).

## Recursos

Hay tres: 🪵 **Madera**, 🪨 **Piedra** y 🌾 **Trigo**. Son solo de este juego: **ni entran ni salen** del juego normal.

- Los producen los **aserraderos** (madera), las **canteras** (piedra) y las **granjas** (trigo) poco a poco, también
  sin estar tú. Cada uno acumula hasta un tope: **recógelo** antes de que se llene, o deja de producir.
- Cuánto puedes tener lo marcan el **Torreón** y los **almacenes** (el trigo, los **graneros**). Lo que no cabe se
  queda esperando donde se produjo.
- La madera y la piedra son para construir; el trigo, para **entrenar tropas**.

--8<-- "_generado/clanes_inicio.md"

## Construir

1. En el **Plano**, elige el edificio.
2. Con él en la mano, **mira al suelo**: sale su contorno, **verde** si cabe y **rojo** si no. Hay que dejar un
   bloque libre con los demás edificios y con la valla (los **muros** sí pueden ir pegados a lo que sea).
3. **Clic derecho** para ponerlo (se paga en ese momento). **Clic izquierdo** o **Q** para cancelar.

Cada **Cabaña** es un **constructor**: hace **una obra a la vez** (construir o mejorar). Mientras se mejora un
aserradero o una cantera, no produce. **Mover** un edificio es gratis y al momento.

--8<-- "_generado/clanes_edificios.md"

## Mejorar

Ningún edificio puede tener más nivel que el **Torreón**, y el Torreón sube **poco a poco**: cada **lunes** (hora de
España) se puede subir un nivel más.

--8<-- "_generado/clanes_semanas.md"

### Torreón

--8<-- "_generado/clanes_torreon.md"

### Aserradero y Cantera

El aserradero se paga con piedra y la cantera con madera.

--8<-- "_generado/clanes_generadores.md"

### Almacenes

Cada almacén se paga con el **otro** recurso.

--8<-- "_generado/clanes_almacenes.md"

### Granja y Granero

La granja se paga con madera y el granero con piedra. El Torreón también guarda trigo.

--8<-- "_generado/clanes_granjas.md"

### Cabañas (constructores)

--8<-- "_generado/clanes_cabanas.md"

### Cuántos edificios puedes tener

--8<-- "_generado/clanes_cuantos.md"

## Herrería, Caldero y altares

Tres edificios nuevos para cuando el fortín ya está avanzado:

- **Herrería** (desde el Torreón 4): mejora tus **tropas** y tus **hechizos**, de uno en uno. Su nivel marca hasta
  dónde.
- **Caldero** (desde el Torreón 5): prepara **hechizos** para los ataques. Tiene pocos huecos y cada hechizo tarda en
  hacerse.
- **Altares** (uno por héroe): en cada uno vive un **héroe** que te acompaña en los ataques y luego descansa un rato.

!!! warning "⚠️ PENDIENTE"
    La Herrería y el Caldero ya funcionan. Los altares de momento solo se pueden **construir**: los héroes llegarán en
    las próximas pruebas (ver [Pendientes](pendientes.md)).

### Herrería

Clic a la Herrería → **Mejorar tropas y hechizos**. Sale cada tropa (y abajo, cada hechizo) con su nivel, lo que gana
en el siguiente y lo que cuesta.

- Mejora **una cosa a la vez**, con tiempo de verdad (también sin estar tú). No usa constructor, pero mientras
  mejora algo **no se puede mejorar la Herrería**.
- Se paga con **trigo** al empezar.
- Cada nivel de tropa pide la **Herrería** a cierto nivel, y la tropa tiene que estar desbloqueada en el cuartel.
- Cada nivel da un **14 % más de vida y de daño** (al Hada, de cura). Las tropas que ya tienes entrenadas también
  suben: cuenta el nivel que tengas al atacar.

--8<-- "_generado/clanes_herreria.md"

#### Niveles de cada tropa

--8<-- "_generado/clanes_tropas_niveles.md"

### Caldero

Clic al Caldero → **Cocer hechizos**.

- Cada hechizo ocupa **un hueco**, ya esté cocido o esperando en la cola. Hay **pocos huecos**: los da el nivel del
  Caldero.
- Se cuecen **de uno en uno**, en orden, con tiempo de verdad (también sin estar tú). Se pagan con **trigo** al
  encargarlos; si cancelas uno de la cola, te devuelve el trigo.
- Los cocidos esperan a tu próximo ataque. Si quieres hacer sitio, puedes **tirar** uno (no se devuelve).
- Cada nivel del Caldero desbloquea un hechizo nuevo.

--8<-- "_generado/clanes_caldero_huecos.md"

--8<-- "_generado/clanes_caldero.md"

#### Hechizos

--8<-- "_generado/clanes_hechizos.md"

Los hechizos suben de nivel en la **Herrería**: cada nivel da un **20 % más** de efecto y **1 segundo más** de
duración.

--8<-- "_generado/clanes_hechizos_niveles.md"

### Altares

Cada altar se construye una vez y no tiene más niveles.

--8<-- "_generado/clanes_altares.md"

## Ejército

Las tropas se entrenan en el **Cuartel** con trigo y esperan en los **Campamentos**.

- En el cuartel (clic → **Entrenar tropas**): **clic** en una tropa para encargar una; **Mayús + clic**, cinco. El
  trigo se paga al encargarla.
- Se entrenan **de una en una**, en orden y con tiempo de verdad, también sin estar tú. Para **cancelar** una, haz
  clic en ella en la cola de abajo: te devuelve el trigo (lo que quepa en tus graneros).
- Cada tropa **ocupa** sitio. Si tus campamentos están llenos, no se puede encargar más y la cola espera.
- En **Mi fortín → Ejército** ves tus tropas y puedes **despedir** alguna para hacer sitio (el trigo no se devuelve).
- Mientras estás en tu fortín, en el campamento se ve **una tropa de cada tipo** que tengas, quieta.

!!! note "Para qué sirven"
    Las tropas son para [atacar los fortines de los demás](#atacar). Las que sueltas en un ataque no vuelven.

### Tropas

El **cuartel** necesita cierto nivel para cada tropa. Cada tropa golpea una vez por segundo.

--8<-- "_generado/clanes_tropas.md"

### Cuartel

--8<-- "_generado/clanes_cuartel.md"

### Campamento

--8<-- "_generado/clanes_campamento.md"

## Muros

Los muros son de **un bloque**, se pagan con piedra y se ponen y mejoran **al momento, sin constructor**.

- **Plano → Muro** y, con él en la mano, **clic derecho** al suelo pone un tramo. Sigues con el muro en la mano para
  poner más; **clic izquierdo** o **Q** para terminar.
- **Mayús + clic derecho**: pone una **línea recta** desde el último tramo hasta donde miras (cobrando cada tramo).
- Clic a un tramo: **Mejorar** ese, o **Mejorar todos** los de su nivel (los que te alcance).
- Cada nivel cambia el material del muro y, desde el 5, es más alto.

--8<-- "_generado/clanes_muros.md"

## Defensas

Las defensas disparan solas a las tropas que te atacan, una vez por segundo, a la más cercana que tengan a su
alcance. Mientras una defensa **se está mejorando no dispara** (pero la pueden destruir).

--8<-- "_generado/clanes_defensas.md"

### Torre de arqueros

--8<-- "_generado/clanes_torre_arqueros.md"

### Ballesta

--8<-- "_generado/clanes_ballesta.md"

### Catapulta

--8<-- "_generado/clanes_catapulta.md"

### Brasero

Escupe fuego a lo que tenga **muy cerca**: hace daño en área tanto a las tropas de tierra como a las que vuelan.

--8<-- "_generado/clanes_brasero.md"

### Escorpión

Una ballesta enorme que **solo apunta al cielo**: no le hace nada a lo que va por tierra, pero es lo que más daño
hace a lo que vuela.

--8<-- "_generado/clanes_escorpion.md"

## Atacar

Con **Atacar** (hueco 1) buscas el fortín de otro jugador para atacarlo. Necesitas tener tropas.

1. **Buscar** cuesta un poco de trigo. Te toca un fortín con un número de trofeos parecido al tuyo. Nunca sale uno con
   **escudo**, uno al que ya están atacando ni uno con su dueño dentro.
2. Llegas **volando por encima** de su base. Tienes unos segundos para **mirarla**: arriba sale cuánto le puedes robar.
   Con la **brújula** (hueco 9) puedes buscar **otro** (vuelve a costar trigo) o **volver a casa** sin atacar.
3. Tus tropas están en la barra. Con una en la mano, **haz clic al suelo** para soltarla: cae desde arriba. Con
   **Mayús + clic** sueltas cinco. Lo marcado en **rojo** está demasiado cerca de un edificio: ahí no se puede.
4. El ataque empieza al soltar la primera tropa (o cuando se acaba el tiempo de mirar) y dura unos minutos. Arriba ves
   el tiempo, el % destruido y las estrellas; encima de cada edificio, su **vida**.
5. Tus **hechizos** también van en la barra. Con uno en la mano, mira al suelo: sale su **círculo**. Haz **clic** para
   lanzarlo; vale también en lo rojo. Si tienes muchas tropas o hechizos, la **flecha** del hueco 8 pasa de página.
   Los hechizos lanzados se gastan; los que no lances vuelven contigo.
6. Acaba cuando se acaba el tiempo, cuando lo destruyes todo, cuando no te quedan tropas o cuando te **rindes** (con
   la bandera del hueco 9). Luego vuelves a tu fortín.

--8<-- "_generado/clanes_ataque.md"

### Cómo atacan las tropas

- Cada tropa va a por lo suyo (ver la tabla de [Tropas](#tropas)): **lo más cercano**, **las defensas**, **los
  muros** o **los almacenes y generadores**. Ninguna va a por un muro si no es que le **corta el paso**: entonces lo
  golpea hasta abrir hueco.
- El **Arquero** y la **Bruja** atacan desde lejos, también por encima de un muro. La Bruja y el **Zapador** hacen
  daño en área; el Zapador explota al llegar (y hace mucho más daño a los muros).
- Las que **vuelan** (Fantasma, Hada e Ifrit) pasan por encima de todo. Solo les pueden dar las **torres de
  arqueros**, los **braseros** y los **escorpiones**.
- El **Saqueador** va a por almacenes, aserraderos, canteras, granjas y graneros, y les hace el doble de daño.
- La **Araña** no rodea los muros: **trepa por encima** y va directa a las defensas. Las defensas de tierra sí le dan.
- El **Hada** no ataca: vuela detrás de tu tropa de tierra más herida y **cura** a las que tiene alrededor.
- El **Ifrit** vuela y hace daño en área desde un poco lejos.
- Con **Rabia**, las tropas que están dentro del círculo pegan más y van más deprisa. Con **Salto**, las de tierra que
  están dentro pasan por encima de los muros. Con **Hielo**, las defensas que están dentro no disparan.
- Un edificio sin vida queda en **ruinas** y un muro, en nada. La decoración no se toca.

### Estrellas y botín

| Estrella | Cómo se gana |
|---|---|
| ★ | Destruir la mitad de los edificios (los muros no cuentan) |
| ★ | Destruir el Torreón |
| ★ | Destruirlo todo |

Te llevas el **botín** multiplicado por la parte destruida: con el 60 % destruido, el 60 % del botín. Las tropas que
soltaste **se pierden** aunque sigan vivas; las que no soltaste vuelven a tu campamento.

### Si te atacan a ti

- No pasa nada mientras estás dentro de tu fortín: entonces no te pueden atacar.
- Después de un ataque te queda un **escudo** unas horas: nadie te puede atacar.
- Tu fortín **vuelve a estar como antes** en cuanto acaba el ataque: no hay que reconstruir nada. Solo pierdes lo que
  te robaron y los trofeos.
- Al entrar en tu fortín te avisa de quién te atacó, y en **Mi fortín → Registro** ves tus últimos ataques y
  defensas.

### Trofeos y premios

Atacar con **1 estrella o más** te da trofeos y se los quita al defensor; con 0 estrellas, los pierdes tú y se los
lleva él. Cuantos más trofeos tiene el rival, más hay en juego. Nadie baja de 0.

--8<-- "_generado/clanes_trofeos.md"

Cada semana hay un **ranking de los trofeos ganados esa semana** (en **Mi fortín → Trofeos** y en el cartel encima
del portal del lobby). Al acabar la semana, los tres primeros se llevan **chips**, que se cobran en la aldea como los
demás premios de minijuegos. Es lo único de Craft of Clans que sale al juego normal.

--8<-- "_generado/clanes_premios.md"

## Guerra

Cuando tu aldea está [en guerra](guerra.md#la-guerra-entre-aldeas) con otra, Craft of Clans también cuenta. Los
**ataques de guerra** son aparte de los normales y se hacen desde el menú **Guerra** (hueco 2).

- Sale el **marcador de Craft of Clans** de esa guerra: las estrellas de tu aldea contra las de la otra. Es **aparte**
  de los puntos de la guerra (los de matar enemigos y los asedios).
- Salen los **fortines de los ciudadanos de la aldea enemiga**: **eliges a quién atacar** (no se busca al azar ni
  cuesta trigo). No se puede atacar a quien está dentro de su fortín ni a quien ya están atacando.
- Los ataques de guerra son **los fines de semana** (sábado y domingo, hora de España). De lunes a viernes solo hay
  ataques normales; el fin de semana, los dos. El menú y el marcador se pueden mirar cualquier día.
- Tienes **un ataque de guerra al día** (cambia a las 0:00). Se gasta al soltar la primera tropa: si vuelves a casa
  sin atacar, lo conservas.
- El ataque es como uno normal, pero **sin botín**, **sin trofeos** y **sin escudo**: el escudo no protege en guerra.
- De cada fortín enemigo cuenta solo **la mejor marca** que le saque tu aldea en toda la guerra: si ya le sacasteis
  ★★ y ahora alguien le saca ★★★, el marcador sube 1. Atacar otra vez al mismo solo suma si se mejora.
- Al acabar cada ataque se avisa a los conectados de las dos aldeas. En el menú se ven los últimos ataques.
- Cuando la guerra termina, el marcador de Craft of Clans queda apuntado en el resultado de la guerra.

--8<-- "_generado/clanes_guerra.md"

Si no eres de ninguna aldea, solo hay ataques normales.

## Decorar

Con **Decorar** eliges bloques (flores, setos, vallas, faroles, caminos, lanas...) y te los pone en la mano. Son
**gratis** y no cuentan para nada: solo para que tu fortín quede bonito.

- **Clic derecho**: poner el bloque. Los caminos (tierra de camino, grava...) sustituyen la hierba del suelo.
- **Clic izquierdo** con un bloque de decoración en la mano: quitar decoración.
- No se puede decorar **encima de un edificio ni pegado a uno** (queda un bloque de paso alrededor).
