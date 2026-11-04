# Comandos y extras

Lo que puedes hacer en el servidor además de jugar: registrarte, sentarte, colgar imágenes, poner música, el color de tu nombre...

## Registrarte y entrar

La primera vez que entras tienes que **elegir una contraseña**:

```
/register <contraseña> <contraseña>
```

(la misma dos veces). A partir de entonces, cada vez que entres:

```
/login <contraseña>
```

Si vuelves a entrar desde la misma conexión en menos de una hora, no te la vuelve a pedir.

!!! warning "Apúntate la contraseña"
    Si la olvidas, habla con el admin. Y no uses la misma que en otros sitios.

## Sentarse y tumbarse

- **Clic derecho en unas escaleras o una losa** con la mano vacía: te sientas.
- `/sit` (sentarte donde estés), `/lay` (tumbarte), `/crawl` (arrastrarte), `/bellyflop` (tirarte boca abajo) y
  `/spin` (girar).

Para levantarte, agáchate (Mayús).

!!! tip "Dormir"
    Para que se haga de día basta con que **duerma la mitad** de los conectados. Quien esté tumbado con `/lay` también
    cuenta, si hay al menos uno en una cama.

## Imágenes en marcos

Puedes colgar **cualquier imagen de internet** (también GIF animados) en marcos:

1. Pon los marcos en la pared, formando un rectángulo.
2. Escribe `/imageframe select` y haz **clic derecho** en el marco de una esquina y luego en el de la esquina
   contraria.
3. `/imageframe create <nombre> <enlace de la imagen> selection`

También puedes pedir la imagen como mapas para ponerla tú: `/imageframe create <nombre> <enlace> <ancho> <alto>`
y luego `/imageframe get <nombre>`. Para borrarla: `/imageframe delete <nombre>`.

El enlace tiene que ser **directo a la imagen** (que acabe en `.png`, `.jpg`, `.gif`...).

## Música: discos con canciones de verdad

En el servidor hay **discos con canciones reales**, que suenan en cualquier tocadiscos. Al entrar, el servidor te
ofrece un **paquete de recursos**: **acéptalo**, o no oirás las canciones. Los discos los reparte el admin, y también
los puedes **grabar tú** en un [Estudio de grabación](arte.md#estudio-de-grabacion), donde además puedes **pedir
canciones nuevas**.

!!! warning "⚠️ PENDIENTE"
    El servidor ya se ha mudado, pero falta probar en el juego que la música suene para todos los jugadores.

## Color de tu nombre

Puedes elegir el **color de tu nombre** en el chat y en la lista de jugadores (Tab): **haz clic en tu nombre** en
cualquier mensaje tuyo del chat (o escribe `/puente color`) y elige uno. Es gratis y lo puedes cambiar cuando quieras.
Si haces clic en el nombre de **otro**, se prepara un mensaje privado para él.

El nombre que sale **encima de la cabeza** no cambia, y el prefijo de **[Alcalde]** o **[Concejal]** se mantiene.

## Skin

El **Barbero** de la aldea te cambia la skin: ver [Los aldeanos](aldeanos.md#barbero). Para **volver a tu skin de
siempre** (gratis): `/puente propia`.

## Otros comandos útiles

| Comando | Para qué |
|---|---|
| `/puente color` | Elegir el [color de tu nombre](#color-de-tu-nombre) |
| `/puente album` | Tu álbum de [cabezas coleccionables](minijuegos.md#cabezas-coleccionables) |
| `/puente cartas` | Leer tus [cartas](casas.md) |
| `/puente fianza` | Pagar la fianza y [salir de la cárcel](justicia.md#la-carcel) |
| `/puente crimen` | Tu organización de los [bajos fondos](crimen.md) (o fundar una) |
| `/puente barcos salir` | Salir de una [regata](minijuegos.md#las-regatas) |
| `/puente barcos empezar` | Arrancar antes tu [partida online](minijuegos.md#partidas-online) de barcos (si ya sois 2 o más) |

Casi todo lo demás se hace **haciendo clic a los aldeanos** o en los **botones del chat**.
