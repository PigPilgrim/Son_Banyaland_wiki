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
| 2 | **Guerra** | Elegir [bando](#guerra-de-bandos) y, el fin de semana, los ataques de guerra |
| 3 | **Plano** | Construir un edificio nuevo |
| 4 | **Decorar** | Bloques de decoración |
| 5 | **Mi fortín** | Tus recursos, tus constructores, tu **ejército**, tus **trofeos**, tu **registro** de ataques, la semana y **Recoger todo** |
| 6 | **Recoger todo** | Vacía de un clic todos los aserraderos, canteras y granjas (hasta donde te quepa) |
| 8 | **Avisos de ataques** | Verde = activados (como viene): te avisa al momento si atacan tu fortín y, al conectarte, si te atacaron mientras no estabas. Clic para desactivarlos (se pone rojo). Al entrar en el fortín siempre ves lo que pasó |
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
- Si una mejora cuesta más de lo que te cabe, el menú te lo dice. Mira si el Torreón ya te deja **otro almacén**
  (desde el Torreón 3 puedes tener 2 de cada) o sube los que tienes.
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


### Herrería

Clic a la Herrería → **Mejorar tropas y hechizos**. Sale cada tropa (y abajo, cada hechizo) con su nivel, lo que gana
en el siguiente y lo que cuesta.

- Mejora **una cosa a la vez**, con tiempo de verdad (también sin estar tú). No usa constructor, pero mientras
  mejora algo **no se puede mejorar la Herrería**.
- Se paga con **trigo** al empezar.
- Cada nivel de tropa pide la **Herrería** a cierto nivel, y la tropa tiene que estar desbloqueada en el cuartel.
- Cada nivel da un **30 % más de vida y de daño** (al Hada, de cura). Las tropas que ya tienes entrenadas también
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

### Altares y héroes

Cada altar se construye una vez y no tiene más niveles. Al terminarlo, su **héroe** vive en él, al nivel 1.

--8<-- "_generado/clanes_altares.md"

Clic al altar: sale tu héroe con su nivel, su habilidad y si está listo.

- **Subirlo de nivel** cuesta trigo y **ocupa un constructor**, como una obra. Mientras sube, no puede ir a los ataques.
  Hasta qué nivel puede llegar lo marca tu **Torreón**.
- En el ataque se suelta como una tropa (va a por lo más cercano). Después, con **clic** en su hueco de la barra, usa
  su **habilidad**: una vez por ataque.
- Tras cada ataque en que lo sueltes, **descansa** un rato: hasta entonces no puede volver a atacar. Se ve en el altar
  y en tu ejército (**Mi fortín**).
- La Curación y el Hada le curan **la mitad**.

--8<-- "_generado/clanes_heroes.md"

#### Niveles de cada héroe

--8<-- "_generado/clanes_heroes_niveles.md"

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
5. Tus **héroes** (los que no descansan) y tus **hechizos** también van en la barra. El héroe se suelta como una
   tropa; luego, clic otra vez en su hueco para su **habilidad**.
   Con un **hechizo** en la mano, mira al suelo: sale su **círculo**. Haz **clic** para lanzarlo; vale también en lo
   rojo. Si tienes muchas tropas o hechizos, la **flecha** del hueco 8 pasa de página.
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

Con **1 estrella o más** es una **victoria** (por ejemplo, solo con tirar el Torreón); con ninguna, una **derrota**.

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
demás premios de minijuegos. Las copas de la [temporada](#temporadas) y los premios de la
[guerra de bandos](#guerra-de-bandos) también salen al juego normal.

--8<-- "_generado/clanes_premios.md"

## Temporadas

Cada **mes** es una temporada: empieza el **día 1 a las 0:00** (hora de España).

- Al acabar, los **tres con más trofeos** se llevan una copa: **Gold Chalice** (1.º), **Iron Chalice** (2.º) y
  **Bronze Chalice** (3.º).
- Después, los **trofeos de todos vuelven a 0** y se eligen **bandos nuevos**. Tu fortín, tus tropas, tus héroes y
  tus niveles **no se tocan**.
- El cartel del lobby enseña el top de **esta semana** y el de **la temporada**.

## Guerra de bandos

Cada temporada hay **dos bandos de colores** (por ejemplo, Rojo contra Azul; la siguiente, otros dos colores).

- En el menú **Guerra** (hueco 2) **eliges bando**. Te quedas en él **toda la temporada**. Quien no elige no juega la
  guerra.
- Para que no se descompense: si un bando ya tiene **2 personas más** que el otro, solo se puede entrar en el otro.
- La guerra es **cada fin de semana**: del **sábado a las 0:00 al domingo a las 24:00**. Tienes **un ataque de guerra
  al día** (dos por fin de semana). Se gasta al soltar la primera tropa: si vuelves a casa sin atacar, lo conservas.
- En el menú salen los **fortines del otro bando**: **eliges a quién atacar** (no se busca al azar ni cuesta trigo).
  No se puede atacar a quien está dentro de su fortín ni a quien ya están atacando.
- El ataque es como uno normal, pero **sin botín**, **sin trofeos** y **sin escudo**: el escudo no protege en guerra.
- De cada fortín enemigo cuenta solo **la mejor marca** que le saque tu bando: si ya le sacasteis ★★ y ahora alguien le
  saca ★★★, suma 1. Atacar otra vez al mismo solo suma si se mejora.
- **Gana el bando que saca más % de las estrellas posibles**, no el que más estrellas tiene: así el bando pequeño no
  pierde por ser menos.
- Al acabar cada ataque se avisa a los que tienen bando. En el menú se ven el marcador y los últimos ataques.

--8<-- "_generado/clanes_guerra.md"

**Premios** (el domingo a las 24:00):

- **Ambrosia**: una para **cada uno del bando ganador**, aunque no haya atacado.
- **Ice Chalice**: para **el mejor de la guerra** (el que más estrellas ha sacado; si empatan, el de más %).
- Si nadie ataca en todo el fin de semana, no hay premios.
- Los premios se dan en el **mundo normal**: si no estás conectado o estás en los minijuegos, te esperan y te llegan al
  volver.

## Decorar

Con **Decorar** eliges bloques (flores, setos, vallas, faroles, caminos, lanas...) y te los pone en la mano. Son
**gratis** y no cuentan para nada: solo para que tu fortín quede bonito.

- **Clic derecho**: poner el bloque. Los caminos (tierra de camino, grava...) sustituyen la hierba del suelo.
- **Clic izquierdo** con un bloque de decoración en la mano: quitar decoración. Se quita también lo que estaba
  apoyado encima (una flor, un farol...).
- La grava y lo que cae tiene que ir **sobre algo**: en el aire no se puede poner.
- No se puede decorar **encima de un edificio ni pegado a uno** (queda un bloque de paso alrededor).
- En el fortín **no se fabrica nada**: la rejilla 2×2 del inventario está bloqueada.
