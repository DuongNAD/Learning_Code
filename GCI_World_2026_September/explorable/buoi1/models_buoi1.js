/**
 * ThreeUI Explorable Interactive Learning System & Slide Engine
 * Buoi 1 Interactive Simulation Models (Universal UMD/IIFE)
 *
 * Course: GCI World 2026 September · Matsuo-Iwasawa Laboratory (The University of Tokyo)
 * Compliance: DeepTutor RFC 2119, emoji_policy: none (Zero Unicode Emojis)
 *
 * Models Included:
 * 1. FoodTruckModel: Censored Demand (Dark Data) & Newsvendor Critical Fractile
 * 2. FlywheelModel: 5-Node Compound Data Flywheel & Defensible AI Moat
 * 3. TanpinKanriModel: Seven-Eleven 4-Phase Empirical Restocking & Loss Trade-off
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.Buoi1Models = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // =========================================================================
  // MODEL 1: Food Truck Censored Demand (Dark Data Simulator)
  // =========================================================================
  var FoodTruckModel = {
    // Economics constants
    DEFAULT_PRICE: 8.0,
    DEFAULT_COST: 3.5,
    DEFAULT_SALVAGE: 1.0,

    /**
     * Compute Newsvendor Critical Fractile F* = (p - c) / (p - s)
     */
    criticalFractile: function (p, c, s) {
      var price = typeof p === 'number' ? p : this.DEFAULT_PRICE;
      var cost = typeof c === 'number' ? c : this.DEFAULT_COST;
      var salvage = typeof s === 'number' ? s : this.DEFAULT_SALVAGE;
      return (price - cost) / (price - salvage);
    },

    /**
     * Evaluate business state variables
     * @param {number} q - Prepared quantity
     * @param {number} d0 - Base latent demand
     * @param {number} w - Weather demand multiplier
     * @param {number} p - Unit price (default 8.0)
     * @param {number} c - Unit cost (default 3.5)
     * @param {number} s - Unit salvage value (default 1.0)
     */
    evaluate: function (q, d0, w, p, c, s) {
      var price = typeof p === 'number' ? p : this.DEFAULT_PRICE;
      var cost = typeof c === 'number' ? c : this.DEFAULT_COST;
      var salvage = typeof s === 'number' ? s : this.DEFAULT_SALVAGE;
      var weather = typeof w === 'number' ? w : 1.0;

      var qInt = Math.max(0, Math.round(Number(q) || 0));
      var d0Num = Math.max(0, Number(d0) || 0);
      var effectiveDemand = Math.max(0, Math.round(d0Num * weather));

      var sold = Math.min(qInt, effectiveDemand);
      var darkData = Math.max(0, effectiveDemand - qInt);
      var waste = Math.max(0, qInt - effectiveDemand);

      var revenue = price * sold + salvage * waste;
      var totalCost = cost * qInt;
      var netProfit = revenue - totalCost;

      var cu = price - cost;   // Underage opportunity penalty
      var co = cost - salvage; // Overage inventory penalty
      var opportunityLoss = cu * darkData;
      var inventoryLoss = co * waste;

      // Stockout timestamp calculation (11:00 to 15:00 window, duration 4.0 hours)
      var stockoutHour = null;
      var stockoutTimeStr = '[Khong het hang / Du hang]';

      if (qInt < effectiveDemand && effectiveDemand > 0) {
        stockoutHour = 11.0 + 4.0 * (qInt / effectiveDemand);
        var totalMinutes = Math.round(stockoutHour * 60);
        var hh = Math.floor(totalMinutes / 60);
        var mm = totalMinutes % 60;
        var hhStr = hh < 10 ? '0' + hh : String(hh);
        var mmStr = mm < 10 ? '0' + mm : String(mm);
        stockoutTimeStr = hhStr + ':' + mmStr + ' (Het hang som)';
      }

      return {
        q: qInt,
        d0: d0Num,
        w: weather,
        d: effectiveDemand,
        sold: sold,
        dark_data: darkData,
        waste: waste,
        revenue: revenue,
        total_cost: totalCost,
        net_profit: netProfit,
        opportunity_loss: opportunityLoss,
        inventory_loss: inventoryLoss,
        stockout_hour: stockoutHour,
        stockout_time_str: stockoutTimeStr,
        critical_fractile: this.criticalFractile(price, cost, salvage)
      };
    },

    /**
     * Render live SVG Gaussian distribution curve with observed and dark data zones
     */
    renderGaussianSVG: function (svgEl, q, d, options) {
      if (!svgEl) return;
      var opts = options || {};
      var width = opts.width || 520;
      var height = opts.height || 200;
      var sigma = opts.sigma || 20;

      var padLeft = 45;
      var padRight = 25;
      var padTop = 25;
      var padBottom = 35;
      var plotW = width - padLeft - padRight;
      var plotH = height - padTop - padBottom;
      var baselineY = padTop + plotH;

      var maxDomain = Math.max(160, Math.ceil((d + 3.5 * sigma) / 20) * 20);

      function xToPx(xVal) {
        return padLeft + (Math.max(0, Math.min(xVal, maxDomain)) / maxDomain) * plotW;
      }

      function normalPdf(xVal, mean, std) {
        var diff = xVal - mean;
        return (1 / (std * Math.sqrt(2 * Math.PI))) * Math.exp(-(diff * diff) / (2 * std * std));
      }

      var maxPdf = normalPdf(d, d, sigma);
      function yToPx(pdfVal) {
        return baselineY - (pdfVal / maxPdf) * (plotH * 0.92);
      }

      // Generate curve samples
      var stepCount = 120;
      var points = [];
      for (var i = 0; i <= stepCount; i++) {
        var xVal = (i / stepCount) * maxDomain;
        var pdf = normalPdf(xVal, d, sigma);
        points.push({ x: xVal, px: xToPx(xVal), py: yToPx(pdf) });
      }

      // Build observed polygon path (x <= Q)
      var observedPoints = points.filter(function (pt) { return pt.x <= q; });
      var qPx = xToPx(q);
      var qPdf = normalPdf(q, d, sigma);
      var qPy = yToPx(qPdf);

      var observedPathD = '';
      if (observedPoints.length > 0) {
        observedPathD = 'M ' + padLeft + ' ' + baselineY;
        for (var j = 0; j < observedPoints.length; j++) {
          observedPathD += ' L ' + observedPoints[j].px + ' ' + observedPoints[j].py;
        }
        observedPathD += ' L ' + qPx + ' ' + qPy;
        observedPathD += ' L ' + qPx + ' ' + baselineY + ' Z';
      }

      // Build dark data polygon path (x > Q)
      var darkPoints = points.filter(function (pt) { return pt.x >= q; });
      var darkPathD = '';
      if (darkPoints.length > 0 && q < maxDomain) {
        darkPathD = 'M ' + qPx + ' ' + baselineY;
        darkPathD += ' L ' + qPx + ' ' + qPy;
        for (var k = 0; k < darkPoints.length; k++) {
          darkPathD += ' L ' + darkPoints[k].px + ' ' + darkPoints[k].py;
        }
        darkPathD += ' L ' + xToPx(maxDomain) + ' ' + baselineY + ' Z';
      }

      // Build main curve stroke
      var curvePathD = 'M ' + points[0].px + ' ' + points[0].py;
      for (var m = 1; m < points.length; m++) {
        curvePathD += ' L ' + points[m].px + ' ' + points[m].py;
      }

      var dPx = xToPx(d);

      // SVG Elements Markup
      var svgContent = '' +
        '<defs>' +
        '  <pattern id="darkHatch" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">' +
        '    <line x1="0" y1="0" x2="0" y2="8" stroke="rgba(244, 63, 94, 0.65)" stroke-width="2.5" />' +
        '  </pattern>' +
        '</defs>' +
        '<!-- Grid Baseline -->' +
        '<line x1="' + padLeft + '" y1="' + baselineY + '" x2="' + (padLeft + plotW) + '" y2="' + baselineY + '" stroke="var(--threeui-border-default, #334155)" stroke-width="1.5" />' +
        '<!-- Observed Sales Area (Cyan/Emerald) -->' +
        (observedPathD ? '<path d="' + observedPathD + '" fill="rgba(6, 182, 212, 0.28)" stroke="none" />' : '') +
        '<!-- Dark Data Zone (Diagonal Hatched Red) -->' +
        (darkPathD ? '<path d="' + darkPathD + '" fill="url(#darkHatch)" stroke="none" />' : '') +
        '<!-- Distribution Curve Stroke -->' +
        '<path d="' + curvePathD + '" fill="none" stroke="var(--threeui-accent-cyan, #06b6d4)" stroke-width="2.5" />' +
        '<!-- D (Mean Demand) Marker Line -->' +
        '<line x1="' + dPx + '" y1="' + padTop + '" x2="' + dPx + '" y2="' + baselineY + '" stroke="var(--threeui-accent-amber, #f59e0b)" stroke-width="1.8" stroke-dasharray="3, 3" />' +
        '<text x="' + dPx + '" y="' + (padTop - 8) + '" text-anchor="middle" font-size="11" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-accent-amber, #f59e0b)">[D=' + d + ']</text>' +
        '<!-- Q (Inventory) Marker Line -->' +
        '<line x1="' + qPx + '" y1="' + padTop + '" x2="' + qPx + '" y2="' + baselineY + '" stroke="var(--threeui-accent-rose, #f43f5e)" stroke-width="2" />' +
        '<text x="' + qPx + '" y="' + (baselineY + 18) + '" text-anchor="middle" font-size="11" font-weight="600" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-accent-rose, #f43f5e)">Q=' + q + '</text>' +
        '<!-- Legend Annotations -->' +
        '<text x="' + (padLeft + 8) + '" y="' + (padTop + 14) + '" font-size="10" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-accent-cyan, #06b6d4)">[Observed: S = ' + Math.min(q, d) + ']</text>' +
        (q < d ? '<text x="' + (padLeft + plotW - 8) + '" y="' + (padTop + 14) + '" text-anchor="end" font-size="10" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-accent-rose, #f43f5e)">[Dark Data Zone: ' + (d - q) + ' mat]</text>' : '');

      svgEl.innerHTML = svgContent;
    }
  };

  // =========================================================================
  // MODEL 2: Compound Data Flywheel & AI Moat Model
  // =========================================================================
  var FlywheelModel = {
    NODES: [
      {
        id: 'v1_workflow_integration',
        num: '01',
        title: 'Workflow Integration',
        tag: '[Nhung vao tac nghiep]',
        desc: 'Nhung sau AI vao quy trinh cong viec hang ngay cua nguoi dung, khong phai widget ben ngoai.'
      },
      {
        id: 'v2_user_operation_telemetry',
        num: '02',
        title: 'User Telemetry',
        tag: '[Ghi nhan tuong tac]',
        desc: 'Thu thap hanh vi that, cac diem sua loi tu dong cua chuyen gia trong luc thao tac.'
      },
      {
        id: 'v3_proprietary_data_synthesis',
        num: '03',
        title: 'Proprietary Data',
        tag: '[Du lieu doc quyen]',
        desc: 'Tong hop du lieu cap (Prompt, Sua doi) dac thu ma public web va doi thu khong the tiep can.'
      },
      {
        id: 'v4_sft_dpo_fine_tuning',
        num: '04',
        title: 'SFT Fine-Tuning',
        tag: '[Tinh chinh mo hinh]',
        desc: 'Huan luyen lien tuc tren du lieu doc quyen, giup mo hinh chuyen biet vuot troi hon generic LLM.'
      },
      {
        id: 'v5_superior_ux_automation',
        num: '05',
        title: 'Superior UX',
        tag: '[Trai nghiem vuot troi]',
        desc: 'Do chinh xac cao hon mang lai trai nghiem vuot bac, tang chi phi chuyen doi cua nguoi dung.'
      }
    ],

    N0: 1000.0,
    GAMMA: 0.40,
    ACC0: 70.0,
    ACC_MAX: 98.5,
    KAPPA: 0.45,

    cumulativeData: function (k) {
      var cycle = Math.max(0, Number(k) || 0);
      return this.N0 * Math.pow(1.0 + this.GAMMA, cycle);
    },

    modelAccuracy: function (k) {
      var cycle = Math.max(0, Number(k) || 0);
      return this.ACC_MAX - (this.ACC_MAX - this.ACC0) * Math.exp(-this.KAPPA * cycle);
    },

    switchingCost: function (k) {
      var cycle = Math.max(0, Number(k) || 0);
      return 1.0 + 9.0 * (1.0 - Math.exp(-0.30 * cycle));
    },

    moatDepthScore: function (k) {
      var cycle = Math.max(0, Number(k) || 0);
      var w1 = 0.35;
      var w2 = 0.35;
      var w3 = 0.30;

      var accTerm = this.modelAccuracy(cycle) / 100.0;
      var dataTerm = Math.log(this.cumulativeData(cycle) / this.N0) / Math.log(100.0);
      dataTerm = Math.max(0.0, Math.min(1.0, dataTerm));
      var switchTerm = this.switchingCost(cycle) / 10.0;

      var score = w1 * accTerm + w2 * dataTerm + w3 * switchTerm;
      return Math.max(0.0, Math.min(1.0, score));
    },

    evaluate: function (k, activeNodeIdx) {
      var cycle = Math.max(0, Number(k) || 0);
      var nodeIdx = typeof activeNodeIdx === 'number' ? Math.max(0, Math.min(4, activeNodeIdx)) : (cycle % 5);

      return {
        cycle: cycle,
        active_node_idx: nodeIdx,
        active_node: this.NODES[nodeIdx],
        cumulative_data: this.cumulativeData(cycle),
        model_accuracy: this.modelAccuracy(cycle),
        switching_cost: this.switchingCost(cycle),
        moat_depth_score: this.moatDepthScore(cycle),
        moat_depth_pct: (this.moatDepthScore(cycle) * 100).toFixed(1) + '%'
      };
    },

    /**
     * Render 5-node cyclic SVG diagram
     */
    renderFlywheelSVG: function (svgEl, activeNodeIdx, cycleK) {
      if (!svgEl) return;
      var cycle = typeof cycleK === 'number' ? cycleK : 0;
      var activeIdx = typeof activeNodeIdx === 'number' ? activeNodeIdx : 0;

      var width = 460;
      var height = 300;
      var centerX = 230;
      var centerY = 150;
      var radius = 100;

      var nodesCount = 5;
      var nodeCoords = [];

      for (var i = 0; i < nodesCount; i++) {
        var angle = i * ((2 * Math.PI) / nodesCount) - Math.PI / 2;
        var x = centerX + radius * Math.cos(angle);
        var y = centerY + radius * Math.sin(angle);
        nodeCoords.push({ x: x, y: y, angle: angle, node: this.NODES[i] });
      }

      // Connecting circular arcs or arrows
      var pathsSvg = '';
      for (var j = 0; j < nodesCount; j++) {
        var nextJ = (j + 1) % nodesCount;
        var p1 = nodeCoords[j];
        var p2 = nodeCoords[nextJ];
        var isTraversed = (j === activeIdx);

        // Control point for subtle curvature
        var midAngle = (p1.angle + p2.angle) / 2;
        if (p2.angle < p1.angle) midAngle += Math.PI;
        var ctrlR = radius * 1.15;
        var cx = centerX + ctrlR * Math.cos(midAngle);
        var cy = centerY + ctrlR * Math.sin(midAngle);

        var strokeColor = isTraversed ? 'var(--threeui-accent-cyan, #06b6d4)' : 'var(--threeui-border-default, #334155)';
        var strokeW = isTraversed ? 2.5 : 1.5;
        var dash = isTraversed ? 'none' : '4, 4';

        pathsSvg += '<path d="M ' + p1.x + ' ' + p1.y + ' Q ' + cx + ' ' + cy + ' ' + p2.x + ' ' + p2.y + '" ' +
          'fill="none" stroke="' + strokeColor + '" stroke-width="' + strokeW + '" stroke-dasharray="' + dash + '" />';
      }

      // Draw nodes
      var nodesSvg = '';
      for (var k = 0; k < nodesCount; k++) {
        var pt = nodeCoords[k];
        var isActive = (k === activeIdx);
        var fill = isActive ? 'var(--threeui-accent-cyan, #06b6d4)' : 'var(--threeui-surface-elevated, #1e293b)';
        var stroke = isActive ? '#38bdf8' : 'var(--threeui-border-highlight, #475569)';
        var textColor = isActive ? '#0f172a' : 'var(--threeui-text-primary, #f8fafc)';
        var filter = isActive ? 'filter="drop-shadow(0 0 10px rgba(6, 182, 212, 0.7))"' : '';

        nodesSvg += '<g class="flywheel-node-group" ' + filter + ' data-node-idx="' + k + '" style="cursor: pointer;">';
        nodesSvg += '  <circle cx="' + pt.x + '" cy="' + pt.y + '" r="22" fill="' + fill + '" stroke="' + stroke + '" stroke-width="2" />';
        nodesSvg += '  <text x="' + pt.x + '" y="' + (pt.y + 5) + '" text-anchor="middle" font-size="11" font-weight="700" fill="' + textColor + '" font-family="var(--threeui-font-mono, monospace)">' + pt.node.num + '</text>';
        nodesSvg += '</g>';
      }

      // Center HUD
      var centerSvg = '' +
        '<circle cx="' + centerX + '" cy="' + centerY + '" r="46" fill="rgba(15, 23, 42, 0.85)" stroke="var(--threeui-border-highlight, #475569)" stroke-width="1.5" />' +
        '<text x="' + centerX + '" y="' + (centerY - 8) + '" text-anchor="middle" font-size="10" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-text-muted, #94a3b8)">[Vong lap: k=' + cycle + ']</text>' +
        '<text x="' + centerX + '" y="' + (centerY + 12) + '" text-anchor="middle" font-size="13" font-weight="700" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-accent-emerald, #10b981)">Moat: ' + (this.moatDepthScore(cycle) * 100).toFixed(0) + '%</text>';

      svgEl.innerHTML = pathsSvg + nodesSvg + centerSvg;
    }
  };

  // =========================================================================
  // MODEL 3: Seven-Eleven Tanpin Kanri (Empirical Restocking & Loss Trade-off)
  // =========================================================================
  var TanpinKanriModel = {
    DEFAULT_PRICE: 8.0,
    DEFAULT_COST: 3.5,
    DEFAULT_SALVAGE: 1.0,

    PHASES: [
      {
        id: 1,
        title: 'Signal Capture',
        badge: '[Buoc 1: Tin hieu]',
        desc: 'Thu thap tin hieu ngoai vi: Du bao thoi tiet mua luc 17:00, le hoi the thao truong hoc gan do.'
      },
      {
        id: 2,
        title: 'POS Telemetry',
        badge: '[Buoc 2: POS Real-Time]',
        desc: 'Ghi nhan dong du lieu POS thoi gian thuc: Ton kho con 12 onigiri, toc do ban 8 cai/gio.'
      },
      {
        id: 3,
        title: 'Hypothesis Restocking',
        badge: '[Buoc 3: Gia thuyet SKU]',
        desc: 'Thiet lap gia thuyet dat hang tung mat hang: Nhap 45 chiec o che mua va 60 suat com hop.'
      },
      {
        id: 4,
        title: 'Waste Audit & Revise',
        badge: '[Buoc 4: Kiem toan & Sua]',
        desc: 'Kiem toan ton that cuoi ngay: Ban duoc 42 o, 2 hop com het han -> Hieu chinh mo hinh cho ngay mai.'
      }
    ],

    optimalFractile: function (p, c, s) {
      var price = typeof p === 'number' ? p : this.DEFAULT_PRICE;
      var cost = typeof c === 'number' ? c : this.DEFAULT_COST;
      var salvage = typeof s === 'number' ? s : this.DEFAULT_SALVAGE;
      var cu = price - cost;
      var co = cost - salvage;
      return cu / (cu + co);
    },

    lossTradeoff: function (alpha, dMean, dStd, p, c, s) {
      var price = typeof p === 'number' ? p : this.DEFAULT_PRICE;
      var cost = typeof c === 'number' ? c : this.DEFAULT_COST;
      var salvage = typeof s === 'number' ? s : this.DEFAULT_SALVAGE;

      var mean = typeof dMean === 'number' ? dMean : 50.0;
      var std = typeof dStd === 'number' ? dStd : 10.0;
      var a = Math.max(0.0, Math.min(1.0, Number(alpha) || 0.0));

      var cu = price - cost;
      var co = cost - salvage;

      var q = mean + (a - 0.5) * 2.0 * std;
      // Calibrated convex loss model: minimum of totalLoss uniquely occurs at alpha* = cu / (cu + co)
      var oppLoss = (cu / 2.0) * Math.pow(1.0 - a, 2) * std;
      var invLoss = (co / 2.0) * Math.pow(a, 2) * std;
      var totalLoss = oppLoss + invLoss;

      return {
        alpha: a,
        q: q,
        opp_loss: oppLoss,
        inv_loss: invLoss,
        total_loss: totalLoss,
        optimal_fractile: this.optimalFractile(price, cost, salvage)
      };
    },

    /**
     * Render U-shaped loss curve SVG
     */
    renderLossCurveSVG: function (svgEl, alpha) {
      if (!svgEl) return;
      var curAlpha = Math.max(0.0, Math.min(1.0, Number(alpha) || 0.0));
      var optAlpha = this.optimalFractile();

      var width = 500;
      var height = 220;
      var padLeft = 50;
      var padRight = 30;
      var padTop = 30;
      var padBottom = 35;
      var plotW = width - padLeft - padRight;
      var plotH = height - padTop - padBottom;
      var baselineY = padTop + plotH;

      var maxLoss = 50.0; // Scaled Y max

      function aToPx(a) {
        return padLeft + a * plotW;
      }

      function lToPx(l) {
        return baselineY - (Math.min(maxLoss, l) / maxLoss) * plotH;
      }

      var self = this;
      var sampleCount = 60;
      var oppPath = '';
      var invPath = '';
      var totPath = '';

      for (var i = 0; i <= sampleCount; i++) {
        var aVal = i / sampleCount;
        var res = self.lossTradeoff(aVal);
        var px = aToPx(aVal);
        var pyOpp = lToPx(res.opp_loss);
        var pyInv = lToPx(res.inv_loss);
        var pyTot = lToPx(res.total_loss);

        if (i === 0) {
          oppPath += 'M ' + px + ' ' + pyOpp;
          invPath += 'M ' + px + ' ' + pyInv;
          totPath += 'M ' + px + ' ' + pyTot;
        } else {
          oppPath += ' L ' + px + ' ' + pyOpp;
          invPath += ' L ' + px + ' ' + pyInv;
          totPath += ' L ' + px + ' ' + pyTot;
        }
      }

      var curRes = self.lossTradeoff(curAlpha);
      var curX = aToPx(curAlpha);
      var curTotY = lToPx(curRes.total_loss);
      var optX = aToPx(optAlpha);

      var svgContent = '' +
        '<!-- Grid Baseline & Axes -->' +
        '<line x1="' + padLeft + '" y1="' + baselineY + '" x2="' + (padLeft + plotW) + '" y2="' + baselineY + '" stroke="var(--threeui-border-default, #334155)" stroke-width="1.5" />' +
        '<line x1="' + padLeft + '" y1="' + padTop + '" x2="' + padLeft + '" y2="' + baselineY + '" stroke="var(--threeui-border-default, #334155)" stroke-width="1.5" />' +
        '<!-- Optimal Fractile Line (alpha* = 64.3%) -->' +
        '<line x1="' + optX + '" y1="' + padTop + '" x2="' + optX + '" y2="' + baselineY + '" stroke="var(--threeui-accent-emerald, #10b981)" stroke-width="1.8" stroke-dasharray="4, 4" />' +
        '<text x="' + optX + '" y="' + (padTop - 8) + '" text-anchor="middle" font-size="10" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-accent-emerald, #10b981)">[alpha* = 64.3%]</text>' +
        '<!-- Opportunity Loss Curve (Blue)Monotonically Decreasing -->' +
        '<path d="' + oppPath + '" fill="none" stroke="var(--threeui-accent-cyan, #06b6d4)" stroke-width="2" />' +
        '<!-- Inventory Waste Loss Curve (Red)Monotonically Increasing -->' +
        '<path d="' + invPath + '" fill="none" stroke="var(--threeui-accent-rose, #f43f5e)" stroke-width="2" />' +
        '<!-- Total Expected Loss U-Shape (Purple/Amber) -->' +
        '<path d="' + totPath + '" fill="none" stroke="var(--threeui-accent-amber, #f59e0b)" stroke-width="3" />' +
        '<!-- Current Stance Cursor -->' +
        '<line x1="' + curX + '" y1="' + padTop + '" x2="' + curX + '" y2="' + baselineY + '" stroke="#fff" stroke-width="1.5" stroke-dasharray="2, 2" />' +
        '<circle cx="' + curX + '" cy="' + curTotY + '" r="5" fill="var(--threeui-accent-amber, #f59e0b)" stroke="#fff" stroke-width="1.5" />' +
        '<!-- Axis Labels -->' +
        '<text x="' + padLeft + '" y="' + (baselineY + 18) + '" font-size="10" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-text-muted, #94a3b8)">alpha=0.0 (Tiet kiem)</text>' +
        '<text x="' + (padLeft + plotW) + '" y="' + (baselineY + 18) + '" text-anchor="end" font-size="10" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-text-muted, #94a3b8)">alpha=1.0 (Hung hang)</text>' +
        '<!-- Legend -->' +
        '<text x="' + (padLeft + 10) + '" y="' + (padTop + 14) + '" font-size="10" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-accent-cyan, #06b6d4)">[Mat co hoi (Cu)]</text>' +
        '<text x="' + (padLeft + 130) + '" y="' + (padTop + 14) + '" font-size="10" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-accent-rose, #f43f5e)">[Huy bo (Co)]</text>' +
        '<text x="' + (padLeft + 240) + '" y="' + (padTop + 14) + '" font-size="10" font-family="var(--threeui-font-mono, monospace)" fill="var(--threeui-accent-amber, #f59e0b)">[Tong ton that U-Curve]</text>';

      svgEl.innerHTML = svgContent;
    }
  };

  // =========================================================================
  // Master Export & Engine Reactive Binder
  // =========================================================================
  var Buoi1Models = {
    FoodTruckModel: FoodTruckModel,
    FlywheelModel: FlywheelModel,
    TanpinKanriModel: TanpinKanriModel,

    /**
     * Bind all models to ThreeUIEngine
     */
    initBuoi1: function (engine) {
      if (!engine || !engine.reactive) {
        return;
      }

      // ---------------------------------------------------------------------
      // 1. Food Truck Reactive Bindings
      // ---------------------------------------------------------------------
      var sigQ = engine.createSignal('ft_q', 40);
      var sigD0 = engine.createSignal('ft_d0', 75);
      var sigW = engine.createSignal('ft_w', 1.0);

      engine.createDerived('ft_eval', ['ft_q', 'ft_d0', 'ft_w'], function (q, d0, w) {
        return FoodTruckModel.evaluate(q, d0, w);
      });

      // Bind KaTeX and Text Slots
      engine.createEffect(['ft_eval'], function (evalRes) {
        // Redraw SVG
        var svg = document.getElementById('svg-food-truck-distribution');
        if (svg) {
          FoodTruckModel.renderGaussianSVG(svg, evalRes.q, evalRes.d);
        }

        // Update KaTeX In-Place Slots
        var elSlotQ = document.getElementById('slot-ft-q'); if (elSlotQ) elSlotQ.textContent = evalRes.q;
        var elSlotD = document.getElementById('slot-ft-d'); if (elSlotD) elSlotD.textContent = evalRes.d;
        var elSlotS = document.getElementById('slot-ft-s'); if (elSlotS) elSlotS.textContent = evalRes.sold;
        var elSlotDark = document.getElementById('slot-ft-dark'); if (elSlotDark) elSlotDark.textContent = evalRes.dark_data;

        // Update Text / HUD Badges
        var elD = document.getElementById('readout-ft-d');
        if (elD) elD.textContent = evalRes.d;
        var elSold = document.getElementById('readout-ft-sold');
        if (elSold) elSold.textContent = evalRes.sold;
        var elDark = document.getElementById('readout-ft-dark');
        if (elDark) elDark.textContent = evalRes.dark_data;
        var elWaste = document.getElementById('readout-ft-waste');
        if (elWaste) elWaste.textContent = evalRes.waste;
        var elProfit = document.getElementById('readout-ft-profit');
        if (elProfit) {
          elProfit.textContent = (evalRes.net_profit >= 0 ? '+' : '') + evalRes.net_profit.toFixed(1) + ' $';
          elProfit.className = 'telemetry-val ' + (evalRes.net_profit >= 0 ? 'accent-emerald' : 'accent-rose');
        }
        var elOppLoss = document.getElementById('readout-ft-opp-loss');
        if (elOppLoss) elOppLoss.textContent = evalRes.opportunity_loss.toFixed(1) + ' $';
        var elStockout = document.getElementById('readout-ft-stockout');
        if (elStockout) elStockout.textContent = evalRes.stockout_time_str;
      });

      // ---------------------------------------------------------------------
      // 2. Compound Flywheel Reactive Bindings
      // ---------------------------------------------------------------------
      var sigFlyK = engine.createSignal('fly_k', 0);
      var sigFlyNode = engine.createSignal('fly_node', 0);

      engine.createDerived('fly_eval', ['fly_k', 'fly_node'], function (k, node) {
        return FlywheelModel.evaluate(k, node);
      });

      engine.createEffect(['fly_eval'], function (evalRes) {
        var svg = document.getElementById('svg-compound-flywheel');
        if (svg) {
          FlywheelModel.renderFlywheelSVG(svg, evalRes.active_node_idx, evalRes.cycle);
        }

        // Active node text
        var elNodeTitle = document.getElementById('fly-active-title');
        if (elNodeTitle) elNodeTitle.textContent = evalRes.active_node.num + '. ' + evalRes.active_node.title;
        var elNodeDesc = document.getElementById('fly-active-desc');
        if (elNodeDesc) elNodeDesc.textContent = evalRes.active_node.desc;

        // Metrics
        var elData = document.getElementById('fly-metric-data');
        if (elData) elData.textContent = Math.round(evalRes.cumulative_data).toLocaleString();
        var elAcc = document.getElementById('fly-metric-acc');
        if (elAcc) elAcc.textContent = evalRes.model_accuracy.toFixed(1) + '%';
        var elSwitch = document.getElementById('fly-metric-switch');
        if (elSwitch) elSwitch.textContent = evalRes.switching_cost.toFixed(1) + ' / 10';
        var elMoat = document.getElementById('fly-metric-moat');
        if (elMoat) elMoat.textContent = evalRes.moat_depth_pct;
      });

      // ---------------------------------------------------------------------
      // 3. Tanpin Kanri Reactive Bindings
      // ---------------------------------------------------------------------
      var sigTkPhase = engine.createSignal('tk_phase', 1);
      var sigTkAlpha = engine.createSignal('tk_alpha', 0.643);

      engine.createDerived('tk_eval', ['tk_alpha'], function (alpha) {
        return TanpinKanriModel.lossTradeoff(alpha);
      });

      engine.createEffect(['tk_eval'], function (evalRes) {
        var svg = document.getElementById('svg-tanpin-kanri-curve');
        if (svg) {
          TanpinKanriModel.renderLossCurveSVG(svg, evalRes.alpha);
        }

        var elQ = document.getElementById('tk-metric-q');
        if (elQ) elQ.textContent = Math.round(evalRes.q);
        var elOpp = document.getElementById('tk-metric-opp');
        if (elOpp) elOpp.textContent = evalRes.opp_loss.toFixed(1) + ' $';
        var elInv = document.getElementById('tk-metric-inv');
        if (elInv) elInv.textContent = evalRes.inv_loss.toFixed(1) + ' $';
        var elTot = document.getElementById('tk-metric-tot');
        if (elTot) elTot.textContent = evalRes.total_loss.toFixed(1) + ' $';
      });

      engine.createEffect(['tk_phase'], function (phaseNum) {
        var p = Math.max(1, Math.min(4, phaseNum));
        var phaseData = TanpinKanriModel.PHASES[p - 1];

        var elBadge = document.getElementById('tk-phase-badge');
        if (elBadge) elBadge.textContent = phaseData.badge;
        var elTitle = document.getElementById('tk-phase-title');
        if (elTitle) elTitle.textContent = phaseData.title;
        var elDesc = document.getElementById('tk-phase-desc');
        if (elDesc) elDesc.textContent = phaseData.desc;

        // Update pills
        var pills = document.querySelectorAll('.tk-phase-pill');
        for (var i = 0; i < pills.length; i++) {
          if (i + 1 === p) {
            pills[i].classList.add('active');
          } else {
            pills[i].classList.remove('active');
          }
        }
      });
    }
  };

  return Buoi1Models;
}));
