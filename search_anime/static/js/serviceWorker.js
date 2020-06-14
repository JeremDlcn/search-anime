const cacheName = 'static-cache';

//dès l'installation on appelle les fichiers de l'app
self.addEventListener('install', async e => {
	const cache = await caches.open(cacheName);
	// on ajout les fichiers statiques
  cache.addAll([
        './',
        './index.html',
        './manifest.json',
        './static/css/styles.css',
        './static/font/H-Bold.otf',
        './static/font/H-Regular.otf',
        './static/js/search.js',
  ]);
});

// Le service worker va intercepté tout les fetch
// et regarder si ils sont en cache
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(cacheName)
      .then(cache => cache.match(event.request, { ignoreSearch: true }))
      .then(response => {
        return response || fetch(event.request);
      })
  );
});