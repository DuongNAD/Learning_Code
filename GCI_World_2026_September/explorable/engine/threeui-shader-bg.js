/**
 * ThreeUI Ambient Background Shader (< 120 lines)
 * WebGL fragment shader with Canvas 2D fallback. Zero dependencies.
 * Compliance: DeepTutor RFC 2119, emoji_policy: none
 */
(function (root, factory) {
  if (typeof define === 'function' && define.amd) define([], factory);
  else if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.ThreeUIShaderBG = factory();
}(typeof self !== 'undefined' ? self : this, function () {
  'use strict';
  var VS_SRC = 'attribute vec2 p; void main(){ gl_Position = vec4(p, 0.0, 1.0); }';
  var FS_SRC = 'precision mediump float;\n' +
    'uniform vec2 u_res; uniform float u_time; uniform vec2 u_mouse; uniform float u_theme;\n' +
    'void main(){\n' +
    '  vec2 uv = gl_FragCoord.xy / u_res.xy; float dist = distance(uv, vec2(0.5) + u_mouse * 0.05);\n' +
    '  float vig = smoothstep(0.9, 0.2, dist); float w = sin(uv.x * 3.0 + u_time * 0.4) * cos(uv.y * 3.0 + u_time * 0.3) * 0.04;\n' +
    '  vec3 d1 = vec3(0.035, 0.051, 0.086), d2 = vec3(0.078, 0.118, 0.200), dg = vec3(0.24, 0.25, 0.59);\n' +
    '  vec3 l1 = vec3(0.97, 0.98, 0.99), l2 = vec3(0.92, 0.94, 0.97), lg = vec3(0.85, 0.88, 0.98);\n' +
    '  vec3 base = mix(mix(d1, d2, uv.y + w), mix(l1, l2, uv.y + w), u_theme);\n' +
    '  vec3 glow = mix(dg, lg, u_theme);\n' +
    '  gl_FragColor = vec4(mix(base, glow, (1.0 - vig) * 0.35 + w), 1.0);\n' +
    '}';

  function initShaderBG(canvasId) {
    var canvas = document.getElementById(canvasId || 'threeui-bg-canvas');
    if (!canvas) return null;
    var gl = canvas.getContext('webgl', { alpha: false, depth: false }) || canvas.getContext('experimental-webgl');
    var isRunning = true, rafId = null, mx = 0, my = 0, tmx = 0, tmy = 0;

    window.addEventListener('pointermove', function (e) {
      tmx = (e.clientX / window.innerWidth) * 2.0 - 1.0;
      tmy = -((e.clientY / window.innerHeight) * 2.0 - 1.0);
    }, { passive: true });

    if (!gl) return init2DFallback(canvas);

    function compile(type, src) {
      var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s);
      return gl.getShaderParameter(s, gl.COMPILE_STATUS) ? s : null;
    }
    var vs = compile(gl.VERTEX_SHADER, VS_SRC), fs = compile(gl.FRAGMENT_SHADER, FS_SRC);
    if (!vs || !fs) return init2DFallback(canvas);

    var prog = gl.createProgram();
    gl.attachShader(prog, vs); gl.attachShader(prog, fs); gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) return init2DFallback(canvas);
    gl.useProgram(prog);

    var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 1,-1, -1,1, -1,1, 1,-1, 1,1]), gl.STATIC_DRAW);
    var posAttr = gl.getAttribLocation(prog, 'p');
    gl.enableVertexAttribArray(posAttr); gl.vertexAttribPointer(posAttr, 2, gl.FLOAT, false, 0, 0);

    var uRes = gl.getUniformLocation(prog, 'u_res'), uTime = gl.getUniformLocation(prog, 'u_time'),
        uMouse = gl.getUniformLocation(prog, 'u_mouse'), uTheme = gl.getUniformLocation(prog, 'u_theme');

    function resize() {
      var dpr = Math.min(window.devicePixelRatio || 1, 1.5);
      canvas.width = window.innerWidth * dpr; canvas.height = window.innerHeight * dpr;
      gl.viewport(0, 0, canvas.width, canvas.height);
      gl.uniform2f(uRes, canvas.width, canvas.height);
    }
    window.addEventListener('resize', resize);
    resize();

    var t0 = Date.now();
    function render() {
      if (!isRunning) return;
      var t = (Date.now() - t0) * 0.001;
      mx += (tmx - mx) * 0.05; my += (tmy - my) * 0.05;
      var isLight = document.documentElement.getAttribute('data-theme') === 'light';
      gl.uniform1f(uTime, t); gl.uniform2f(uMouse, mx, my); gl.uniform1f(uTheme, isLight ? 1.0 : 0.0);
      gl.drawArrays(gl.TRIANGLES, 0, 6);
      rafId = requestAnimationFrame(render);
    }
    document.addEventListener('visibilitychange', function () {
      isRunning = !document.hidden;
      if (isRunning) rafId = requestAnimationFrame(render);
      else if (rafId) cancelAnimationFrame(rafId);
    });
    rafId = requestAnimationFrame(render);
    return { type: 'webgl', destroy: function () { isRunning = false; if (rafId) cancelAnimationFrame(rafId); } };
  }

  function init2DFallback(canvas) {
    var ctx = canvas.getContext('2d'), rafId = null, isRunning = true;
    function render2D() {
      if (!isRunning || !ctx) return;
      var isLight = document.documentElement.getAttribute('data-theme') === 'light';
      canvas.width = window.innerWidth; canvas.height = window.innerHeight;
      var g = ctx.createRadialGradient(canvas.width * 0.5, canvas.height * 0.4, 40, canvas.width * 0.5, canvas.height * 0.5, canvas.width * 0.8);
      g.addColorStop(0, isLight ? '#f8fafc' : '#141e33'); g.addColorStop(1, isLight ? '#e2e8f0' : '#090d16');
      ctx.fillStyle = g; ctx.fillRect(0, 0, canvas.width, canvas.height);
      rafId = requestAnimationFrame(render2D);
    }
    rafId = requestAnimationFrame(render2D);
    return { type: 'canvas2d', destroy: function () { isRunning = false; if (rafId) cancelAnimationFrame(rafId); } };
  }

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { initShaderBG(); });
    else setTimeout(function () { initShaderBG(); }, 0);
  }
  return { init: initShaderBG };
}));
