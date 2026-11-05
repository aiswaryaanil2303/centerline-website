
document.addEventListener('DOMContentLoaded', function () {

    const animationGroups = [
        { selector: '.hero-content', effect: 'up' },
        { selector: '.about-image', effect: 'left' },
        { selector: '.about-content', effect: 'right' },
        { selector: '.about-features > div', effect: 'up', stagger: true },
        { selector: '.services-label, .services-title, .services-description', effect: 'up' },
        { selector: '.service-card', effect: 'up', stagger: true },
        { selector: '.solutions-heading', effect: 'up' },
        { selector: '.solutions-card', effect: 'up', stagger: true },
{ selector: '.clients-heading', effect: 'up' },
{ selector: '.client-card', effect: 'up', stagger: true },
        { selector: '.contact-content', effect: 'left' },
        { selector: '.contact-card', effect: 'right' },
        { selector: 'footer p', effect: 'up' }
    ];

    const elements = [];

    animationGroups.forEach(function (group) {

        document.querySelectorAll(group.selector).forEach(function (element, index) {

            element.classList.add('reveal-element', 'reveal-' + group.effect);

            if (group.stagger) {
                element.style.transitionDelay = (index * 120) + 'ms';
            }

            elements.push(element);
        });
    });

    const observer = new IntersectionObserver(function (entries) {

        entries.forEach(function (entry) {

            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-visible');
            } else {
                // Hide again when leaving the screen,
                // so it can animate again when scrolling back.
                entry.target.classList.remove('reveal-visible');
            }

        });

    }, {
        threshold: 0.15
    });

    elements.forEach(function (element) {
        observer.observe(element);
    });

    console.log('Scroll animations initialized');

});
