"""
Cryptographic SHA-256 Tamper-Evident ESG Audit Ledger.
Compliant with ISO 14064-3 and EU CBAM / Japan Green Transformation (GX)
non-repudiation audit requirements.
Provides both high-level cryptographic chain verification and modular
block-hashing utilities.
"""

import hashlib
import json
from datetime import datetime, timezone
from typing import Dict, Any, List, Tuple, Optional
from pydantic import BaseModel, Field, ConfigDict


def create_block_hash(
    record_id: str,
    timestamp: str,
    farm_id: str,
    action: str,
    co2e_kg: float,
    prev_hash: str,
) -> str:
    """
    Computes deterministic SHA-256 block hash for ledger entry.
    Format: record_id|timestamp|farm_id|action|co2e_kg:.3f|prev_hash
    """
    payload = f"{record_id}|{timestamp}|{farm_id}|{action}|{float(co2e_kg):.3f}|{prev_hash}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def verify_ledger_integrity(chain: List[Dict[str, Any]]) -> bool:
    """
    Verifies the SHA-256 cryptographic chain continuity for dictionary-based ledger chains.
    Returns True if unbroken and authentic, False if any entry was altered or re-ordered.
    """
    if not chain:
        return True

    for i in range(len(chain)):
        current = chain[i]
        expected_prev = chain[i - 1]["hash"] if i > 0 else "0" * 64

        if current.get("prev_hash") != expected_prev:
            return False

        computed_hash = create_block_hash(
            record_id=current["record_id"],
            timestamp=current["timestamp"],
            farm_id=current["farm_id"],
            action=current["action"],
            co2e_kg=float(current["co2e_kg"]),
            prev_hash=current["prev_hash"],
        )

        if current.get("hash") != computed_hash:
            return False

    return True


class ESGAuditEntryModel(BaseModel):
    """Pydantic v2 schema for an immutable, hash-chained ESG audit entry."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    index: int = Field(..., ge=0, description="Sequential 0-based block height in ledger")
    timestamp: str = Field(..., description="ISO 8601 UTC timestamp of audit generation")
    batch_id: str = Field(..., min_length=1, description="Unique harvest or export batch identifier")
    farm_id: str = Field(..., min_length=1, description="Registered farm identifier")
    crop_type: str = Field(..., min_length=2, description="Crop cultivar name")
    scope1_co2e_kg: float = Field(..., ge=0.0, description="Scope 1 emissions in kg CO2e")
    scope2_co2e_kg: float = Field(..., ge=0.0, description="Scope 2 emissions in kg CO2e")
    scope3_co2e_kg: float = Field(..., ge=0.0, description="Scope 3 emissions in kg CO2e")
    total_co2e_kg: float = Field(..., ge=0.0, description="Total lifecycle emissions in kg CO2e")
    baseline_co2e_kg: float = Field(..., ge=0.0, description="Baseline reference emissions in kg CO2e")
    reduction_pct: float = Field(..., description="Percentage CO2e reduction achieved")
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Operational metadata and agronomic telemetry"
    )
    previous_hash: str = Field(..., min_length=64, max_length=64, description="SHA-256 digest of previous block")
    entry_hash: str = Field(default="", description="Cryptographic SHA-256 hash of this entry")

    def compute_hash(self) -> str:
        """
        Computes deterministic SHA-256 digest over canonical JSON representation.
        Excludes `entry_hash` itself. Keys are alphabetically sorted, separators are strict.
        """
        payload = self.model_dump(exclude={"entry_hash"}, mode="json")
        canonical_str = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        return hashlib.sha256(canonical_str.encode("utf-8")).hexdigest()


class ESGLedger:
    """In-memory and persistent cryptographic ledger instance."""

    def __init__(self):
        self.chain: List[ESGAuditEntryModel] = []
        self._initialize_genesis_block()

    def _initialize_genesis_block(self):
        """Creates the immutable genesis root block of the AgriCarbon ledger."""
        genesis = ESGAuditEntryModel(
            index=0,
            timestamp="2026-09-08T00:00:00Z",
            batch_id="GENESIS-AGRICARBON-2026",
            farm_id="SYSTEM_ROOT",
            crop_type="GENESIS",
            scope1_co2e_kg=0.0,
            scope2_co2e_kg=0.0,
            scope3_co2e_kg=0.0,
            total_co2e_kg=0.0,
            baseline_co2e_kg=0.0,
            reduction_pct=0.0,
            metadata={
                "system": "AgriCarbon Agent Cryptographic ESG Ledger",
                "version": "1.0.0",
                "standard": "ISO 14064-3 / IPCC 2019 Refinement",
                "origin": "Vietnam Japan AI Hackathon 2026 - Tokyo Innovation Base",
            },
            previous_hash="0" * 64,
        )
        genesis.entry_hash = genesis.compute_hash()
        self.chain.append(genesis)

    @property
    def latest_entry(self) -> ESGAuditEntryModel:
        return self.chain[-1]

    def append_entry(
        self,
        batch_id: str,
        farm_id: str,
        crop_type: str,
        scope1_co2e_kg: float,
        scope2_co2e_kg: float,
        scope3_co2e_kg: float,
        baseline_co2e_kg: float,
        metadata: Optional[Dict[str, Any]] = None,
        timestamp: Optional[str] = None,
    ) -> ESGAuditEntryModel:
        """Appends a new verified audit record to the ledger, computing cryptographic link."""
        if not self.chain:
            self._initialize_genesis_block()

        prev_block = self.chain[-1]
        now_utc = timestamp or datetime.now(timezone.utc).isoformat()
        total_co2e = round(scope1_co2e_kg + scope2_co2e_kg + scope3_co2e_kg, 2)
        reduction_pct = (
            round(((baseline_co2e_kg - total_co2e) / baseline_co2e_kg * 100.0), 1)
            if baseline_co2e_kg > 0
            else 0.0
        )

        entry = ESGAuditEntryModel(
            index=len(self.chain),
            timestamp=now_utc,
            batch_id=batch_id,
            farm_id=farm_id,
            crop_type=crop_type,
            scope1_co2e_kg=round(scope1_co2e_kg, 2),
            scope2_co2e_kg=round(scope2_co2e_kg, 2),
            scope3_co2e_kg=round(scope3_co2e_kg, 2),
            total_co2e_kg=total_co2e,
            baseline_co2e_kg=round(baseline_co2e_kg, 2),
            reduction_pct=reduction_pct,
            metadata=metadata or {},
            previous_hash=prev_block.entry_hash,
        )
        entry.entry_hash = entry.compute_hash()
        self.chain.append(entry)
        return entry

    def export_to_dict(self) -> List[Dict[str, Any]]:
        return [entry.model_dump(mode="json") for entry in self.chain]

    def export_to_json(self, filepath: str) -> None:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.export_to_dict(), f, indent=2)

    @classmethod
    def load_from_dict(cls, data: List[Dict[str, Any]]) -> "ESGLedger":
        ledger = cls.__new__(cls)
        ledger.chain = [ESGAuditEntryModel.model_validate(item) for item in data]
        return ledger


def verify_ledger_chain(chain: List[ESGAuditEntryModel]) -> Tuple[bool, Optional[str]]:
    """
    Cryptographic verification function for the ESG Audit Ledger.
    Returns: (True, None) if completely untampered and structurally sound.
             (False, error_diagnostic) upon any failure.
    """
    if not chain:
        return True, None

    for i, block in enumerate(chain):
        # 1. Verify strict sequential index height
        if block.index != i:
            return False, f"Index height violation at position {i}: expected {i}, found {block.index}."

        # 2. Verify genesis root hash
        if i == 0:
            if block.previous_hash != "0" * 64:
                return False, f"Genesis block previous_hash must be 64 zeros, found: {block.previous_hash}."
        else:
            # 3. Verify cryptographic linkage with parent block
            parent_block = chain[i - 1]
            if block.previous_hash != parent_block.entry_hash:
                return (
                    False,
                    f"Cryptographic link broken at index {i}: "
                    f"block.previous_hash ({block.previous_hash[:12]}...) "
                    f"does not match parent.entry_hash ({parent_block.entry_hash[:12]}...).",
                )

        # 4. Verify cryptographic hash integrity of the block payload
        recomputed_hash = block.compute_hash()
        if block.entry_hash != recomputed_hash:
            return (
                False,
                f"Tampering detected at block index {i} (batch: {block.batch_id}): "
                f"stored hash ({block.entry_hash[:12]}...) != recomputed hash ({recomputed_hash[:12]}...).",
            )

    return True, None
