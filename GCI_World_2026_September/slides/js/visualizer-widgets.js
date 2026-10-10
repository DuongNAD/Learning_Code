/**
 * ThreeUI Explorable Slide Widgets Bundle
 * Interactive NumPy Visualizers: Broadcasting, Strides & Slicing, Vectorization Benchmark
 * Course: GCI World 2026 September · Matsuo-Iwasawa Lab (The University of Tokyo)
 * Strict Compliance: emoji_policy: none (Zero Unicode Emojis)
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.GciWidgets = factory();
    root.Buoi2Widgets = root.GciWidgets; // Alias for backward compatibility
  }
}(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var GciWidgets = {};

  // =========================================================================
  // 1. WIDGET 1: NumPy Broadcasting Rules Simulator
  // =========================================================================

  GciWidgets.mountBroadcastingWidget = function (containerOrId) {
    var container = (typeof containerOrId === 'string')
      ? document.getElementById(containerOrId)
      : containerOrId;
    if (!container) return;

    var state = {
      preset: 'outer',
      shapeA: [3, 1],
      shapeB: [1, 4],
      valuesA: [[10], [20], [30]],
      valuesB: [[1, 2, 3, 4]]
    };

    function broadcastShapes(shapeA, shapeB) {
      var lenA = shapeA.length;
      var lenB = shapeB.length;
      var maxLen = Math.max(lenA, lenB);

      var paddedA = [];
      for (var i = 0; i < maxLen - lenA; i++) paddedA.push(1);
      for (var a = 0; a < lenA; a++) paddedA.push(shapeA[a]);

      var paddedB = [];
      for (var j = 0; j < maxLen - lenB; j++) paddedB.push(1);
      for (var b = 0; b < lenB; b++) paddedB.push(shapeB[b]);

      var resShape = [];
      var isCompatible = true;
      var mismatchAxis = null;

      for (var k = 0; k < maxLen; k++) {
        var da = paddedA[k];
        var db = paddedB[k];
        if (da === db) {
          resShape.push(da);
        } else if (da === 1) {
          resShape.push(db);
        } else if (db === 1) {
          resShape.push(da);
        } else {
          isCompatible = false;
          mismatchAxis = k;
          break;
        }
      }

      return {
        compatible: isCompatible,
        resShape: isCompatible ? resShape : null,
        paddedA: paddedA,
        paddedB: paddedB,
        mismatchAxis: mismatchAxis
      };
    }

    function setPreset(name) {
      state.preset = name;
      if (name === 'outer') {
        state.shapeA = [3, 1];
        state.shapeB = [1, 4];
        state.valuesA = [[10], [20], [30]];
        state.valuesB = [[1, 2, 3, 4]];
      } else if (name === 'row_bias') {
        state.shapeA = [3, 3];
        state.shapeB = [1, 3];
        state.valuesA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
        state.valuesB = [[100, 200, 300]];
      } else if (name === 'incompatible') {
        state.shapeA = [3, 2];
        state.shapeB = [3, 3];
        state.valuesA = [[1, 2], [3, 4], [5, 6]];
        state.valuesB = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
      } else if (name === 'tensor_3d') {
        state.shapeA = [2, 3, 1];
        state.shapeB = [1, 4];
        state.valuesA = [[[1], [2], [3]], [[4], [5], [6]]];
        state.valuesB = [[10, 20, 30, 40]];
      }
      render();
    }

    function render() {
      var alignment = broadcastShapes(state.shapeA, state.shapeB);

      var html = [
        '<div class="widget-root">',
        '  <div class="widget-controls-bar">',
        '    <div class="widget-btn-group">',
        '      <button class="widget-btn ' + (state.preset === 'outer' ? 'active' : '') + '" data-preset="outer">Mẫu 1: Tích ngoài (Outer Product) (3,1) + (1,4)</button>',
        '      <button class="widget-btn ' + (state.preset === 'row_bias' ? 'active' : '') + '" data-preset="row_bias">Mẫu 2: Cộng chệch hàng (Row Bias Add) (3,3) + (1,3)</button>',
        '      <button class="widget-btn ' + (state.preset === 'incompatible' ? 'active' : '') + '" data-preset="incompatible">Mẫu 3: Không tương thích (Incompatible) (3,2) + (3,3)</button>',
        '    </div>',
        '    <div class="widget-telemetry-badge">',
        '      <span>Quy tắc (Rule):</span> <span class="widget-telemetry-val">Căn lề từ phải sang trái (Right-to-Left Trailing Alignment)</span>',
        '    </div>',
        '  </div>',
        '',
        '  <div id="broadcast-alignment-card">',
        renderAlignmentCard(alignment),
        '  </div>',
        '',
        '  <div class="broadcast-grids-wrapper">',
        '    <div class="broadcast-matrix-panel">',
        '      <div class="matrix-title">Mảng A (Array A) ' + JSON.stringify(state.shapeA) + '</div>',
        '      <div id="broadcast-grid-a" class="matrix-grid-table">',
        renderGridA(),
        '      </div>',
        '    </div>',
        '    <div class="broadcast-operator">+</div>',
        '    <div class="broadcast-matrix-panel">',
        '      <div class="matrix-title">Mảng B (Array B) ' + JSON.stringify(state.shapeB) + '</div>',
        '      <div id="broadcast-grid-b" class="matrix-grid-table">',
        renderGridB(),
        '      </div>',
        '    </div>',
        '    <div class="broadcast-operator">=</div>',
        '    <div class="broadcast-matrix-panel">',
        '      <div class="matrix-title">Ma trận kết quả (Result Matrix) ' + (alignment.compatible ? JSON.stringify(alignment.resShape) : '[LỖI]') + '</div>',
        '      <div id="broadcast-grid-c" class="matrix-grid-table">',
        renderGridC(alignment),
        '      </div>',
        '    </div>',
        '  </div>',
        '',
        '  <div class="broadcast-telemetry-strip">',
        renderTelemetry(alignment),
        '  </div>',
        '</div>'
      ].join('\n');

      container.innerHTML = html;

      // Attach event listeners
      var buttons = container.querySelectorAll('[data-preset]');
      for (var b = 0; b < buttons.length; b++) {
        buttons[b].addEventListener('click', function () {
          setPreset(this.getAttribute('data-preset'));
        });
      }
    }

    function renderAlignmentCard(align) {
      var lines = [];
      lines.push('<div style="display:flex; justify-content:space-between; align-items:center;">');
      lines.push('  <div><strong>Xác thực căn chỉnh chiều (Dimension Alignment Verification):</strong></div>');
      if (align.compatible) {
        lines.push('  <span class="badge-tag view">[TƯƠNG THÍCH (COMPATIBLE): Shape đầu ra ' + JSON.stringify(align.resShape) + ']</span>');
      } else {
        lines.push('  <span class="badge-tag error">[LỖI BROADCASTING: Lệch trục (Axis Mismatch)]</span>');
      }
      lines.push('</div>');

      lines.push('<div style="margin-top:10px; display:flex; gap:20px; align-items:center;">');
      lines.push('  <div><span style="color:#94a3b8;">Kích thước mảng A (Shape A):</span></div>');
      lines.push('  <div style="display:flex; gap:6px;">');
      for (var i = 0; i < align.paddedA.length; i++) {
        var cls = (i === align.mismatchAxis) ? 'error' : (align.paddedA[i] === 1 ? 'stretch' : 'match');
        lines.push('    <div class="broadcast-dim-cell ' + cls + '">' + align.paddedA[i] + '</div>');
      }
      lines.push('  </div>');
      lines.push('</div>');

      lines.push('<div style="margin-top:6px; display:flex; gap:20px; align-items:center;">');
      lines.push('  <div><span style="color:#94a3b8;">Kích thước mảng B (Shape B):</span></div>');
      lines.push('  <div style="display:flex; gap:6px;">');
      for (var j = 0; j < align.paddedB.length; j++) {
        var cls2 = (j === align.mismatchAxis) ? 'error' : (align.paddedB[j] === 1 ? 'stretch' : 'match');
        lines.push('    <div class="broadcast-dim-cell ' + cls2 + '">' + align.paddedB[j] + '</div>');
      }
      lines.push('  </div>');
      lines.push('</div>');

      if (!align.compatible) {
        lines.push('<div style="margin-top:12px; color:#fb7185; font-size:12px; background:rgba(244,63,94,0.1); padding:8px; border-radius:6px; border-left:3px solid #f43f5e;">');
        lines.push('  Lỗi ValueError: operands could not be broadcast together with shapes ' + JSON.stringify(state.shapeA) + ' ' + JSON.stringify(state.shapeB) + ' (Không thể lan truyền kích thước do lệch trục và khác 1)');
        lines.push('</div>');
      }

      return lines.join('\n');
    }

    function renderGridA() {
      var rows = state.valuesA.length;
      var cols = state.valuesA[0].length;
      var cells = [];
      var gridStyle = 'grid-template-columns: repeat(' + cols + ', 44px);';
      for (var r = 0; r < rows; r++) {
        for (var c = 0; c < cols; c++) {
          cells.push('<div class="matrix-cell real">' + state.valuesA[r][c] + '</div>');
        }
      }
      return '<div style="display:inline-grid; gap:4px; ' + gridStyle + '">' + cells.join('') + '</div>';
    }

    function renderGridB() {
      var rows = state.valuesB.length;
      var cols = state.valuesB[0].length;
      var cells = [];
      var gridStyle = 'grid-template-columns: repeat(' + cols + ', 44px);';
      for (var r = 0; r < rows; r++) {
        for (var c = 0; c < cols; c++) {
          cells.push('<div class="matrix-cell real">' + state.valuesB[r][c] + '</div>');
        }
      }
      return '<div style="display:inline-grid; gap:4px; ' + gridStyle + '">' + cells.join('') + '</div>';
    }

    function renderGridC(align) {
      if (!align.compatible) {
        return '<div style="color:#f43f5e; padding:20px; font-size:13px;">Phép toán thất bại: Không tương thích kích thước (Shape Mismatch)</div>';
      }

      var outRows = align.resShape[0];
      var outCols = align.resShape[1];
      var cells = [];
      var gridStyle = 'grid-template-columns: repeat(' + outCols + ', 44px);';

      for (var r = 0; r < outRows; r++) {
        for (var c = 0; c < outCols; c++) {
          var valA = state.valuesA[r % state.valuesA.length][c % state.valuesA[0].length];
          var valB = state.valuesB[r % state.valuesB.length][c % state.valuesB[0].length];
          var sum = valA + valB;
          var isVirtual = (state.valuesA.length === 1 || state.valuesA[0].length === 1 || state.valuesB.length === 1 || state.valuesB[0].length === 1);
          var cellClass = isVirtual ? 'matrix-cell virtual' : 'matrix-cell result';
          var badge = isVirtual ? '<div class="cell-stride-badge">stride=0</div>' : '';

          cells.push('<div class="' + cellClass + '">' + sum + badge + '</div>');
        }
      }

      return '<div style="display:inline-grid; gap:4px; ' + gridStyle + '">' + cells.join('') + '</div>';
    }

    function renderTelemetry(align) {
      if (!align.compatible) {
        return '<span style="color:#f43f5e;">Không cấp phát bộ nhớ do kích thước các trục không tương thích (Incompatible Dimensions).</span>';
      }
      var countA = state.shapeA.reduce(function (acc, v) { return acc * v; }, 1);
      var countB = state.shapeB.reduce(function (acc, v) { return acc * v; }, 1);
      var totalStored = countA + countB;
      var storedBytes = totalStored * 8;

      var outCount = align.resShape.reduce(function (acc, v) { return acc * v; }, 1);
      var naiveBytes = (outCount * 2) * 8;
      var savedPct = (((naiveBytes - storedBytes) / naiveBytes) * 100).toFixed(1);

      return [
        '<div>Lưu thực tế trong RAM (Stored In RAM): <strong style="color:#67e8f9;">' + totalStored + ' phần tử (' + storedBytes + ' B)</strong></div>',
        '<div>Sao chép thô ngây thơ (Naive Duplication): <strong style="color:#f59e0b;">' + (outCount * 2) + ' phần tử (' + naiveBytes + ' B)</strong></div>',
        '<div>Tiết kiệm RAM (RAM Conserved): <strong style="color:#34d399;">' + savedPct + '% Saved (Không tốn RAM vật lý)</strong></div>'
      ].join('\n');
    }

    render();
  };

  // =========================================================================
  // 2. WIDGET 2: ndarray Strides & Slicing Memory Visualizer
  // =========================================================================

  GciWidgets.mountStridesWidget = function (containerOrId) {
    var container = (typeof containerOrId === 'string')
      ? document.getElementById(containerOrId)
      : containerOrId;
    if (!container) return;

    var state = {
      shape: [4, 5],
      itemsize: 8,
      baseAddress: 4096, // 0x1000
      startRow: 0,
      stopRow: 3,
      stepRow: 1,
      startCol: 1,
      stopCol: 5,
      stepCol: 2,
      fancyIndexing: false
    };

    function cContiguousStrides(shape, itemsize) {
      var strides = new Array(shape.length);
      var current = itemsize;
      for (var i = shape.length - 1; i >= 0; i--) {
        strides[i] = current;
        current *= shape[i];
      }
      return strides;
    }

    function computeSlice() {
      var origStrides = cContiguousStrides(state.shape, state.itemsize);
      var rCount = Math.max(0, Math.ceil((state.stopRow - state.startRow) / state.stepRow));
      var cCount = Math.max(0, Math.ceil((state.stopCol - state.startCol) / state.stepCol));
      var newShape = [rCount, cCount];
      var newStrides = [origStrides[0] * state.stepRow, origStrides[1] * state.stepCol];
      var baseOffset = state.startRow * origStrides[0] + state.startCol * origStrides[1];

      var activeIndices = {};
      for (var r = state.startRow; r < state.stopRow; r += state.stepRow) {
        for (var c = state.startCol; c < state.stopCol; c += state.stepCol) {
          activeIndices[r + ',' + c] = true;
        }
      }

      return {
        origStrides: origStrides,
        newShape: newShape,
        newStrides: newStrides,
        baseOffset: baseOffset,
        activeIndices: activeIndices,
        elementCount: rCount * cCount
      };
    }

    function render() {
      var calc = computeSlice();

      var html = [
        '<div class="widget-root">',
        '  <div class="widget-controls-bar">',
        '    <div>',
        '      <span style="color:#94a3b8; font-size:12px; margin-right:8px;">Biểu thức cắt lát (Slice Expression):</span>',
        '      <span id="strides-slice-code">arr[' + state.startRow + ':' + state.stopRow + ':' + state.stepRow + ', ' + state.startCol + ':' + state.stopCol + ':' + state.stepCol + ']</span>',
        '    </div>',
        '    <div class="widget-btn-group">',
        '      <button class="widget-btn ' + (!state.fancyIndexing ? 'active' : '') + '" data-mode="view">Cắt lát cơ bản (Basic Slicing - View)</button>',
        '      <button class="widget-btn ' + (state.fancyIndexing ? 'active' : '') + '" data-mode="copy">Chỉ mục nâng cao (Fancy Indexing - Copy)</button>',
        '    </div>',
        '  </div>',
        '',
        '  <div class="strides-controls-grid">',
        '    <div class="slider-group">',
        '      <label><span>Hàng bắt đầu (Row Start): ' + state.startRow + '</span><span>0..3</span></label>',
        '      <input type="range" id="slider-r-start" min="0" max="3" value="' + state.startRow + '">',
        '    </div>',
        '    <div class="slider-group">',
        '      <label><span>Hàng dừng (Row Stop): ' + state.stopRow + '</span><span>1..4</span></label>',
        '      <input type="range" id="slider-r-stop" min="1" max="4" value="' + state.stopRow + '">',
        '    </div>',
        '    <div class="slider-group">',
        '      <label><span>Bước nhảy hàng (Row Step): ' + state.stepRow + '</span><span>1..2</span></label>',
        '      <input type="range" id="slider-r-step" min="1" max="2" value="' + state.stepRow + '">',
        '    </div>',
        '    <div class="slider-group">',
        '      <label><span>Cột bắt đầu (Col Start): ' + state.startCol + '</span><span>0..4</span></label>',
        '      <input type="range" id="slider-c-start" min="0" max="4" value="' + state.startCol + '">',
        '    </div>',
        '    <div class="slider-group">',
        '      <label><span>Cột dừng (Col Stop): ' + state.stopCol + '</span><span>1..5</span></label>',
        '      <input type="range" id="slider-c-stop" min="1" max="5" value="' + state.stopCol + '">',
        '    </div>',
        '    <div class="slider-group">',
        '      <label><span>Bước nhảy cột (Col Step): ' + state.stepCol + '</span><span>1..3</span></label>',
        '      <input type="range" id="slider-c-step" min="1" max="3" value="' + state.stepCol + '">',
        '    </div>',
        '  </div>',
        '',
        '  <div class="strides-display-columns">',
        '    <div id="strides-grid-container">',
        '      <div style="display:flex; justify-content:space-between; margin-bottom:6px;">',
        '        <span class="matrix-title">Ma trận logic 2D (2D Logical Matrix) Shape (4, 5)</span>',
        '        <span class="badge-tag ' + (state.fancyIndexing ? 'copy' : 'view') + '">' + (state.fancyIndexing ? '[COPY: ' + (calc.elementCount * 8) + ' B Allocated - Cấp phát mới]' : '[VIEW: 0 Bytes Allocated] (Không tốn RAM)') + '</span>',
        '      </div>',
        renderGrid(calc),
        '    </div>',
        '    <div>',
        '      <div style="display:flex; justify-content:space-between; margin-bottom:6px;">',
        '        <span class="matrix-title">Dải lưu trữ RAM vật lý 1D (1D Physical RAM Storage Strip - Contiguous 20 x 8B)</span>',
        '        <span style="font-family:var(--font-mono); font-size:11px; color:#94a3b8;">Gốc địa chỉ (Base: 0x1000 (+ ' + calc.baseOffset + ' B))</span>',
        '      </div>',
        '      <div id="strides-ram-strip">',
        renderRamStrip(calc),
        '      </div>',
        '      <div style="margin-top:12px; font-family:var(--font-mono); font-size:12px; background:rgba(15,23,42,0.7); padding:10px; border-radius:6px; border:1px solid rgba(255,255,255,0.06);">',
        '        <div>Shape mới (New Shape): <strong style="color:#67e8f9;">' + JSON.stringify(calc.newShape) + '</strong> | Bước nhảy (Strides): <strong style="color:#a5b4fc;">' + JSON.stringify(calc.newStrides) + ' Bytes</strong></div>',
        '        <div style="margin-top:4px; color:#94a3b8;">Công thức định vị byte (Formula: Addr(i, j) = 0x1000 + i * ' + calc.newStrides[0] + ' + j * ' + calc.newStrides[1] + ')</div>',
        '      </div>',
        '    </div>',
        '  </div>',
        '</div>'
      ].join('\n');

      container.innerHTML = html;

      // Bind slider inputs
      function bindSlider(id, key, minVal, maxVal) {
        var el = container.querySelector('#' + id);
        if (el) {
          el.addEventListener('input', function () {
            state[key] = parseInt(this.value, 10);
            if (key === 'startRow' && state.startRow >= state.stopRow) state.stopRow = state.startRow + 1;
            if (key === 'stopRow' && state.stopRow <= state.startRow) state.startRow = state.stopRow - 1;
            if (key === 'startCol' && state.startCol >= state.stopCol) state.stopCol = state.startCol + 1;
            if (key === 'stopCol' && state.stopCol <= state.startCol) state.startCol = state.stopCol - 1;
            render();
          });
        }
      }

      bindSlider('slider-r-start', 'startRow');
      bindSlider('slider-r-stop', 'stopRow');
      bindSlider('slider-r-step', 'stepRow');
      bindSlider('slider-c-start', 'startCol');
      bindSlider('slider-c-stop', 'stopCol');
      bindSlider('slider-c-step', 'stepCol');

      var modeButtons = container.querySelectorAll('[data-mode]');
      for (var m = 0; m < modeButtons.length; m++) {
        modeButtons[m].addEventListener('click', function () {
          state.fancyIndexing = (this.getAttribute('data-mode') === 'copy');
          render();
        });
      }
    }

    function renderGrid(calc) {
      var cells = [];
      for (var r = 0; r < 4; r++) {
        for (var c = 0; c < 5; c++) {
          var isActive = calc.activeIndices[r + ',' + c];
          var cls = isActive ? 'grid-2d-cell active-slice' : 'grid-2d-cell';
          var val = r * 5 + c;
          var addr = state.baseAddress + (r * 40) + (c * 8);
          cells.push(
            '<div class="' + cls + '">' +
            '  <div>' + val + '</div>' +
            '  <div class="cell-byte-addr">+ ' + (addr - state.baseAddress) + 'B</div>' +
            '</div>'
          );
        }
      }
      return '<div class="grid-2d-table" style="grid-template-columns: repeat(5, 1fr);">' + cells.join('') + '</div>';
    }

    function renderRamStrip(calc) {
      var cells = [];
      for (var i = 0; i < 20; i++) {
        var r = Math.floor(i / 5);
        var c = i % 5;
        var isActive = calc.activeIndices[r + ',' + c];
        var cls = isActive ? 'ram-cell active-slice' : 'ram-cell';
        cells.push('<div class="' + cls + '">' + i + '</div>');
      }
      return cells.join('');
    }

    render();
  };

  // =========================================================================
  // 3. WIDGET 3: Vectorization vs Python Loop Benchmark
  // =========================================================================

  GciWidgets.mountVectorizationWidget = function (containerOrId) {
    var container = (typeof containerOrId === 'string')
      ? document.getElementById(containerOrId)
      : containerOrId;
    if (!container) return;

    var state = {
      logN: 5, // N = 100,000
      op: 'add'
    };

    function timePythonNs(n, op) {
      var base = n * 62.5;
      var factor = (op === 'cumsum') ? 1.45 : ((op === 'filter') ? 1.80 : 1.0);
      return base * factor;
    }

    function timeNumpyNs(n, op) {
      var base = 2500.0 + n * 0.21;
      var factor = (op === 'cumsum') ? 1.20 : ((op === 'filter') ? 1.15 : 1.0);
      return base * factor;
    }

    function formatTime(ns) {
      if (ns < 1000) return ns.toFixed(1) + ' ns';
      if (ns < 1000000) return (ns / 1000).toFixed(2) + ' µs';
      if (ns < 1000000000) return (ns / 1000000).toFixed(2) + ' ms';
      return (ns / 1000000000).toFixed(3) + ' s';
    }

    function render() {
      var n = Math.pow(10, state.logN);
      var tPy = timePythonNs(n, state.op);
      var tNp = timeNumpyNs(n, state.op);
      var speedup = tPy / tNp;

      var html = [
        '<div class="widget-root">',
        '  <div class="widget-controls-bar">',
        '    <div style="display:flex; align-items:center; gap:16px;">',
        '      <span style="font-family:var(--font-mono); font-size:12px; color:#94a3b8;">Kích thước mảng N (Array Size N):</span>',
        '      <input type="range" id="slider-vec-logN" min="2" max="7" step="0.2" value="' + state.logN + '" style="width:200px; accent-color:var(--accent-cyan);">',
        '      <span class="widget-telemetry-badge"><span class="widget-telemetry-val">N = ' + n.toLocaleString('en-US') + '</span></span>',
        '    </div>',
        '    <div class="widget-btn-group">',
        '      <button class="widget-btn ' + (state.op === 'add' ? 'active' : '') + '" data-op="add">Cộng từng phần tử: Element Add (a + b)</button>',
        '      <button class="widget-btn ' + (state.op === 'cumsum' ? 'active' : '') + '" data-op="cumsum">Tổng tích lũy (Cumsum)</button>',
        '      <button class="widget-btn ' + (state.op === 'filter' ? 'active' : '') + '" data-op="filter">Lọc theo ngưỡng (Threshold Filter)</button>',
        '    </div>',
        '  </div>',
        '',
        '  <div class="vec-telemetry-grid">',
        '    <div class="vec-stat-box">',
        '      <div class="vec-stat-label">Kích thước mảng (Array Size - Phần tử)</div>',
        '      <div class="vec-stat-val cyan">' + n.toLocaleString('en-US') + '</div>',
        '    </div>',
        '    <div class="vec-stat-box">',
        '      <div class="vec-stat-label">Vòng lặp Python thuần (Python Loop Execution)</div>',
        '      <div class="vec-stat-val rose">' + formatTime(tPy) + '</div>',
        '    </div>',
        '    <div class="vec-stat-box">',
        '      <div class="vec-stat-label">Véc-tơ hóa NumPy C / SIMD (Vectorized)</div>',
        '      <div class="vec-stat-val emerald">' + formatTime(tNp) + '</div>',
        '    </div>',
        '    <div class="vec-stat-box">',
        '      <div class="vec-stat-label">Hệ số tăng tốc (Speedup Factor)</div>',
        '      <div class="vec-stat-val cyan">Nhanh hơn ' + speedup.toFixed(1) + 'x (Faster)</div>',
        '    </div>',
        '  </div>',
        '',
        '  <div class="vec-visual-race">',
        '    <div class="race-row">',
        '      <div class="race-label"><span>Véc-tơ hóa NumPy (NumPy Vectorized - AVX-512 SIMD)</span><span style="color:#34d399;">100% thông lượng (Throughput: ' + formatTime(tNp) + ')</span></div>',
        '      <div class="race-track"><div id="race-bar-numpy" class="race-bar" style="width:100%;"></div></div>',
        '    </div>',
        '    <div class="race-row">',
        '      <div class="race-label"><span>Vòng lặp tuần tự Python (Python Iterative for-loop)</span><span style="color:#fb7185;">Tốc độ tương đối ' + (100 / Math.max(1, speedup)).toFixed(2) + '% (Relative Speed: ' + formatTime(tPy) + ')</span></div>',
        '      <div class="race-track"><div id="race-bar-python" class="race-bar" style="width:' + Math.max(0.5, Math.min(100, 100 / speedup)) + '%;"></div></div>',
        '    </div>',
        '  </div>',
        '',
        '  <div>',
        '    <svg id="vec-speedup-svg" viewBox="0 0 600 160">',
        renderSvgCurve(state.logN, state.op),
        '    </svg>',
        '  </div>',
        '</div>'
      ].join('\n');

      container.innerHTML = html;

      // Event listener for logN slider
      var slider = container.querySelector('#slider-vec-logN');
      if (slider) {
        slider.addEventListener('input', function () {
          state.logN = parseFloat(this.value);
          render();
        });
      }

      var opButtons = container.querySelectorAll('[data-op]');
      for (var o = 0; o < opButtons.length; o++) {
        opButtons[o].addEventListener('click', function () {
          state.op = this.getAttribute('data-op');
          render();
        });
      }
    }

    function renderSvgCurve(currentLogN, op) {
      var w = 600;
      var h = 160;
      var padLeft = 60;
      var padRight = 30;
      var padTop = 20;
      var padBottom = 30;

      var minLog = 2;
      var maxLog = 7;
      var maxSpeedup = 320;

      function toX(logVal) {
        return padLeft + ((logVal - minLog) / (maxLog - minLog)) * (w - padLeft - padRight);
      }

      function toY(sVal) {
        return (h - padBottom) - (sVal / maxSpeedup) * (h - padTop - padBottom);
      }

      // Generate curve points
      var points = [];
      for (var l = minLog; l <= maxLog; l += 0.25) {
        var num = Math.pow(10, l);
        var s = timePythonNs(num, op) / timeNumpyNs(num, op);
        points.push(toX(l).toFixed(1) + ',' + toY(s).toFixed(1));
      }

      var currentN = Math.pow(10, currentLogN);
      var currentS = timePythonNs(currentN, op) / timeNumpyNs(currentN, op);
      var curX = toX(currentLogN);
      var curY = toY(currentS);
      var ceilingY = toY(297.6);

      return [
        '<!-- Grid and axes -->',
        '<line x1="' + padLeft + '" y1="' + (h - padBottom) + '" x2="' + (w - padRight) + '" y2="' + (h - padBottom) + '" stroke="rgba(255,255,255,0.15)" />',
        '<line x1="' + padLeft + '" y1="' + padTop + '" x2="' + padLeft + '" y2="' + (h - padBottom) + '" stroke="rgba(255,255,255,0.15)" />',
        '<!-- Asymptotic SIMD limit -->',
        '<line x1="' + padLeft + '" y1="' + ceilingY + '" x2="' + (w - padRight) + '" y2="' + ceilingY + '" stroke="#f59e0b" stroke-dasharray="4,4" opacity="0.6" />',
        '<text x="' + (w - padRight - 10) + '" y="' + (ceilingY - 5) + '" fill="#f59e0b" font-size="10" font-family="monospace" text-anchor="end">Trần giới hạn phần cứng (AVX-512 Ceiling ~297.6x)</text>',
        '<!-- Speedup curve -->',
        '<polyline fill="none" stroke="#06b6d4" stroke-width="2.5" points="' + points.join(' ') + '" />',
        '<!-- Current Position Indicator -->',
        '<circle cx="' + curX + '" cy="' + curY + '" r="5" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />',
        '<text x="' + curX + '" y="' + (curY - 10) + '" fill="#ffffff" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">' + currentS.toFixed(1) + 'x</text>',
        '<!-- X Axis Labels -->',
        '<text x="' + toX(2) + '" y="' + (h - 10) + '" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">10^2</text>',
        '<text x="' + toX(3) + '" y="' + (h - 10) + '" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">10^3</text>',
        '<text x="' + toX(4) + '" y="' + (h - 10) + '" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">10^4</text>',
        '<text x="' + toX(5) + '" y="' + (h - 10) + '" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">10^5</text>',
        '<text x="' + toX(6) + '" y="' + (h - 10) + '" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">10^6</text>',
        '<text x="' + toX(7) + '" y="' + (h - 10) + '" fill="#94a3b8" font-size="10" font-family="monospace" text-anchor="middle">10^7</text>',
        '<!-- Y Axis Label -->',
        '<text x="20" y="' + (h / 2) + '" fill="#94a3b8" font-size="10" font-family="monospace" transform="rotate(-90 20 ' + (h / 2) + ')" text-anchor="middle">Hệ số tăng tốc - Speedup (x)</text>'
      ].join('\n');
    }

    render();
  };

  // =========================================================================
  // 4. Slide Transition & Mount Router
  // =========================================================================

  GciWidgets.handleSlideChange = function (slideElement) {
    if (!slideElement) return;

    var bCast = slideElement.querySelector('#widget-broadcasting-container');
    if (bCast && (!bCast.children || bCast.children.length === 0)) {
      GciWidgets.mountBroadcastingWidget(bCast);
    }

    var strides = slideElement.querySelector('#widget-strides-container');
    if (strides && (!strides.children || strides.children.length === 0)) {
      GciWidgets.mountStridesWidget(strides);
    }

    var vec = slideElement.querySelector('#widget-vectorization-container');
    if (vec && (!vec.children || vec.children.length === 0)) {
      GciWidgets.mountVectorizationWidget(vec);
    }
  };

  // Auto-mount immediately if DOM already has widgets
  document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('widget-broadcasting-container')) {
      GciWidgets.mountBroadcastingWidget('widget-broadcasting-container');
    }
    if (document.getElementById('widget-strides-container')) {
      GciWidgets.mountStridesWidget('widget-strides-container');
    }
    if (document.getElementById('widget-vectorization-container')) {
      GciWidgets.mountVectorizationWidget('widget-vectorization-container');
    }
  });

  return GciWidgets;
}));
