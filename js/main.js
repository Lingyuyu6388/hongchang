// 等待 DOM 加载
document.addEventListener('DOMContentLoaded', function() {

// 语言切换功能
let currentLang = 'zh';
const langToggle = document.getElementById('langToggle');
if (langToggle) {
    langToggle.addEventListener('click', function() {
        if (currentLang === 'zh') {
            currentLang = 'en';
            document.documentElement.lang = 'en';
        } else {
            currentLang = 'zh';
            document.documentElement.lang = 'zh-CN';
        }
        switchLanguage(currentLang);
    });
}

function switchLanguage(lang) {
    const elements = document.querySelectorAll('[data-zh][data-en]');
    elements.forEach(function(el) {
        const text = el.getAttribute('data-' + lang);
        if (text) {
            if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                el.placeholder = text;
            } else {
                el.innerHTML = text;
            }
        }
    });
}

// 移动端导航菜单切换
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

if (hamburger && navLinks) {
    hamburger.addEventListener('click', function() {
        navLinks.classList.toggle('active');
        const spans = hamburger.querySelectorAll('span');
        if (navLinks.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
        } else {
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });
}

const navItems = document.querySelectorAll('.nav-link');
navItems.forEach(function(item) {
    item.addEventListener('click', function() {
        if (navLinks && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
        }
    });
});

document.querySelectorAll('a[href^=\"#\"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offsetTop = target.offsetTop - 70;
            window.scrollTo({ top: offsetTop, behavior: 'smooth' });
        }
    });
});

window.addEventListener('scroll', function() {
    const navbar = document.getElementById('navbar');
    const backToTop = document.getElementById('backToTop');
    if (navbar) {
        if (window.scrollY > 50) { navbar.classList.add('scrolled'); }
        else { navbar.classList.remove('scrolled'); }
    }
    if (backToTop) {
        if (window.scrollY > 400) { backToTop.classList.add('show'); }
        else { backToTop.classList.remove('show'); }
    }
});

const backToTopBtn = document.getElementById('backToTop');
if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

function handleScrollAnimation() {
    const elements = document.querySelectorAll('.fade-in, .fade-up');
    elements.forEach(function(el) {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight * 0.85) {
            el.classList.add('visible');
        }
    });
}

window.addEventListener('scroll', handleScrollAnimation);
handleScrollAnimation();

function animateCounters() {
    const counters = document.querySelectorAll('.stat-number[data-target]');
    counters.forEach(function(counter) {
        const rect = counter.getBoundingClientRect();
        if (rect.top < window.innerHeight && !counter.dataset.animated) {
            counter.dataset.animated = 'true';
            const target = parseInt(counter.getAttribute('data-target'));
            const duration = 2000;
            const step = target / (duration / 16);
            let current = 0;
            function updateCounter() {
                current += step;
                if (current < target) {
                    counter.textContent = Math.floor(current);
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.textContent = target;
                }
            }
            updateCounter();
        }
    });
}

window.addEventListener('scroll', animateCounters);
animateCounters();

function updateActiveNav() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPos = window.scrollY + 100;
    sections.forEach(function(section) {
        const top = section.offsetTop;
        const height = section.offsetHeight;
        const id = section.getAttribute('id');
        const link = document.querySelector('.nav-link[href=\"#' + id + '\"]');
        if (link) {
            if (scrollPos >= top && scrollPos < top + height) {
                document.querySelectorAll('.nav-link').forEach(function(l) {
                    l.classList.remove('active');
                });
                link.classList.add('active');
            }
        }
    });
}

window.addEventListener('scroll', updateActiveNav);

const loader = document.getElementById('loader');
if (loader) {
    setTimeout(function() { loader.classList.add('hidden'); }, 800);
}

}); // DOMContentLoaded end
// 钻头包装盒图片切换
const drillBoxImages = ['images/drill-box-1.jpg', 'images/drill-box-2.jpg', 'images/drill-box-3.jpg', 'images/drill-box-4.jpg'];
function changeDrillBox(index) {
    const mainImg = document.querySelector('.gallery-main');
    const thumbs = document.querySelectorAll('.gallery-thumbs img');
    if (mainImg) {
        mainImg.style.opacity = '0.5';
        setTimeout(function() {
            mainImg.src = drillBoxImages[index];
            mainImg.style.opacity = '1';
        }, 150);
    }
    if (thumbs.length > 0) {
        thumbs.forEach(function(t) { t.classList.remove('active'); });
        thumbs[index].classList.add('active');
    }
}
// 产品详情弹窗
const popupImages = ['images/drill-box-1.jpg', 'images/drill-box-2.jpg', 'images/drill-box-3.jpg', 'images/drill-box-4.jpg'];
let currentPopupIndex = 0;

function openPopup() {
    const popup = document.getElementById('productPopup');
    if (popup) {
        popup.classList.add('show');
        document.body.style.overflow = 'hidden';
    }
}

function closePopup() {
    const popup = document.getElementById('productPopup');
    if (popup) {
        popup.classList.remove('show');
        document.body.style.overflow = '';
    }
}

function changePopupImg(index) {
    const mainImg = document.getElementById('popupMainImg');
    const thumbs = document.querySelectorAll('.popup-thumb');
    if (mainImg) {
        mainImg.style.opacity = '0.5';
        setTimeout(function() {
            mainImg.src = popupImages[index];
            mainImg.style.opacity = '1';
        }, 150);
    }
    if (thumbs.length > 0) {
        thumbs.forEach(function(t) { t.classList.remove('active'); });
        thumbs[index].classList.add('active');
    }
    currentPopupIndex = index;
}

// ESC 键关闭弹窗
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') { closePopup(); }
});