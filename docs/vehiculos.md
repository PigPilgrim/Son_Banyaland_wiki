# Vehículos

Caballos, burros y happy ghasts de marca, con su **llave**, su **maletero** y su **depósito**. Cada aldea tiene **un
Concesionario** y **una Gasolinera**, que reparte **el Alcalde**, y cada uno es
[una empresa del SEPE](hacienda.md#el-sepe-empresas).

!!! warning "⚠️ PENDIENTE"
    **Todavía no está en el servidor**: se está probando aparte. Los precios, las velocidades y los consumos pueden
    cambiar cuando se vea cómo funciona.

## Los modelos

--8<-- "_generado/vehiculos.md"

La velocidad se lee así: un caballo normal va de 0,11 a 0,34 y un burro o una mula, a 0,175, así que **todos los
modelos corren más que cualquier animal normal**. El Ghastla vuela y se mide aparte: un happy ghast normal va a 0,05.

**Cuando nadie lo monta, se queda quieto**: no se va paseando. Y **en la zona de una aldea que está sufriendo un
[asedio](guerra.md#el-asedio-entre-aldeas) no se puede volar**: si entras volando, el Ghastla baja despacio y te deja
en el suelo. En el resto del mundo se vuela con normalidad.

El precio de la tabla es lo que **le cuesta al Concesionario** pedirlo a fábrica, y se paga con chips de cualquier nivel:
si das de más, te devuelve el cambio. Lo que pagas tú **lo negocias con él**.

## La llave

**Quien tiene la llave tiene el vehículo.** Si la vendes, vendes el vehículo, y si te la roban, te lo pueden quitar.

- **Clic derecho al vehículo**, con la llave en el inventario: montar.
- **Agachado y clic derecho**: abrir el maletero.
- **Clic derecho con la llave en la mano**: te dice dónde está, su vida, su estado y su combustible.

Sin la llave no se puede montar, ni abrir el maletero, ni repostar.

!!! tip "Antes de comprar, mira la llave"
    La llave dice **el modelo y la matrícula** del vehículo, y **no se puede renombrar en el yunque** (los bidones
    tampoco). Si alguien te enseña una llave sin esa descripción, no es de un vehículo.

## Combustible

Mientras te mueves gasta, y **sin combustible anda muy despacio**. Para repostar, **haz clic derecho al vehículo con el
combustible en la mano y su llave en el inventario**. Cada vehículo sale de fábrica con un cuarto de depósito.

### Combustible casero

Solo sirve lo de esta tabla (nada de tablones, palos ni troncos). Es **de mala calidad**: cada vez que lo echas,
**le quita estado al vehículo**, y arreglarlo cuesta chips.

--8<-- "_generado/combustibles.md"

Sale más caro que la gasolina: lo que te ahorras en carbón lo pagas después reparando.

### Gasolina 95 y 98

Solo las refina **la Gasolinera**, y tarda. **No desgastan.** Las vende en sus surtidores, al precio que ella decida:

--8<-- "_generado/gasolinas.md"

Si mezclas, pierdes lo bueno: la velocidad extra de la 98 **solo la da un depósito sin mezclar**. El rendimiento sí
cuenta siempre.

## Vida, estado y averías

Cada vehículo tiene **vida** y **estado** (de 0 a 100). Los ves en la barra de abajo cuando vas montado.

- **La vida** baja con los golpes. Los jugadores no pueden hacerle daño, pero sí los monstruos, la lava, una caída o
  una explosión.
- **El estado** baja con el combustible casero.

**Con 0 de vida o de estado no muere: se avería.** Se queda parado, su nombre sale en rojo con **AVERIADO**, nadie lo
puede montar y ya no recibe más daño. El maletero sí se puede abrir. Si es el Ghastla y vas montado, **baja despacio
hasta el suelo** contigo encima.

Solo se pierde de verdad si **cae al vacío**: entonces suelta lo que llevaba en el maletero y la llave deja de servir.
Tampoco se pueden criar.

**No se curan solos ni dándoles de comer**: hay que llevarlos al Concesionario o a la Gasolinera, que tienen la
**Llave inglesa**. Con ella en la mano, clic derecho al vehículo: primero cura la vida y, cuando está llena, arregla el
estado. En cuanto tiene vida y estado, vuelve a andar.

--8<-- "_generado/llave_inglesa.md"

La llave **no se rompe**, pero cuando está gastada no sirve hasta que se repara, con experiencia, en
[el yunque del Herrero](aldeanos.md#reparar-con-experiencia). Lo que te cobren a ti por la reparación **lo negocias
con ellos**.

## El Concesionario

El **Ordenador del Concesionario** se **coloca como un bloque**, por ejemplo encima de una mesa. Con clic derecho sobre
él eliges un modelo, lo pagas en chips y llega unas horas después. Al recogerlo sale delante de ti con su llave, en el
mundo normal o en el Nether, así que deja sitio alrededor, sobre todo para el Ghastla. Solo puede tener
**5 pedidos a la vez**.

Solo su Concesionario puede colocarlo, usarlo y quitarlo; al romperlo vuelve a ser el Ordenador. Con la Refinería y los
surtidores pasa lo mismo con la Gasolinera. Las explosiones no le hacen nada.

## Tuneo

El Concesionario y la Gasolinera tienen el **Kit de tuneo**. Con él en la mano, clic derecho al vehículo y eliges qué
hacerle. Lo pagan ellos en chips, y a ti te lo cobran al precio que acordéis.

Las armaduras de **hierro, diamante y netherita** solo se pueden poner cuando ha llegado su edad, como las de los
jugadores. Las de cobre y oro, siempre.

--8<-- "_generado/tuneo.md"

## La Gasolinera

La **Refinería** se **coloca como un bloque**. Con clic derecho sobre ella eliges 95 o 98 y gasta el carbón, la lava, las
varas de blaze o las algas secas que lleves en el inventario. Las tandas se refinan una detrás de otra, también si no
estás conectado, y hay sitio para **9 tandas a la vez**.

### Surtidores

En la Refinería se **encargan los surtidores**, y cada uno cuesta más que el anterior:

--8<-- "_generado/surtidores.md"

- **La Gasolinera** lo coloca donde quiera, lo carga con sus bidones y pone el precio de cada uno. Lo cobrado se queda en el
  surtidor hasta que lo recoge.
- **Para repostar**, ve montado o acerca tu vehículo a 8 bloques o menos, haz clic derecho al surtidor y elige la
  gasolina. **Hace falta llevar su llave.** Se paga en chips.
- **Pagas el precio que ves al abrir el menú.** Si la Gasolinera lo cambia mientras lo tienes abierto, no se te cobra
  nada y te enseña el nuevo.
- Encima del surtidor hay un letrero con los precios y lo que queda.
- **Si la aldea se queda sin Gasolinera, sus surtidores cierran** hasta que haya otra, que se los queda vacíos.

## La licencia

1. **El Alcalde lo reparte:** desde su Despacho, en **Permisos exclusivos**, elige a un ciudadano conectado. La aldea necesita tener el SEPE.
2. **Lo registras en el SEPE** de tu aldea, eligiéndolo como tipo de empresa. Si ya tienes otra empresa, antes tienes que
   dejarla.
3. Recibes el Ordenador o la Refinería, la Llave inglesa y el Kit de tuneo, que **solo le sirven al dueño de la licencia**.
   Su nombre sale en el cartel del Funcionario.

Si cierras la empresa, o el Alcalde te la quita, pierdes la licencia. Cuando te la quita él, la empresa sigue con su caja,
pero pasa a ser de tipo *Otro*.

**Lo que era tuyo no se lo queda el siguiente:**

- El dinero cobrado en los surtidores y los bidones que tenían cargados, te los devuelven.
- Los pedidos a fábrica que aún no habías recogido, te los pagan a su precio.
- Las tandas de la Refinería te llegan cuando acaban de refinarse.

Si no estás conectado, te llega al entrar.
