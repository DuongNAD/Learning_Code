"""
Streamlit UI Component: Interactive Metrics Dashboard & Telemetry Gauges.
Displays quantitative sustainable impact metrics:
- Water saved (-38.0%)
- Carbon emissions avoided (-28.1% to -34.97%)
- Chemical fertilizer reduction (-30.5%)
- Cost savings (15.1M VND / crop)
- EVN peak electricity tariff avoidance (-63.3%)
Authoritative source: PROJECT.md § Architecture, Feature Inventory
"""

from typing import Dict, Any, Optional
import streamlit as st


def render_telemetry_gauges(telemetry: Dict[str, Any], weather: Optional[Dict[str, Any]] = None):
    """Renders IoT telemetry cards and sensor statuses."""
    st.markdown("### 🛰️ Real-Time Farm IoT Telemetry")

    col1, col2, col3, col4 = st.columns(4)

    moisture = telemetry.get("soil_moisture_pct", 0.0)
    col1.metric(
        label="🌱 Soil Moisture",
        value=f"{moisture:.1f}%",
        delta="Above RAW threshold" if moisture >= 25 else "Below RAW threshold",
        delta_color="normal" if moisture >= 25 else "inverse"
    )

    temp_c = telemetry.get("soil_temperature_c") or telemetry.get("soil_temperature_celsius", 28.0)
    col2.metric(
        label="🌡️ Soil Temperature",
        value=f"{temp_c:.1f} °C",
        delta="Optimal"
    )

    pump_status = telemetry.get("pump_status") or telemetry.get("pump_operational_state", "STANDBY")
    col3.metric(
        label="⚡ Pump Status",
        value=str(pump_status).upper(),
        delta="Auto AWD Relay"
    )

    rain_prob = 0.0
    if weather:
        rain_prob = weather.get("rain_probability") or weather.get("summary_48h", {}).get("precipitation_probability_pct", 0.0)
    col4.metric(
        label="🌧️ Rain Probability",
        value=f"{rain_prob:.0f}%",
        delta="Convective storm building" if rain_prob > 50 else "Low rain chance"
    )


def render_metrics_dashboard(data: Dict[str, Any]):
    """
    Renders high-impact sustainability comparison cards proving measurable Green Impact.
    """
    st.markdown("### 📊 Measurable Sustainable Impact vs. Conventional Baseline")

    # Top KPI summary cards
    c1, c2, c3, c4 = st.columns(4)

    water_saved = data.get("water_saved_pct", 38.0)
    c1.metric(
        label="💧 Water Reduction",
        value=f"-{water_saved:.1f}%",
        delta="14,250 m³ conserved (AWD)",
        delta_color="normal"
    )

    co2e_saved = data.get("co2e_saved_pct", 28.1)
    c2.metric(
        label="🌱 CO₂e Reduction",
        value=f"-{co2e_saved:.1f}%",
        delta="10.22 tCO₂e avoided",
        delta_color="normal"
    )

    fert_saved = data.get("fertilizer_saved_pct", 30.5)
    c3.metric(
        label="🧪 Fertilizer (N) Saved",
        value=f"-{fert_saved:.1f}%",
        delta="275 kg N synthetic avoided",
        delta_color="normal"
    )

    c4.metric(
        label="💰 Farmer Cost Savings",
        value="15.1M VND",
        delta="~$610 USD / 5ha crop",
        delta_color="normal"
    )

    st.markdown("---")

    # Detailed comparative breakdown table
    st.markdown("#### 🔬 Detailed Environmental & Economic Balance")
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(
            """
            <div style="background: #fff5f5; padding: 14px; border-radius: 8px; border-left: 4px solid #e53e3e;">
                <h5 style="color: #c53030; margin-top: 0;">❌ Conventional Flood Practice (Baseline)</h5>
                <ul style="font-size: 14px; line-height: 1.6; color: #4a5568;">
                    <li><strong>Water Use:</strong> 7,500 m³/ha (37,500 m³ total)</li>
                    <li><strong>GHG Emissions:</strong> 29.22 tCO₂e (Anaerobic CH₄ surge)</li>
                    <li><strong>Pumping Power:</strong> 9,000 kWh (16.8M VND)</li>
                    <li><strong>Chemical N:</strong> 180 kg/ha (High nitrate leaching)</li>
                    <li><strong>Audit Time:</strong> 21 days manual certification</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_right:
        st.markdown(
            """
            <div style="background: #f0fff4; padding: 14px; border-radius: 8px; border-left: 4px solid #38a169;">
                <h5 style="color: #276749; margin-top: 0;">✅ AgriCarbon Autonomous Agent Optimization</h5>
                <ul style="font-size: 14px; line-height: 1.6; color: #2d3748;">
                    <li><strong>Water Use:</strong> 4,650 m³/ha (<strong>-38.0%</strong> savings via AWD)</li>
                    <li><strong>GHG Emissions:</strong> 19.00 tCO₂e (<strong>-34.97%</strong> Scope 1-3)</li>
                    <li><strong>Pumping Power:</strong> 5,750 kWh (<strong>-36.1%</strong>, EVN off-peak)</li>
                    <li><strong>Chemical N:</strong> 125 kg/ha (<strong>-30.5%</strong> precision dosage)</li>
                    <li><strong>Audit Time:</strong> <strong>&lt; 5.0 seconds</strong> instant SHA-256 ledger</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Tariff avoidance bar
    st.markdown("#### ⚡ EVN Electricity Tariff Optimization")
    st.progress(0.633, text="63.3% Cost Savings Achieved: Pumping scheduled during Off-Peak Hours (1,120 VND/kWh vs. Peak 3,050 VND/kWh)")
