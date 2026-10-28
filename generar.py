"""Genera las tablas de la wiki de Son Banyaland a partir de los mismos datos que usa el servidor.

Uso (desde la carpeta del servidor, con las herramientas del servidor al lado en ../mazmorras-tools):
    python -I wiki/generar.py
Escribe docs/_generado/*.md; las páginas de docs/ las incluyen con  --8<-- "_generado/<nombre>.md".
Los textos de las páginas se escriben a mano; las tablas, siempre con este programa (así nunca se desfasan).
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
HERRAMIENTAS = os.path.normpath(os.path.join(AQUI, "..", "mazmorras-tools"))
sys.path.insert(0, HERRAMIENTAS)
os.chdir(HERRAMIENTAS)

import aldea, asedio, bebidas, casas, misiones, barberia, oficina, forja  # noqa: E402

SALIDA = os.path.join(AQUI, "docs", "_generado")
ROMANO = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI"}
VANILLA = {
    "diamond": "Diamante", "trident": "Tridente", "paper": "Papel", "emerald": "Esmeralda", "smooth_stone": "Piedra lisa",
    "bricks": "Ladrillos", "stone_bricks": "Ladrillos de piedra", "iron_bars": "Barrotes de hierro", "candle": "Velas",
    "arrow": "Flechas", "iron_block": "Bloque de hierro",
}
EFECTOS = {
    "absorption": "Absorción", "blindness": "Ceguera", "darkness": "Oscuridad", "dolphins_grace": "Gracia del delfín",
    "fire_resistance": "Resistencia al fuego", "haste": "Prisa", "hunger": "Hambre", "jump_boost": "Salto",
    "mining_fatigue": "Fatiga minera", "nausea": "Náuseas", "night_vision": "Visión nocturna", "regeneration": "Regeneración",
    "resistance": "Resistencia", "saturation": "Saturación", "slow_falling": "Caída lenta", "slowness": "Lentitud",
    "speed": "Velocidad", "strength": "Fuerza", "water_breathing": "Respiración acuática", "weakness": "Debilidad",
    "wither": "Wither",
}
ATRIBUTO = {"alcance": "+2 bloques de alcance", "menos_corazones": "−4 corazones de vida máxima",
            "mas_corazones": "+4 corazones de vida máxima"}


# ---------------------------------------------------------------- utilidades
def texto(c):
    """Componente de texto de Minecraft (o MiniMessage) → texto plano."""
    if isinstance(c, str): return re.sub(r"<[^>]+>", "", c)
    if isinstance(c, list): return "".join(texto(x) for x in c)
    if isinstance(c, dict): return texto(c.get("text", "")) + "".join(texto(x) for x in c.get("extra", []))
    return ""


def nombre(it):
    if isinstance(it, tuple) and it[0] == "botella": return bebidas.CARTA[it[1]]["nombre"]
    comps = it.get("components", {})
    clave = (comps.get("minecraft:custom_data", {}).get("PublicBukkitValues") or {}).get("excellentcrates:key.id", "")
    if clave.startswith("chip_"): return f"Chip {ROMANO[int(clave[5:])]}"
    for k in ("minecraft:custom_name", "minecraft:item_name"):
        if k in comps: return re.sub(r"^[★☆\s]+", "", texto(comps[k])).strip()
    i = it["id"].split(":")[1]
    return VANILLA.get(i) or aldea.NOMBRES.get(i) or i.replace("_", " ").capitalize()


def cosa(it):
    n = it[2] if isinstance(it, tuple) else it.get("count", 1)
    return f"{n} × {nombre(it)}"


def tabla(cabecera, filas):
    out = ["| " + " | ".join(cabecera) + " |", "|" + "---|" * len(cabecera)]
    out += ["| " + " | ".join(str(c) for c in f) + " |" for f in filas]
    return "\n".join(out) + "\n"


def escribir(nombre_fichero, contenido):
    os.makedirs(SALIDA, exist_ok=True)
    with open(os.path.join(SALIDA, nombre_fichero), "w", encoding="utf-8", newline="\n") as f:
        f.write(contenido)


def existencias(n):
    return "sin límite" if n >= 999 else str(n)


# ---------------------------------------------------------------- dinero
def dinero():
    filas = [(f"Chip {ROMANO[n]}", f"{64 ** (n - 1):,}".replace(",", ".") + " chips I") for n in range(1, 7)]
    escribir("chips.md", tabla(["Moneda", "Equivale a"], filas))
    escribir("canje_sellos.md", f"1 Sello de la Aldea → {misiones.CANJE_CHIPS} chips I (en el Secretario, solo en ese sentido).\n")


# ---------------------------------------------------------------- aldea
def objeto_encargo(o):
    if isinstance(o, tuple) and o[0] == "chip": return f"Chip {ROMANO[o[1]]}"
    return aldea.nombre_objeto(o)


def niveles():
    filas = []
    for n, d in enumerate(aldea.NIVELES, start=1):
        enc = "<br>".join(f"{c} × {objeto_encargo(o)} · {e} entregas (**{c * e}** en total)" for o, c, e in d["encargo"])
        llegan = ", ".join(aldea.ROLES[r][0] for r in d.get("roles", [])) or "—"
        edificio = f"Terminar {d['edificio']}" if d["edificio"] else "—"
        filas.append((n, d["titulo"], enc, edificio, llegan, f"{aldea.RADIOS[n]} bloques"))
    escribir("niveles.md", tabla(["Nivel", "Qué se consigue", "Encargo del Secretario", "Además hace falta", "Llegan",
                                  "Zona segura"], filas))
    escribir("zona_segura.md", tabla(["Aldea", "Radio de la zona segura"],
                                     [("Recién fundada", f"{aldea.RADIOS[0]} bloques")]
                                     + [(f"Nivel {n}", f"{aldea.RADIOS[n]} bloques") for n in range(1, len(aldea.NIVELES) + 1)]))


def campana():
    filas = []
    for a in asedio.ASEDIOS:
        lo, hi = a["niveles"]
        cuando = "Recién fundada, nivel 1 o 2" if lo == 0 else (f"Nivel {lo}" if lo == hi else f"Niveles {lo} y {hi}")
        mats = "<br>".join(f"{c} × {objeto_encargo(o)} · {e} entregas (**{c * e}** en total)" for o, c, e in a["reparacion"])
        filas.append((cuando, mats))
    escribir("campana.md", tabla(["Aldea", "Para reparar la campana"], filas))


def tienda(rol):
    filas = []
    for o in aldea.TIENDAS_ROL.get(rol, []):
        pide = cosa(o[0]) + (f" + {cosa(o[3])}" if len(o) > 3 else "")
        filas.append((pide, cosa(o[1]), existencias(o[2])))
    return tabla(["Pagas", "Recibes", "Existencias"], filas)


def tiendas():
    for rol in ("tabernero", "herrero", "barbero", "mago"):
        escribir(f"tienda_{rol}.md", tienda(rol) + f"\nLas existencias se reponen solas cada {aldea.REPOSICION_MIN} minutos "
                                                  "con el servidor encendido.\n")
    filas = [(cosa(misiones.sello(1)), f"{misiones.CANJE_CHIPS} × Chip I", "sin límite", "aldea de nivel 1 o más")]
    for o in casas.ofertas():
        n = casas.NIVEL_ESCRITURAS if "Escritura" in nombre(o["sell"]) else casas.NIVEL_FUNDACION
        filas.append((cosa(o["buy"]), cosa(o["sell"]), "sin límite", f"aldea de nivel {n - 1} o más"))
    escribir("tienda_secretario.md", tabla(["Pagas", "Recibes", "Existencias", "Cuándo"], filas))
    escribir("reparar.md", f"**{forja.REPARAR_CHIPS} chips I** por reparación.\n")
    escribir("barbero.md", f"La primera vez que hablas con el Barbero te **regala un Vale de barbería**. Después cuestan "
                           f"**{barberia.PRECIO_DIAMANTES} diamantes** o **{barberia.PRECIO_CHIPS} chips I**.\n")


def proyectos():
    filas = []
    for k, (nom, desc, costes, _) in oficina.PROYECTOS.items():
        mats = "<br>".join(f"{n} × {oficina.NOMBRE_COSTE.get(t, t)}" for t, n in costes)
        req = oficina.REQUIERE.get(k)
        filas.append((f"**{nom}**", " ".join(desc), mats, oficina.PROYECTOS[req][0] if req else "—"))
    escribir("proyectos.md", tabla(["Proyecto", "Qué trae", "Materiales", "Necesita antes"], filas))


# ---------------------------------------------------------------- taberna
def efectos(lista):
    return "<br>".join(f"{EFECTOS.get(e, e)} {ROMANO.get(n, n)} · {s} s" for e, n, s in lista) or "—"


def taberna():
    orden = ["común", "poco común", "rara", "épica", "legendaria"]
    filas = []
    for k, b in sorted(bebidas.CARTA.items(), key=lambda kv: (orden.index(kv[1]["rareza"]), kv[1]["nombre"])):
        extra = []
        if b.get("atributo"):
            a, s = b["atributo"]
            extra.append(f"{ATRIBUTO.get(a, a)} · {s} s")
        filas.append((f"**{b['nombre']}**", b["rareza"], f"{b['alcohol']} %", "<br>".join([efectos(b["efectos"])] + extra),
                      efectos(b.get("al_beber", [])), efectos(b.get("resaca", []))))
    nota = ("\nLa duración de los efectos depende de la calidad con la que te salga: mala ×"
            f"{bebidas.CALIDAD['+']:g}, buena ×{bebidas.CALIDAD['++']:g}, excelente ×{bebidas.CALIDAD['+++']:g} "
            "(la tabla muestra la buena). *Al beber* llega en el momento; la *resaca*, cuando se acaba el efecto principal.\n")
    escribir("bebidas.md", tabla(["Bebida", "Rareza", "Alcohol", "Efectos (calidad buena)", "Al beber", "Resaca"], filas) + nota)
    # Probabilidad de cada rareza en la Receta sellada (peso por bebida según su rareza)
    total = sum(bebidas.PESO_SOBRE.get(b["rareza"], 0) for b in bebidas.CARTA.values())
    filas = []
    for r in orden:
        cuales = [b for b in bebidas.CARTA.values() if b["rareza"] == r]
        peso = bebidas.PESO_SOBRE.get(r, 0) * len(cuales)
        cada = bebidas.PESO_SOBRE.get(r, 0) / total * 100
        filas.append((r, len(cuales), f"{peso / total * 100:.0f} %" if peso else "nunca",
                      (f"{cada:.2f}".rstrip("0").rstrip(".") + " %").replace(".", ",") if peso else "—"))
    escribir("receta_sellada.md", tabla(["Rareza", "Bebidas", "Probabilidad de que salga una de esta rareza",
                                         "De cada bebida concreta"], filas))


def main():
    dinero(); niveles(); campana(); tiendas(); proyectos(); taberna()
    print("Tablas generadas en", SALIDA)


if __name__ == "__main__":
    main()
