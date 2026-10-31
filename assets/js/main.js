// MAIN JAVASCRIPT FOR ADEEL ENGINEERING WORKS
import { COMPANY_INFO } from './products-data.js';

document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initMobileDrawer();
  initAccordion();
  initBackToTop();
  initWhatsAppButtons();
  highlightActiveNav();
});

// STICKY HEADER SCROLL EFFECT
function initHeader() {
  const header = document.querySelector('.header');
  if (!header) return;
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

// MOBILE DRAWER NAVIGATION
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const overlay = document.querySelector('.drawer-overlay');
  const closeBtn = document.querySelector('.drawer-close');

  if (!toggleBtn || !drawer || !overlay) return;

  function openDrawer() {
    drawer.classList.add('active');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('active');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  toggleBtn.addEventListener('click', openDrawer);
  overlay.addEventListener('click', closeDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);

  // Close when clicking an inner link
  drawer.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeDrawer);
  });
}

// ACCORDION FOR FAQS
function initAccordion() {
  const items = document.querySelectorAll('.accordion-item');
  items.forEach(item => {
    const header = item.querySelector('.accordion-header');
    if (!header) return;
    header.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      // Close others
      items.forEach(i => i.classList.remove('active'));
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });
}

// BACK TO TOP
function initBackToTop() {
  const btn = document.querySelector('.back-to-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// WHATSAPP BUTTONS CLICK HANDLER
function initWhatsAppButtons() {
  const phone = '923027012696'; // Adeel Niazi primary business WhatsApp
  const buttons = document.querySelectorAll('[data-whatsapp]');
  buttons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const product = btn.getAttribute('data-product') || 'industrial packing machinery';
      const text = encodeURIComponent(`Hello Adeel Engineering Works, I am inquiring about the ${product}. Please share specifications, pricing, and availability.`);
      window.open(`https://wa.me/${phone}?text=${text}`, '_blank');
    });
  });
}

// ACTIVE NAVIGATION LINK HIGHLIGHTER
function highlightActiveNav() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link, .dropdown-link, .drawer-nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    if (href === currentPath || (currentPath === '/' && href === '/index.html') || currentPath.endsWith(href)) {
      link.classList.add('active');
    }
  });
}
