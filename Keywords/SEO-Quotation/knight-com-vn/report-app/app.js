/* ============================================
   GOHA AUDIT REPORT — Interactive JS
   ============================================ */
document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initNavScroll();
    initNavHighlight();
    initTabs();
    initGauges();
    initCounters();
    initScoreBars();
    initCompareBars();
});

// ============ SCROLL ANIMATIONS ============
function initScrollAnimations() {
    const els = document.querySelectorAll(
        '.hm-card, .info-card, .score-card-hero, .s-item, .sw-card, ' +
        '.ps-card, .chip, .stat, .ux-card, .callout, .cta-box'
    );
    els.forEach(el => el.classList.add('animate-in'));

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((e, i) => {
            if (e.isIntersecting) {
                setTimeout(() => e.target.classList.add('visible'), i * 50);
                observer.unobserve(e.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    els.forEach(el => observer.observe(el));
}

// ============ NAV ============
function initNavScroll() {
    const nav = document.getElementById('nav');
    window.addEventListener('scroll', () => {
        nav.classList.toggle('scrolled', window.scrollY > 40);
    });
}

function initNavHighlight() {
    const sections = document.querySelectorAll('section[id]');
    const links = document.querySelectorAll('.nav-link');

    const obs = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                links.forEach(l => l.classList.remove('active'));
                const id = entry.target.id;
                const link = document.querySelector(`.nav-link[href="#${id}"]`);
                if (link) link.classList.add('active');
            }
        });
    }, { threshold: 0.3 });

    sections.forEach(s => obs.observe(s));
}

// ============ TABS ============
function initTabs() {
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => {
            const group = tab.closest('.section');
            group.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            group.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            tab.classList.add('active');
            document.getElementById(tab.dataset.tab).classList.add('active');
        });
    });
}

// ============ GAUGES ============
function initGauges() {
    const gauge = document.querySelector('.gauge-fill');
    if (!gauge) return;

    const obs = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const score = parseInt(gauge.dataset.score);
                const circ = 2 * Math.PI * 85;
                gauge.style.strokeDasharray = circ;
                gauge.style.strokeDashoffset = circ - (score / 100) * circ;
                if (score >= 70) gauge.style.stroke = '#22c55e';
                else if (score >= 50) gauge.style.stroke = '#eab308';
                else gauge.style.stroke = '#ef4444';
                obs.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    obs.observe(gauge.closest('.gauge-wrap'));
}

// ============ COUNTERS ============
function initCounters() {
    const counters = document.querySelectorAll('.gauge-num, .hm-value');
    counters.forEach(el => {
        const obs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = parseInt(el.dataset.target);
                    animate(el, target);
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        obs.observe(el);
    });
}

function animate(el, target) {
    let cur = 0;
    const dur = 1200;
    const step = target / (dur / 16);
    function tick() {
        cur += step;
        if (cur >= target) { el.textContent = target; return; }
        el.textContent = Math.floor(cur);
        requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
}

// ============ SCORE BARS ============
function initScoreBars() {
    document.querySelectorAll('.s-fill').forEach(fill => {
        const obs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const pct = fill.closest('.s-item').dataset.percent;
                    fill.style.setProperty('--w', pct + '%');
                    fill.style.width = pct + '%';
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });
        obs.observe(fill);
    });
}

// ============ COMPARE BARS ============
function initCompareBars() {
    document.querySelectorAll('.cb-fill').forEach(fill => {
        const obs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const w = getComputedStyle(fill).getPropertyValue('--w');
                    fill.style.width = w;
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });
        obs.observe(fill);
    });
}

// ============ PDF EXPORT ============
function exportPDF() {
    const overlay = document.getElementById('pdfOverlay');
    overlay.classList.add('active');
    forceComplete();
    setTimeout(() => {
        overlay.classList.remove('active');
        window.print();
    }, 1200);
}

function forceComplete() {
    document.querySelectorAll('.animate-in').forEach(el => el.classList.add('visible'));

    const gauge = document.querySelector('.gauge-fill');
    if (gauge) {
        const s = parseInt(gauge.dataset.score);
        const c = 2 * Math.PI * 85;
        gauge.style.strokeDasharray = c;
        gauge.style.strokeDashoffset = c - (s / 100) * c;
    }

    document.querySelectorAll('.gauge-num, .hm-value').forEach(el => {
        el.textContent = el.dataset.target;
    });

    document.querySelectorAll('.s-fill').forEach(fill => {
        const p = fill.closest('.s-item').dataset.percent;
        fill.style.width = p + '%';
    });

    document.querySelectorAll('.cb-fill').forEach(fill => {
        fill.style.width = getComputedStyle(fill).getPropertyValue('--w');
    });

    document.querySelectorAll('.tab-content').forEach(c => c.style.display = 'block');
}

window.addEventListener('afterprint', () => {
    document.querySelectorAll('.tab-content').forEach(c => {
        if (!c.classList.contains('active')) c.style.display = '';
    });
});
