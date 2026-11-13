# Taller de runas

El **Taller de runas** es un tipo de [empresa del SEPE](empresas.md). A quien trabaja en él se le llama
**Encantador**. No compite con la mesa de encantamientos, que sigue igual: el Encantador **abre huecos** en
herramientas, armas y armaduras y les **engasta runas** que fabrica él. Las runas y los encantamientos se pueden
tener a la vez.

Hay dos familias de runas:

- **Runas de oficio:** ayudan a **trabajar**: minar, talar, cultivar, pescar y explorar.
- **Runas de mazmorra:** de combate, y **solo funcionan dentro de las mazmorras y contra monstruos**. No cambian nada
  del PvP.

Ninguna runa da más minerales, diamantes ni chips, y ninguna repara objetos.

!!! warning "⚠️ PENDIENTE"
    El Taller de runas **aún no ha llegado al servidor**: está hecho, pero falta probarlo en el juego. Todos los
    números pueden cambiar.

## El Taller de runas

### Abrir uno

1. Registra la empresa en el **SEPE** con el tipo **Taller de runas**.
2. Elige la **caja**. Te dan el **Ordenador del Taller de runas** y la **Mesa de runas**.
3. Pon el **Ordenador** cerca de la caja y la **Mesa** cerca del Ordenador.

--8<-- "_generado/runas_numeros.md"

El Ordenador es el de todas las empresas: ver [El Ordenador y la investigación](empresas.md#el-ordenador-y-la-investigacion).
Las runas se **investigan por nivel**, de la I a la III: para la II hay que tener la I. Las de mazmorra solo tienen
nivel III. El Taller **no se especializa**: puede investigarlo todo.

--8<-- "_generado/runas_investigacion.md"

### El Taller

En la pestaña **Taller** del Ordenador se fabrica, con tus materiales, cualquier runa ya investigada. Las runas llevan
el nombre de tu Taller. Además, sin investigar nada:

--8<-- "_generado/runas_taller.md"

- **Polvo de runa:** se fabrica y también queda cuando una runa se rompe al engastarla.
- **Polvo arcano:** lo piden las runas II y III. **Lo vende el Mago** (ver [Magia](magia.md)).
- **Polvo de estabilidad:** sube la probabilidad de un servicio de la Mesa.

Las runas se venden a mano o con **dependientes**, como en cualquier empresa del módulo.

### Mejoras

--8<-- "_generado/runas_mejoras.md"

## Huecos y servicios

### Los huecos

Cada hueco se ve en la descripción del objeto: **◇ Hueco vacío** o **◆ Runa de Imán II**. Cuántos puede tener depende
del material:

--8<-- "_generado/runas_huecos.md"

- Admiten huecos los **picos, palas, hachas, azadas, cañas de pescar, tijeras, las 4 piezas de armadura y las armas**.
- **Las armas solo admiten runas de mazmorra.** El hacha es herramienta y arma, así que admite las dos familias.
- Las **armas con plano** y las piezas de los **sets de la Forja** admiten **un** hueco, y solo para runas de mazmorra.
- Los objetos **ilegales** no admiten nada.
- **Cada runa, una vez por objeto**: no se pueden poner dos runas de Imán en el mismo pico, aunque sean de distinto
  nivel.
- La armadura usa los mismos huecos para las dos familias: hay que elegir, por ejemplo, entre Pulmón y Barrera en el
  casco.

### Los servicios de la Mesa

En la **Mesa de runas** se hacen tres servicios, y cualquiera puede salir mal. Solo la usan el dueño del Taller y los
empleados con permiso para fabricar.

--8<-- "_generado/runas_servicios.md"

- **Mala suerte con límite:** cada fallo en **ese mismo objeto** suma **+10 %** al siguiente intento del mismo
  servicio, y el **5.º intento sale seguro**. El objeto lleva la cuenta: da igual en qué Taller lo intentes.
- **Polvo de estabilidad:** **+15 %** a un intento. Se gasta aunque falle.
- La mejora **Mesa tallada** sube la probabilidad de todos los servicios.
- La Mesa enseña **siempre** la probabilidad desglosada antes de aceptar.
- Las chips de cada servicio salen de la **caja del Taller** y desaparecen. El Encantador cobra aparte lo que quiera al
  cliente, y eso va a la caja.

### Servicio a un cliente

Para que el cliente no tenga que darle su objeto al Encantador y fiarse:

1. El Encantador abre la Mesa, elige **Servicio a un cliente** y elige a alguien que esté cerca de la Mesa.
2. Al cliente le sale un aviso: con un clic se abre una **ventana compartida**.
3. El cliente pone **su objeto**; el Encantador, **la runa**, el **Polvo de estabilidad** si quiere y el **precio**.
   Los dos ven la probabilidad.
4. Los dos pulsan **Aceptar**. **Cualquier cambio quita los dos Aceptar.**
5. Se cobra el precio al cliente, se hace el servicio y **el objeto vuelve solo al cliente**, salga bien o mal.

Si alguien cierra la ventana, se desconecta, se aleja de la Mesa o muere, o si el servidor se apaga, **cada cosa vuelve
a su dueño**. Si en ese momento no puede recibirla, la recibe al entrar o al reaparecer.

El Encantador también puede usar la Mesa **para lo suyo**, sin cliente.

### Yunque, piedra de afilar y mesa de herrería

- **Yunque:** renombrar o echar un libro encantado **conserva** los huecos y las runas. **No se pueden juntar** dos
  objetos si alguno tiene huecos.
- **Piedra de afilar:** quita los encantamientos, pero **nunca** toca los huecos ni las runas. Tampoco junta dos objetos
  con huecos.
- **Mesa de herrería:** al mejorar a netherita se **conservan** los huecos y las runas, y el objeto pasa a admitir los
  huecos del material nuevo (hay que abrirlos).
- Si el objeto **se rompe** por desgaste, las runas se pierden con él.

## Runas de oficio

Tienen tres niveles. **No funcionan en los minijuegos**, ni en la cárcel, ni en creativo.

- **Cuenta el objeto que usas.** Las de pico, hacha, azada y caña, con esa herramienta en la mano. Las de armadura,
  con la pieza puesta.
- **Imán y Sabiduría** cuentan en cualquier objeto: en la mano o en la armadura puesta. Si las llevas en varios, cuenta
  **la de nivel más alto**; no se suman.
- **Autofundido** no hace nada con **Toque de seda**. Con **Fortuna** da los lingotes que darías **sin** Fortuna: no
  sirve para tener más material.
- **Replantar** y **Hojarasca** solo funcionan en **árboles de verdad**, no en casas de troncos ni en árboles con hojas
  puestas a mano. En los árboles de 2×2, Replantar pone un brote por cada tronco de abajo que rompas.
- **Sembrador** usa una semilla de lo que suelta el cultivo, nunca de tu inventario. **Nunca** replanta plantas
  ilegales.
- **Picada rápida** y **Atracción** se suman, pero con un tope: con Atracción III, la runa ya casi no añade nada.
- **Pescador experto** nunca da más tesoros: solo más experiencia y, a veces, un pez normal más.
- **Andarín** se apaga unos segundos cada vez que golpeas a un jugador o te golpea uno.
- **Imán** no recoge lo que alguien acaba de tirar (tampoco lo tuyo, para que puedas soltar cosas) ni lo que suelta
  otro jugador al morir. Pasado un rato, sí.

--8<-- "_generado/runas_oficio.md"

## Runas de mazmorra

- **Solo funcionan dentro de las mazmorras**; fuera, el objeto lo dice: *(inactiva fuera de las mazmorras)*.
- **Solo contra monstruos y jefes.** Nunca hacen nada contra jugadores, ni siquiera dentro de una mazmorra.
- Siempre son de **nivel III**: se investigan con la probabilidad más difícil, se fabrican con materiales de mazmorra y
  se engastan con la probabilidad de las runas III.
- Se pueden fabricar y engastar desde **la edad del diamante**.
- Como mucho cuentan **unas pocas a la vez** por jugador, sumando arma y armadura (mira la tabla). Si llevas más, cuentan
  en orden y te sale un aviso con las que se quedan sin efecto.
- Las de **arma** cuentan con el arma en la mano y **cuerpo a cuerpo**. **Eco** cuenta con el arco o la ballesta en la
  mano; su flecha de más solo hace daño a monstruos y no se puede recoger.
- **Barrera** salta al dar o recibir el primer golpe de una pelea con un monstruo; **Segundo aliento**, cuando un
  monstruo te deja con poca vida. Las dos tienen recarga.
- **Piel de piedra** baja el daño de las explosiones y de las flechas que vienen de monstruos.
- Ninguna da más botín, cofres, chips ni materiales de mazmorra.

--8<-- "_generado/runas_mazmorra_reglas.md"

--8<-- "_generado/runas_mazmorra.md"
