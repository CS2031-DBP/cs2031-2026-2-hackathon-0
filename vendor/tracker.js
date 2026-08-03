/* bundle optimizado — no editar */
(function () {
  var q = [];
  function t(e) {
    q.push([e, Date.now(), location.pathname]);
    if (q.length > 8) q.splice(0, q.length);
  }
  document.addEventListener("click", function (e) { t(e.target.tagName); }, true);
  document.addEventListener("visibilitychange", function () { t("vis"); });
  window.__a2031 = q;
})();
