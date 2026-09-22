"""
Tool 4: record_esg_audit_entry
Cryptographic SHA-256 tamper-evident ESG audit ledger entry recorder.
Conforms strictly to PROJECT.md § Tools & Connectors and tests/tier1_feature/test_tools.py.
"""

from typing import Dict, Any, Optional
from datetime import datetime, timezone
from core.domain.esg_ledger import create_block_hash, ESGLedger


# Global in-memory singleton ledger instance for session continuity
_SESSION_LEDGER = ESGLedger()


def get_session_ledger() -> ESGLedger:
    """Returns the current active session ledger singleton."""
    global _SESSION_LEDGER
    return _SESSION_LEDGER


def reset_session_ledger() -> ESGLedger:
    """Resets the active session ledger to a fresh genesis block (useful for test isolation)."""
    global _SESSION_LEDGER
    _SESSION_LEDGER = ESGLedger()
    return _SESSION_LEDGER


def record_esg_audit_entry(
    record_id: str,
    farm_id: str,
    action: str,
    co2e_kg: float,
    prev_hash: str = "0" * 64,
    timestamp: Optional[str] = None,
    crop_type: str = "rice",
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Appends a cryptographically sealed ESG audit record to the tamper-evident ledger.
    Mutates the global _SESSION_LEDGER singleton to maintain an unbroken cryptographic chain.

    Returns:
        Dict with:
            record_id, timestamp, farm_id, action, co2e_kg,
            prev_hash, hash, status="committed", certificate_id,
            chain_index, chain_length
    """
    global _SESSION_LEDGER

    ts = timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    safe_co2e = round(float(co2e_kg), 3)

    clean_farm = farm_id.replace("_", "-").upper()
    cert_id = f"CERT-VJAI-2026-{clean_farm[:8]}-{record_id[-4:].upper()}"

    combined_metadata = {
        "action": action,
        "certificate_id": cert_id,
        **(metadata or {})
    }

    # Extract or estimate baseline emissions
    baseline_co2e = float(
        combined_metadata.get(
            "baseline_co2e_kg",
            round(safe_co2e / (1.0 - 0.281), 3) if safe_co2e > 0 else 100.0
        )
    )

    # Append to the global singleton ledger instance
    entry = _SESSION_LEDGER.append_entry(
        batch_id=record_id,
        farm_id=farm_id,
        crop_type=crop_type,
        scope1_co2e_kg=safe_co2e,
        scope2_co2e_kg=float(combined_metadata.get("scope2_co2e_kg", 0.0)),
        scope3_co2e_kg=float(combined_metadata.get("scope3_co2e_kg", 0.0)),
        baseline_co2e_kg=baseline_co2e,
        metadata=combined_metadata,
        timestamp=ts
    )

    return {
        "record_id": record_id,
        "timestamp": ts,
        "farm_id": farm_id,
        "action": action,
        "co2e_kg": safe_co2e,
        "prev_hash": entry.previous_hash,
        "hash": entry.entry_hash,
        "status": "committed",
        "certificate_id": cert_id,
        "crop_type": crop_type,
        "metadata": combined_metadata,
        "chain_index": entry.index,
        "chain_length": len(_SESSION_LEDGER.chain)
    }
