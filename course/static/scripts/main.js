'use strict';

$(function() {
    // navbar dropdown
    var $navbarBurgers = $('body').find('.navbar-burger');

    if ($navbarBurgers.length > 0) {
        $navbarBurgers.each(function(i){
            $(this).on('click', function(e) {
                e.preventDefault();

                var target = $(this).data('target'),
                    $target = $('#sidebar');

                $(this).toggleClass('is-active');
                $target.toggleClass('is-active');
            });
        });
    }
});

function throttle(fn, delay) {
    var last = void 0;
    var timer = void 0;

    return function () {
        var now = +new Date();

        if (last && now < last + delay) {
            clearTimeout(timer);

            timer = setTimeout(function () {
                last = now;
                fn ();
            }, delay);
        } else {
            last = now;
            fn ();
        }
    };
}

var isOffline = false;
window.addEventListener('load', checkConnectivity);

function checkConnectivity() {
    updateStatus();
    window.addEventListener('online', updateStatus);
    window.addEventListener('offline', updateStatus);
}

function updateStatus() {
    if (typeof navigator.onLine !== 'undefined') {
        isOffline = !navigator.onLine;
        document.documentElement.classList.toggle('is-offline', isOffline);
    }
    var notification = document.querySelector('#notification');
    if (isOffline) {
        notification.textContent = "You appear to be offline ";
        notification.removeAttribute('hidden');
    } else {
        notification.textContent = "";
        notification.removeAttribute('hidden');
    }
}

var links = document.querySelectorAll('a[href]');

Array.from(links).forEach((link) => {
    caches.match(link.href, { ignoreSearch: true }).then((response) => {
        if (response) {
            link.classList.add('is-cached');
        }
    });
});
