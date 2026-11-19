/**
 * TACHREF STUDIO® — CORE JAVASCRIPT
 * Award-winning Editorial Micro-interactions, Canvas Visualizer & Controls
 */

document.addEventListener('DOMContentLoaded', () => {
  initCursor();
  initMobileMenu();
  initLiveClock();
  initScrollReveals();
  initHeroParallax();
  initProjectFilters();
  initProjectModals();
  initLabCanvas();
  initContactForm();
});

/* -------------------------------------------------------------
 * 1. CUSTOM CURSOR
 * ------------------------------------------------------------- */
function initCursor() {
  const isTouch = ('ontouchstart' in window) || navigator.maxTouchPoints > 0;
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (isTouch || prefersReduced) return;

  const cursor = document.createElement('div');
  cursor.className = 'custom-cursor';
  const follower = document.createElement('div');
  follower.className = 'custom-cursor-follower';

  document.body.appendChild(cursor);
  document.body.appendChild(follower);

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let followerX = mouseX;
  let followerY = mouseY;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursor.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;
  });

  function renderFollower() {
    followerX += (mouseX - followerX) * 0.15;
    followerY += (mouseY - followerY) * 0.15;
    follower.style.transform = `translate3d(${followerX}px, ${followerY}px, 0) translate(-50%, -50%)`;
    requestAnimationFrame(renderFollower);
  }
  requestAnimationFrame(renderFollower);

  // Hover states
  const interactives = document.querySelectorAll('a, button, input, textarea, select, .project-card, .department-card, .lab-item');
  interactives.forEach(el => {
    el.addEventListener('mouseenter', () => {
      cursor.style.transform += ' scale(2)';
      cursor.style.backgroundColor = '#ffffff';
      follower.style.borderColor = 'rgba(255, 94, 0, 0.9)';
      follower.style.transform += ' scale(1.6)';
    });
    el.addEventListener('mouseleave', () => {
      cursor.style.backgroundColor = 'var(--accent-orange)';
      follower.style.borderColor = 'rgba(255, 94, 0, 0.4)';
    });
  });
}

/* -------------------------------------------------------------
 * 2. MOBILE NAVIGATION
 * ------------------------------------------------------------- */
function initMobileMenu() {
  const btn = document.querySelector('.mobile-menu-btn');
  const overlay = document.querySelector('.mobile-nav-overlay');
  if (!btn || !overlay) return;

  btn.addEventListener('click', () => {
    const isOpen = btn.classList.toggle('active');
    overlay.classList.toggle('open', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  const links = overlay.querySelectorAll('a');
  links.forEach(l => {
    l.addEventListener('click', () => {
      btn.classList.remove('active');
      overlay.classList.remove('open');
      document.body.style.overflow = '';
    });
  });
}

/* -------------------------------------------------------------
 * 3. LIVE STUDIO CLOCK
 * ------------------------------------------------------------- */
function initLiveClock() {
  const clockEl = document.querySelector('.live-clock');
  if (!clockEl) return;

  function update() {
    const now = new Date();
    const utcHours = String(now.getUTCHours()).padStart(2, '0');
    const utcMins = String(now.getUTCMinutes()).padStart(2, '0');
    const utcSecs = String(now.getUTCSeconds()).padStart(2, '0');
    clockEl.textContent = `UTC ${utcHours}:${utcMins}:${utcSecs} // STUDIO OPERATIONAL`;
  }
  update();
  setInterval(update, 1000);
}

/* -------------------------------------------------------------
 * 4. SCROLL REVEALS
 * ------------------------------------------------------------- */
function initScrollReveals() {
  const revealElements = document.querySelectorAll('.department-card, .project-card, .community-banner, .lab-split, .section-header');
  if (!('IntersectionObserver' in window)) return;

  revealElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = 'opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1)';
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  revealElements.forEach(el => observer.observe(el));
}

/* -------------------------------------------------------------
 * 5. HERO 3D SCULPTURE PARALLAX
 * ------------------------------------------------------------- */
function initHeroParallax() {
  const stage = document.querySelector('.sculpture-stage');
  const imgWrap = document.querySelector('.sculpture-img-wrap');
  if (!stage || !imgWrap) return;

  window.addEventListener('mousemove', (e) => {
    const rect = stage.getBoundingClientRect();
    const stageCenterX = rect.left + rect.width / 2;
    const stageCenterY = rect.top + rect.height / 2;
    const deltaX = (e.clientX - stageCenterX) / (window.innerWidth / 2);
    const deltaY = (e.clientY - stageCenterY) / (window.innerHeight / 2);

    imgWrap.style.transform = `perspective(800px) rotateY(${deltaX * 12}deg) rotateX(${-deltaY * 12}deg) translateZ(10px)`;
  });

  stage.addEventListener('mouseleave', () => {
    imgWrap.style.transform = 'perspective(800px) rotateY(0deg) rotateX(0deg) translateZ(0)';
  });
}

/* -------------------------------------------------------------
 * 6. PROJECT FILTERS
 * ------------------------------------------------------------- */
function initProjectFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');
  if (!filterBtns.length || !projectCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 10);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(16px)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 250);
        }
      });
    });
  });
}

/* -------------------------------------------------------------
 * 7. PROJECT DETAILS MODAL
 * ------------------------------------------------------------- */
function initProjectModals() {
  const modal = document.querySelector('.modal-overlay');
  const modalClose = document.querySelector('.modal-close');
  if (!modal) return;

  const cards = document.querySelectorAll('.project-card[data-details]');

  cards.forEach(card => {
    card.addEventListener('click', () => {
      const title = card.querySelector('.project-title')?.textContent || 'Project Concept';
      const desc = card.querySelector('.project-desc')?.textContent || '';
      const dept = card.querySelector('.project-dept')?.textContent || '';
      const stack = card.querySelector('.project-stack')?.innerHTML || '';

      document.getElementById('modalTitle').textContent = title;
      document.getElementById('modalDept').textContent = dept;
      document.getElementById('modalDesc').textContent = desc;
      document.getElementById('modalStack').innerHTML = stack;

      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  if (modalClose) {
    modalClose.addEventListener('click', () => {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    });
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    }
  });
}

/* -------------------------------------------------------------
 * 8. INTERACTIVE LAB CANVAS (GENERATIVE QUANTUM VORTEX)
 * ------------------------------------------------------------- */
function initLabCanvas() {
  const canvas = document.getElementById('labCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width, height;
  let particles = [];
  const PARTICLE_COUNT = 90;

  function resize() {
    width = canvas.parentElement.clientWidth;
    height = canvas.parentElement.clientHeight - 45; // toolbar offset
    canvas.width = width * window.devicePixelRatio;
    canvas.height = height * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }
  window.addEventListener('resize', resize);
  resize();

  class Particle {
    constructor() {
      this.reset();
    }
    reset() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.vx = (Math.random() - 0.5) * 1.2;
      this.vy = (Math.random() - 0.5) * 1.2;
      this.radius = Math.random() * 2 + 1;
      this.color = Math.random() > 0.4 ? '#ff5e00' : (Math.random() > 0.5 ? '#00f5d4' : '#ffffff');
      this.alpha = Math.random() * 0.7 + 0.3;
    }
    update(mouseX, mouseY) {
      this.x += this.vx;
      this.y += this.vy;

      if (this.x < 0 || this.x > width) this.vx *= -1;
      if (this.y < 0 || this.y > height) this.vy *= -1;

      // Mouse attraction
      if (mouseX !== null) {
        const dx = mouseX - this.x;
        const dy = mouseY - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 130) {
          this.x += (dx / dist) * 1.8;
          this.y += (dy / dist) * 1.8;
        }
      }
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fillStyle = this.color;
      ctx.globalAlpha = this.alpha;
      ctx.fill();
    }
  }

  for (let i = 0; i < PARTICLE_COUNT; i++) {
    particles.push(new Particle());
  }

  let mouse = { x: null, y: null };
  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });
  canvas.addEventListener('mouseleave', () => {
    mouse.x = null;
    mouse.y = null;
  });

  function animate() {
    ctx.clearRect(0, 0, width, height);

    // Draw connecting lines
    for (let i = 0; i < particles.length; i++) {
      particles[i].update(mouse.x, mouse.y);
      particles[i].draw();

      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 90) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = 'rgba(255, 94, 0, ' + (1 - dist / 90) * 0.25 + ')';
          ctx.stroke();
        }
      }
    }

    requestAnimationFrame(animate);
  }
  animate();
}

/* -------------------------------------------------------------
 * 9. CONTACT FORM INTERACTION
 * ------------------------------------------------------------- */
function initContactForm() {
  const form = document.querySelector('.contact-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.innerHTML;

    btn.innerHTML = 'TRANSMITTING INQUIRY...';
    btn.style.opacity = '0.7';

    setTimeout(() => {
      btn.innerHTML = 'INQUIRY RECEIVED ✓';
      btn.style.backgroundColor = '#00f5d4';
      btn.style.color = '#000000';
      form.reset();

      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.style.backgroundColor = '';
        btn.style.color = '';
        btn.style.opacity = '1';
      }, 4000);
    }, 1200);
  });
}
