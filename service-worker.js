self.addEventListener("install", function(event) {
  event.waitUntil(
    caches.open("v1").then(function(cache) {
      return cache.addAll([
        "/",
        "/static/style.css",
        "/static/manifest.json",
        "/static/icon-192.png",
        "/static/icon-512.png"
      ]);
    })
  );
});

self.addEventListener("fetch", function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
self.addEventListener("install", e => {
  e.waitUntil(
    caches.open("ladli-cache").then(cache => {
      return cache.addAll([
        "/",
        "/static/style.css",
        "/static/manifest.json"
      ]);
    })
  );
});

self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request).then(response => response || fetch(e.request))
  );
});
