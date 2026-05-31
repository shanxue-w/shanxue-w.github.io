(function () {
  var toggle = document.querySelector(".nav-toggle");
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".site-nav a[data-section]"));

  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  if (!("IntersectionObserver" in window) || navLinks.length === 0) {
    return;
  }

  var linksById = navLinks.reduce(function (map, link) {
    map[link.getAttribute("data-section")] = link;
    return map;
  }, {});

  var headings = Object.keys(linksById)
    .map(function (id) {
      return document.getElementById(id);
    })
    .filter(Boolean);

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) {
          return;
        }
        navLinks.forEach(function (link) {
          link.classList.remove("is-active");
        });
        var activeLink = linksById[entry.target.id];
        if (activeLink) {
          activeLink.classList.add("is-active");
        }
      });
    },
    {
      rootMargin: "-25% 0px -65% 0px",
      threshold: 0.01
    }
  );

  headings.forEach(function (heading) {
    observer.observe(heading);
  });
})();
