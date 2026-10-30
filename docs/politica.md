# Política

Cada aldea se gobierna sola: **elige su nombre**, **elige Alcalde y Consejo** y **vota sus leyes**.

## Plazos

--8<-- "_generado/plazos.md"

---

## El nombre de la aldea

Cuando se funda una aldea, empieza sola la votación de su nombre:

1. **Propuestas:** al entrar en la aldea recibes **Pergaminos de propuesta**. Renombra uno en un **yunque** con el
   nombre que quieras y haz **clic derecho**. Los nombres repetidos no cuentan.
2. **Votación:** en el chat sale una papeleta con botones **[3] [2] [1]** para dar puntos (`/trigger votar set 1` la
   abre). Se puede cambiar hasta el final.
3. **Gana** el que más puntos sume (si empatan: el que tenga más votos de 3; si siguen empatados, el que se propuso
   antes).

**Premios** (se cobran al conectarte):

--8<-- "_generado/premios_nombre.md"

Además, cada uno se lleva una **cabeza decorativa** para poner en casa: *Placa del Fundador* (1.º), *Mención de
Honor* (2.º y 3.º) y *Pilar de Oro* (el de más puntos).

---

## Elecciones: Alcalde y Consejo

Las primeras elecciones **se convocan solas al fundar la aldea**. Después las convoca el admin, o salen de una
[moción de censura](#mocion-de-censura).

1. **Candidaturas:** pulsa **[Presentarme]** en el chat (`/trigger elecciones set 1`) y te da un **Libro de
   candidatura**. Escribe tu programa y **fírmalo con tu lema como título**. Con el libro en la mano, pulsa
   **[Entregar candidatura]** (`/trigger elecciones set 2`). Para retirarte: `/trigger elecciones set 3`.
2. **Votación:** `/trigger elecciones set 4` enseña los candidatos con **[Leer programa]** y **[Votar]**. El voto es
   **secreto** y se puede cambiar hasta el final.
3. **Resultado:**
    - El más votado es **Alcalde** (si empatan, el que se presentó antes).
    - Se reparten **5 escaños** del Consejo según los votos de cada uno (sistema D'Hondt, como en las elecciones de
      verdad). Quien tenga escaños es **Concejal**.
    - En el chat sale **[Alcalde]** o **[Concejal]** delante del nombre.
    - Los cargos duran **hasta las siguientes elecciones**. Si nadie vota, siguen los de antes.

Sin elecciones en marcha, `/trigger elecciones set 4` enseña el Consejo actual.

### El Alcalde

El Alcalde recibe el **Libro del Alcalde** (se le quita si pierde el cargo). Con **clic derecho** abre su
**Despacho**, desde donde puede:

- **Proponer leyes** y **proyectos** (ver abajo y [Proyectos](proyectos.md)).
- Ver el **Libro de Leyes**.
- **Colocar a los aldeanos** donde quiera dentro de la aldea.
- Con **Hacienda**: poner los **impuestos**.
- Con **Cuartel**: declarar **guerras** (página propia más adelante).

El fundador de una aldea nueva es su **Alcalde provisional** hasta que haya elecciones.

---

## Leyes y parlamento

1. El Alcalde escribe un **Proyecto de ley** (un libro; el título es el nombre de la ley), lo firma y lo presenta desde
   su Despacho (o junto al atril del Parlamento, en el Ayuntamiento).
2. Elige **cómo se vota**:

--8<-- "_generado/modos_ley.md"

3. Todos los que votan reciben la papeleta: **[Leer la ley]**, **[Sí]**, **[No]**, **[Abstención]**
   (`/trigger ley set 4`). El voto es secreto y se puede cambiar.
4. **Sale aprobada si el Sí supera al No.** Si empatan, gana lo que votó el Alcalde.

Las leyes aprobadas van al **Libro de Leyes** (`/trigger ley set 6`). **Las aplica el admin**: avísale si una ley no
se está cumpliendo.

---

## Moción de censura

Si no estáis contentos con el Alcalde, cualquier ciudadano puede abrir una **moción de censura** en el **Funcionario**
(con un motivo).

- Si en **48 horas** la firma **más de la mitad de los vecinos activos** (los que han entrado en los últimos 7 días),
  **hay elecciones**.
- Con el **25 % de las firmas** ya hay **huelga**: mientras dure, no se cobra el impuesto sobre los premios.
- Solo puede haber **una moción por semana**.

## Tablón de quejas

En el **Funcionario** también hay un **tablón de quejas**: se escribe en un yunque y se anuncia a todos.
