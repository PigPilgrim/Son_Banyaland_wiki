// Apartados que se movieron a otra página al reordenar la wiki (noviembre de 2026).
// Si alguien llega con un enlace viejo (por ejemplo minijuegos/#la-liga), lo lleva a su sitio nuevo.
// Las páginas no cambiaron de ruta: solo hay que redirigir los apartados (#) que ahora están en otra.
(function () {
  var MOVIDOS = {
    "": {
      "las-edades": "primeros-pasos/#las-edades",
      "normas-del-servidor": "primeros-pasos/#normas-del-servidor",
      "mazmorras-y-minijuegos": "primeros-pasos/#mazmorras-y-minijuegos"
    },
    "plugins/": {
      "registrarte-y-entrar": "primeros-pasos/#registrarte-y-entrar"
    },
    "minijuegos/": {
      "las-regatas": "regatas/#las-regatas",
      "las-pistas": "regatas/#las-pistas",
      "los-modos": "regatas/#los-modos",
      "clasificacion": "regatas/#clasificacion",
      "3-vueltas": "regatas/#3-vueltas",
      "gestion": "regatas/#gestion",
      "partidas-online": "regatas/#partidas-online",
      "neumaticos-modo-gestion": "regatas/#neumaticos-modo-gestion",
      "boxes": "regatas/#boxes",
      "rankings-y-premios-de-la-semana": "regatas/#rankings-y-premios-de-la-semana",
      "la-liga": "regatas/#la-liga",
      "gran-premio-del-dia": "regatas/#gran-premio-del-dia",
      "escuderias": "regatas/#escuderias",
      "premios-de-la-semana": "regatas/#premios-de-la-semana",
      "cabezas-coleccionables": "cabezas/",
      "el-album": "cabezas/#el-album",
      "reciclar-repetidas": "cabezas/#reciclar-repetidas"
    },
    "hacienda/": {
      "el-sepe-empresas": "empresas/",
      "registrar-una-empresa": "empresas/#registrar-una-empresa",
      "la-caja": "empresas/#la-caja",
      "duenos-y-empleados": "empresas/#duenos-y-empleados",
      "estrellas-y-empresa-de-la-semana": "empresas/#estrellas-y-empresa-de-la-semana"
    }
  };

  function mirar() {
    var ancla = decodeURIComponent(location.hash.slice(1));
    if (!ancla) return;
    var raiz = typeof __md_scope !== "undefined" ? __md_scope : new URL(".", location);
    var pagina = location.pathname.slice(raiz.pathname.length).replace(/index\.html$/, "");
    var destino = (MOVIDOS[pagina] || {})[ancla];
    if (destino) location.replace(new URL(destino, raiz).href);
  }

  if (typeof document$ !== "undefined") document$.subscribe(mirar);
  else mirar();
})();
