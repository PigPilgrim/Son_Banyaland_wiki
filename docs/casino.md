# Casino

El **Casino** es un tipo de [empresa del SEPE](empresas.md). Lo abre un jugador en su aldea, pone **máquinas y mesas**
en su local y la gente va a jugar. El casino gana lo que la suerte le da; los jugadores, a veces, mucho más.

!!! warning "⚠️ PENDIENTE"
    **Todavía no está en el servidor:** se está probando y llegará más adelante. Todos los números de esta página pueden
    cambiar.

!!! info "Adiós al casino del lobby"
    El casino del **lobby de minijuegos** cierra. Sus tragaperras se quitan, y las **tiradas gratis** que te quedaran
    se cambian por **chips I** (una por tirada; si no estás conectado, te llegan al entrar). La lotería hace su
    **último sorteo** el lunes siguiente a las 0:00 con **el bote entero** (60/25/15 %); hasta entonces todavía se
    pueden comprar boletos. Tus **cosméticos** y las **cabezas de La Feria del Azar** se quedan contigo, y la
    [Máquina de la Feria](#maquina-de-la-feria) pasa a los Casinos.

## Jugar

**Clic derecho** a una máquina o una mesa. Cada una tiene un **cartel** encima que dice lo que es, cuánto se apuesta y
**cuánto devuelve** (por ejemplo, *Retorno: 92 %*: de cada 100 chips que se juegan, devuelve 92 de media).

--8<-- "_generado/casino_numeros.md"

- Se juega con las **chips I** que llevas encima (o en el cofre de ender).
- **No puedes jugar en tu propio casino** ni en el que trabajas.
- El resultado se decide **en cuanto apuestas**. Si cierras el menú, te desconectas o se apaga el servidor a mitad de
  tirada, **el premio se paga igual** (si no te cabe o no estás, te espera y te llega al entrar).
- Cada máquina tiene su propia **banca** (lo que tiene para pagar premios). La apuesta máxima baja sola si la banca no
  llega, y sin banca la máquina se cierra hasta que el casino la cargue.

### Máquinas y mesas

--8<-- "_generado/casino_puestos.md"

### Tragaperras pequeña

Una **estantería**: sus tres huecos son los rodillos, que se paran uno a uno.

--8<-- "_generado/casino_pequena.md"

### Tragaperras grande

Como la pequeña, con apuestas más altas y un **bote** que crece con cada tirada.

--8<-- "_generado/casino_grande.md"

### Todo o nada

Pones lo que quieras: o te lo **doblan** o lo **pierdes**. La probabilidad de ganar es la mitad del retorno (con un
retorno del 90 %, ganas 45 de cada 100 veces).

### Máquina de la Feria

Es para **coleccionar**: da las **cabezas del set La Feria del Azar** (que solo salen aquí; van a tu
[álbum](cabezas.md#el-album)), **cosméticos** y chips. Si te sale algo que **ya tienes**, te pagan su **valor en
chips**.

--8<-- "_generado/casino_objetos.md"

**Regalos por jugar:** al llegar a ciertas **tiradas pagadas** en la Feria (sumando las de todos los casinos) te
regalan algo **que aún no tienes** de esa rareza: primero una cabeza del set que te falte y, si ya las tienes, un
cosmético.

--8<-- "_generado/casino_hitos.md"

!!! info "Lo épico y lo legendario se anuncia"
    Si te sale algo **épico o legendario**, se entera todo el servidor.

### Blackjack

Contra el **crupier**, una mano cada vez en cada mesa. Las cartas salen en el menú.

--8<-- "_generado/casino_blackjack.md"

Si te levantas de la mesa a mitad de mano (cierras el menú o te vas), **te plantas**.

### Ruleta

Una **mesa compartida**: todos los que miran ven **el mismo giro**. Apuestas a **rojo**, **negro** o **verde**; la
primera apuesta abre la cuenta atrás y luego gira la tira hasta pararse bajo la flecha. Arriba se ven las últimas
tiradas.

--8<-- "_generado/casino_ruleta.md"

Si se apaga el servidor mientras gira, la tirada se paga igual; si se apaga durante la cuenta atrás, te devuelven la
apuesta.

## Eventos

### La rifa

Cada casino puede hacer **una rifa a la semana** (si la ha investigado). Los boletos se compran al **Crupier**. El
**domingo**, a la hora de ese casino, salen tres boletos al azar. El bote es lo que se vende (menos la comisión del
casino) **más lo que el casino quiera poner** de su caja. Es un premio: si tu aldea tiene Hacienda, **paga el impuesto
sobre premios**. No hace falta estar conectado: te avisa y lo cobras al volver.

--8<-- "_generado/casino_rifa.md"

### Concursos

El casino puede organizar un **concurso** (un torneo, una carrera...). Lo pide desde su Ordenador con el tipo, la
fecha y el premio, y el premio **queda apartado** desde ese momento. El **staff** lo aprueba (y se anuncia a todos) o
lo rechaza (el premio vuelve al casino), y al final le da el premio a quien gane.

### La subasta

En la subasta del casino (se abre desde el **Crupier**) se puja por **lotes del casino y de otros jugadores**, y puedes
subastar lo tuyo: lleva el objeto en la mano.

- Lo que pujas **se cobra ya** y queda guardado. Si alguien te supera, **te lo devuelven entero** en ese momento.
- Al acabar, el objeto le llega al que gana (aunque no esté conectado) y el vendedor cobra lo pujado menos la comisión
  del casino. Si nadie puja, el objeto vuelve.
- No se subasta dinero, cosas ilegales, cajas de shulker ni nada que tenga dueño (llaves, armas legendarias,
  planos...).

--8<-- "_generado/casino_subasta.md"

Además, el casino puede comprar cosas del **catálogo de la semana**:

--8<-- "_generado/casino_catalogo.md"

## Abrir un casino

1. Hace falta una **aldea de nivel 3**; cuántos casinos puede tener cada aldea depende de su nivel.
2. Registra la empresa en el **SEPE** con el tipo **Casino**, elige la **caja** y pon el **Ordenador del Casino** cerca.
3. **Investiga** las máquinas y mesas (no hay especialidad: se puede investigar todo). Cada cosa investigada se saca del
   Ordenador, en la pestaña **Sala**, y se pone en el local. Cuántas caben a la vez depende de la mejora **Sala de
   juego**.
4. **Clic derecho** a cada máquina (tú o tu gente) para **cargar su banca** desde la caja, **retirarla** cuando nadie
   juega y elegir el **retorno** con la barra (o, en el blackjack y la ruleta, sus reglas). Cambiarlo tiene una espera
   y no se puede mientras alguien juega; queda apuntado.
5. Los **dependientes** son los **crupieres**: venden los boletos de la rifa, abren la subasta y pueden vender lo que
   les pongas en el mostrador.

Cuando una máquina paga un premio que la deja sin banca, **se cierra sola** y te avisa. La pestaña **Eventos** del
Ordenador lleva la rifa, los concursos y la subasta.

!!! tip "Ciudadanos"
    Los [ciudadanos](ciudadanos.md) también vienen a jugar unas tiradas: dejan un poco de ganancia en la caja. Prefieren
    los casinos con **más retorno**, y un local con **mucha luz, máquinas y mesas** (los asientos cuentan poco).

## Cosméticos

Salen en la [Máquina de la Feria](#maquina-de-la-feria). Son **de tu cuenta**: no se pierden, no se tiran y no se
pueden pasar a otros. Se ponen en el menú de **Cosméticos** (en un [Tocador](crafteos.md#tocador), con el botón del
[álbum](cabezas.md#el-album) o con `/puente cosmeticos`). Lo que aún no tienes sale como *???*.

- **Títulos:** salen detrás de tu nombre en el chat. Algunos tienen otra forma: **Mayús + clic** para elegirla
  (*Rey del Casino* o *Reina del Casino*).
- **Rastros al andar:** unas pocas partículas cuando andas (no cuando estás quieto).
- **Al ganar:** un efecto cuando te toca algo gordo en el casino.
- **Sombreros:** clic y te dan uno para ponértelo; si lo pierdes, pides otro. Solo vale **el último que pediste** y
  solo **en ti**: si alguien lleva uno tuyo, o tú uno viejo guardado, se desvanece.

En el mismo menú puedes **dejar de ver las partículas** (los rastros y los efectos de todos).

??? note "Los cosméticos"
    --8<-- "_generado/cosmeticos.md"

!!! tip "Dios del Azar"
    Cada apuesta pagada en un casino (y cada boleto de rifa) da **devoción** si sigues al Dios del Azar. Ver
    [La Iglesia](iglesia.md).

## Misiones

El [Pregonero](misiones.md) puede pedirte **jugar a la ruleta**, **ganar una mano de blackjack**, **comprar un boleto de
una rifa** o **pujar en una subasta**, siempre en un casino que no sea tuyo y solo si hay alguno abierto que lo tenga.
