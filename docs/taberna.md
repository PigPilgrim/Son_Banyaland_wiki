# La Taberna

La Taberna llega con el **nivel 2** de la aldea, y con ella el **Tabernero**. En el servidor las bebidas **se fabrican
de verdad** gracias al plugin **[TheBrewingProject](https://hangar.papermc.io/BreweryTeam/TheBrewingProject)**: se
cuecen en un caldero, algunas se destilan y otras se envejecen en barril. Y al beberlas, **te emborrachas** (con
todo lo que eso conlleva).

En esta página: [cómo funciona el plugin](#como-se-hace-una-bebida), [la borrachera](#la-borrachera),
[las recetas secretas](#las-recetas-son-secretas), [la tienda del Tabernero](#la-tienda-del-tabernero) y
[todas las bebidas con sus efectos](#las-bebidas-y-sus-efectos).

!!! info "Los mensajes del plugin salen en inglés"
    Por ejemplo *Created a barrel* ("barril creado") o *You passed out... ZZzzz* ("te has desmayado").

---

## Cómo se hace una bebida

En el servidor **solo existen las 21 bebidas de la carta** de la Taberna (las que trae el plugin de fábrica están
quitadas). Y **solo se pueden echar al caldero ingredientes que salgan en alguna receta**: si algo no entra, es que
no sirve para ninguna.

Cada bebida pasa por uno, dos o los tres pasos siguientes, según su receta.

### 1. Cocer (siempre)

1. Pon un **caldero con agua** (o con **nieve en polvo**, si la receta lo dice).
2. Debajo tiene que haber **calor**: fuego, fuego de almas, **hoguera encendida** (normal o de almas), **lava** (de
   fuente) o un **bloque de magma**.
3. Echa los ingredientes con **clic derecho**.
4. Espera los **minutos** de la receta. Un minuto de receta es **un minuto real**. Ojo: **cada vez que echas un
   ingrediente, el tiempo vuelve a empezar**, así que echa todo seguido.
5. Saca la bebida con **botellas de cristal** (clic derecho al caldero).

!!! tip "Usa un reloj"
    Si haces clic derecho al caldero con un **reloj** en la mano, te dice abajo de la pantalla cuánto tiempo lleva
    cociendo.

### 2. Destilar (algunas)

Se hace en una **destilería**, que se construye así (de abajo arriba):

```
  vista de lado           arriba:   valla de bambú ── valla de bambú
                          medio:    vasija decorada   valla de bambú
                          abajo:    vasija decorada   vasija decorada
```

Son **3 vasijas decoradas** y **3 vallas de bambú**, en una columna de 2 de ancho y 3 de alto. Al poner el último
bloque sale el mensaje *Created a distillery*. Abriendo las vasijas verás dos huecos: la **mezcla** (*Mixture*, donde
metes la bebida) y el **destilado** (*Distillate*, donde sale). Cada pasada cuenta como una vez destilada.

### 3. Envejecer en barril (algunas)

El barril es una construcción de madera, de **la madera que pida la receta** (roble, abedul, abeto, acacia, cerezo,
roble oscuro...). Hay dos tamaños:

- **Barril pequeño** (9 huecos): 8 **escaleras** formando un cubo de 2×2×2 (4 abajo boca abajo y 4 arriba normales,
  mirando hacia dentro).
- **Barril grande** (27 huecos): 5 de largo, 3 de ancho y 3 de alto, hecho de **tablones y escaleras**, con una
  **valla** de grifo en un extremo.

Cuando lo tengas construido, **ponle un cartel** (sin escribir nada especial): sale *Created a barrel*.

**Un año en el barril son 20 minutos reales** (un día de Minecraft). Si la madera no es la de la receta, envejece
igual pero **la calidad baja** (unas maderas se parecen más que otras).

### La calidad

Según lo bien que hayas seguido la receta (ingredientes, minutos, veces destilada, años y madera del barril), la
bebida sale con **una, dos o tres estrellas**: **mala, buena o excelente**. Cuanto mejor la calidad, **más duran los
efectos** (ver la tabla de abajo). Si te sale muy mal, sale una bebida **fallida** que no sirve para nada: se puede
vaciar en una tolva.

---

## La borrachera

Cada bebida tiene dos números (están en [la tabla de bebidas](#las-bebidas-y-sus-efectos)):

- **Alcohol**: lo que sube tu barra de alcohol, que va de **0 a 100**. Al beber la ves abajo de la pantalla.
- **Toxinas**: lo que le sienta mal a tu cuerpo, también de **0 a 100**.

Las dos **bajan solas con el tiempo**. Con la borrachera pasan cosas al azar, más cuanto más alto estés:

| Si tu alcohol llega a... | Puede pasarte |
|---|---|
| **10** | Hablas raro: tus mensajes del chat salen **con letras cambiadas**, y cada vez más cuanto más alcohol llevas. |
| **40** | **Tropiezas** (te empuja hacia un lado) y a ratos **ves todo oscuro** un momento. Si vas montado (caballo, vagoneta) o con élitros, **das bandazos**. |
| **60** | **Andas haciendo eses** durante un rato, y puedes **salir volando por los aires** de un "pedo" (te deja con 6 corazones si tenías más). |
| **70** | **Alucinaciones**. |
| **80** | **Te desmayas**: te echa del servidor y **no puedes volver a entrar en 5 minutos**. |
| **85** | Al intentar entrar en el servidor, **puede que no te deje** ("demasiado borracho"). |
| **90** | **Pierdes la memoria**: te desmayas y, al volver, **apareces en otro sitio** al azar cerca del centro del mapa (a veces bajo tierra). |
| **99** | **Pones un huevo.** Sí. |

| Si tus toxinas llegan a... | Puede pasarte |
|---|---|
| **30** | **Náuseas** (la pantalla da vueltas). |
| **45** | **Vomitas.** |
| **50** | Lo peor: náuseas, **fiebre** (te congelas 10 segundos y luego ardes 5), vomitas y te quedas **a oscuras** 5 segundos. |
| **más de 25 mucho rato** | Te entra **resaca**: lentitud a ratos. |

**Cómo bajarla antes:**

| Comer o beber | Efecto |
|---|---|
| **Cubo de leche** | −3 de alcohol |
| **Pan** | −2 de alcohol y −1 de toxinas |
| Carne podrida | **+3** de toxinas |
| Ojo de araña | **+2** de toxinas |

!!! info "El aguante"
    Cuanto más bebes a lo largo del tiempo, **más aguante** coges: la misma bebida te sube un poco menos el alcohol.
    El aguante baja muy despacio si dejas de beber.

---

## Las recetas son secretas

**Las recetas no se publican a propósito:** descubrirlas es parte del juego. Para eso existe la **Receta sellada**, que
vende el Tabernero. Al abrirla te sale la receta de una bebida al azar, con **los números aproximados** (por ejemplo,
*"5 a 7 de trigo"*, *"unos 3 a 5 minutos"*). Los materiales de mazmorra sí vienen siempre exactos. La receta exacta,
la que da calidad excelente, hay que encontrarla probando.

Lo que puede salir en una Receta sellada:

--8<-- "_generado/receta_sellada.md"

!!! warning "⚠️ PENDIENTE"
    Cómo se consiguen las recetas de las bebidas **épicas y legendarias**, que nunca salen en la Receta sellada.

---

## La tienda del Tabernero

--8<-- "_generado/tienda_tabernero.md"

---

## Las bebidas y sus efectos

Todas las bebidas, con sus efectos exactos. Además de lo bueno, muchas tienen **algo malo al beberlas** o **resaca**
cuando se pasa el efecto. Los efectos raros (más o menos corazones, más alcance) se quitan solos al acabarse el tiempo.
*Alcohol* y *Toxinas* son los puntos que te suben al beberla (ver [La borrachera](#la-borrachera)).

--8<-- "_generado/bebidas.md"
