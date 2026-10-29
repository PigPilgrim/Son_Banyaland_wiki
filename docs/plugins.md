# Comandos y extras

Lo que puedes hacer en el servidor además de jugar: registrarte, sentarte, colgar imágenes, poner música...

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
ofrece un **paquete de recursos**: **acéptalo**, o no oirás las canciones. Los discos los reparte el admin.

!!! warning "⚠️ PENDIENTE"
    Ahora mismo la música todavía no funciona para todos los jugadores. Se arreglará cuando el servidor se mude.

## Mapa del mundo

Hay un **mapa web** del servidor: se abre en el navegador y puedes recorrer el mundo desde arriba o en 3D, con tus
construcciones y las aldeas. Tiene el **mundo normal, el Nether y el End** (las mazmorras y los minijuegos no salen,
para no estropear la sorpresa). **Los jugadores no aparecen** en el mapa: nadie puede ver dónde estás.

!!! warning "⚠️ PENDIENTE"
    El enlace al mapa se pondrá aquí cuando el servidor se mude.

## Skin

El **Barbero** de la aldea te cambia la skin: ver [Los aldeanos](aldeanos.md#barbero). Para **volver a tu skin de
siempre** (gratis): `/puente propia`.

## Otros comandos útiles

| Comando | Para qué |
|---|---|
| `/puente album` | Tu álbum de [cabezas coleccionables](minijuegos.md#cabezas-coleccionables) |
| `/puente cartas` | Leer tus [cartas](casas.md) |
| `/puente fianza` | Pagar la fianza y [salir de la cárcel](justicia.md#la-carcel) |
| `/puente barcos salir` | Salir de una [regata](minijuegos.md#las-regatas) |

Casi todo lo demás se hace **haciendo clic a los aldeanos** o en los **botones del chat**.
