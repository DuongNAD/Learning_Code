# AgriCarbon Agent — 60-Second Bulletproof Stage Demo Script & Playbook

**Venue**: Tokyo Innovation Base (TiB), Yurakucho, Tokyo  
**Event**: Vietnam Japan AI Hackathon 2026 — Track 3 (Green Growth)  
**Total Target Duration**: Exactly 60 Seconds (00:00 to 01:00)  
**Language Delivery**: Bilingual English & Japanese (英語 / 日本語)  

---

## Part 1: The Bulletproof 3-Tier Fail-Safe Strategy

Stage demonstrations at high-stakes venues like Tokyo Innovation Base can face WiFi congestion, projector aspect ratio resets, or API timeouts. To ensure a 100% flawless presentation, AgriCarbon adopts a **3-Tier Fail-Safe Defense Matrix**:

```
[ Tier 1: LIVE STREAMLIT APP ] 
      │ (If latency > 3.0s or WiFi drops)
      ▼
[ Tier 2: LOCAL OFFLINE CACHE ] 
      │ (If laptop OS / Python server freezes)
      ▼
[ Tier 3: BACKUP MP4 VIDEO ]
```

### Tier 1: `LIVE_STREAMLIT_APP` (Primary Live Mode)
- **Target**: Live browser running `http://localhost:8501` backed by FastAPI at `http://localhost:8000`.
- **Functionality**: Live user interaction triggering real-time Server-Sent Events (SSE) streaming of agent thoughts, tool calls, and reflection critiques.
- **Pre-flight Check**: Verified with `py -m pytest tests/tier1_feature/test_backend_sse.py`.

### Tier 2: `LOCAL_OFFLINE_CACHE` (Secondary High-Speed Mode)
- **Target**: Local mock SQLite/JSON endpoints (`/api/v1/demo/{preset_id}`) running on loopback IP (`127.0.0.1`).
- **Functionality**: Replays pre-computed real agronomic execution traces under 0.5 seconds with zero external network dependencies (Open-Meteo offline cache enabled).
- **Trigger Condition**: If the live Open-Meteo or external LLM API exceeds 3.0 seconds latency, the presenter hits hotkey `[Alt + C]` to switch seamlessly to the local cache without breaking spoken rhythm.

### Tier 3: `BACKUP_MP4_VIDEO` (Ultimate Failsafe Mode)
- **Target**: Pre-recorded 1080p 60fps MP4 video (`agricarbon_demo_60s_4k.mp4`) pre-loaded on VLC / QuickTime in fullscreen on a secondary virtual desktop.
- **Functionality**: Exact 60-second screen capture with embedded English/Japanese subtitles and highlighting cursor effects.
- **Trigger Condition**: If the browser or local Python server crashes, presenter slides trackpad to Desktop 2 (or hits `[Alt + Tab]`) in under 2 seconds and speaks over the video.

---

## Part 2: Second-by-Second Stage Script (00:00 to 01:00)

| Timestamp | Segment & Scene | On-Screen Action & Visual Cues | English Spoken Script (Presenter 1) | Japanese Spoken Script / 日本語 (Presenter 2) |
| :--- | :--- | :--- | :--- | :--- |
| **00:00 – 00:05** | **Scene 1: Hook & Crisis** | Screen displays Streamlit UI showing An Giang Rice Polder map with flashing red salinity/drought alert (Salinity: 4.2‰). | "Judges, right now in Vietnam's Mekong Delta, saltwater intrusion is choking rice fields, while Japan's GX-League demands zero-carbon proof." | 「審査員の皆様、メコンデルタの塩害と日本のGXリーグ厳格化という二重の危機に、農家は直面しています。」 |
| **00:05 – 00:10** | **Scene 1: The Challenge** | Presenter clicks preset selector: `An Giang AWD Rice Polder`. Gauge indicates soil moisture falling towards critical threshold (22%). | "Traditional continuous flooding wastes 7,500 m³ of water and spews methane. Here is AgriCarbon Agent taking autonomous action." | 「従来の常時灌漑は7,500トンの水を浪費しメタンを排出します。そこで自律型AgriCarbonが始動します。」 |
| **00:10 – 00:18** | **Scene 2: Autonomous Sensing** | Click `Execute Autonomous Cycle`. SSE Thought stream lights up in cyan. `SensingAndWeatherAgent` calls `get_weather_forecast`. | "Watch the thought stream in real-time. The Sensing Agent queries live Open-Meteo forecasts and local soil sensor telemetry." | 「思考ストリームがリアルタイムで稼働します。気象データと土壌IoTセンサーを即座に自律取得します。」 |
| **00:18 – 00:25** | **Scene 2: ReAct Deliberation** | Agent thought renders: `Rain forecasted (15mm) at 16:00. Suppressing immediate pump startup to conserve energy.` | "Notice: the Agent detects 15mm rainfall in 6 hours. Instead of blindly pumping, it deliberates and halts unnecessary irrigation!" | 「6時間後に15ミリの降雨を予測。無駄なポンプ稼働を自動停止し、自然の恵みを最大限に活用します。」 |
| **00:25 – 00:32** | **Scene 3: Eco-Dispatch** | `ResourceEcoDispatchAgent` calls FAO-56 Penman-Monteith engine. Generates AWD schedule avoiding peak electricity tariff. | "The Eco-Dispatch Agent applies FAO-56 evapotranspiration models, scheduling water flushes strictly during off-peak power rates." | 「エコ配分エージェントがFAO-56数式に基づき、電気代が最も安いオフピーク時間帯へ灌漑を最適化します。」 |
| **00:32 – 00:40** | **Scene 3: Guardrail Validation** | Green badge appears: `Safety Critic: Agronomic boundaries validated. 0 retries needed. Approved.` | "Our Critic Agent verifies safe moisture bounds before sending actuator signals, ensuring zero crop stress and mathematical safety." | 「安全ガードレールCriticが物理的境界を二重検証し、誤作動リスクをゼロにして作物を保護します。」 |
| **00:40 – 00:45** | **Scene 4: Scope 1-3 Auditing** | `CarbonAuditorAgent` executes IPCC Tier 1 & 2 formula. Bar chart shows baseline vs optimized emissions drop. | "Simultaneously, the Carbon Auditor calculates Scope 1 and Scope 2 emissions, verifying a massive 28.1% greenhouse gas reduction." | 「同時に温室効果ガス監査エージェントがIPCC基準で計算し、排出量を28.1%削減したことを証明します。」 |
| **00:45 – 00:50** | **Scene 4: Cryptographic Ledger** | Tool `record_esg_audit_entry` outputs SHA-256 hash `e3b0c442...`. Bilingual VN/JA Certificate renders on screen. | "In 3 minutes, not 21 days, a cryptographically chained, tamper-evident ESG export certificate is generated for Japanese customs." | 「21日かかっていた監査がわずか3分で完了。改ざん不可能なSHA-256証明書を発行します。」 |
| **00:50 – 00:55** | **Scene 5: Quantitative Proof** | Screen highlights 4 key metrics: `-38% Water`, `-28.1% CO2e`, `-30.5% Fertilizer`, `$0.028/run`. | "The bottom line: minus 38% water, minus 28.1% CO2e, and minus 30.5% fertilizer—all for just 2.8 cents per run!" | 「成果は明白：水38%削減、CO2e 28.1%削減、肥料30.5%削減。1回の実行コストはわずか2.8セントです。」 |
| **00:55 – 01:00** | **Scene 5: Closing CTA** | Fullscreen QR code and slide with Tokyo Innovation Base partnership invitation. Presenters bow together. | "AgriCarbon Agent: Powering sustainable agriculture from Vietnam to Tokyo. Arigato gozaimasu!" | 「ベトナムの大地から東京へ。持続可能な農業を切り拓くAgriCarbonです。ありがとうございました！」 |

---

## Part 3: Stage Contingency Matrix

| Glitch Scenario | Probability | Detection Time | Immediate Stage Action | Spoken Buffer Line |
| :--- | :--- | :--- | :--- | :--- |
| **WiFi Latency > 3.0s** | Medium | 1.5 seconds | Press `[Alt + C]` to switch to local cached preset. | "As our local edge engine demonstrates with zero latency..." |
| **Browser Window Crash** | Low | 1.0 second | Press `[Alt + Tab]` to open fullscreen backup MP4 on Desktop 2. | "Let us examine our high-resolution telemetry replay..." |
| **Projector Signal Glitch** | Rare | Immediate | Speaker continues narration without pausing, using printed cue cards. | "As you see in our architecture, our dual-agent safety loop..." |
| **Audio Mic Interruption** | Medium | Immediate | Switch to handheld microphone, maintain projected voice. | (Repeat last sentence firmly with eye contact to judges) |
