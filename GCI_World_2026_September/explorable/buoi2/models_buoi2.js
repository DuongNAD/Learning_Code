/**
 * ThreeUI Explorable Learning System · Buoi 2 Models
 * NumPy Multi-Dimensional Array Slicing, Strides, Broadcasting & SIMD Vectorization
 *
 * Course: GCI World 2026 September · Matsuo-Iwasawa Laboratory (The University of Tokyo)
 * Compliance: Strict RFC 2119, emoji_policy: none (Zero Unicode Emojis)
 * Architecture: Zero-dependency UMD/IIFE, Sub-16.6ms Reactive DAG, CLS = 0
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.Buoi2Models = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // =========================================================================
  // MODEL 1: NumPy Multi-Dimensional Array Slicing & Memory Strides
  // =========================================================================

  var StridesModel = {
    state: {
      shapeMode: '2d',       // '2d' or '3d'
      itemsize: 8,           // 8 bytes (int64 / float64)
      baseAddress: 4096,     // 0x1000
      shape2d: [4, 5],       // 4 rows x 5 columns = 20 elements
      shape3d: [2, 3, 4],    // 2 x 3 x 4 = 24 elements
      startRow: 0,
      stopRow: 3,
      stepRow: 1,
      startCol: 1,
      stopCol: 5,
      stepCol: 2,
      fancyIndexing: false   // When true, simulates advanced indexing (copy)
    },

    /**
     * Compute C-contiguous (row-major) strides recursively.
     * stride_{k-1} = itemsize, stride_i = stride_{i+1} * dim_{i+1}
     */
    cContiguousStrides: function (shape, itemsize) {
      itemsize = itemsize || 8;
      var strides = new Array(shape.length);
      var current = itemsize;
      for (var i = shape.length - 1; i >= 0; i--) {
        strides[i] = current;
        current *= shape[i];
      }
      return strides;
    },

    /**
     * Compute physical byte address using affine mapping:
     * Addr(indices) = Base + sum_k (indices_k * stride_k)
     */
    affineByteAddress: function (base, indices, strides) {
      var addr = base;
      for (var i = 0; i < indices.length; i++) {
        addr += indices[i] * strides[i];
      }
      return addr;
    },

    /**
     * Calculate new shape and strides for basic slicing without memory copy.
     * sliceSpecs: array of [start, stop, step]
     */
    sliceStridesAndShape: function (origShape, origStrides, sliceSpecs) {
      var newShape = [];
      var newStrides = [];
      for (var i = 0; i < sliceSpecs.length; i++) {
        var spec = sliceSpecs[i];
        var start = spec[0];
        var stop = spec[1];
        var step = spec[2];
        var count = Math.max(0, Math.ceil((stop - start) / step));
        newShape.push(count);
        newStrides.push(origStrides[i] * step);
      }
      return {
        shape: newShape,
        strides: newStrides
      };
    },

    /**
     * Compute full derived state
     */
    compute: function (s) {
      var currentShape = s.shapeMode === '3d' ? s.shape3d : s.shape2d;
      var origStrides = this.cContiguousStrides(currentShape, s.itemsize);

      var sliceSpecs = [
        [s.startRow, s.stopRow, s.stepRow],
        [s.startCol, s.stopCol, s.stepCol]
      ];

      var sliced = this.sliceStridesAndShape(
        [currentShape[0], currentShape[1]],
        [origStrides[0], origStrides[1]],
        sliceSpecs
      );

      // Selected row and column coordinates
      var selectedRows = [];
      for (var r = s.startRow; r < s.stopRow; r += s.stepRow) {
        if (r >= 0 && r < currentShape[0]) selectedRows.push(r);
      }
      var selectedCols = [];
      for (var c = s.startCol; c < s.stopCol; c += s.stepCol) {
        if (c >= 0 && c < currentShape[1]) selectedCols.push(c);
      }

      var selectedSet = Object.create(null);
      var selectedCells = [];
      for (var ri = 0; ri < selectedRows.length; ri++) {
        var row = selectedRows[ri];
        for (var ci = 0; ci < selectedCols.length; ci++) {
          var col = selectedCols[ci];
          var key = row + '_' + col;
          var flatIdx = row * currentShape[1] + col;
          var byteOffset = row * origStrides[0] + col * origStrides[1];
          var addr = s.baseAddress + byteOffset;
          selectedSet[key] = true;
          selectedCells.push({
            row: row,
            col: col,
            flatIdx: flatIdx,
            byteOffset: byteOffset,
            addr: addr
          });
        }
      }

      var baseOffsetBytes = s.startRow * origStrides[0] + s.startCol * origStrides[1];
      var totalElements = selectedCells.length;
      var isView = !s.fancyIndexing;
      var deltaAllocatedBytes = isView ? 0 : totalElements * s.itemsize;

      return {
        currentShape: currentShape,
        origStrides: origStrides,
        sliceSpecs: sliceSpecs,
        newShape: sliced.shape,
        newStrides: sliced.strides,
        selectedRows: selectedRows,
        selectedCols: selectedCols,
        selectedSet: selectedSet,
        selectedCells: selectedCells,
        baseOffsetBytes: baseOffsetBytes,
        baseAddress: s.baseAddress,
        totalElements: totalElements,
        isView: isView,
        deltaAllocatedBytes: deltaAllocatedBytes,
        sliceExpression: 'arr[' + s.startRow + ':' + s.stopRow + ':' + s.stepRow + ', ' +
                          s.startCol + ':' + s.stopCol + ':' + s.stepCol + ']'
      };
    },

    /**
     * Render DOM updates for Strides Model
     */
    render: function (container, s, derived) {
      if (!container) return;

      // Update KaTeX / Text readouts
      var elSliceCode = container.querySelector('#strides-slice-code');
      if (elSliceCode) elSliceCode.textContent = derived.sliceExpression;

      if (typeof document !== 'undefined') {
        var elS0 = document.getElementById('readout-strides-s0'); if (elS0) elS0.textContent = s.startRow;
        var elE0 = document.getElementById('readout-strides-e0'); if (elE0) elE0.textContent = s.stopRow;
        var elSt0 = document.getElementById('readout-strides-st0'); if (elSt0) elSt0.textContent = s.stepRow;
        var elS1 = document.getElementById('readout-strides-s1'); if (elS1) elS1.textContent = s.startCol;
        var elE1 = document.getElementById('readout-strides-e1'); if (elE1) elE1.textContent = s.stopCol;
        var elSt1 = document.getElementById('readout-strides-st1'); if (elSt1) elSt1.textContent = s.stepCol;
      }

      var elShape = container.querySelector('#strides-out-shape');
      if (elShape) elShape.textContent = '(' + derived.newShape.join(', ') + ')';

      var elStrides = container.querySelector('#strides-out-strides');
      if (elStrides) elStrides.textContent = '(' + derived.newStrides.join(', ') + ') B';

      var elOffset = container.querySelector('#strides-out-offset');
      if (elOffset) elOffset.textContent = '+' + derived.baseOffsetBytes + ' B';

      var elAlloc = container.querySelector('#strides-out-alloc');
      if (elAlloc) {
        elAlloc.textContent = derived.deltaAllocatedBytes + ' B';
        if (derived.isView) {
          elAlloc.className = 'telemetry-val accent-emerald';
        } else {
          elAlloc.className = 'telemetry-val accent-amber';
        }
      }

      var elBadge = container.querySelector('#strides-view-badge');
      if (elBadge) {
        if (derived.isView) {
          elBadge.textContent = '[VIEW: 0 Bytes Allocated]';
          elBadge.style.color = 'var(--threeui-accent-emerald)';
          elBadge.style.borderColor = 'var(--threeui-accent-emerald)';
          elBadge.style.background = 'rgba(16, 185, 129, 0.15)';
        } else {
          elBadge.textContent = '[COPY: New Buffer Allocated]';
          elBadge.style.color = 'var(--threeui-accent-amber)';
          elBadge.style.borderColor = 'var(--threeui-accent-amber)';
          elBadge.style.background = 'rgba(245, 158, 11, 0.15)';
        }
      }

      // Render 2D Grid
      var gridEl = container.querySelector('#strides-grid-container');
      if (gridEl) {
        var rows = derived.currentShape[0];
        var cols = derived.currentShape[1];
        var html = '<table class="strides-table">';
        
        // Header columns
        html += '<thead><tr><th></th>';
        for (var c = 0; c < cols; c++) {
          var isColActive = derived.selectedCols.indexOf(c) !== -1;
          html += '<th class="' + (isColActive ? 'axis-active' : '') + '">Col ' + c + '</th>';
        }
        html += '</tr></thead><tbody>';

        for (var r = 0; r < rows; r++) {
          var isRowActive = derived.selectedRows.indexOf(r) !== -1;
          html += '<tr>';
          html += '<th class="' + (isRowActive ? 'axis-active' : '') + '">Row ' + r + '</th>';
          for (var col = 0; col < cols; col++) {
            var cellKey = r + '_' + col;
            var isSelected = !!derived.selectedSet[cellKey];
            var flatIdx = r * cols + col;
            var byteOffset = r * derived.origStrides[0] + col * derived.origStrides[1];
            var val = (r * 10 + col);

            html += '<td class="strides-cell ' + (isSelected ? 'cell-selected' : 'cell-unselected') + '" ' +
                    'data-row="' + r + '" data-col="' + col + '" ' +
                    'title="Addr: 0x' + (s.baseAddress + byteOffset).toString(16) + ' | Offset: +' + byteOffset + 'B">' +
                    '<span class="cell-val">' + val + '</span>' +
                    '<span class="cell-sub">+' + byteOffset + 'B</span>' +
                    '</td>';
          }
          html += '</tr>';
        }
        html += '</tbody></table>';
        gridEl.innerHTML = html;
      }

      // Render 1D RAM Strip
      var ramEl = container.querySelector('#strides-ram-strip');
      if (ramEl) {
        var totalCells = derived.currentShape[0] * derived.currentShape[1];
        var ramHtml = '<div class="ram-strip-container">';
        for (var idx = 0; idx < totalCells; idx++) {
          var rIdx = Math.floor(idx / derived.currentShape[1]);
          var cIdx = idx % derived.currentShape[1];
          var inSlice = !!derived.selectedSet[rIdx + '_' + cIdx];
          var bOffset = idx * s.itemsize;
          ramHtml += '<div class="ram-block ' + (inSlice ? 'ram-selected' : 'ram-unselected') + '" ' +
                     'title="Element [' + rIdx + ',' + cIdx + '] at +' + bOffset + 'B">' +
                     '<span class="ram-block-val">' + (rIdx * 10 + cIdx) + '</span>' +
                     '<span class="ram-block-sub">+' + bOffset + 'B</span>' +
                     '</div>';
        }
        ramHtml += '</div>';
        ramEl.innerHTML = ramHtml;
      }
    }
  };


  // =========================================================================
  // MODEL 2: NumPy Broadcasting Rules Visualizer
  // =========================================================================

  var BroadcastingModel = {
    state: {
      preset: 'outer',       // 'outer', 'row_bias', 'incompatible', 'tensor_3d'
      shapeA: [3, 1],
      shapeB: [1, 4],
      valuesA: [[10], [20], [30]],
      valuesB: [[1, 2, 3, 4]]
    },

    /**
     * Mathematical broadcasting alignment oracle.
     * Aligns shapes from right to left (trailing dimensions first).
     */
    broadcastShapes: function (shapeA, shapeB) {
      var lenA = shapeA.length;
      var lenB = shapeB.length;
      var maxLen = Math.max(lenA, lenB);

      // Pad shorter shape with leading 1s
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
    },

    /**
     * Switch to preset configuration
     */
    setPreset: function (presetName) {
      this.state.preset = presetName;
      if (presetName === 'outer') {
        // (3, 1) + (1, 4) -> (3, 4)
        this.state.shapeA = [3, 1];
        this.state.shapeB = [1, 4];
        this.state.valuesA = [[10], [20], [30]];
        this.state.valuesB = [[1, 2, 3, 4]];
      } else if (presetName === 'row_bias') {
        // (4, 3) + (3,) -> (4, 3) + (1, 3) -> (4, 3)
        this.state.shapeA = [4, 3];
        this.state.shapeB = [3];
        this.state.valuesA = [
          [10, 15, 20],
          [20, 25, 30],
          [30, 35, 40],
          [40, 45, 50]
        ];
        this.state.valuesB = [1, 2, 3];
      } else if (presetName === 'incompatible') {
        // (3, 2) + (3, 3) -> FAIL
        this.state.shapeA = [3, 2];
        this.state.shapeB = [3, 3];
        this.state.valuesA = [[1, 2], [3, 4], [5, 6]];
        this.state.valuesB = [[1, 1, 1], [2, 2, 2], [3, 3, 3]];
      } else if (presetName === 'tensor_3d') {
        // (2, 3, 1) + (1, 4) -> (2, 3, 4)
        this.state.shapeA = [2, 3, 1];
        this.state.shapeB = [1, 4];
        this.state.valuesA = [[[10], [20], [30]], [[40], [50], [60]]];
        this.state.valuesB = [[1, 2, 3, 4]];
      }
    },

    /**
     * Compute full derived state for broadcasting
     */
    compute: function (s) {
      var alignment = this.broadcastShapes(s.shapeA, s.shapeB);

      if (!alignment.compatible) {
        return {
          compatible: false,
          shapeA: s.shapeA,
          shapeB: s.shapeB,
          paddedA: alignment.paddedA,
          paddedB: alignment.paddedB,
          mismatchAxis: alignment.mismatchAxis,
          errorMessage: 'ValueError: operands could not be broadcast together with shapes (' +
                        s.shapeA.join(',') + ') (' + s.shapeB.join(',') + ')'
        };
      }

      var resShape = alignment.resShape;
      var rows = resShape[0];
      var cols = resShape.length > 1 ? resShape[1] : 1;

      // Calculate stored elements vs naive copy elements
      var countA = 1;
      for (var a = 0; a < s.shapeA.length; a++) countA *= s.shapeA[a];
      var countB = 1;
      for (var b = 0; b < s.shapeB.length; b++) countB *= s.shapeB[b];
      var storedElements = countA + countB;
      var storedBytes = storedElements * 8;

      var totalOutputElements = 1;
      for (var r = 0; r < resShape.length; r++) totalOutputElements *= resShape[r];
      var naiveCopyElements = totalOutputElements * 2;
      var naiveCopyBytes = naiveCopyElements * 8;
      var memorySavedPct = ((naiveCopyBytes - storedBytes) / naiveCopyBytes) * 100;

      // Construct Result Matrix values and real/virtual mapping
      var gridResult = [];
      for (var row = 0; row < rows; row++) {
        var rowArr = [];
        for (var col = 0; col < cols; col++) {
          var valA, isRealA;
          var valB, isRealB;

          if (s.preset === 'outer') {
            valA = s.valuesA[row][0];
            isRealA = (col === 0);
            valB = s.valuesB[0][col];
            isRealB = (row === 0);
          } else if (s.preset === 'row_bias') {
            valA = s.valuesA[row][col];
            isRealA = true;
            valB = s.valuesB[col];
            isRealB = (row === 0);
          } else {
            valA = 10;
            isRealA = true;
            valB = 1;
            isRealB = true;
          }

          rowArr.push({
            row: row,
            col: col,
            valA: valA,
            valB: valB,
            isRealA: isRealA,
            isRealB: isRealB,
            sum: valA + valB,
            isVirtual: (!isRealA || !isRealB)
          });
        }
        gridResult.push(rowArr);
      }

      return {
        compatible: true,
        shapeA: s.shapeA,
        shapeB: s.shapeB,
        paddedA: alignment.paddedA,
        paddedB: alignment.paddedB,
        resShape: resShape,
        rows: rows,
        cols: cols,
        gridResult: gridResult,
        storedElements: storedElements,
        storedBytes: storedBytes,
        naiveCopyElements: naiveCopyElements,
        naiveCopyBytes: naiveCopyBytes,
        memorySavedPct: memorySavedPct
      };
    },

    /**
     * Render DOM updates for Broadcasting Model
     */
    render: function (container, s, derived) {
      if (!container) return;

      var elStatus = container.querySelector('#broadcast-status-badge');
      var elAlignment = container.querySelector('#broadcast-alignment-card');
      var elGridA = container.querySelector('#broadcast-grid-a');
      var elGridB = container.querySelector('#broadcast-grid-b');
      var elGridC = container.querySelector('#broadcast-grid-c');

      var elStored = container.querySelector('#broadcast-stored-elements');
      var elNaive = container.querySelector('#broadcast-naive-elements');
      var elSaved = container.querySelector('#broadcast-memory-saved');

      if (!derived.compatible) {
        if (elStatus) {
          elStatus.textContent = '[INCOMPATIBLE SHAPE ERROR]';
          elStatus.className = 'brand-badge';
          elStatus.style.borderColor = 'var(--threeui-accent-rose)';
          elStatus.style.color = 'var(--threeui-accent-rose)';
          elStatus.style.background = 'rgba(244, 63, 94, 0.15)';
        }
        if (elAlignment) {
          elAlignment.innerHTML =
            '<div class="alignment-err-box">' +
            '  <span class="err-title">[Dimension Mismatch at Axis ' + derived.mismatchAxis + ']</span>' +
            '  <div class="err-msg">' + derived.errorMessage + '</div>' +
            '  <div class="alignment-trace">' +
            '    <div>Shape A: (' + derived.paddedA.join(', ') + ')</div>' +
            '    <div>Shape B: (' + derived.paddedB.join(', ') + ')</div>' +
            '    <div style="color:var(--threeui-accent-rose); font-weight:700;">Dim ' +
                 derived.paddedA[derived.mismatchAxis] + ' != ' + derived.paddedB[derived.mismatchAxis] +
                 ' (Neither is 1)</div>' +
            '  </div>' +
            '</div>';
        }
        if (elGridC) {
          elGridC.innerHTML = '<div class="broadcast-error-placeholder">[Broadcast Operation Blocked]</div>';
        }
        if (elStored) elStored.textContent = '-';
        if (elNaive) elNaive.textContent = '-';
        if (elSaved) elSaved.textContent = '0%';
        return;
      }

      // Compatible State
      if (elStatus) {
        elStatus.textContent = '[BROADCAST COMPATIBLE: (' + derived.resShape.join(', ') + ')]';
        elStatus.className = 'brand-badge';
        elStatus.style.borderColor = 'var(--threeui-accent-emerald)';
        elStatus.style.color = 'var(--threeui-accent-emerald)';
        elStatus.style.background = 'rgba(16, 185, 129, 0.15)';
      }

      // Render Trailing Alignment Trace
      if (elAlignment) {
        elAlignment.innerHTML =
          '<div class="alignment-trace-grid">' +
          '  <div class="trace-row"><span class="trace-label">Shape A:</span><span class="trace-val">(' + derived.paddedA.join(', ') + ')</span></div>' +
          '  <div class="trace-row"><span class="trace-label">Shape B:</span><span class="trace-val">(' + derived.paddedB.join(', ') + ')</span></div>' +
          '  <div class="trace-divider"></div>' +
          '  <div class="trace-row trace-result"><span class="trace-label">Result:</span><span class="trace-val accent-cyan">(' + derived.resShape.join(', ') + ')</span></div>' +
          '</div>';
      }

      // Update Telemetry
      if (elStored) elStored.textContent = derived.storedElements + ' items (' + derived.storedBytes + ' B)';
      if (elNaive) elNaive.textContent = derived.naiveCopyElements + ' items (' + derived.naiveCopyBytes + ' B)';
      if (elSaved) elSaved.textContent = derived.memorySavedPct.toFixed(1) + '%';

      // Render Grid A
      if (elGridA) {
        var htmlA = '<div class="matrix-card"><div class="matrix-title">Array A (' + s.shapeA.join(',') + ')</div><table class="broadcast-table">';
        if (s.preset === 'outer') {
          for (var i = 0; i < s.valuesA.length; i++) {
            htmlA += '<tr><td class="b-cell cell-real">' + s.valuesA[i][0] + '</td></tr>';
          }
        } else if (s.preset === 'row_bias') {
          for (var rA = 0; rA < s.valuesA.length; rA++) {
            htmlA += '<tr>';
            for (var cA = 0; cA < s.valuesA[rA].length; cA++) {
              htmlA += '<td class="b-cell cell-real">' + s.valuesA[rA][cA] + '</td>';
            }
            htmlA += '</tr>';
          }
        }
        htmlA += '</table></div>';
        elGridA.innerHTML = htmlA;
      }

      // Render Grid B
      if (elGridB) {
        var htmlB = '<div class="matrix-card"><div class="matrix-title">Array B (' + s.shapeB.join(',') + ')</div><table class="broadcast-table">';
        if (s.preset === 'outer') {
          htmlB += '<tr>';
          for (var j = 0; j < s.valuesB[0].length; j++) {
            htmlB += '<td class="b-cell cell-real">' + s.valuesB[0][j] + '</td>';
          }
          htmlB += '</tr>';
        } else if (s.preset === 'row_bias') {
          htmlB += '<tr>';
          for (var cB = 0; cB < s.valuesB.length; cB++) {
            htmlB += '<td class="b-cell cell-real">' + s.valuesB[cB] + '</td>';
          }
          htmlB += '</tr>';
        }
        htmlB += '</table></div>';
        elGridB.innerHTML = htmlB;
      }

      // Render Broadcast Result Grid C
      if (elGridC) {
        var htmlC = '<div class="matrix-card"><div class="matrix-title">Result Grid C (' + derived.resShape.join(',') + ')</div><table class="broadcast-table result-table">';
        for (var rowIdx = 0; rowIdx < derived.gridResult.length; rowIdx++) {
          htmlC += '<tr>';
          var rowData = derived.gridResult[rowIdx];
          for (var colIdx = 0; colIdx < rowData.length; colIdx++) {
            var item = rowData[colIdx];
            var cellClass = item.isVirtual ? 'cell-virtual' : 'cell-real';
            var strideNotice = item.isVirtual ? '<span class="cell-stride-tag">stride=0</span>' : '';
            htmlC += '<td class="b-cell ' + cellClass + '" title="A[' + item.valA + '] + B[' + item.valB + '] = ' + item.sum + '">' +
                     '<span class="cell-sum">' + item.sum + '</span>' +
                     strideNotice +
                     '</td>';
          }
          htmlC += '</tr>';
        }
        htmlC += '</table></div>';
        elGridC.innerHTML = htmlC;
      }
    }
  };


  // =========================================================================
  // MODEL 3: Vectorization Speed Benchmark Simulator
  // =========================================================================

  var VectorizationModel = {
    state: {
      logN: 4,               // Exponent: N = 10^logN (range 2 to 7)
      operation: 'add'       // 'add', 'cumsum', 'filter'
    },

    /**
     * Analytical Python iterative loop time:
     * T_py(N) = N * 62.5 ns
     */
    timePythonNs: function (n, op) {
      var base = n * 62.5;
      var factor = 1.0;
      if (op === 'cumsum') factor = 1.45;
      if (op === 'filter') factor = 1.80;
      return base * factor;
    },

    /**
     * Analytical NumPy C-vectorized SIMD time:
     * T_np(N) = 2500.0 ns + N * 0.21 ns
     */
    timeNumpyNs: function (n, op) {
      var base = 2500.0 + n * 0.21;
      var factor = 1.0;
      if (op === 'cumsum') factor = 1.20;
      if (op === 'filter') factor = 1.15;
      return base * factor;
    },

    /**
     * Speedup factor:
     * S(N) = T_py(N) / T_np(N)
     */
    speedup: function (n, op) {
      var tPy = this.timePythonNs(n, op);
      var tNp = this.timeNumpyNs(n, op);
      return tPy / tNp;
    },

    /**
     * Format nanoseconds into readable time units
     */
    formatTime: function (ns) {
      if (ns < 1000) {
        return ns.toFixed(1) + ' ns';
      } else if (ns < 1000000) {
        return (ns / 1000).toFixed(2) + ' µs';
      } else if (ns < 1000000000) {
        return (ns / 1000000).toFixed(2) + ' ms';
      } else {
        return (ns / 1000000000).toFixed(3) + ' s';
      }
    },

    /**
     * Compute full derived state for Vectorization Simulator
     */
    compute: function (s) {
      var n = Math.pow(10, s.logN);
      var tPy = this.timePythonNs(n, s.operation);
      var tNp = this.timeNumpyNs(n, s.operation);
      var speedupFactor = tPy / tNp;

      // Sample curve points across decades for SVG chart
      var curvePoints = [];
      for (var exp = 2.0; exp <= 7.0; exp += 0.2) {
        var sampleN = Math.pow(10, exp);
        var sampleSpeedup = this.speedup(sampleN, s.operation);
        curvePoints.push({
          exp: exp,
          n: sampleN,
          speedup: sampleSpeedup
        });
      }

      var asymptoticCeiling = 62.5 / 0.21; // ~297.6x

      return {
        n: n,
        tPy: tPy,
        tNp: tNp,
        speedupFactor: speedupFactor,
        asymptoticCeiling: asymptoticCeiling,
        curvePoints: curvePoints,
        formattedN: n.toLocaleString('en-US'),
        formattedTPy: this.formatTime(tPy),
        formattedTNp: this.formatTime(tNp),
        formattedSpeedup: speedupFactor.toFixed(1) + 'x'
      };
    },

    /**
     * Render DOM updates for Vectorization Model
     */
    render: function (container, s, derived) {
      if (!container) return;

      var elN = container.querySelector('#vec-val-n');
      if (elN) elN.textContent = derived.formattedN;

      var elTPy = container.querySelector('#vec-time-python');
      if (elTPy) elTPy.textContent = derived.formattedTPy;

      var elTNp = container.querySelector('#vec-time-numpy');
      if (elTNp) elTNp.textContent = derived.formattedTNp;

      var elSpeedup = container.querySelector('#vec-speedup-multiplier');
      if (elSpeedup) elSpeedup.textContent = '[' + derived.formattedSpeedup + ' Faster]';

      var elRacePy = container.querySelector('#race-bar-python');
      var elRaceNp = container.querySelector('#race-bar-numpy');
      if (elRacePy && elRaceNp) {
        // NumPy always finishes instantly
        elRaceNp.style.width = '100%';
        // Python bar width relative to inverse speedup
        var pyRatio = Math.max(2, Math.min(100, (1.0 / derived.speedupFactor) * 100 * 50));
        elRacePy.style.width = pyRatio + '%';
      }

      // Render SVG Speedup Curve
      var svgEl = container.querySelector('#vec-speedup-svg');
      if (svgEl) {
        var width = 460;
        var height = 160;
        var padLeft = 45;
        var padBottom = 28;
        var padTop = 15;
        var padRight = 15;

        var plotW = width - padLeft - padRight;
        var plotH = height - padTop - padBottom;

        // X mapped from exp 2 to 7, Y mapped from 0 to 320
        function mapX(exp) {
          return padLeft + ((exp - 2.0) / 5.0) * plotW;
        }
        function mapY(val) {
          return height - padBottom - (val / 320.0) * plotH;
        }

        var pathD = '';
        for (var i = 0; i < derived.curvePoints.length; i++) {
          var pt = derived.curvePoints[i];
          var px = mapX(pt.exp);
          var py = mapY(pt.speedup);
          if (i === 0) {
            pathD += 'M ' + px.toFixed(1) + ' ' + py.toFixed(1);
          } else {
            pathD += ' L ' + px.toFixed(1) + ' ' + py.toFixed(1);
          }
        }

        var curX = mapX(s.logN);
        var curY = mapY(derived.speedupFactor);
        var ceilingY = mapY(derived.asymptoticCeiling);

        var svgContent =
          '<!-- Grid Lines -->' +
          '<line x1="' + padLeft + '" y1="' + mapY(100) + '" x2="' + (width - padRight) + '" y2="' + mapY(100) + '" stroke="var(--threeui-border-subtle)" stroke-dasharray="3,3" />' +
          '<line x1="' + padLeft + '" y1="' + mapY(200) + '" x2="' + (width - padRight) + '" y2="' + mapY(200) + '" stroke="var(--threeui-border-subtle)" stroke-dasharray="3,3" />' +
          '<line x1="' + padLeft + '" y1="' + mapY(300) + '" x2="' + (width - padRight) + '" y2="' + mapY(300) + '" stroke="var(--threeui-border-subtle)" stroke-dasharray="3,3" />' +

          '<!-- Asymptotic Ceiling -->' +
          '<line x1="' + padLeft + '" y1="' + ceilingY + '" x2="' + (width - padRight) + '" y2="' + ceilingY + '" stroke="var(--threeui-accent-amber)" stroke-dasharray="4,4" stroke-width="1.2" />' +
          '<text x="' + (width - padRight) + '" y="' + (ceilingY - 4) + '" text-anchor="end" font-size="10" fill="var(--threeui-accent-amber)" font-family="var(--threeui-font-mono)">[AVX-512 Limit: ~297.6x]</text>' +

          '<!-- Speedup Curve Path -->' +
          '<path d="' + pathD + '" fill="none" stroke="var(--threeui-accent-cyan)" stroke-width="2.5" />' +

          '<!-- Current Active Point Indicator -->' +
          '<circle cx="' + curX + '" cy="' + curY + '" r="6" fill="var(--threeui-accent-cyan)" stroke="#ffffff" stroke-width="2" />' +
          '<circle cx="' + curX + '" cy="' + curY + '" r="12" fill="none" stroke="var(--threeui-accent-cyan)" stroke-width="1" opacity="0.5" />' +
          '<text x="' + Math.min(curX + 8, width - 70) + '" y="' + Math.max(curY - 8, 20) + '" font-size="11" font-weight="700" fill="var(--threeui-text)" font-family="var(--threeui-font-mono)">' + derived.formattedSpeedup + '</text>' +

          '<!-- Axes -->' +
          '<line x1="' + padLeft + '" y1="' + (height - padBottom) + '" x2="' + (width - padRight) + '" y2="' + (height - padBottom) + '" stroke="var(--threeui-border-medium)" />' +
          '<line x1="' + padLeft + '" y1="' + padTop + '" x2="' + padLeft + '" y2="' + (height - padBottom) + '" stroke="var(--threeui-border-medium)" />' +

          '<!-- X-Axis Labels -->' +
          '<text x="' + mapX(2) + '" y="' + (height - 8) + '" text-anchor="middle" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">10^2</text>' +
          '<text x="' + mapX(3) + '" y="' + (height - 8) + '" text-anchor="middle" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">10^3</text>' +
          '<text x="' + mapX(4) + '" y="' + (height - 8) + '" text-anchor="middle" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">10^4</text>' +
          '<text x="' + mapX(5) + '" y="' + (height - 8) + '" text-anchor="middle" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">10^5</text>' +
          '<text x="' + mapX(6) + '" y="' + (height - 8) + '" text-anchor="middle" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">10^6</text>' +
          '<text x="' + mapX(7) + '" y="' + (height - 8) + '" text-anchor="middle" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">10^7</text>' +

          '<!-- Y-Axis Labels -->' +
          '<text x="' + (padLeft - 6) + '" y="' + (mapY(0) + 3) + '" text-anchor="end" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">0x</text>' +
          '<text x="' + (padLeft - 6) + '" y="' + (mapY(100) + 3) + '" text-anchor="end" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">100x</text>' +
          '<text x="' + (padLeft - 6) + '" y="' + (mapY(200) + 3) + '" text-anchor="end" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">200x</text>' +
          '<text x="' + (padLeft - 6) + '" y="' + (mapY(300) + 3) + '" text-anchor="end" font-size="10" fill="var(--threeui-text-muted)" font-family="var(--threeui-font-mono)">300x</text>';

        svgEl.innerHTML = svgContent;
      }
    }
  };


  // =========================================================================
  // Master Controller & Auto-Initialization
  // =========================================================================

  var Buoi2Models = {
    stridesModel: StridesModel,
    broadcastingModel: BroadcastingModel,
    vectorizationModel: VectorizationModel,

    initStrides: function (container) {
      container = container || document;
      var self = this;

      function update() {
        var derived = self.stridesModel.compute(self.stridesModel.state);
        self.stridesModel.render(container, self.stridesModel.state, derived);
      }

      // Bind Range Sliders
      var sliderStartRow = container.querySelector('#strides-slider-start-row');
      var sliderStopRow = container.querySelector('#strides-slider-stop-row');
      var sliderStepRow = container.querySelector('#strides-slider-step-row');

      var sliderStartCol = container.querySelector('#strides-slider-start-col');
      var sliderStopCol = container.querySelector('#strides-slider-stop-col');
      var sliderStepCol = container.querySelector('#strides-slider-step-col');

      if (sliderStartRow) {
        sliderStartRow.addEventListener('input', function (e) {
          self.stridesModel.state.startRow = parseInt(e.target.value, 10);
          var elS0 = document.getElementById('readout-strides-s0'); if (elS0) elS0.textContent = self.stridesModel.state.startRow;
          update();
        });
      }
      if (sliderStopRow) {
        sliderStopRow.addEventListener('input', function (e) {
          self.stridesModel.state.stopRow = parseInt(e.target.value, 10);
          var elE0 = document.getElementById('readout-strides-e0'); if (elE0) elE0.textContent = self.stridesModel.state.stopRow;
          update();
        });
      }
      if (sliderStepRow) {
        sliderStepRow.addEventListener('input', function (e) {
          self.stridesModel.state.stepRow = parseInt(e.target.value, 10);
          var elSt0 = document.getElementById('readout-strides-st0'); if (elSt0) elSt0.textContent = self.stridesModel.state.stepRow;
          update();
        });
      }
      if (sliderStartCol) {
        sliderStartCol.addEventListener('input', function (e) {
          self.stridesModel.state.startCol = parseInt(e.target.value, 10);
          var elS1 = document.getElementById('readout-strides-s1'); if (elS1) elS1.textContent = self.stridesModel.state.startCol;
          update();
        });
      }
      if (sliderStopCol) {
        sliderStopCol.addEventListener('input', function (e) {
          self.stridesModel.state.stopCol = parseInt(e.target.value, 10);
          var elE1 = document.getElementById('readout-strides-e1'); if (elE1) elE1.textContent = self.stridesModel.state.stopCol;
          update();
        });
      }
      if (sliderStepCol) {
        sliderStepCol.addEventListener('input', function (e) {
          self.stridesModel.state.stepCol = parseInt(e.target.value, 10);
          var elSt1 = document.getElementById('readout-strides-st1'); if (elSt1) elSt1.textContent = self.stridesModel.state.stepCol;
          update();
        });
      }

      // Fancy Indexing Toggle
      var toggleFancy = container.querySelector('#btn-toggle-fancy-indexing');
      if (toggleFancy) {
        toggleFancy.addEventListener('click', function () {
          self.stridesModel.state.fancyIndexing = !self.stridesModel.state.fancyIndexing;
          if (self.stridesModel.state.fancyIndexing) {
            toggleFancy.classList.add('active');
            toggleFancy.textContent = '[Mode: Fancy Indexing (Copy)]';
          } else {
            toggleFancy.classList.remove('active');
            toggleFancy.textContent = '[Mode: Basic Slice (View)]';
          }
          update();
        });
      }

      // Initial render
      update();
    },

    initBroadcasting: function (container) {
      container = container || document;
      var self = this;

      function update() {
        var derived = self.broadcastingModel.compute(self.broadcastingModel.state);
        self.broadcastingModel.render(container, self.broadcastingModel.state, derived);
      }

      // Preset buttons
      var presets = ['outer', 'row_bias', 'incompatible', 'tensor_3d'];
      for (var i = 0; i < presets.length; i++) {
        (function (p) {
          var btn = container.querySelector('#btn-broadcast-' + p);
          if (btn) {
            btn.addEventListener('click', function () {
              for (var j = 0; j < presets.length; j++) {
                var other = container.querySelector('#btn-broadcast-' + presets[j]);
                if (other) other.classList.remove('active');
              }
              btn.classList.add('active');
              self.broadcastingModel.setPreset(p);
              update();
            });
          }
        }(presets[i]));
      }

      update();
    },

    initVectorization: function (container) {
      container = container || document;
      var self = this;

      function update() {
        var derived = self.vectorizationModel.compute(self.vectorizationModel.state);
        self.vectorizationModel.render(container, self.vectorizationModel.state, derived);
      }

      var sliderN = container.querySelector('#vec-slider-n');
      if (sliderN) {
        sliderN.addEventListener('input', function (e) {
          self.vectorizationModel.state.logN = parseFloat(e.target.value);
          update();
        });
      }

      var ops = ['add', 'cumsum', 'filter'];
      for (var i = 0; i < ops.length; i++) {
        (function (op) {
          var btn = container.querySelector('#btn-vec-op-' + op);
          if (btn) {
            btn.addEventListener('click', function () {
              for (var j = 0; j < ops.length; j++) {
                var other = container.querySelector('#btn-vec-op-' + ops[j]);
                if (other) other.classList.remove('active');
              }
              btn.classList.add('active');
              self.vectorizationModel.state.operation = op;
              update();
            });
          }
        }(ops[i]));
      }

      update();
    },

    initAll: function (container) {
      container = container || (typeof document !== 'undefined' ? document : null);
      if (!container) return;
      this.initStrides(container);
      this.initBroadcasting(container);
      this.initVectorization(container);
    }
  };

  // Auto-boot if in browser context
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function () {
        Buoi2Models.initAll();
      });
    } else {
      setTimeout(function () {
        Buoi2Models.initAll();
      }, 0);
    }
  }

  return Buoi2Models;
}));
