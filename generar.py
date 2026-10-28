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

import aldea, asedio, bebidas, casas, misiones, barberia, oficina, forja, magia, build, cofres_mazmorra  # noqa: E402

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
        filas = [("Vida", f"{j['vida']} ({j['vida'] // 2} ♥)"), ("Armadura", f"{attr.get('armor', 0):g}"),
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


def main():
    dinero(); niveles(); campana(); tiendas(); proyectos(); taberna()
    mobs(); jefes(); trials(); cofres(); mercader(); forja_tablas(); magia_tablas()
    print("Tablas generadas en", SALIDA)


if __name__ == "__main__":
    main()
