# Cod Zombies: el archivo de historia

Esta página es para quien **edita** la historia de [Cod Zombies](zombies.md): los diálogos, los personajes y los
objetivos de cada tramo. Para jugar no hace falta leerla (y destripa un poco la historia).

## Dónde está y cómo se aplica

- Se edita `mazmorras-tools/zombies_historia.yml` (en el repositorio del servidor).
- `python -I mazmorras-tools/zombies.py` lo copia al plugin (`plugins/Puente/zombies-historia.yml`).
- En el juego, `/puente zombies recargar` lo vuelve a leer sin reiniciar. Las partidas que ya estén en marcha siguen
  con lo de antes; se nota al empezar el siguiente tramo.
- Si el archivo tiene un error, la consola lo dice y los tramos se juegan sin historia (solo oleadas).

## Personajes

```yaml
personajes:
  marta: {nombre: Marta, color: aqua, medio: radio}
  ruiz: {nombre: Sargento Ruiz, color: blue}
```

- `nombre`: cómo sale en el chat.
- `color`: `aqua`, `white`, `blue`, `gold`, `yellow`, `green`, `red`, `gray`, `dark_aqua`...
- `medio`: `radio` (sale *📻 [Radio]* y un pitido), `megafonia` (*📢 [Megafonía]*) o nada (habla en persona).

Una **línea de diálogo** es `[personaje, "texto"]`. Mejor frases cortas (una o dos líneas de chat) y nunca más de
tres seguidas: se leen mientras se juega. Cada línea espera según lo larga que sea, y tras tres seguidas hay una
pausa algo mayor.

## Tramos

Cada tramo con historia va en `tramos`, con su identificador (`T3`, `T5`...). Los que no estén siguen siendo solo
oleadas.

```yaml
tramos:
  T5:
    npcs:
      ruiz: {personaje: ruiz, skin: wide/steve, papel: Policía, sitio: [-328.5, 70, 509.5, 180]}
    bloques:
      barricada:
        - [-332, 70, 506, "minecraft:spruce_planks"]
    atrancadas:
      - {sitio: [-332, 70, 505], texto: "Está atrancada por dentro."}
    pasos:
      - tipo: ir
        sitio: [-329.5, 69, 502.5]
        radio: 5
        objetivo: "Llega a la puerta de la comisaría"
        al_acabar:
          - [ruiz, "¡No abráis! Está atrancada por dentro."]
```

- **`npcs`**: las personas del tramo. `skin` es una de las del juego: `wide/` o `slim/` seguido de `steve`, `alex`,
  `ari`, `efe`, `kai`, `makena`, `noor`, `sunny` o `zuri`. `papel` es el texto pequeño bajo el nombre. `sitio` es
  `[x, y, z, mirando]`, y mirando es `0` sur, `90` oeste, `180` norte o `-90` este. No se les puede hacer daño.
- **`bloques`**: grupos de bloques que se ponen al empezar el tramo (barricadas, camillas...). Se apunta lo que había
  y se devuelve al acabar, incluso si el servidor se cae a medias.
- **`atrancadas`**: puertas que no se abren (sale el `texto`) hasta que un paso `abrir` las abra.
- **`pasos`**: lo que pasa, en orden. Un paso no empieza hasta que se ha dicho todo lo del anterior.

## Pasos

Todos los pasos pueden llevar:

- `objetivo`: lo que se ve arriba de la pantalla mientras dura.
- `al_empezar` y `al_acabar`: líneas de diálogo.
- `oleada`: el número de una oleada de ese tramo (las de `zombies.py`). En un paso de tipo `oleada` el paso es esa
  oleada; en los demás, los zombis de esa oleada van saliendo **mientras dura el paso**.

| Tipo | Qué hace | Acaba cuando |
|---|---|---|
| `oleada` | Saca la oleada `oleada` | No queda ningún zombi de ella |
| `ir` | — (`sitio`, `radio`) | Alguien del grupo llega |
| `recoger` | Pone objetos que brillan en `sitios`; `objeto` (por ahora `botiquin`, o un bloque u objeto de Minecraft); `texto_coger` | Se han cogido todos (clic derecho) |
| `hablar` | La persona `npc` brilla | Alguien le hace clic derecho |
| `aguantar` | Durante `segundos`, con zombis sin parar; el tiempo corre mientras haya alguien a menos de `radio` de `sitio` (si no, sale `fuera`). `civiles`: `npcs` que salen andando, uno cada `cada` segundos, hasta `hasta` | Se acaba el tiempo |
| `despejar` | — | No queda ningún zombi |
| `dialogo` | Solo habla (`al_empezar`) | Se ha dicho todo |
| `esperar` | — (`segundos`) | Pasa el tiempo |
| `curar` | Cura a todo el grupo | Al momento |
| `dar` | Da el `arma` (`escopeta`, `rifle`, `pistola`, `machete`, `hacha`) con su munición a quien no la tenga | Al momento |
| `abrir` | Quita el grupo de `bloques` y abre las `puertas` (que dejan de estar atrancadas) | Al momento |

Cuando se acaban los pasos, si quedan zombis hay que acabar con ellos, y el tramo queda despejado como siempre.

En `objetivo` y `texto_coger` se pueden poner: `{n}` y `{total}` (lo recogido), `{tiempo}` (lo que queda de
aguantar), `{civiles}` y `{civiles_total}` (los que han salido) y `{jugador}` (quien lo ha cogido).

## Cosas a tener en cuenta

- Todo avanza para el **grupo**. Si alguien cae o se va, los demás pueden seguir. Si caen todos, el tramo empieza
  de nuevo, con su historia desde el principio.
- Las personas que salen andando buscan el camino solas por el mapa. Si no lo encuentran, van en línea recta, así
  que nunca se quedan atascadas.
- `/historia saltar`: corta el diálogo que se esté diciendo cuando lo pide todo el grupo.
- Las coordenadas se sacan con F3. Los `sitio` de `ir`, `recoger` y `npcs` tienen que ser sitios donde se pueda
  estar de pie.
