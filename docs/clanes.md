# Craft of Clans

Un minijuego aparte del juego normal: tienes tu propio **fortín**, lo llenas de edificios y los vas mejorando. Las
mejoras tardan **tiempo de verdad** (minutos al principio, horas después) y siguen avanzando aunque no estés conectado.

!!! warning "⚠️ PENDIENTE"
    Está en pruebas. Ya se puede construir, mejorar, decorar, **entrenar tropas** y poner **muros y defensas**, pero
    **todavía no se lucha**: los **ataques a los fortines de los demás** llegarán más adelante. Los números de abajo
    pueden cambiar.

## Entrar y salir

- Se entra desde el **lobby de minijuegos** (ver [Ir y volver](minijuegos.md#ir-y-volver)), por su portal o con
  `/puente clanes`.
- Como en los demás minijuegos, se juega en **modo aventura** y con el **inventario del lobby**: lo que llevabas se
  queda en la [mochila](minijuegos.md#tu-inventario-y-la-mochila) y vuelve al salir. Dentro no recibes daño ni pasas
  hambre.
- Para salir, la **puerta** del hueco 9 de tu barra: vuelves al lobby.

La primera vez que entras te dan una **parcela de 48×48** con una valla alrededor. Es solo tuya.

## Tu barra

| Hueco | Objeto | Para qué |
|---|---|---|
| 1 | **Plano** | Construir un edificio nuevo |
| 2 | **Decorar** | Bloques de decoración |
| 3 | **Mi fortín** | Tus recursos, tus constructores, tu **ejército**, la semana y **Recoger todo** |
| 9 | **Salir al lobby** | Volver al lobby de minijuegos |

**Haz clic a cualquier edificio** para ver su menú: **Mejorar**, **Recoger** (aserraderos, canteras y granjas),
**Entrenar tropas** (cuartel) y **Mover**. Ahí también se ve su **vida** (contará en los ataques). Encima de cada
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
    Las tropas son para **atacar los fortines de los demás**, que llegará más adelante. De momento solo se entrenan y
    esperan.

### Tropas

El **cuartel** necesita cierto nivel para cada tropa; los números de combate son para cuando lleguen los ataques.

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

Las defensas son para cuando lleguen los ataques: **todavía no disparan**. Ya se pueden construir y mejorar.

--8<-- "_generado/clanes_defensas.md"

### Torre de arqueros

--8<-- "_generado/clanes_torre_arqueros.md"

### Ballesta

--8<-- "_generado/clanes_ballesta.md"

### Catapulta

Su nivel máximo es el 6.

--8<-- "_generado/clanes_catapulta.md"

## Decorar

Con **Decorar** eliges bloques (flores, setos, vallas, faroles, caminos, lanas...) y te los pone en la mano. Son
**gratis** y no cuentan para nada: solo para que tu fortín quede bonito.

- **Clic derecho**: poner el bloque. Los caminos (tierra de camino, grava...) sustituyen la hierba del suelo.
- **Clic izquierdo** con un bloque de decoración en la mano: quitar decoración.
- No se puede decorar **encima de un edificio ni pegado a uno** (queda un bloque de paso alrededor).
