/**
 * Reveal.js 5.1.0 Bootstrapper & HUD Controller
 * Course: GCI World 2026 September · Matsuo-Iwasawa Lab (The University of Tokyo)
 * Strict Compliance: emoji_policy: none (Zero Unicode Emojis)
 */

(function () {
  'use strict';

  function createKeyboardHud() {
    if (document.getElementById('keyboard-hud-overlay')) return;

    var overlay = document.createElement('div');
    overlay.id = 'keyboard-hud-overlay';
    overlay.className = 'keyboard-hud-overlay';

    overlay.innerHTML = [
      '<div class="keyboard-hud-modal">',
      '  <h3>',
      '    <span>Bảng điều khiển & Phím tắt (Navigation & Controls HUD)</span>',
      '    <button id="close-hud-btn" style="background:transparent;border:none;color:#94a3b8;font-size:18px;cursor:pointer;">[X]</button>',
      '  </h3>',
      '  <div class="shortcut-row">',
      '    <span>Slide tiếp theo / Hiệu ứng con (Next Slide / Fragment)</span>',
      '    <span class="kbd-badge">Space / Right</span>',
      '  </div>',
      '  <div class="shortcut-row">',
      '    <span>Slide trước đó (Previous Slide)</span>',
      '    <span class="kbd-badge">Left</span>',
      '  </div>',
      '  <div class="shortcut-row">',
      '    <span>Tiến trình dọc (Chủ đề chuyên sâu - Vertical Progression)</span>',
      '    <span class="kbd-badge">Down / Up</span>',
      '  </div>',
      '  <div class="shortcut-row">',
      '    <span>Bật/Tắt lưới tổng quan 2D (Slide Overview Grid)</span>',
      '    <span class="kbd-badge">O hoặc Esc</span>',
      '  </div>',
      '  <div class="shortcut-row">',
      '    <span>Chế độ trình chiếu toàn màn hình (Fullscreen Mode)</span>',
      '    <span class="kbd-badge">F</span>',
      '  </div>',
      '  <div class="shortcut-row">',
      '    <span>Mở cửa sổ ghi chú diễn giả (Speaker Notes Console)</span>',
      '    <span class="kbd-badge">S</span>',
      '  </div>',
      '  <div class="shortcut-row">',
      '    <span>Tạm dừng / Màn hình đen (Pause / Blank Screen)</span>',
      '    <span class="kbd-badge">B hoặc .</span>',
      '  </div>',
      '  <div class="shortcut-row">',
      '    <span>Phóng to thành phần chỉ định (Zoom in on Element)</span>',
      '    <span class="kbd-badge">Alt + Click</span>',
      '  </div>',
      '  <div class="shortcut-row">',
      '    <span>Bật/Tắt bảng trợ giúp phím tắt này (Toggle Help HUD)</span>',
      '    <span class="kbd-badge">?</span>',
      '  </div>',
      '</div>'
    ].join('');

    document.body.appendChild(overlay);

    function toggleHud() {
      overlay.style.display = (overlay.style.display === 'flex') ? 'none' : 'flex';
    }

    document.getElementById('close-hud-btn').addEventListener('click', function () {
      overlay.style.display = 'none';
    });

    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) overlay.style.display = 'none';
    });

    window.addEventListener('keydown', function (e) {
      if (e.key === '?' || (e.shiftKey && e.key === '/')) {
        toggleHud();
      } else if (e.key === 'Escape' && overlay.style.display === 'flex') {
        overlay.style.display = 'none';
      }
    });

    var hudTriggerBtn = document.getElementById('hud-trigger-btn');
    if (hudTriggerBtn) {
      hudTriggerBtn.addEventListener('click', toggleHud);
    }
  }

  window.initGciReveal = function (customOptions) {
    createKeyboardHud();

    var defaults = {
      hash: true,
      slideNumber: 'c/t',
      navigationMode: 'grid',
      transition: 'slide',
      transitionSpeed: 'fast',
      backgroundTransition: 'fade',
      center: true,
      controls: true,
      progress: true,
      keyboard: true,
      overview: true,
      touch: true,
      plugins: [
        RevealMarkdown,
        RevealHighlight,
        RevealNotes,
        RevealMath.KaTeX,
        RevealZoom
      ]
    };

    var config = Object.assign({}, defaults, customOptions || {});

    return Reveal.initialize(config).then(function () {
      // Auto-mount widgets on active slide change
      Reveal.on('slidechanged', function (event) {
        if (window.GciWidgets && typeof window.GciWidgets.handleSlideChange === 'function') {
          window.GciWidgets.handleSlideChange(event.currentSlide);
        }
      });

      // Initial mount for the active slide
      if (window.GciWidgets && typeof window.GciWidgets.handleSlideChange === 'function') {
        window.GciWidgets.handleSlideChange(Reveal.getCurrentSlide());
      }
    }).catch(function (err) {
      console.error('Failed to initialize Reveal.js presentation:', err);
    });
  };
})();
