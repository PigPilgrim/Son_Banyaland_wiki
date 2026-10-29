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

import aldea, asedio, bebidas, casas, misiones, barberia, oficina, forja, magia, build, cofres_mazmorra, elecciones, parlamento, mj_comun, votacion, crimen  # noqa: E402

SALIDA = os.path.join(AQUI, "docs", "_generado")
ROMANO = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
VANILLA = {
    "diamond": "Diamante", "trident": "Tridente", "paper": "Papel", "emerald": "Esmeralda", "smooth_stone": "Piedra lisa",
    "bricks": "Ladrillos", "stone_bricks": "Ladrillos de piedra", "iron_bars": "Barrotes de hierro", "candle": "Velas",
    "arrow": "Flechas", "iron_block": "Bloque de hierro", "diamond_pickaxe": "Pico de diamante",
    "diamond_sword": "Espada de diamante", "diamond_spear": "Lanza de diamante", "netherite_sword": "Espada de netherita",
    "mace": "Maza", "crossbow": "Ballesta", "bow": "Arco", "netherite_chestplate": "Peto de netherita",
    "golden_sword": "Espada de oro", "goat_horn": "Cuerno de cabra",
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
    if "minecraft:stored_enchantments" in comps:
        return "Libro: " + ", ".join(f"{ENCANT[k.split(':')[1]]} {ROMANO[v]}" for k, v in comps["minecraft:stored_enchantments"].items())
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
        minutos = aldea.REPOSICION_TABERNA_MIN if rol == "tabernero" else aldea.REPOSICION_MIN
        cada = f"{minutos // 60} horas" if minutos % 60 == 0 else f"{minutos} minutos"
        escribir(f"tienda_{rol}.md", tienda(rol) + f"\nLas existencias se reponen solas cada {cada} "
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
        filas.append((f"**{b['nombre']}**", b["rareza"], b["alcohol"], f"{bebidas.toxinas(b):g}".replace(".", ","), "<br>".join([efectos(b["efectos"])] + extra),
                      efectos(b.get("al_beber", [])), efectos(b.get("resaca", []))))
    nota = ("\nLa duración de los efectos depende de la calidad con la que te salga: mala ×"
            f"{bebidas.CALIDAD['+']:g}, buena ×{bebidas.CALIDAD['++']:g}, excelente ×{bebidas.CALIDAD['+++']:g} "
            "(la tabla muestra la buena). *Al beber* llega en el momento; la *resaca*, cuando se acaba el efecto principal.\n")
    escribir("bebidas.md", tabla(["Bebida", "Rareza", "Alcohol", "Toxinas", "Efectos (calidad buena)", "Al beber", "Resaca"], filas) + nota)
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


# ---------------------------------------------------------------- mazmorras
MAZMORRA_DE = {"enanos": "enanos", "samurai": "samurai"}
ARMA_MOB = {"iron_sword": "Espada de hierro", "bow": "Arco", "golden_axe": "Hacha de oro", "iron_axe": "Hacha de hierro",
            "crossbow": "Ballesta", "iron_pickaxe": "Pico de hierro", "golden_sword": "Espada de oro",
            "netherite_sword": "Espada de netherita"}
ENCANT = {"sharpness": "Afilado", "unbreaking": "Irrompibilidad", "fire_aspect": "Aspecto ígneo", "lunge": "Embestida",
          "efficiency": "Eficiencia", "loyalty": "Lealtad", "impaling": "Empalamiento", "density": "Densidad",
          "breach": "Brecha", "power": "Poder", "punch": "Retroceso", "quick_charge": "Carga rápida",
          "piercing": "Perforación", "protection": "Protección", "feather_falling": "Caída de pluma", "mending": "Reparación",
          "fortune": "Fortuna"}
# Lo que no se ve en los números: cómo pelea cada uno (se escribe aquí; los números salen de build.py)
ESPECIAL = {
    "espiritu": "Vuela y atraviesa paredes; muere de un golpe.",
    "esqueleto": "Arco con Poder IV y Retroceso.",
    "soldado": "Armadura de oro, Fuerza, Afilado III; casi no se le empuja.",
    "espiritu_helado": "Arco con Poder II; sus flechas ralentizan.",
    "guerrero_enano": "Pequeño pero duro; casi no se le empuja.",
    "ballestero_enano": "Ballesta con Perforación II y Carga rápida.",
    "minero_enano": "Rápido. Su pico te da **Fatiga minera II 6 s**.",
    "samurai": "Esqueleto del Wither: sus golpes dan Wither.",
    "ninja": "**Invisible** (solo se ve su ropa) y rápido. Su espada te **ciega 2 s**.",
    "ninja_arquero": "**Invisible** (solo se ve su ropa). Arco con Poder II.",
    "tsuchigumo": "Araña de cueva gigante: envenena.",
    "tengu": "Vuela y ataca desde arriba.",
}


def pct(p):
    v = p * 100
    s = f"{v:.2f}".rstrip("0").rstrip(".") if v < 10 else f"{v:.1f}".rstrip("0").rstrip(".")
    return s.replace(".", ",") + " %"


def material(clave):
    return build.MATERIALES[clave][0]


def mobs():
    for donde in ("egipcia", "enanos", "samurai"):
        filas = []
        for k, m in build.MOBS.items():
            if MAZMORRA_DE.get(next((t for t in m["Tags"] if t in MAZMORRA_DE), ""), "egipcia") != donde: continue
            arma = m.get("equipment", {}).get("mainhand", {}).get("id", "").split(":")[-1]
            lo, hi = build.MOB_CHIP_COUNT.get(k, (1, 1))
            sueltan = [f"Chip I ×{lo}{f'-{hi}' if hi != lo else ''} · {pct(build.MOB_CHIP_CHANCE[k])}"]
            if k in build.MOB_CHIP2_CHANCE: sueltan.append(f"Chip II · {pct(build.MOB_CHIP2_CHANCE[k])}")
            sueltan += [f"{material(c)} · {pct(p)}" for c, p, _, _ in build.MOB_MATERIALES.get(k, [])]
            extra = {"forja:sets/enano": "Pieza del set Enano", "forja:planos/epicos": "Plano épico al azar"}
            sueltan += [f"{extra[t]} · {pct(p)}" for t, p in build.MOB_EXTRA.get(k, [])]
            filas.append((f"**{texto(m['CustomName'])}**", f"{float(m['Health']):g} ({float(m['Health']) / 2:g} ♥)".replace(".", ","),
                          ARMA_MOB.get(arma, "—"), ESPECIAL.get(k, ""), "<br>".join(sueltan)))
        escribir(f"mobs_{donde}.md", tabla(["Monstruo", "Vida", "Arma", "Cómo pelea", "Suelta (probabilidad)"], filas))
    escribir("materiales.md", tabla(["Material", "Rareza", "Descripción"],
                                    [(f"**{n}**", r, d) for n, r, _, _, d in build.MATERIALES.values()]))


def jefes():
    for k, j in build.JEFES.items():
        e = j["entidad"]
        attr = {a["id"].split(":")[1]: a["base"] for a in e["attributes"]}
        b, t = j["botin"], j["tesoro_botin"]
        filas = [("Vida", f"{j['vida']} ({j['vida'] // 2} ♥) + {j['vida_extra']} por cada jugador más en la sala"),
                 ("Armadura", f"{attr.get('armor', 0):g}"),
                 ("Daño base", f"{attr.get('attack_damage', 0):g}"), ("Tamaño", f"×{attr.get('scale', 1):g}"),
                 ("Al 66 % de vida", j["fase1"][0]), ("Al 33 % de vida", j["fase2"][0] + (" Se vuelve más rápido y fuerte." if j["furia"] else ""))]
        if j["teletransporte"]:
            filas.append(("Desde el 66 % de vida", f"Cada {build.TELETRANSPORTE_CADA // 4} s aparece **a la espalda de un jugador** al azar."))
        escribir(f"jefe_{k}.md", tabla(["", texto(e["CustomName"])], filas))
        lo2, hi2 = b["chips2"]
        al_morir = [f"{lo2}-{hi2} × Chip II", f"Chip III · {pct(b['chip3'])}"] + [
            f"{lo}{f'-{hi}' if hi != lo else ''} × {material(c)}" + ("" if p >= 1 else f" · {pct(p)}") for c, p, lo, hi in b["materiales"]]
        nombres = {"forja:planos/epicos": "Plano épico al azar", "forja:planos/legendarios": "Plano legendario al azar",
                   "forja:planos/katana": "Plano de la Katana", "forja:samurai/pieza": "Pieza del set Samurái",
                   "magia:grimorios/epicos": "Grimorio épico al azar", "magia:grimorios/legendarios": "Grimorio legendario al azar"}
        lo, hi = t["chips"]
        tesoro = [f"Receta de bebida **épica** · {pct(t['epica'])}", f"Receta de bebida **legendaria** · {pct(t['legendaria'])}",
                  f"{lo}-{hi} × Chip I", f"Chip II · {pct(t['chip2'])}"] + [
            f"{l}{f'-{h}' if h != l else ''} × {material(c)}" + ("" if p >= 1 else f" · {pct(p)}") for c, p, l, h in t["materiales"]] + [
            f"{nombres.get(tb) or 'Pieza del set ' + forja.SETS[tb.split('/')[-1]][0]} · {pct(p)}" for tb, p in t.get("extra", [])]
        escribir(f"botin_{k}.md", tabla(["Al morir (lo suelta el jefe)", "Tesoro (cada jugador, una vez por partida)"],
                                        [("<br>".join(al_morir), "<br>".join(tesoro))]))


def trials():
    filas = []
    for _, (nombre_t, cfg, r) in build.TRIALS.items():
        quien = " y ".join(texto(build.MOBS[m]["CustomName"]) for m, _ in cfg["spawn_potentials"])
        lo, hi = r["chips"]
        dp, dlo, dhi = r["diamante"]
        premio = [f"{lo}-{hi} × Chip I", f"{dlo}{f'-{dhi}' if dhi != dlo else ''} × Diamante" + ("" if dp >= 1 else f" · {pct(dp)}"),
                  f"Chip II · {pct(r['chip2'])}"] + [
            f"{l}{f'-{h}' if h != l else ''} × {material(c)}" + ("" if p >= 1 else f" · {pct(p)}") for c, p, l, h in r["materiales"]]
        filas.append((f"**{'Flojo' if nombre_t == 'amarilla' else 'Fuerte'}**", quien,
                      f"{cfg['total_mobs']:g} (+{cfg['total_mobs_added_per_player']:g} por cada jugador más)",
                      f"{cfg['simultaneous_mobs']:g} (+{cfg['simultaneous_mobs_added_per_player']:g} por jugador)",
                      "<br>".join(premio)))
    escribir("trials.md", tabla(["Desafío", "Monstruos", "Cuántos en total", "A la vez", "Premio (para cada jugador)"], filas))


def cofres():
    for clave, c in cofres_mazmorra.CAJAS.items():
        filas = []
        for rareza in ("común", "poco común", "rara", "épica", "legendaria"):
            ps = [p for p in cofres_mazmorra.premios(clave) if p[3] == cofres_mazmorra.R_EC[rareza]]
            if not ps: continue
            filas.append((f"**{rareza.capitalize()}**", f"**{pct(c['porcentaje'][rareza] / 100)}**", ""))
            filas += [("", pct(peso / 100), n) for _, n, peso, _, _ in ps]
        constancia = sorted({nombre(o) for o in c["constancia"]})
        escribir(f"cofre_{clave}.md", tabla(["Rareza", "Probabilidad", "Premio"], filas) +
                 f"\n**Constancia:** cada **{c['cada']}** aperturas de este cofre te toca seguro: "
                 + (constancia[0] if len(constancia) == 1 else f"un {('plano o grimorio ' + ('épico' if c['nivel'] == 2 else 'legendario'))} al azar") + ".\n")
    filas = [(re.sub(r"<[^>]+>", "", c["nombre"]), f"1 × Chip {ROMANO[c['nivel']]}", c["cada"]) for c in cofres_mazmorra.CAJAS.values()]
    escribir("cofres.md", tabla(["Cofre", "Se abre con", "Premio seguro cada"], filas))


def mercader():
    filas = []
    for _, (nom, _, _, ofertas) in build.TIENDAS.items():
        for o in ofertas:
            filas.append((f"**{nom}**", cosa(o[0]), cosa(o[1]), existencias(o[2]) + " (no se reponen)" if len(o) > 2 else "sin límite"))
    escribir("mercader.md", tabla(["Quién", "Pagas", "Recibes", "Existencias"], filas))


# ---------------------------------------------------------------- forja
def encantamientos(o):
    enc = o["components"].get("minecraft:enchantments", {})
    return ", ".join(f"{ENCANT[k.split(':')[1]]} {ROMANO[v]}" for k, v in enc.items() if k.startswith("minecraft:")) or "—"


def descripcion(o):
    """Las líneas en cursiva del objeto (sin la de rareza)."""
    return "<br>".join(texto(l) for l in o["components"]["minecraft:lore"] if l.get("italic"))


def danio(o):
    mods = {m["id"].split(":")[1]: m["amount"] for m in o["components"].get("minecraft:attribute_modifiers", [])}
    clave = next((k[:-5] for k in mods if k.endswith("_dano")), None)
    if not clave: return "como el objeto normal"
    return f"{mods[clave + '_dano'] + 1:g} de daño · {4 + mods[clave + '_velocidad']:g} de velocidad".replace(".", ",")


def forja_tablas():
    for rareza, fich in (("épica", "armas_epicas.md"), ("legendaria", "armas_legendarias.md")):
        filas = []
        for k, (o, (mat, n)) in forja.ARMAS.items():
            if forja.rareza_arma(k) != rareza: continue
            pide = f"{n} × Chip I" if mat == "chips" else f"{n} × {material(mat)}"
            filas.append((f"**{nombre(o)}**", VANILLA.get(o["id"].split(":")[1], o["id"].split(":")[1]),
                          danio(o), encantamientos(o), descripcion(o), f"Plano + {pide}"))
        escribir(fich, tabla(["Arma", "Base", "Daño (en la mano)", "Encantamientos", "Qué hace", "Se fabrica con"], filas))
    filas = []
    for k, (nom, (dibujo, mat), piezas_, bonus, _) in forja.SETS.items():
        filas.append((f"**Set {nom}**", "<br>".join(piezas_), bonus[0].upper() + bonus[1:]))
    escribir("sets.md", tabla(["Set", "Piezas (casco, peto, perneras, botas)", "Con las 4 puestas"], filas))
    for clave, (nom, rareza, txt, objetos) in forja.ENCARGOS.items():
        filas = [(f"**{nombre(o)}**", encantamientos(o)) for o in objetos if "set" not in o["components"].get("minecraft:custom_data", {})]
        n_sets = sum(1 for o in objetos if "set" in o["components"].get("minecraft:custom_data", {}))
        if n_sets: filas.append((f"**Una pieza de set al azar** ({n_sets} posibles: 4 de cada uno de los {n_sets // 4} sets)",
                                 f"{pct(n_sets / len(objetos))} en total"))
        escribir(f"encargo_{clave}.md", f"Cada objeto tiene la misma probabilidad: **{pct(1 / len(objetos))}** "
                 f"(1 entre {len(objetos)}).\n\n" + tabla(["Puede salir", "Encantamientos"], filas))


# ---------------------------------------------------------------- magia
def magia_tablas():
    filas = [(f"**{n}**", t_, f"{p} × Diamante", r and f"{r} s" or "—") for n, _, t_, p, _, r, _ in magia.PERGAMINOS.values()]
    escribir("pergaminos.md", tabla(["Pergamino", "Qué hace", "Precio en el Mago", "Recarga"], filas))
    filas = []
    for k, (n, rareza, _, recarga, t_, (mat, cuantos_), _) in magia.VARITAS.items():
        filas.append((f"**{n}**", rareza, t_, f"{recarga} s", f"Grimorio + {cuantos_} × {material(mat)}"))
    escribir("varitas.md", tabla(["Varita", "Rareza", "Qué hace", "Recarga", "Se fabrica con"], filas))


# ---------------------------------------------------------------- misiones
def misiones_tablas():
    cond = {misiones.TAB: "Con la Taberna (aldea nivel 2 o más)", misiones.MAZ: "Con el Guía de las Mazmorras (aldea nivel 3 o más)",
            f"{misiones.MAZ} {misiones.DOMINGO}": "Solo el 7.º día de cada semana (aldea nivel 3 o más)"}
    for dif, titulo in (("facil", "fáciles"), ("normal", "normales"), ("dificil", "difíciles")):
        filas = []
        for clave, d, txt, _, _, c in misiones.MISIONES:
            if d != dif: continue
            if c and "abierto_" in c and c.split("abierto_")[1].split()[0] not in mj_comun.JUEGOS: continue  # juego retirado
            if c and "abierto" in c: cuando = "Con el Maestro de Juegos (aldea nivel 2 o más), si las regatas están abiertas"
            else: cuando = cond.get(c, "Siempre") if c else "Siempre"
            filas.append((txt, misiones.SELLOS_MISION.get(clave, misiones.SELLOS[dif]), cuando))
        escribir(f"misiones_{dif}.md", tabla(["Misión", "Sellos", "Puede salir"], filas))
    escribir("misiones_semana.md", tabla(["Misión de la semana"], [(txt,) for _, txt, _, _, _ in misiones.SEMANALES])
             + f"\nSi la aldea la cumple, **todos los que hayan aportado algo** reciben **{misiones.SELLOS_SEMANA} sellos**.\n")


# ---------------------------------------------------------------- política
def politica():
    filas = [("Nombre de la aldea: propuestas", f"{votacion.PROPUESTAS_H} h",
              f"{votacion.POR_JUGADOR} nombres por jugador; si hay menos de {votacion.MIN_PROPUESTAS}, {votacion.PRORROGA_H} h más"),
             ("Nombre de la aldea: votación", f"{votacion.VOTACION_H} h", "Puntos 3, 2 y 1; no puedes votar lo tuyo"),
             ("Elecciones: candidaturas", f"{elecciones.CAMPANA_H} h", f"Si nadie se presenta, {elecciones.PRORROGA_H} h más"),
             ("Elecciones: votación", f"{elecciones.VOTACION_H} h", f"Un voto secreto; se reparten {elecciones.ESCANOS} escaños"),
             ("Una ley o proyecto: votación", f"{parlamento.VOTACION_H} h", "Una a la vez"),
             ("Entre una ley y la siguiente", f"{parlamento.ESPERA_H} h", "Lo que tiene que esperar el Alcalde")]
    escribir("plazos.md", tabla(["Qué", "Dura", "Detalles"], filas) +
             "\nLas horas solo cuentan **con el servidor encendido**. Mientras dura, se recuerda en el chat cada "
             f"{elecciones.RECORDATORIO_MIN} minutos.\n")
    escribir("modos_ley.md", tabla(["Modo", "Quién vota"], [(f"**{n}**", d[0].upper() + d[1:] + ".") for n, d in parlamento.MODOS.values()]))
    nombres = {"primero": "Autor del nombre ganador", "segundo": "Autor del 2.º", "tercero": "Autor del 3.º",
               "pluma": "Quien más puntos sume con todos sus nombres"}
    escribir("premios_nombre.md", tabla(["Quién", "Premio"], [(nombres[k], f"{n} × Chip {ROMANO[nivel]}")
                                                            for k, (nivel, n) in votacion.PREMIOS.items()]))


# ---------------------------------------------------------------- iglesia, justicia, hacienda (datos en el plugin Puente)
PUENTE = os.path.join(HERRAMIENTAS, "puente", "src", "es", "servidor", "puente")
MATERIAL = {"ROTTEN_FLESH": "Carne podrida", "BONE": "Hueso", "SPIDER_EYE": "Ojo de araña", "GUNPOWDER": "Pólvora",
            "ENDER_PEARL": "Perla de Ender", "WITHER_SKELETON_SKULL": "Cráneo de esqueleto del Wither",
            "PLAYER_HEAD": "Cabeza de jugador", "DIAMOND": "Diamante", "EMERALD": "Esmeralda", "RABBIT_FOOT": "Pata de conejo",
            "GOLD_NUGGET": "Pepita de oro", "GOLD_INGOT": "Lingote de oro", "SUNFLOWER": "Girasol", "BREAD": "Pan",
            "HONEY_BOTTLE": "Botella de miel", "GOLDEN_APPLE": "Manzana dorada", "GLOWSTONE_DUST": "Polvo de piedra luminosa"}


def java(nombre_clase):
    return open(os.path.join(PUENTE, f"{nombre_clase}.java"), encoding="utf-8").read()


def java_int(fuente, nombre_cte):
    """Constante entera del Java; vale también un producto como 20 * 60."""
    expr = re.search(rf"\b{nombre_cte}\s*=\s*(\d+(?:\s*\*\s*\d+)*)", fuente).group(1)
    n = 1
    for f in expr.split("*"): n *= int(f)
    return n


def iglesia():
    src = java("Iglesia")
    caminos = {i: (n, int(p)) for i, n, p in re.findall(r'new Camino\("(\w+)", "([^"]+)", Material\.\w+, (\d+)\)', src)}
    bendiciones = {i: (n, int(c), " ".join(e)) for i, n, c, *e in
                   [(m[0], m[1], m[2], *re.findall(r'"([^"]*)"', m[3])) for m in
                    re.findall(r'new Bendicion\("(\w+)", "([^"]+)", Material\.\w+, (\d+), ((?:"[^"]*",?\s*)+)\)', src)]}
    filas = []
    for bloque in re.findall(r'DIOSES\.put\((.*?)Particle\.\w+\)\);', src, re.S):
        nom = re.search(r'new Dios\("\w+", "([^"]+)"', bloque).group(1)
        listas = re.findall(r'List\.of\(([^)]*)\)', bloque)
        desc = " ".join(re.findall(r'"([^"]*)"', listas[0]))
        cam = [caminos[c] for c in re.findall(r'"(\w+)"', listas[1])]
        ben = [bendiciones[b] for b in re.findall(r'"(\w+)"', listas[2])]
        ofr = re.findall(r'Material\.(\w+), new int\[\]\{(\d+), (\d+)\}', re.search(r'Map\.of\((.*?)\),\s*List', bloque, re.S).group(1))
        filas.append((f"**{nom}**", desc,
                      "<br>".join(f"{n}: +{p}" for n, p in cam),
                      "<br>".join(f"{q} × {MATERIAL.get(m, m)}: +{p}" for m, p, q in ofr),
                      "<br>".join(f"**{n}** ({c}): {e}" for n, c, e in ben)))
    escribir("dioses.md", tabla(["Dios", "Cómo es", "Devoción por actos", "Ofrendas que acepta", "Bendiciones (coste)"], filas))
    escribir("caminos.md", tabla(["Acto", "Devoción"], [(n, f"+{p}") for n, p in caminos.values()]))
    escribir("bendiciones.md", tabla(["Bendición", "Coste", "Qué hace"], [(f"**{n}**", c, e) for n, c, e in bendiciones.values()]))
    escribir("iglesia_numeros.md", tabla(["Qué", "Cuánto"], [
        ("Rezar (una vez al día)", f"+{java_int(src, 'REZAR')} devoción"),
        ("Tope de devoción por actos al día", str(java_int(src, "TOPE_DIARIO"))),
        ("Ofrendas", "sin tope; cada chip I = +1 (las chips y los diamantes van al Tesoro de la aldea)"),
        ("Fundar una religión", f"{oficina.IGLESIA_PRECIO[0]} diamantes o {oficina.IGLESIA_PRECIO[1]} chips I")]))


def justicia():
    src = java("Justicia")
    escribir("justicia_numeros.md", tabla(["Qué", "Cuánto"], [
        ("Multa si el jurado declara culpable", f"{java_int(src, 'MULTA_JURADO')} chips I (al Tesoro)"),
        ("Fianza para salir de la cárcel", f"{java_int(src, 'FIANZA_POR_MINUTO')} chips I por minuto que te quede")]))
    d = oficina.DEFECTO
    escribir("impuestos.md", tabla(["Impuesto", "Qué se cobra", "Al empezar"], [
        ("**Sobre premios**", "Un % de los sellos y chips que ganas en misiones y minijuegos", f"{d['#imp_premios']} %"),
        ("**A los ricos** (semanal)", "Un % de lo que haya en tus buzones por encima del mínimo exento",
         f"{d['#imp_riqueza']} % de lo que pase de {d['#imp_umbral']} chips I"),
        ("**A las empresas** (semanal, con SEPE)", "Un % de lo que haya en la caja de cada empresa", f"{d['#imp_empresas']} %")])
             + f"\nEl Alcalde puede cambiarlos (entre 0 y {java_int(java('Oficina'), 'MAX_IMP')} %). Cada cambio se anuncia a todos.\n")
    escribir("sepe_numeros.md", tabla(["Qué", "Cuánto"], [
        ("Registrar una empresa", f"{barberia.PRECIO_DIAMANTES} diamantes o {barberia.PRECIO_CHIPS} chips I (van al Tesoro)"),
        ("Premio de la Empresa de la semana", f"{oficina.PREMIO_EMPRESA} chips I + la Placa de la Empresa de la Semana")]))


MOB_ASEDIO = {"zombi": "Zombi", "esqueleto_comun": "Esqueleto", "arana": "Araña", "zombi_acorazado": "Zombi acorazado"}


def mob_asedio(clave):
    return MOB_ASEDIO.get(clave) or texto(build.MOBS[clave]["CustomName"])


def asedios():
    filas = []
    for a in asedio.ASEDIOS:
        lo, hi = a["niveles"]
        cuando = "Recién fundada, nivel 1 o 2" if lo == 0 else (f"Nivel {lo}" if lo == hi else f"Niveles {lo} y {hi}")
        rondas = []
        for k, r in enumerate(a["rondas"], start=1):
            linea = f"**{k}.** {r['base']} + {r['por_jugador']} por defensor: " + ", ".join(mob_asedio(m) for m, _ in r["mobs"])
            if "jefe" in r:
                linea += f" · jefe: **{texto(asedio.JEFES_ASEDIO[r['jefe']][0]['CustomName'])}**"
            rondas.append(linea)
        p = a["premio"]
        premio = [f"{p['chip1'][0]}-{p['chip1'][1]} × Chip I"]
        if "chip2" in p: premio.append(f"Chip II · {pct(p['chip2'])}")
        if "chip2_seguras" in p: premio.append(f"{p['chip2_seguras'][0]} × Chip II")
        filas.append((cuando, "<br>".join(rondas), "<br>".join(premio)))
    escribir("asedios.md", tabla(["Aldea", "Rondas (monstruos)", "Premio para cada defensor"], filas))
    jefes_vida = ", ".join(f"{texto(j[0]['CustomName'])} {j[1]}" for j in asedio.JEFES_ASEDIO.values())
    escribir("asedio_numeros.md", tabla(["Qué", "Cuánto"], [
        ("Vida de la Campana", str(asedio.VIDA_CAMPANA)),
        ("Tiempo para prepararse", f"{asedio.PREPARACION_S} segundos"),
        ("Descanso entre rondas", f"{asedio.PAUSA_S} segundos"),
        ("Vida que quita a la Campana cada segundo pegado a ella",
         f"monstruo normal {asedio.GOLPE['normal']} · de mazmorra {asedio.GOLPE['mazmorra']} · jefe {asedio.GOLPE['jefe']}"),
        ("Vida de los jefes del asedio", jefes_vida)]))


def guerra():
    src = java("Guerra")
    escribir("guerra_numeros.md", tabla(["Qué", "Cuánto"], [
        ("Matar a un ciudadano enemigo", f"+{java_int(src, 'PUNTOS_MUERTE')} punto"),
        ("Ganar un asedio", f"+{java_int(src, 'PUNTOS_ASEDIO')} puntos y el {java_int(src, 'TRIBUTO')} % del Tesoro enemigo"),
        ("Rendirse", f"pagas el {java_int(src, 'TRIBUTO')} % de tu Tesoro al enemigo"),
        ("Duración de un asedio", f"{java_int(src, 'DURACION_S') // 60} minutos"),
        ("Ocupación para conquistar", f"{java_int(src, 'CONQUISTA_S') // 60} minutos en total"),
        ("Zona de la Campana", f"{java_int(src, 'ZONA')} bloques alrededor")]))


def regatas():
    import json
    import barcos
    datos = json.load(open(os.path.join(HERRAMIENTAS, "..", "plugins", "Puente", "barcos.json"), encoding="utf-8"))["mapas"]
    filas = []
    for k, (nom, _, _) in barcos.MAPAS.items():
        m = datos.get(k)
        if not m: continue
        modos = "Carrera, Clasificación" + (", Gestión" if m.get("boxes") else "")
        filas.append((f"**{nom}**", f"~{m['largo']} bloques", len(m["parrilla"]), modos, barcos.COPAS[k][0]))
    escribir("pistas.md", tabla(["Pista", "Una vuelta", "Barcos en la parrilla", "Modos", "Copa del 1.º de la semana"], filas))
    v = barcos.VUELTAS
    base, rival = barcos.PREMIO_CARRERA["carrera"]
    escribir("regatas_numeros.md", tabla(["Qué", "Cuánto"], [
        ("Vueltas", f"Carrera {v['carrera']} · Gestión {v['gestion']} · Clasificación: las que quieras"),
        ("Salida en falso (Carrera)", f"+{barcos.PENALIZACION_SALIDA} s"),
        ("Gestión sin usar 2 neumáticos distintos", f"+{barcos.PENALIZACION_SIN_PARADA} s"),
        ("Ganar una carrera", f"{base} chips I + {rival} por cada rival (como mucho {barcos.TOPE_PREMIOS_DIA} premios al día)"),
        ("Top 3 de la semana (cada pista, en Clasificación y en Gestión)",
         " · ".join(f"{n}.º {c} chips I" for n, c in enumerate(barcos.PREMIO_SEMANA, start=1)) + " · y el 1.º, la copa de la pista"),
        ("Probabilidad de lluvia / de noche cada día", f"{pct(barcos.PROB_LLUVIA)} / {pct(barcos.PROB_NOCHE)}"),
        ("Parada en boxes", f"{barcos.RUEDAS_PARADA} teclas, {barcos.VENTANA_TICKS / 20:g} s para cada una")]))
    escribir("neumaticos.md", tabla(["Neumático", "Hielo azul (más rápido)", "Se gasta por vuelta", "Dura unas", "Con lluvia"], [
        (f"**{n['nombre']}**", "nada" if not n["hielo"] else f"{pct(n['hielo'])} del hielo compacto", f"{n['desgaste']} %",
         f"{round(100 / n['desgaste'])} vueltas", "igual" if n["lluvia"] == 1 else f"se gasta un {round((n['lluvia'] - 1) * 100)} % más")
        for n in barcos.NEUMATICOS.values()]))


def cabezas_tablas():
    import cabezas
    r = cabezas.RAREZAS
    escribir("cofres_cabezas.md", tabla(["Cofre", "Se abre con"] + [x.capitalize() for x in r], [
        (f"**{texto(cabezas.NOMBRE_COFRE[n])}**", f"1 × Chip {ROMANO[n]}", *[f"{cabezas.PESOS[n][x]} %" for x in r])
        for n in sorted(cabezas.PESOS)]))
    escribir("sets_cabezas.md", tabla(["Set", "Cabezas", "Premio al completarlo"], [
        (f"**{s['nombre']}**", len(s["cabezas"]), f"{len(s['cabezas']) * cabezas.PREMIO_POR_CABEZA} chips I + Trofeo")
        for s in sorted(cabezas.CATALOGO.values(), key=lambda s: -len(s["cabezas"]))]))

    def chips(cuartos):
        if cuartos == 4: return "1 chip I"
        return f"{cuartos // 4} chips I" if cuartos % 4 == 0 else f"{cuartos}/4 de chip I" if cuartos < 4 else f"{cuartos / 4:g} chips I"
    escribir("reciclar_cabezas.md", tabla(["Rareza", "Reciclar una repetida"], [
        (x.capitalize(), "no se recicla" if not c else chips(c)) for x, c in cabezas.RECICLAR.items()])
             + "\nLos cuartos de chip se guardan y se suman la próxima vez que recicles.\n")


def crimen_tablas():
    """Los bajos fondos (crimen.py). Las recetas del Alquimista no se publican: se ven al investigar cada cosa."""
    R, niveles = crimen.REGLAS, {n["id"]: n["nombre"] for n in crimen.NIVELES}

    def efectos(lista):
        return ", ".join(f"{crimen.EFECTOS[e]} {ROMANO[n + 1]} ({s // 60} min)" if s >= 60 and s % 60 == 0 else
                         f"{crimen.EFECTOS[e]} {ROMANO[n + 1]} ({s} s)" for e, n, s in lista)

    def requisitos(n):
        r = []
        if n.get("edad"): r.append(f"edad del {crimen.EDADES[n['edad']]}")
        if n.get("miembros"): r.append(f"{n['miembros']} miembros")
        if n.get("ventas"): r.append(f"{n['ventas']} ventas al Perista")
        if n.get("fm"): r.append(f"pagar {n['fm']} Fichas marcadas")
        if n.get("fm2"): r.append(f"pagar {n['fm2']} Fichas marcadas II")
        if n.get("legendario"): r.append(f"{n['legendario']} material legendario de mazmorra")
        if n.get("dias"): r.append(f"haber aguantado una redada o llevar {n['dias']} días")
        return ", ".join(r) if r else f"fundarla: {crimen.FUNDAR['chips']} chips I"
    escribir("crimen_niveles.md", tabla(["Nivel", "Miembros (máx.)", "Tandas a la vez", "Mercancía al día", "Matas plantadas (máx.)", "Para llegar"], [
        (f"**{n['nombre']}**", n["max"], n["tandas"], n["produccion"], n["matas"], requisitos(n)) for n in crimen.NIVELES]))
    invest = {i["id"]: i for i in crimen.INVESTIGACION}
    escribir("crimen_mercancia.md", tabla(["Mercancía", "Familia", "Efecto", "Bajón (después)", "Experiencia", "El Perista paga", "Quiere al día", "Hace falta ser"], [
        (f"**{d['nombre']}**", crimen.FAMILIAS[d["familia"]], efectos(d["buenos"]), efectos(d["malos"]), f"+{d['xp']}",
         f"{d['precio']} FM", d["demanda"], niveles[invest[d["id"]]["nivel"]]) for d in crimen.DROGAS]))
    edad = {"épica": "hierro", "legendaria": "diamante"}
    escribir("crimen_armas.md", tabla(["Arma", "Rareza", "Qué hace", "Se puede usar desde", "Hace falta ser"], [
        (f"**{a['nombre']}**" + (f" (de {a['cantidad']} en {a['cantidad']})" if a["cantidad"] > 1 else ""), a["rareza"].capitalize(),
         " ".join(a["desc"]), f"la edad del {edad[a['rareza']]}" if a["rareza"] in edad else "siempre", niveles[invest[a["id"]]["nivel"]])
        for a in crimen.ARMAS]))

    def coste(i):
        c = []
        if i["fm"]: c.append(f"{i['fm']} FM")
        if i["fm2"]: c.append(f"{i['fm2']} FM II")
        for ing, n in i["materiales"]:
            t, x = ing.split(":")
            c.append(f"{n} × " + (build.MATERIALES[x][0] if t == "mazmorra" else crimen.NOMBRES[ing]))
        return ", ".join(c) if c else "gratis"

    def tiempo(m):
        return f"{m // 60} h" if m % 60 == 0 else f"{m // 60} h {m % 60} min" if m > 60 else f"{m} min"
    nombres = {**{d["id"]: d["nombre"] for d in crimen.DROGAS}, **{a["id"]: a["nombre"] for a in crimen.ARMAS}}
    escribir("crimen_investigacion.md", tabla(["Qué", "Hace falta ser", "Tarda", "Cuesta"], [
        (f"**{nombres[i['id']]}**", niveles[i["nivel"]], tiempo(i["min"]), coste(i)) for i in crimen.INVESTIGACION]))
    escribir("crimen_plantas.md", tabla(["Sale", "Al cortar", "Probabilidad", "Hace falta haber investigado"], [
        (f"**{p['nombre']}**", {"tall_grass": "Hierba alta", "large_fern": "Helecho grande"}[p["de"]], pct(p["prob"]), nombres[p["necesita"]])
        for p in crimen.PLANTAS]))
    escribir("crimen_cultivo.md", tabla(["Planta", "La mata parece", "Tarda", "Cosecha"], [
        (f"**{p['nombre']}**", {"wheat": "trigo", "beetroots": "remolacha"}.get(p["cultivo"]["bloque"], p["cultivo"]["bloque"]),
         tiempo(p["cultivo"]["min"]), f"{p['cultivo']['cosecha'][0]} a {p['cultivo']['cosecha'][1]}")
        for p in crimen.PLANTAS if p.get("cultivo")]))
    plural = lambda i: "prueba" if i == 0 else "pruebas"
    escribir("crimen_cuerpo.md", tabla(["Qué", "Cuánto"], [
        ("Tolerancia (por familia)", f"+{R['tol_dosis']} por dosis (máx. {R['tol_max']}); baja {R['tol_baja_h']} por hora sin tomar"),
        ("Con tolerancia", "el efecto dura menos (con 100, un 67 % menos) y el bajón, más (con 100, el doble)"),
        ("Sobredosis", f"{R['sobredosis_dosis']} dosis en {R['sobredosis_min']} min: Náuseas 10 s y Lentitud 30 s (no mata)"),
        ("Dependencia (por familia)", f"+{R['dep_dosis']} por dosis a partir de la {R['dep_desde']}.ª en 24 h; baja {R['dep_baja_h']} por hora conectado sin tomar"),
        ("Mono", f"con {R['mono_dep']} de dependencia o más y {R['mono_tras_min'] // 60} h conectado sin tomar: cada {R['mono_cada_min']} min, "
                 f"30 s de Hambre o Fatiga minera (desde {R['mono_fuerte']}, Debilidad en vez de Hambre). Nunca quita vida"),
        ("Fin del mono", f"tomando; con algo más flojo de la misma familia (1 h de calma y −{R['dep_dosis']}); con el Cura; "
                         f"o solo, a las {R['mono_fin_min'] // 60} h (la dependencia baja a {R['mono_fin_dep']})"),
        ("Desintoxicación (Cura)", f"{R['desintox_devocion']} de devoción: dependencia a 0 en 1 h, sin mono mientras")]))
    escribir("crimen_policia.md", tabla(["Qué", "Cuánto"], [
        ("Agentes", f"hasta {R['agentes']} por aldea (los nombra el Juez)"),
        ("Cacheos", f"{R['cacheos_dia']} al día por policía; al mismo jugador, uno cada {R['cacheo_mismo_min']} min; a {R['cacheo_distancia']} bloques"),
        ("Multa del cacheo", f"el doble del precio base de lo que lleve (armas épicas {R['multa_arma_epica']}, legendarias "
                             f"{R['multa_arma_legendaria']} chips I), al Tesoro"),
        ("Tomar mercancía en una aldea delante de un policía", f"{R['multa_leve']} chips I"),
        ("Pistas de la guarida", " · ".join(f"{i + 1} {plural(i)}: círculo de {r} bloques" for i, r in enumerate(R["pistas"]))),
        ("Orden de registro", f"{R['pruebas_orden']} pruebas (duran {R['pruebas_dias']} días); la organización, con más de {R['redada_org_dias']} días"),
        ("Soplo acertado", f"cuenta como prueba y, si la redada sale bien, el {R['chivato_pct']} % de lo requisado")]))
    escribir("crimen_redadas.md", tabla(["Qué", "Cuánto"], [
        ("Chivatazo a la organización", f"{R['redada_aviso_min']} min antes"),
        ("Duración", f"{R['redada_min']} min; zona de {R['redada_zona']} bloques alrededor del Alijo"),
        ("Para ganar la Policía", f"{R['redada_conquista_s'] // 60} min (en total) con policías dentro y nadie de la organización"),
        ("Sin nadie de la organización conectado", "registro sin combate: se requisa la mitad"),
        ("Lo requisado", f"mercancía y fichas al Tesoro a la mitad de su precio ({R['redada_agentes_pct']} % para los agentes); las armas se destruyen; "
                         f"como mucho {R['redada_tope_dia']} chips I al día por aldea"),
        ("Walter Brick detenido", f"{R['alquimista_pausa_h']} h sin trabajar y la investigación pierde un {R['alquimista_pierde_pct']} %"),
        ("Después", f"{R['redada_proteccion_h']} h sin redadas, gane quien gane")]))
    escribir("crimen_blanqueo.md", tabla(["Qué", "Cuánto"], [
        ("Cuánto se blanquea por semana", f"{R['blanqueo_base']} FM + {R['blanqueo_estrella']} por cada estrella de la empresa esa semana"),
        ("Lo que vuelve", f"el {R['blanqueo_limpio_pct']} % en chips I a la caja ({R['blanqueo_tesoro_pct']} % al Tesoro, el resto se pierde)"),
        ("La empresa", f"con más de {R['blanqueo_empresa_dias']} días"),
        ("Si Hacienda la pilla", f"fichas requisadas, empresa precintada {R['blanqueo_cierre_dias']} días y un caso en el Juzgado"),
        ("En la Iglesia", f"hasta {R['iglesia_fm']} FM a la semana: la mitad vuelve en chips I (y al Innombrable le gustan)")]))
    escribir("crimen_fundar.md", tabla(["Qué", "Cuánto"], [
        ("Para fundar o entrar", f"más de {R['horas_miembro']} h jugadas; no ser Juez ni agente"),
        ("Fundar", f"{crimen.FUNDAR['chips']} chips I y un cofre (el Alijo) a {crimen.FUNDAR['distancia']} bloques o más del centro de cualquier aldea, en el mundo normal"),
        ("El Perista", f"cada venta baja el precio un {round(R['perista_baja'] * 100)} % (hasta el {round(R['perista_minimo'] * 100)} %); "
                       f"se recupera en {R['perista_recupera_h']} h. Los precios y la demanda son para todo el servidor"),
        ("Fichas marcadas", "64 Fichas marcadas = 1 Ficha marcada II")]))


def main():
    dinero(); niveles(); campana(); tiendas(); proyectos(); taberna()
    mobs(); jefes(); trials(); cofres(); mercader(); forja_tablas(); magia_tablas(); misiones_tablas(); politica(); iglesia(); justicia()
    asedios(); guerra(); regatas(); cabezas_tablas(); crimen_tablas()
    print("Tablas generadas en", SALIDA)


if __name__ == "__main__":
    main()
