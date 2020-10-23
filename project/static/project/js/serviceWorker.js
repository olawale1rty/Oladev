var staticCacheName = 'olawale-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/',
        '/new_client',
        '/blog',
        '/blog/comment',
        '/blog/search',
        '/static/project/css/style.css',
        '/static/blog/css/style.css',
        '/static/blog/js/main.js',
        '/static/project/js/main.js',
        '/static/project/js/typed.min.js',
        '/static/blog/js/typed.min.js',
        '/static/blog/browserconfig.xml',
        '/static/project/browserconfig.xml',
        '/static/project/img/apple-icon-57x57.png',
        '/static/blog/img/apple-icon-57x57.png',
        '/static/project/img/apple-icon-60x60.png',
        '/static/blog/img/apple-icon-60x60.png',
        '/static/project/img/apple-icon-72x72.png',
        '/static/blog/img/apple-icon-72x72.png',
        '/static/project/img/apple-icon-76x76.png',
        '/static/blog/img/apple-icon-76x76.png',
        '/static/project/img/apple-icon-114x114.png',
        '/static/blog/img/apple-icon-114x114.png',
        '/static/project/img/apple-icon-120x120.png',
        '/static/blog/img/apple-icon-120x120.png',
        '/static/project/img/apple-icon-144x144.png',
        '/static/project/img/apple-icon-152x152.png',
        '/static/project/img/apple-icon-180x180.png',
        '/static/project/img/apple-icon-512x512.png', 
        '/static/project/img/android-icon-192x192.png',
        '/static/project/img/android-icon-512x512.png',
        '/static/project/img/favicon-32x32.png',
        '/static/project/img/favicon-96x96.png',
        '/static/project/img/favicon-16x16.png',
        '/static/blog/img/apple-icon-144x144.png',
        '/static/blog/img/apple-icon-152x152.png',
        '/static/blog/img/apple-icon-180x180.png',
        '/static/blog/img/apple-icon-512x512.png', 
        '/static/blog/img/android-icon-192x192.png',
        '/static/blog/img/android-icon-512x512.png',
        '/static/blog/img/favicon-32x32.png',
        '/static/blog/img/favicon-96x96.png',
        '/static/blog/img/favicon-16x16.png',
        '/static/project/img/ms-icon-144x144.png',
        '/static/blog/img/ms-icon-144x144.png',
        '/static/project/vendor/bootstrap/css/bootstrap.min.css',
        '/static/project/vendor/icofont/icofont.min.css',
        '/static/project/vendor/animate/animate.css',
        '/static/project/vendor/remixicon/remixicon.css',
        '/static/project/vendor/owl.carousel/assets/owl.carousel.min.css',
        '/static/project/vendor/boxicons/css/boxicons.min.css',
        '/static/project/vendor/venobox/venobox.css',
        '/static/project/vendor/fontawesome-free/css/all.min.css',
        '/static/project/vendor/jquery/jquery.min.js',
        '/static/project/vendor/bootstrap/js/bootstrap.bundle.min.js',
        '/static/project/vendor/jquery.easing/jquery.easing.min.js',
        '/static/project/vendor/php-email-form/validate.js',
        '/static/project/vendor/waypoints/jquery.waypoints.min.js',
        '/static/project/vendor/counterup/counterup.min.js',
        '/static/project/vendor/owl.carousel/owl.carousel.min.js',
        '/static/project/vendor/isotope-layout/isotope.pkgd.min.js',
        '/static/project/vendor/venobox/venobox.min.js',
        '/static/project/vendor/sweetalert/sweetalert.min.js',
        '/static/blog/vendor/bootstrap/css/bootstrap.min.css',
        '/static/blog/vendor/icofont/icofont.min.css',
        '/static/blog/vendor/animate/animate.css',
        '/static/blog/vendor/remixicon/remixicon.css',
        '/static/blog/vendor/owl.carousel/assets/owl.carousel.min.css',
        '/static/blog/vendor/boxicons/css/boxicons.min.css',
        '/static/blog/vendor/venobox/venobox.css',
        '/static/blog/vendor/fontawesome-free/css/all.min.css',
        '/static/blog/vendor/jquery/jquery.min.js',
        '/static/blog/vendor/bootstrap/js/bootstrap.bundle.min.js',
        '/static/blog/vendor/jquery.easing/jquery.easing.min.js',
        '/static/blog/vendor/php-email-form/validate.js',
        '/static/blog/vendor/waypoints/jquery.waypoints.min.js',
        '/static/blog/vendor/counterup/counterup.min.js',
        '/static/blog/vendor/owl.carousel/owl.carousel.min.js',
        '/static/blog/vendor/isotope-layout/isotope.pkgd.min.js',
        '/static/blog/vendor/venobox/venobox.min.js',
        '/static/blog/vendor/sweetalert/sweetalert.min.js',
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});