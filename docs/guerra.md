# Guerra y asedios

Hay dos cosas distintas que se llaman *asedio*:

- **El asedio de monstruos:** una horda ataca **la Campana** de tu aldea y los vecinos la defienden juntos.
- **La guerra entre aldeas:** dos aldeas se enfrentan, y una puede **asediar** la Campana de la otra.

Los dos los organiza **el admin**: nunca te pillan por sorpresa.

## El asedio de monstruos

### Cómo va

1. Se avisa a todos los que estén cerca de la aldea: **hay un minuto para prepararse**.
2. Los monstruos llegan **por rondas**, desde **dos sitios al azar** fuera de la [zona segura](aldea.md#zona-segura).
   Van a por la **Campana**: si se encuentran a alguien por el camino, se pelean con él.
3. **No rompen puertas**, pero **trepan por los muros** (despacio, un bloque por segundo).
4. Una ronda se acaba cuando han caído todos sus monstruos. Hay un pequeño descanso antes de la siguiente.
5. Cuando quedan pocos, **brillan**, para que no se queden escondidos.

Arriba de la pantalla tienes una barra con la ronda y los monstruos que quedan, otra con **la vida de la Campana** y,
si hay jefe, otra con la del jefe.

### Cuántos monstruos vienen

Cuantos más defensores, más monstruos. Cuenta como **defensor** quien esté cerca de la aldea (hasta 32 bloques
fuera de la zona segura) mientras hay una ronda en marcha.

El tipo de asedio depende del nivel de la aldea:

--8<-- "_generado/asedios.md"

Los monstruos de cada ronda salen al azar entre los de su lista. El **jefe** llega al empezar la última ronda y, a
mitad de vida, **se enfada**: se vuelve más rápido y fuerte y llama a más monstruos.

--8<-- "_generado/asedio_numeros.md"

!!! warning "Ojo: es el mundo normal"
    El asedio es en tu aldea, en el mundo normal: **si mueres, pierdes lo que llevas**, como siempre. Los monstruos
    del asedio no sueltan chips, y los jefes no sueltan nada: el premio es el de la tabla.

### Ganar o perder

- **Si aguantáis todas las rondas**, cada defensor recibe su premio de chips.
- **Si la Campana cae**, la ronda sigue hasta el final, pero luego los monstruos se retiran **sin premio**, y
  **todas las tiendas de la aldea cierran** hasta que se repare. Qué pide el Secretario para repararla está en
  [La Campana](aldea.md#la-campana).

## La guerra entre aldeas

Para declarar la guerra, la aldea necesita el **Cuartel** (un [proyecto de la Oficina](proyectos.md)). Todo lo hace
**el Alcalde**, desde su Despacho → **Guerra**. Allí salen las demás aldeas **por su nombre** (nunca dónde están).

### Declarar la guerra

Es **gratis**. Se avisa a los vecinos de las dos aldeas, y desde ese momento:

- **Cada enemigo que matas suma un punto** a tu aldea (sale en la barra de abajo).
- **Morir a manos de un enemigo no te hace perder nada**: ni el inventario ni la experiencia.
- **No se puede romper ni poner bloques dentro de la aldea enemiga** (en toda su zona segura). Las casas están a
  salvo: la guerra es entre personas.

--8<-- "_generado/guerra_numeros.md"

### El asedio entre aldeas

1. **El Alcalde pide el asedio** (Despacho → Guerra → la aldea enemiga). A la otra aldea le llega el aviso.
2. **El admin le pone hora**, hablando con las dos aldeas. Se avisa 10, 5 y 1 minuto antes.
3. Cuando empieza, **la Campana de la aldea atacada brilla en rojo** (se ve a través de las paredes), con un haz de
   luz hacia el cielo y **un círculo de partículas** alrededor.
4. **Si dentro del círculo hay atacantes y ningún defensor, la conquista sube.** Si hay de los dos, está *disputada*
   y no se mueve. La barra de arriba enseña el % de conquista y el tiempo que queda.
5. **Si la conquista llega al 100 %, ganan los atacantes.** Si se acaba el tiempo antes, ganan los defensores.

Quien gana se lleva **10 puntos** y **el 10 % del Tesoro** de la otra aldea (de cada moneda).

!!! tip "Para defender basta con estar"
    La conquista no baja, pero **solo sube si no queda ningún defensor vivo dentro del círculo**. Un defensor que
    aguante en el círculo la frena del todo.

### Acabar la guerra

- **La paz:** un Alcalde la propone y el otro la acepta (Despacho → Guerra). Nadie paga nada.
- **Rendirse:** se acaba al momento, pero tu aldea **paga el 10 % de su Tesoro** a la otra.

Al acabar, se anuncia el resultado final a las dos aldeas.
