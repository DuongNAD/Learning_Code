/**
 * ThreeUI Explorable Interactive Learning System & Slide Engine
 * Core Reactive Signal Engine, KaTeX Slot Binder, and Dual-View Controller
 *
 * Compliance: DeepTutor RFC 2119, emoji_policy: none
 * Architecture: Zero-dependency UMD/IIFE, sub-16.6ms reactive DAG, CLS = 0
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.ThreeUIEngine = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /**
   * High-precision performance timestamp helper
   */
  function nowMs() {
    if (typeof performance !== 'undefined' && performance.now) {
      return performance.now();
    }
    return Date.now();
  }

  /**
   * Safe localStorage wrapper for file:// and sandboxed environments
   */
  var storage = {
    getItem: function (key) {
      try {
        if (typeof window !== 'undefined' && window.localStorage) {
          return window.localStorage.getItem(key);
        }
      } catch (e) {
        /* Ignore storage errors under restricted file:// origins */
      }
      return null;
    },
    setItem: function (key, value) {
      try {
        if (typeof window !== 'undefined' && window.localStorage) {
          window.localStorage.setItem(key, value);
        }
      } catch (e) {
        /* Ignore storage errors under restricted file:// origins */
      }
    }
  };

  /**
   * Reactive Signal Engine (DAG)
   */
  function ReactiveEngine() {
    this.signals = Object.create(null);
    this.derived = Object.create(null);
    this.effects = [];
    this.dirtySignals = [];
    this.isFlushScheduled = false;
    this.subscriberGraph = Object.create(null); // nodeKey -> array of dependent node keys / effect IDs
    this.effectIdCounter = 0;
    this.latencyHistory = [];
    this.maxLatencyHistory = 60;
  }

  /**
   * Create a root reactive variable (Producer)
   * Supports: createSignal(key, initialValue) or createSignal(initialValue)
   */
  ReactiveEngine.prototype.createSignal = function (keyOrVal, maybeVal) {
    var key;
    var initialValue;
    if (typeof keyOrVal === 'string') {
      key = keyOrVal;
      initialValue = maybeVal;
    } else {
      key = 'sig_' + Math.random().toString(36).substr(2, 9);
      initialValue = keyOrVal;
    }

    var self = this;
    var signalObj = {
      key: key,
      value: initialValue,
      get: function () {
        return self.get(key);
      },
      set: function (newVal) {
        self.set(key, newVal);
      },
      subscribe: function (fn) {
        return self.createEffect([key], function (val) {
          fn(val);
        });
      }
    };

    this.signals[key] = signalObj;
    if (!this.subscriberGraph[key]) {
      this.subscriberGraph[key] = [];
    }

    return signalObj;
  };

  /**
   * Create a derived/computed variable (Intermediate DAG Node)
   * Supports: createDerived(key, deps, computeFn) or createDerived(deps, computeFn)
   */
  ReactiveEngine.prototype.createDerived = function (keyOrDeps, depsOrFn, maybeFn) {
    var key;
    var deps;
    var computeFn;

    if (typeof keyOrDeps === 'string') {
      key = keyOrDeps;
      deps = depsOrFn;
      computeFn = maybeFn;
    } else {
      key = 'der_' + Math.random().toString(36).substr(2, 9);
      deps = keyOrDeps;
      computeFn = depsOrFn;
    }

    var self = this;
    var derivedObj = {
      key: key,
      dependencies: deps,
      computeFn: computeFn,
      cachedValue: null,
      isDirty: true,
      get: function () {
        return self.get(key);
      },
      subscribe: function (fn) {
        return self.createEffect([key], function (val) {
          fn(val);
        });
      }
    };

    this.derived[key] = derivedObj;
    if (!this.subscriberGraph[key]) {
      this.subscriberGraph[key] = [];
    }

    // Register dependency links in graph
    for (var i = 0; i < deps.length; i++) {
      var depKey = deps[i];
      if (!this.subscriberGraph[depKey]) {
        this.subscriberGraph[depKey] = [];
      }
      this.subscriberGraph[depKey].push(key);
    }

    return derivedObj;
  };

  /**
   * Register a consumer effect (DOM, KaTeX, Canvas redraw)
   */
  ReactiveEngine.prototype.createEffect = function (deps, effectFn) {
    var self = this;
    var effectId = 'eff_' + (++this.effectIdCounter);
    var effectObj = {
      id: effectId,
      dependencies: deps,
      fn: effectFn,
      run: function () {
        var args = [];
        for (var i = 0; i < deps.length; i++) {
          args.push(self.get(deps[i]));
        }
        effectFn.apply(null, args);
      }
    };

    this.effects.push(effectObj);

    for (var i = 0; i < deps.length; i++) {
      var depKey = deps[i];
      if (!this.subscriberGraph[depKey]) {
        this.subscriberGraph[depKey] = [];
      }
      this.subscriberGraph[depKey].push(effectId);
    }

    // Execute immediately on initial mount
    try {
      effectObj.run();
    } catch (err) {
      if (typeof console !== 'undefined' && console.error) {
        console.error('[ThreeUI Reactive Effect Error]', err);
      }
    }

    // Return disposer function
    return function () {
      self.effects = self.effects.filter(function (e) {
        return e.id !== effectId;
      });
      for (var k in self.subscriberGraph) {
        self.subscriberGraph[k] = self.subscriberGraph[k].filter(function (id) {
          return id !== effectId;
        });
      }
    };
  };

  /**
   * Retrieve current value of signal or derived node
   */
  ReactiveEngine.prototype.get = function (key) {
    if (this.signals[key]) {
      return this.signals[key].value;
    }
    if (this.derived[key]) {
      var node = this.derived[key];
      if (node.isDirty) {
        var args = [];
        for (var i = 0; i < node.dependencies.length; i++) {
          args.push(this.get(node.dependencies[i]));
        }
        node.cachedValue = node.computeFn.apply(null, args);
        node.isDirty = false;
      }
      return node.cachedValue;
    }
    return undefined;
  };

  /**
   * Mutate a signal value and trigger batched DAG propagation
   */
  ReactiveEngine.prototype.set = function (key, value) {
    var sig = this.signals[key];
    if (!sig) {
      // Auto-create signal if not existing
      this.createSignal(key, value);
      sig = this.signals[key];
    }
    if (sig.value === value) {
      return;
    }
    sig.value = value;
    if (this.dirtySignals.indexOf(key) === -1) {
      this.dirtySignals.push(key);
    }
    this.scheduleFlush();
  };

  /**
   * Schedule batched flush on requestAnimationFrame (< 16.6ms / 60fps)
   */
  ReactiveEngine.prototype.scheduleFlush = function () {
    if (this.isFlushScheduled) {
      return;
    }
    this.isFlushScheduled = true;
    var self = this;

    if (typeof requestAnimationFrame === 'function') {
      requestAnimationFrame(function () {
        self.flush();
      });
    } else {
      setTimeout(function () {
        self.flush();
      }, 0);
    }
  };

  /**
   * Synchronous flush for hot loops or explicit updates
   */
  ReactiveEngine.prototype.flush = function () {
    var startTime = nowMs();
    this.isFlushScheduled = false;

    if (this.dirtySignals.length === 0) {
      return;
    }

    var dirtyRoots = this.dirtySignals.slice();
    this.dirtySignals = [];

    // Topological dirty marking
    var affectedDerived = Object.create(null);
    var affectedEffects = Object.create(null);
    var queue = dirtyRoots.slice();

    while (queue.length > 0) {
      var currentKey = queue.shift();
      var subscribers = this.subscriberGraph[currentKey] || [];
      for (var i = 0; i < subscribers.length; i++) {
        var subId = subscribers[i];
        if (subId.indexOf('eff_') === 0) {
          affectedEffects[subId] = true;
        } else if (this.derived[subId]) {
          if (!affectedDerived[subId]) {
            affectedDerived[subId] = true;
            this.derived[subId].isDirty = true;
            queue.push(subId);
          }
        }
      }
    }

    // Execute affected effects
    for (var j = 0; j < this.effects.length; j++) {
      var eff = this.effects[j];
      if (affectedEffects[eff.id]) {
        try {
          eff.run();
        } catch (err) {
          if (typeof console !== 'undefined' && console.error) {
            console.error('[ThreeUI Reactive Flush Error]', err);
          }
        }
      }
    }

    var elapsed = nowMs() - startTime;
    this.latencyHistory.push(elapsed);
    if (this.latencyHistory.length > this.maxLatencyHistory) {
      this.latencyHistory.shift();
    }
  };

  /**
   * Get rolling latency statistics
   */
  ReactiveEngine.prototype.getLatencyStats = function () {
    if (this.latencyHistory.length === 0) {
      return { avg: 0, max: 0, count: 0, fpsBound: 60 };
    }
    var sum = 0;
    var max = 0;
    for (var i = 0; i < this.latencyHistory.length; i++) {
      var val = this.latencyHistory[i];
      sum += val;
      if (val > max) {
        max = val;
      }
    }
    var avg = sum / this.latencyHistory.length;
    return {
      avg: Math.round(avg * 100) / 100,
      max: Math.round(max * 100) / 100,
      count: this.latencyHistory.length,
      fpsBound: max < 16.6 ? 60 : Math.round(1000 / max)
    };
  };

  /**
   * KaTeX Slot Binder (Zero Cumulative Layout Shift / CLS = 0)
   */
  ReactiveEngine.prototype.bindKatexSlot = function (slotSelectorOrId, signalOrKey, formatter) {
    var self = this;
    var depKey = typeof signalOrKey === 'string' ? signalOrKey : signalOrKey.key;
    var format = formatter || function (val) {
      if (typeof val === 'number') {
        return Number.isInteger(val) ? val.toString() : val.toFixed(2);
      }
      return String(val);
    };

    var effect = this.createEffect([depKey], function (newVal) {
      var el = null;
      if (typeof slotSelectorOrId === 'string') {
        if (slotSelectorOrId.charAt(0) === '#' || slotSelectorOrId.charAt(0) === '.') {
          el = document.querySelector(slotSelectorOrId);
        } else {
          el = document.getElementById(slotSelectorOrId) || document.querySelector('[data-slot="' + slotSelectorOrId + '"]');
        }
      } else if (slotSelectorOrId && slotSelectorOrId.nodeType) {
        el = slotSelectorOrId;
      }

      if (el) {
        var formatted = format(newVal);
        if (el.textContent !== formatted) {
          el.textContent = formatted;
          if (!el.classList.contains('dyn-slot')) {
            el.classList.add('dyn-slot');
          }
        }
      }
    });

    return effect;
  };

  /**
   * Dual-View Controller & Presentation Lifecycle
   */
  function DualViewController(engine) {
    this.engine = engine;
    this.viewMode = 'document'; // 'document' | 'deck'
    this.currentSlideIndex = 0;
    this.totalSlides = 0;
    this.currentStep = 0;
    this.totalStepsInSlide = 0;
    this.slides = [];
    this.initialized = false;
    this.scaleFactor = 1.0;
  }

  /**
   * Scan DOM and bind dual-view architecture
   */
  DualViewController.prototype.init = function () {
    if (typeof document === 'undefined') {
      return;
    }
    var self = this;

    // Collect slides
    var slideElements = document.querySelectorAll('.slide-frame, .threeui-slide, [data-slide-index]');
    this.slides = Array.prototype.slice.call(slideElements);
    this.totalSlides = this.slides.length;

    // Determine initial view mode from HTML/body or storage
    var storedView = storage.getItem('threeui_view_mode');
    var bodyAttr = document.body ? document.body.getAttribute('data-view') : null;
    var htmlAttr = document.documentElement.getAttribute('data-view');
    var initialMode = storedView || bodyAttr || htmlAttr || 'document';
    this.setViewMode(initialMode);

    // Bind keyboard navigation
    window.addEventListener('keydown', function (evt) {
      if (evt.ctrlKey || evt.altKey || evt.metaKey) return;
      self.handleKeyDown(evt);
    });

    // Bind auto-scaler on resize
    window.addEventListener('resize', function () {
      if (self.viewMode === 'deck') {
        self.fitDeckCanvas();
      }
    });

    window.addEventListener('orientationchange', function () {
      if (self.viewMode === 'deck') {
        setTimeout(function () {
          self.fitDeckCanvas();
        }, 100);
      }
    });

    this.initialized = true;
    this.updateHUD();
  };

  /**
   * Set View Mode: 'document' vs 'deck'
   */
  DualViewController.prototype.setViewMode = function (mode) {
    if (mode !== 'document' && mode !== 'deck') {
      mode = 'document';
    }
    this.viewMode = mode;
    storage.setItem('threeui_view_mode', mode);

    if (typeof document !== 'undefined' && document.body) {
      document.body.setAttribute('data-view', mode);
      document.documentElement.setAttribute('data-view', mode);

      if (mode === 'document') {
        document.body.classList.remove('threeui-view-deck');
        document.body.classList.add('threeui-view-doc');
        this.resetDeckScaling();
      } else {
        document.body.classList.remove('threeui-view-doc');
        document.body.classList.add('threeui-view-deck');
        this.fitDeckCanvas();
        this.goToSlide(this.currentSlideIndex, 0);
      }
    }

    this.updateViewButtons();
    this.updateHUD();

    // Dispatch custom event
    if (typeof window !== 'undefined' && window.dispatchEvent) {
      var evt;
      try {
        evt = new CustomEvent('threeui:viewchange', { detail: { mode: mode } });
      } catch (e) {
        evt = document.createEvent('CustomEvent');
        evt.initCustomEvent('threeui:viewchange', true, true, { mode: mode });
      }
      window.dispatchEvent(evt);
    }
  };

  /**
   * Toggle between document and deck view modes
   */
  DualViewController.prototype.toggleViewMode = function () {
    var nextMode = this.viewMode === 'document' ? 'deck' : 'document';
    this.setViewMode(nextMode);
  };

  /**
   * Reset deck stage transform when returning to document mode
   */
  DualViewController.prototype.resetDeckScaling = function () {
    var stage = document.querySelector('.slide-deck-stage, .threeui-deck-stage');
    if (stage) {
      stage.style.transform = '';
      stage.style.position = '';
      stage.style.left = '';
      stage.style.top = '';
    }
  };

  /**
   * 16:9 Projection auto-scaler using CSS transform: min(W/1920, H/1080)
   */
  DualViewController.prototype.fitDeckCanvas = function () {
    var stage = document.querySelector('.slide-deck-stage, .threeui-deck-stage');
    if (!stage) {
      return;
    }

    var targetW = 1920;
    var targetH = 1080;
    var winW = window.innerWidth;
    var winH = window.innerHeight;

    var scale = Math.min(winW / targetW, winH / targetH);
    this.scaleFactor = scale;

    stage.style.width = targetW + 'px';
    stage.style.height = targetH + 'px';
    stage.style.transform = 'scale(' + scale + ')';
    stage.style.transformOrigin = 'center center';
    stage.style.position = 'absolute';
    stage.style.left = ((winW - targetW * scale) / 2) + 'px';
    stage.style.top = ((winH - targetH * scale) / 2) + 'px';
  };

  /**
   * Navigate to specific slide index
   */
  DualViewController.prototype.goToSlide = function (slideIdx, targetStep) {
    if (this.totalSlides === 0) {
      return;
    }
    if (slideIdx < 0) {
      slideIdx = 0;
    }
    if (slideIdx >= this.totalSlides) {
      slideIdx = this.totalSlides - 1;
    }

    this.currentSlideIndex = slideIdx;
    var currentSlide = this.slides[slideIdx];

    // Count steps in current slide
    var steps = currentSlide ? currentSlide.querySelectorAll('[data-step]') : [];
    this.totalStepsInSlide = steps.length;

    if (typeof targetStep === 'number') {
      this.currentStep = Math.max(0, Math.min(targetStep, this.totalStepsInSlide));
    } else {
      this.currentStep = 0;
    }

    // Toggle slide visibility
    for (var i = 0; i < this.slides.length; i++) {
      var slide = this.slides[i];
      if (i === slideIdx) {
        slide.classList.add('active');
        slide.setAttribute('aria-hidden', 'false');
      } else {
        slide.classList.remove('active');
        slide.setAttribute('aria-hidden', 'true');
      }
    }

    // Apply stepper states
    this.applyStepStates();
    this.updateHUD();
  };

  /**
   * Apply progressive stepper reveals on current slide
   */
  DualViewController.prototype.applyStepStates = function () {
    var currentSlide = this.slides[this.currentSlideIndex];
    if (!currentSlide) {
      return;
    }

    var steps = currentSlide.querySelectorAll('[data-step]');
    for (var i = 0; i < steps.length; i++) {
      var stepEl = steps[i];
      var stepNum = parseInt(stepEl.getAttribute('data-step'), 10) || 1;
      if (stepNum <= this.currentStep) {
        stepEl.classList.add('step-revealed');
        stepEl.classList.remove('step-hidden');
      } else {
        stepEl.classList.remove('step-revealed');
        stepEl.classList.add('step-hidden');
      }
    }
  };

  /**
   * Advance step or slide
   */
  DualViewController.prototype.nextStepOrSlide = function () {
    if (this.currentStep < this.totalStepsInSlide) {
      this.currentStep++;
      this.applyStepStates();
      this.updateHUD();
    } else if (this.currentSlideIndex < this.totalSlides - 1) {
      this.goToSlide(this.currentSlideIndex + 1, 0);
    }
  };

  /**
   * Retreat step or slide
   */
  DualViewController.prototype.prevStepOrSlide = function () {
    if (this.currentStep > 0) {
      this.currentStep--;
      this.applyStepStates();
      this.updateHUD();
    } else if (this.currentSlideIndex > 0) {
      var prevSlide = this.slides[this.currentSlideIndex - 1];
      var prevSteps = prevSlide ? prevSlide.querySelectorAll('[data-step]').length : 0;
      this.goToSlide(this.currentSlideIndex - 1, prevSteps);
    }
  };

  /**
   * Keyboard Navigation Dispatcher
   */
  DualViewController.prototype.handleKeyDown = function (e) {
    if (e.ctrlKey || e.altKey || e.metaKey) return;
    // Avoid hijacking when typing into inputs, textareas or contenteditable
    var tag = e.target ? e.target.tagName : '';
    if (tag === 'INPUT' || tag === 'TEXTAREA' || e.target.isContentEditable) {
      return;
    }

    var key = e.key;

    // View-independent shortcuts
    if (key === 't' || key === 'T') {
      window.ThreeUIEngine.toggleTheme();
      e.preventDefault();
      return;
    }

    if (key === 'm' || key === 'M' || key === 'v' || key === 'V') {
      this.toggleViewMode();
      e.preventDefault();
      return;
    }

    if (key === 'f' || key === 'F') {
      this.toggleFullscreen();
      e.preventDefault();
      return;
    }

    if (key === 'o' || key === 'O') {
      this.toggleOverview();
      e.preventDefault();
      return;
    }

    // Deck-specific navigation shortcuts
    if (this.viewMode === 'deck') {
      if (key === 'ArrowRight' || key === ' ' || key === 'PageDown') {
        this.nextStepOrSlide();
        e.preventDefault();
      } else if (key === 'ArrowLeft' || key === 'PageUp') {
        this.prevStepOrSlide();
        e.preventDefault();
      } else if (key === 'Home') {
        this.goToSlide(0, 0);
        e.preventDefault();
      } else if (key === 'End') {
        this.goToSlide(this.totalSlides - 1, 0);
        e.preventDefault();
      }
    }
  };

  /**
   * Fullscreen Toggle
   */
  DualViewController.prototype.toggleFullscreen = function () {
    if (typeof document === 'undefined') {
      return;
    }
    if (!document.fullscreenElement) {
      var docEl = document.documentElement;
      if (docEl.requestFullscreen) {
        docEl.requestFullscreen();
      } else if (docEl.webkitRequestFullscreen) {
        docEl.webkitRequestFullscreen();
      }
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
      }
    }
  };

  /**
   * Toggle Slide Overview Drawer / Grid
   */
  DualViewController.prototype.toggleOverview = function () {
    var modal = document.querySelector('.slide-overview-modal, #slide-overview-modal');
    if (!modal) {
      modal = this.createOverviewModal();
    }
    if (modal) {
      var isOpen = modal.classList.contains('active');
      if (isOpen) {
        modal.classList.remove('active');
        modal.setAttribute('aria-hidden', 'true');
      } else {
        this.populateOverviewThumbnails(modal);
        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
      }
    }
  };

  /**
   * Dynamically build Overview Modal container if not present
   */
  DualViewController.prototype.createOverviewModal = function () {
    var modal = document.createElement('div');
    modal.className = 'slide-overview-modal';
    modal.id = 'slide-overview-modal';
    modal.setAttribute('aria-hidden', 'true');
    modal.innerHTML = '<div class="overview-backdrop"></div>' +
      '<div class="overview-content threeui-glass-card">' +
      '  <div class="overview-header">' +
      '    <div class="overview-title">[Slide Overview]</div>' +
      '    <button class="overview-close-btn" aria-label="Close">[Close (Esc/O)]</button>' +
      '  </div>' +
      '  <div class="overview-grid" id="overview-grid"></div>' +
      '</div>';

    document.body.appendChild(modal);

    var closeBtn = modal.querySelector('.overview-close-btn');
    var backdrop = modal.querySelector('.overview-backdrop');
    var self = this;
    var closeHandler = function () {
      modal.classList.remove('active');
      modal.setAttribute('aria-hidden', 'true');
    };
    if (closeBtn) closeBtn.addEventListener('click', closeHandler);
    if (backdrop) backdrop.addEventListener('click', closeHandler);

    return modal;
  };

  /**
   * Populate thumbnail tiles in overview grid
   */
  DualViewController.prototype.populateOverviewThumbnails = function (modal) {
    var grid = modal.querySelector('#overview-grid');
    if (!grid) return;
    grid.innerHTML = '';
    var self = this;

    for (var i = 0; i < this.slides.length; i++) {
      var slide = this.slides[i];
      var title = slide.getAttribute('data-slide-title') ||
                  (slide.querySelector('h1, h2, .slide-title') ? slide.querySelector('h1, h2, .slide-title').textContent : 'Slide ' + (i + 1));

      var thumb = document.createElement('button');
      thumb.className = 'overview-thumb ' + (i === this.currentSlideIndex ? 'active' : '');
      thumb.innerHTML = '<span class="thumb-idx">' + (i + 1) + '</span><span class="thumb-title">' + title + '</span>';
      (function (idx) {
        thumb.addEventListener('click', function () {
          self.goToSlide(idx, 0);
          modal.classList.remove('active');
          modal.setAttribute('aria-hidden', 'true');
        });
      })(i);
      grid.appendChild(thumb);
    }
  };

  /**
   * Update HUD Elements (Slide Counter, Progress Bar, Active Buttons)
   */
  DualViewController.prototype.updateHUD = function () {
    if (typeof document === 'undefined') {
      return;
    }

    // Update slide counter
    var counters = document.querySelectorAll('.slide-counter-hud, #slide-counter');
    var counterText = (this.currentSlideIndex + 1) + ' / ' + Math.max(1, this.totalSlides);
    for (var i = 0; i < counters.length; i++) {
      counters[i].textContent = counterText;
    }

    // Update progress bar
    var progressBars = document.querySelectorAll('.slide-progress-bar, #slide-progress');
    var pct = this.totalSlides > 1 ? ((this.currentSlideIndex) / (this.totalSlides - 1)) * 100 : 100;
    for (var j = 0; j < progressBars.length; j++) {
      progressBars[j].style.width = pct + '%';
    }
  };

  /**
   * Update View Switcher Buttons State
   */
  DualViewController.prototype.updateViewButtons = function () {
    var docBtns = document.querySelectorAll('[data-view-btn="document"], #view-doc-btn');
    var deckBtns = document.querySelectorAll('[data-view-btn="deck"], #view-deck-btn');

    for (var i = 0; i < docBtns.length; i++) {
      if (this.viewMode === 'document') {
        docBtns[i].classList.add('active');
      } else {
        docBtns[i].classList.remove('active');
      }
    }

    for (var j = 0; j < deckBtns.length; j++) {
      if (this.viewMode === 'deck') {
        deckBtns[j].classList.add('active');
      } else {
        deckBtns[j].classList.remove('active');
      }
    }
  };

  /**
   * Theme Controller
   */
  function ThemeController() {
    this.currentTheme = 'dark'; // 'dark' | 'light'
  }

  ThemeController.prototype.init = function () {
    if (typeof document === 'undefined') {
      return;
    }
    var saved = storage.getItem('threeui_theme');
    var initial = saved || document.documentElement.getAttribute('data-theme') || 'dark';
    this.setTheme(initial);
  };

  ThemeController.prototype.setTheme = function (theme) {
    this.currentTheme = theme === 'light' ? 'light' : 'dark';
    storage.setItem('threeui_theme', this.currentTheme);

    if (typeof document !== 'undefined') {
      document.documentElement.setAttribute('data-theme', this.currentTheme);
      if (document.body) {
        document.body.setAttribute('data-theme', this.currentTheme);
      }
    }

    this.updateThemeButtons();

    // Dispatch event
    if (typeof window !== 'undefined' && window.dispatchEvent) {
      var evt;
      try {
        evt = new CustomEvent('threeui:themechange', { detail: { theme: this.currentTheme } });
      } catch (e) {
        evt = document.createEvent('CustomEvent');
        evt.initCustomEvent('threeui:themechange', true, true, { theme: this.currentTheme });
      }
      window.dispatchEvent(evt);
    }
  };

  ThemeController.prototype.toggleTheme = function () {
    var next = this.currentTheme === 'dark' ? 'light' : 'dark';
    this.setTheme(next);
  };

  ThemeController.prototype.updateThemeButtons = function () {
    var btns = document.querySelectorAll('[data-theme-btn], #theme-toggle-btn');
    var label = this.currentTheme === 'dark' ? '[Theme: Dark]' : '[Theme: Light]';
    for (var i = 0; i < btns.length; i++) {
      btns[i].textContent = label;
      btns[i].setAttribute('data-theme-current', this.currentTheme);
    }
  };

  /**
   * Master ThreeUIEngine Facade
   */
  var reactiveEngine = new ReactiveEngine();
  var dualViewController = new DualViewController(reactiveEngine);
  var themeController = new ThemeController();

  var ThreeUIEngine = {
    version: '1.0.0',
    reactive: reactiveEngine,
    view: dualViewController,
    theme: themeController,

    // Core Reactive Signals API
    createSignal: function (k, v) {
      return reactiveEngine.createSignal(k, v);
    },
    createDerived: function (k, deps, fn) {
      return reactiveEngine.createDerived(k, deps, fn);
    },
    createEffect: function (deps, fn) {
      return reactiveEngine.createEffect(deps, fn);
    },
    get: function (k) {
      return reactiveEngine.get(k);
    },
    set: function (k, v) {
      reactiveEngine.set(k, v);
    },
    flushSync: function () {
      reactiveEngine.flush();
    },
    getLatencyStats: function () {
      return reactiveEngine.getLatencyStats();
    },

    // KaTeX Math Slot Binder
    bindKatexSlot: function (slotId, signalOrKey, formatter) {
      return reactiveEngine.bindKatexSlot(slotId, signalOrKey, formatter);
    },

    // View Management
    setViewMode: function (mode) {
      dualViewController.setViewMode(mode);
    },
    toggleViewMode: function () {
      dualViewController.toggleViewMode();
    },
    goToSlide: function (idx, step) {
      dualViewController.goToSlide(idx, step);
    },
    nextSlide: function () {
      dualViewController.nextStepOrSlide();
    },
    prevSlide: function () {
      dualViewController.prevStepOrSlide();
    },
    fitDeckCanvas: function () {
      dualViewController.fitDeckCanvas();
    },

    // Theme Management
    setTheme: function (theme) {
      themeController.setTheme(theme);
    },
    toggleTheme: function () {
      themeController.toggleTheme();
    },

    // UI Binding Helpers
    bindSlider: function (selectorOrEl, signalKey, formatter) {
      var el = typeof selectorOrEl === 'string' ? document.querySelector(selectorOrEl) : selectorOrEl;
      if (!el) return;

      // Initialize signal from slider value
      var initialVal = parseFloat(el.value);
      if (reactiveEngine.get(signalKey) === undefined) {
        reactiveEngine.createSignal(signalKey, initialVal);
      } else {
        el.value = reactiveEngine.get(signalKey);
      }

      el.addEventListener('input', function (e) {
        var val = parseFloat(e.target.value);
        reactiveEngine.set(signalKey, val);
      }, { passive: true });

      // Keep slider in sync if signal changes from elsewhere
      reactiveEngine.createEffect([signalKey], function (val) {
        if (parseFloat(el.value) !== val) {
          el.value = val;
        }
      });
    },

    bindText: function (selectorOrEl, signalKey, formatter) {
      var el = typeof selectorOrEl === 'string' ? document.querySelector(selectorOrEl) : selectorOrEl;
      if (!el) return;

      var format = formatter || function (v) {
        return typeof v === 'number' ? (Number.isInteger(v) ? v.toString() : v.toFixed(2)) : String(v);
      };

      reactiveEngine.createEffect([signalKey], function (val) {
        el.textContent = format(val);
      });
    },

    // Auto-scan and boot
    init: function () {
      themeController.init();
      dualViewController.init();

      // Scan and bind [data-slider="signalKey"]
      if (typeof document !== 'undefined') {
        var sliders = document.querySelectorAll('[data-slider]');
        for (var i = 0; i < sliders.length; i++) {
          var s = sliders[i];
          var key = s.getAttribute('data-slider');
          this.bindSlider(s, key);
        }

        // Scan and bind [data-bind="signalKey"]
        var boundTexts = document.querySelectorAll('[data-bind]');
        for (var j = 0; j < boundTexts.length; j++) {
          var b = boundTexts[j];
          var bKey = b.getAttribute('data-bind');
          this.bindText(b, bKey);
        }

        // Scan and bind [data-katex-slot="signalKey"]
        var slots = document.querySelectorAll('[data-katex-slot]');
        for (var k = 0; k < slots.length; k++) {
          var slot = slots[k];
          var slotKey = slot.getAttribute('data-katex-slot');
          this.bindKatexSlot(slot, slotKey);
        }
      }
    }
  };

  // Auto-boot when DOM is ready
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function () {
        ThreeUIEngine.init();
      });
    } else {
      setTimeout(function () {
        ThreeUIEngine.init();
      }, 0);
    }
  }

  return ThreeUIEngine;
}));
