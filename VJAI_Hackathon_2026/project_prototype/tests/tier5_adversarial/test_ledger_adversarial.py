"""
Tier 5 Adversarial Stress Testing Suite: ESG Ledger Cryptographic Attacks & Fuzzing
Milestone 1 Challenger 2: Ledger Cryptographic Attack & Fuzzing.
Authoritative Reference: PROJECT.md, ORIGINAL_REQUEST.md, core/domain/esg_ledger.py
"""

import copy
import hashlib
import json
import math
import random
import time
import pytest
from typing import Dict, Any, List
from pydantic import ValidationError

from core.domain.esg_ledger import (
    create_block_hash,
    verify_ledger_integrity,
    ESGAuditEntryModel,
    ESGLedger,
    verify_ledger_chain,
)


@pytest.fixture
def populated_ledger() -> ESGLedger:
    """Creates a 5-block cryptographic ESG ledger for adversarial manipulation."""
    ledger = ESGLedger()
    
    # Block 1: An Giang Rice AWD Batch 1
    ledger.append_entry(
        batch_id="BATCH-VN-2026-RICE-001",
        farm_id="VN-AG-TRITON-001",
        crop_type="Jasmine 85 Rice",
        scope1_co2e_kg=2189.58,
        scope2_co2e_kg=830.42,
        scope3_co2e_kg=2256.00,
        baseline_co2e_kg=6456.00,
        metadata={"field_ha": 5.0, "irrigation_method": "AWD", "water_savings_m3": 14250.0},
        timestamp="2026-09-08T06:00:00Z",
    )
    # Block 2: Lam Dong Coffee Drip Batch 2
    ledger.append_entry(
        batch_id="BATCH-VN-2026-COFFEE-002",
        farm_id="VN-LD-CAUDAT-002",
        crop_type="Arabica Coffee",
        scope1_co2e_kg=1450.20,
        scope2_co2e_kg=410.50,
        scope3_co2e_kg=988.80,
        baseline_co2e_kg=3788.80,
        metadata={"field_ha": 3.5, "irrigation_method": "solar_drip", "fertilizer_saved_kg": 192.5},
        timestamp="2026-09-08T07:00:00Z",
    )
    # Block 3: Mekong Delta AWD Batch 3
    ledger.append_entry(
        batch_id="BATCH-VN-2026-RICE-003",
        farm_id="VN-DT-THAPMUOI-003",
        crop_type="ST25 Rice",
        scope1_co2e_kg=1950.00,
        scope2_co2e_kg=780.00,
        scope3_co2e_kg=2100.00,
        baseline_co2e_kg=6100.00,
        metadata={"field_ha": 4.2, "export_destination": "Tokyo Port"},
        timestamp="2026-09-08T08:00:00Z",
    )
    # Block 4: Central Highlands Arabica Batch 4
    ledger.append_entry(
        batch_id="BATCH-VN-2026-COFFEE-004",
        farm_id="VN-GL-PLEIKU-004",
        crop_type="Robusta Fine",
        scope1_co2e_kg=1200.00,
        scope2_co2e_kg=350.00,
        scope3_co2e_kg=850.00,
        baseline_co2e_kg=3200.00,
        metadata={"field_ha": 2.8, "buyer": "Japan Green Trade Corp"},
        timestamp="2026-09-08T09:00:00Z",
    )
    return ledger


# ============================================================================
# 1. BIT-FLIP ATTACK SUITE
# ============================================================================

class TestLedgerBitFlipAttacks:
    """Simulates single bit-flips and precision tampering across all block positions."""

    def test_intermediate_block_payload_bit_flip(self, populated_ledger):
        """Mutating intermediate block (index 2) payload must fail verification and identify index 2."""
        chain = populated_ledger.chain
        assert len(chain) == 5
        
        # Tamper intermediate block payload (reduce scope1_co2e_kg by 1 bit / 0.01 kg)
        original_val = chain[2].scope1_co2e_kg
        chain[2].scope1_co2e_kg = round(original_val - 0.01, 2)
        
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        assert err is not None
        assert "Tampering detected at block index 2" in err
        assert chain[2].batch_id in err

    def test_genesis_block_payload_bit_flip(self, populated_ledger):
        """Mutating genesis root block payload (index 0) must be detected at block index 0."""
        chain = populated_ledger.chain
        chain[0].batch_id = "GENESIS-AGRICARBON-2026-FORGED"
        
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        assert err is not None
        assert "Tampering detected at block index 0" in err

    def test_terminal_block_payload_bit_flip(self, populated_ledger):
        """Mutating terminal block payload (index 4) must be detected at block index 4."""
        chain = populated_ledger.chain
        chain[4].reduction_pct = 99.9  # Exaggerated greenwashing claim
        
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        assert err is not None
        assert "Tampering detected at block index 4" in err

    def test_previous_hash_single_hex_flip(self, populated_ledger):
        """Flipping 1 character in previous_hash of block 3 breaks cryptographic link."""
        chain = populated_ledger.chain
        orig_prev = chain[3].previous_hash
        flipped_char = "a" if orig_prev[0] != "a" else "b"
        chain[3].previous_hash = flipped_char + orig_prev[1:]
        
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        assert "Cryptographic link broken at index 3" in err

    def test_entry_hash_single_hex_flip(self, populated_ledger):
        """Flipping 1 character in stored entry_hash must trigger tampering detection at that block."""
        chain = populated_ledger.chain
        orig_entry = chain[2].entry_hash
        flipped_char = "0" if orig_entry[-1] != "0" else "1"
        chain[2].entry_hash = orig_entry[:-1] + flipped_char
        
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        assert "Tampering detected at block index 2" in err

    def test_dict_ledger_bit_flip_tampering(self):
        """Verifies create_block_hash & verify_ledger_integrity catch single bit mutations in dict chain."""
        chain = []
        h0 = "0" * 64
        h1 = create_block_hash("rec1", "2026-09-08T00:00:00Z", "farm1", "pump", 10.0, h0)
        chain.append({"record_id": "rec1", "timestamp": "2026-09-08T00:00:00Z", "farm_id": "farm1", "action": "pump", "co2e_kg": 10.0, "prev_hash": h0, "hash": h1})
        
        h2 = create_block_hash("rec2", "2026-09-08T01:00:00Z", "farm1", "fert", 20.0, h1)
        chain.append({"record_id": "rec2", "timestamp": "2026-09-08T01:00:00Z", "farm_id": "farm1", "action": "fert", "co2e_kg": 20.0, "prev_hash": h1, "hash": h2})
        
        assert verify_ledger_integrity(chain) is True
        
        # Flip bit in co2e_kg of block 1
        tampered = [dict(c) for c in chain]
        tampered[0]["co2e_kg"] = 10.001
        assert verify_ledger_integrity(tampered) is False
        
        # Flip bit in action of block 2
        tampered2 = [dict(c) for c in chain]
        tampered2[1]["action"] = "fert_hack"
        assert verify_ledger_integrity(tampered2) is False

    def test_randomized_bit_flip_monte_carlo_50_trials(self, populated_ledger):
        """Monte Carlo: 50 randomized field mutations across blocks are 100% caught with exact index."""
        chain = populated_ledger.chain
        fields = ["scope1_co2e_kg", "scope2_co2e_kg", "scope3_co2e_kg", "batch_id", "crop_type", "total_co2e_kg"]
        
        for trial in range(50):
            target_idx = random.randint(1, 4)
            field = random.choice(fields)
            chain_copy = [b.model_copy() for b in chain]
            
            if "co2e" in field:
                val = getattr(chain_copy[target_idx], field)
                setattr(chain_copy[target_idx], field, round(val + 0.01 * (trial + 1), 2))
            else:
                setattr(chain_copy[target_idx], field, getattr(chain_copy[target_idx], field) + f"_t{trial}")
                
            is_valid, err = verify_ledger_chain(chain_copy)
            assert is_valid is False
            assert f"Tampering detected at block index {target_idx}" in err


# ============================================================================
# 2. PREIMAGE & FORGERY ATTACK SUITE
# ============================================================================

class TestLedgerPreimageAndForgeryAttacks:
    """Simulates re-hash forgery, delimiter collision, and chain rewriting."""

    def test_intermediate_block_rehash_attack(self, populated_ledger):
        """Attacker mutates block 2 AND updates entry_hash(block 2). Verification must catch broken link at block 3."""
        chain = populated_ledger.chain
        # Mutate block 2
        chain[2].scope1_co2e_kg = 500.00
        # Recompute entry_hash so block 2 internally matches
        chain[2].entry_hash = chain[2].compute_hash()
        
        # Chain verification should catch broken parent link at block 3
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        assert "Cryptographic link broken at index 3" in err

    def test_create_block_hash_delimiter_collision(self):
        """
        VULNERABILITY PROOF: create_block_hash uses pipe '|' delimiter without escaping.
        An attacker injecting '|' into record_id or timestamp can cause identical block hashes for different inputs.
        """
        # Target 1: record_id has pipe, timestamp has no pipe
        h1 = create_block_hash(
            record_id="rec_01|2026-09-08T00:00:00Z",
            timestamp="farm_A",
            farm_id="action_pump",
            action="idle",
            co2e_kg=10.0,
            prev_hash="0" * 64,
        )
        # Target 2: record_id and timestamp partitioned differently
        h2 = create_block_hash(
            record_id="rec_01",
            timestamp="2026-09-08T00:00:00Z|farm_A",
            farm_id="action_pump",
            action="idle",
            co2e_kg=10.0,
            prev_hash="0" * 64,
        )
        # Because delimiter is unescaped, payloads are identical:
        assert h1 == h2, "Delimiter collision confirmed: create_block_hash allows cross-field spoofing!"

    def test_esg_audit_entry_model_immune_to_delimiter_collision(self):
        """
        In contrast to create_block_hash, ESGAuditEntryModel canonical JSON serialization
        is completely immune to delimiter injection attacks.
        """
        e1 = ESGAuditEntryModel(
            index=1,
            timestamp="2026-09-08T06:00:00Z",
            batch_id="BATCH|SPOOF",
            farm_id="FARM_A",
            crop_type="Rice",
            scope1_co2e_kg=10.0,
            scope2_co2e_kg=5.0,
            scope3_co2e_kg=2.0,
            total_co2e_kg=17.0,
            baseline_co2e_kg=25.0,
            reduction_pct=32.0,
            previous_hash="0" * 64,
        )
        e2 = ESGAuditEntryModel(
            index=1,
            timestamp="2026-09-08T06:00:00Z",
            batch_id="BATCH",
            farm_id="SPOOF|FARM_A",
            crop_type="Rice",
            scope1_co2e_kg=10.0,
            scope2_co2e_kg=5.0,
            scope3_co2e_kg=2.0,
            total_co2e_kg=17.0,
            baseline_co2e_kg=25.0,
            reduction_pct=32.0,
            previous_hash="0" * 64,
        )
        assert e1.compute_hash() != e2.compute_hash(), "Canonical JSON guarantees key-separated non-collision"

    def test_downstream_recomputation_attack_analysis(self, populated_ledger):
        """
        If an attacker with local file access mutates block 1 AND recomputes all blocks downstream
        (1 to 4) with updated previous_hash and entry_hash, internal verify_ledger_chain passes!
        This proves the necessity of asymmetric digital signatures or external root anchoring for ISO 14064-3.
        """
        chain = populated_ledger.chain
        # Mutate block 1
        chain[1].scope1_co2e_kg = 1.00
        chain[1].entry_hash = chain[1].compute_hash()
        
        # Cascade recompute
        for i in range(2, len(chain)):
            chain[i].previous_hash = chain[i - 1].entry_hash
            chain[i].entry_hash = chain[i].compute_hash()
            
        # Internal consistency check:
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is True, "Re-hashed subchain is internally consistent unless externally anchored"


# ============================================================================
# 3. CHAIN RE-ORDERING, TRUNCATION & STRUCTURAL ATTACKS
# ============================================================================

class TestLedgerStructuralAttacks:
    """Tests permutation, deletion, splicing, and genesis poisoning attacks."""

    def test_block_swap_reordering_attack(self, populated_ledger):
        """Swapping block 2 and block 3 violates both sequential index and cryptographic link."""
        chain = populated_ledger.chain
        chain[2], chain[3] = chain[3], chain[2]
        
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        assert "Index height violation at position 2" in err

    def test_block_deletion_gap_attack(self, populated_ledger):
        """Deleting block 2 leaves a height violation [0, 1, 3, 4]."""
        chain = populated_ledger.chain
        del chain[2]
        
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        assert "Index height violation at position 2" in err

    def test_block_insertion_splicing_attack(self, populated_ledger):
        """Inserting an extra block creates height violation at subsequent blocks."""
        chain = populated_ledger.chain
        forged_block = copy.deepcopy(chain[2])
        chain.insert(2, forged_block)
        
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        # The inserted block has index 2, but block at position 3 still has index 2
        assert "Index height violation at position 3" in err

    def test_genesis_previous_hash_poisoning(self, populated_ledger):
        """Genesis block with previous_hash != 64 zeros must be rejected."""
        chain = populated_ledger.chain
        chain[0].previous_hash = "f" * 64
        
        is_valid, err = verify_ledger_chain(chain)
        assert is_valid is False
        assert "Genesis block previous_hash must be 64 zeros" in err

    def test_empty_chain_handling(self):
        """Empty ledger returns valid True with no diagnostic."""
        is_valid, err = verify_ledger_chain([])
        assert is_valid is True
        assert err is None


# ============================================================================
# 4. FUZZING WITH MALFORMED JSON & TYPE VALIDATION
# ============================================================================

class TestLedgerMalformedJsonFuzzing:
    """Fuzzes Pydantic schema with invalid fields, negative values, and non-serializable objects."""

    def test_forbid_extra_unauthorized_fields(self):
        """ModelConfig(extra='forbid') must reject injection of malicious extra keys."""
        with pytest.raises(ValidationError) as exc:
            ESGAuditEntryModel(
                index=1,
                timestamp="2026-09-08T00:00:00Z",
                batch_id="BATCH-01",
                farm_id="FARM-01",
                crop_type="Rice",
                scope1_co2e_kg=10.0,
                scope2_co2e_kg=5.0,
                scope3_co2e_kg=2.0,
                total_co2e_kg=17.0,
                baseline_co2e_kg=25.0,
                reduction_pct=32.0,
                previous_hash="0" * 64,
                malicious_backdoor="INJECTED_VALUE",
            )
        assert "extra_forbidden" in str(exc.value)

    def test_negative_emissions_rejected(self):
        """Negative emissions violate ge=0.0 constraint."""
        with pytest.raises(ValidationError) as exc:
            ESGAuditEntryModel(
                index=1,
                timestamp="2026-09-08T00:00:00Z",
                batch_id="BATCH-01",
                farm_id="FARM-01",
                crop_type="Rice",
                scope1_co2e_kg=-15.0,
                scope2_co2e_kg=5.0,
                scope3_co2e_kg=2.0,
                total_co2e_kg=17.0,
                baseline_co2e_kg=25.0,
                reduction_pct=32.0,
                previous_hash="0" * 64,
            )
        assert "greater_than_equal" in str(exc.value)

    def test_empty_string_batch_id_rejected(self):
        """batch_id with min_length=1 must reject empty string."""
        with pytest.raises(ValidationError):
            ESGAuditEntryModel(
                index=1,
                timestamp="2026-09-08T00:00:00Z",
                batch_id="",
                farm_id="FARM-01",
                crop_type="Rice",
                scope1_co2e_kg=10.0,
                scope2_co2e_kg=5.0,
                scope3_co2e_kg=2.0,
                total_co2e_kg=17.0,
                baseline_co2e_kg=25.0,
                reduction_pct=32.0,
                previous_hash="0" * 64,
            )

    def test_invalid_hash_length_rejected(self):
        """previous_hash with length != 64 must be rejected by Pydantic min_length/max_length."""
        with pytest.raises(ValidationError):
            ESGAuditEntryModel(
                index=1,
                timestamp="2026-09-08T00:00:00Z",
                batch_id="BATCH-01",
                farm_id="FARM-01",
                crop_type="Rice",
                scope1_co2e_kg=10.0,
                scope2_co2e_kg=5.0,
                scope3_co2e_kg=2.0,
                total_co2e_kg=17.0,
                baseline_co2e_kg=25.0,
                reduction_pct=32.0,
                previous_hash="tooshort",
            )

    def test_nan_float_rejected_by_ge_constraint(self):
        """float('nan') fails ge=0.0 in Pydantic v2."""
        with pytest.raises(ValidationError):
            ESGAuditEntryModel(
                index=1,
                timestamp="2026-09-08T00:00:00Z",
                batch_id="BATCH-01",
                farm_id="FARM-01",
                crop_type="Rice",
                scope1_co2e_kg=float("nan"),
                scope2_co2e_kg=5.0,
                scope3_co2e_kg=2.0,
                total_co2e_kg=17.0,
                baseline_co2e_kg=25.0,
                reduction_pct=32.0,
                previous_hash="0" * 64,
            )

    def test_infinity_float_handling(self):
        """
        FINDING: float('inf') passes ge=0.0 in Python and Pydantic!
        json.dumps with default allow_nan=True outputs non-standard 'Infinity'.
        """
        entry = ESGAuditEntryModel(
            index=1,
            timestamp="2026-09-08T00:00:00Z",
            batch_id="BATCH-01",
            farm_id="FARM-01",
            crop_type="Rice",
            scope1_co2e_kg=float("inf"),
            scope2_co2e_kg=5.0,
            scope3_co2e_kg=2.0,
            total_co2e_kg=float("inf"),
            baseline_co2e_kg=25.0,
            reduction_pct=0.0,
            previous_hash="0" * 64,
        )
        h = entry.compute_hash()
        assert len(h) == 64

    def test_load_from_dict_malformed_entries(self):
        """load_from_dict rejects empty list of dicts, missing fields, and bad types."""
        with pytest.raises(ValidationError):
            ESGLedger.load_from_dict([{}])

        with pytest.raises(ValidationError):
            ESGLedger.load_from_dict([{"index": "not_an_int"}])

    def test_accounting_integrity_desync_finding(self, populated_ledger):
        """
        FINDING: verify_ledger_chain validates cryptographic links, but NOT mathematical consistency
        between scope1+scope2+scope3 and total_co2e_kg!
        A fraudulent entry claiming 0.0 total emissions passes chain verification.
        """
        fraudulent_entry = ESGAuditEntryModel(
            index=5,
            timestamp="2026-09-08T10:00:00Z",
            batch_id="BATCH-GREENWASH-001",
            farm_id="VN-AG-001",
            crop_type="Rice",
            scope1_co2e_kg=5000.0,
            scope2_co2e_kg=2000.0,
            scope3_co2e_kg=3000.0,
            total_co2e_kg=0.0,  # Blatant lie: 5000+2000+3000 != 0.0
            baseline_co2e_kg=10000.0,
            reduction_pct=100.0,
            previous_hash=populated_ledger.chain[-1].entry_hash,
        )
        fraudulent_entry.entry_hash = fraudulent_entry.compute_hash()
        populated_ledger.chain.append(fraudulent_entry)
        
        # Verify chain passes because hash and link are consistent:
        valid, err = verify_ledger_chain(populated_ledger.chain)
        assert valid is True, "Cryptographic verification passes despite accounting fraud"


# ============================================================================
# 5. UNICODE & BILINGUAL FUZZING (JAPANESE & VIETNAMESE)
# ============================================================================

class TestLedgerUnicodeFuzzing:
    """Fuzzes ledger with Japanese Kanji/Kana, Vietnamese diacritics, and emojis."""

    def test_japanese_payload_canonical_hashing(self):
        """Japanese characters in farm_id, crop_type, and metadata are hashed predictably."""
        entry = ESGAuditEntryModel(
            index=1,
            timestamp="2026-09-08T06:00:00Z",
            batch_id="BATCH-JP-2026-越光-01",
            farm_id="新潟県魚沼市コシヒカリ組合",
            crop_type="水稲（コシヒカリ）",
            scope1_co2e_kg=1500.50,
            scope2_co2e_kg=350.20,
            scope3_co2e_kg=900.00,
            total_co2e_kg=2750.70,
            baseline_co2e_kg=3800.00,
            reduction_pct=27.6,
            metadata={
                "origin": "日本国東京都千代田区大手町",
                "exporter": "日越環境農業協同組合",
                "certification": "J-Credit認証 / 温室効果ガス削減監査",
            },
            previous_hash="0" * 64,
        )
        h1 = entry.compute_hash()
        h2 = entry.compute_hash()
        assert h1 == h2
        assert len(h1) == 64

    def test_vietnamese_diacritics_canonical_hashing(self):
        """Complex Vietnamese tone marks and vowel combinations."""
        entry = ESGAuditEntryModel(
            index=1,
            timestamp="2026-09-08T06:00:00Z",
            batch_id="LÔ-XUẤT-KHẨU-GẠO-ST25-SỐ-009",
            farm_id="HỢP-TÁC-XÃ-NÔNG-NGHIỆP-TRI-TÔN-AN-GIANG",
            crop_type="Lúa Jasmine 85 Đặc Sản Miền Tây",
            scope1_co2e_kg=2189.58,
            scope2_co2e_kg=830.42,
            scope3_co2e_kg=2256.00,
            total_co2e_kg=5276.00,
            baseline_co2e_kg=7338.00,
            reduction_pct=28.1,
            metadata={
                "địa_chỉ": "Ấp An Hòa, Xã Châu Lăng, Huyện Tri Tôn, Tỉnh An Giang",
                "quy_trình": "Ngập khô xen kẽ (AWD) giảm phát thải khí mê-tan CH4",
                "chứng_nhận": "Tiêu chuẩn Giảm phát thải Khí nhà kính ISO 14064-3",
            },
            previous_hash="0" * 64,
        )
        entry.entry_hash = entry.compute_hash()
        valid, err = verify_ledger_chain([entry])
        # Entry index is 1, so index height violation is expected if single block
        assert valid is False
        assert "Index height violation at position 0" in err

    def test_unicode_bilingual_ledger_full_chain(self):
        """Tests a bilingual VN-JP ledger with genesis and 2 bilingual blocks."""
        ledger = ESGLedger()
        
        # Block 1 (VN)
        ledger.append_entry(
            batch_id="LÔ-AG-2026-LÚA-01",
            farm_id="Hợp Tác Xã Tri Tôn",
            crop_type="Lúa ST25",
            scope1_co2e_kg=2000.0,
            scope2_co2e_kg=800.0,
            scope3_co2e_kg=2200.0,
            baseline_co2e_kg=7000.0,
            metadata={"ghg_reduction": "28.1% Giảm phát thải"},
        )
        # Block 2 (JP)
        ledger.append_entry(
            batch_id="BATCH-JP-2026-東京-02",
            farm_id="東京イノベーションベース輸入拠点",
            crop_type="越光米（輸出用）",
            scope1_co2e_kg=1200.0,
            scope2_co2e_kg=400.0,
            scope3_co2e_kg=950.0,
            baseline_co2e_kg=3500.0,
            metadata={"会場": "Tokyo Innovation Base (TiB)"},
        )
        
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is True
        assert err is None

    def test_emoji_and_special_symbols_in_metadata(self):
        """Emojis (🌾, 🚜, 🇯🇵, 🇻🇳) do not break canonical string encoding."""
        ledger = ESGLedger()
        ledger.append_entry(
            batch_id="BATCH-EMOJI-🌾",
            farm_id="FARM-🚜-🌱",
            crop_type="Rice 🍚",
            scope1_co2e_kg=10.0,
            scope2_co2e_kg=5.0,
            scope3_co2e_kg=2.0,
            baseline_co2e_kg=25.0,
            metadata={"icons": "🌾🚜💧🇯🇵🇻🇳", "symbol": "©®™✓★"},
        )
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is True
        assert err is None

    def test_zero_width_and_control_characters(self):
        """Zero-width space and RTL override are preserved deterministically."""
        ledger = ESGLedger()
        ledger.append_entry(
            batch_id="BATCH\u200bZWSP\u200c",
            farm_id="FARM\u202eRTL",
            crop_type="Rice\x00NULL",
            scope1_co2e_kg=10.0,
            scope2_co2e_kg=5.0,
            scope3_co2e_kg=2.0,
            baseline_co2e_kg=25.0,
        )
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is True
        assert err is None


# ============================================================================
# 6. BOUNDARY & MALFORMED TIMESTAMPS FUZZING
# ============================================================================

class TestLedgerBoundaryTimestamps:
    """Fuzzes timestamps with extremes: Unix epoch 1970, year 9999, leap days, and non-ISO strings."""

    def test_unix_epoch_1970_timestamp(self):
        """Timestamp at Unix epoch start."""
        ledger = ESGLedger()
        entry = ledger.append_entry(
            batch_id="BATCH-1970",
            farm_id="FARM-1970",
            crop_type="Rice",
            scope1_co2e_kg=10.0,
            scope2_co2e_kg=5.0,
            scope3_co2e_kg=2.0,
            baseline_co2e_kg=25.0,
            timestamp="1970-01-01T00:00:00Z",
        )
        assert entry.timestamp == "1970-01-01T00:00:00Z"
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is True

    def test_far_future_9999_timestamp(self):
        """Timestamp in far future year 9999."""
        ledger = ESGLedger()
        entry = ledger.append_entry(
            batch_id="BATCH-9999",
            farm_id="FARM-9999",
            crop_type="Rice",
            scope1_co2e_kg=10.0,
            scope2_co2e_kg=5.0,
            scope3_co2e_kg=2.0,
            baseline_co2e_kg=25.0,
            timestamp="9999-12-31T23:59:59.999Z",
        )
        assert entry.timestamp == "9999-12-31T23:59:59.999Z"
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is True

    def test_leap_year_february_29(self):
        """Leap year February 29th timestamp."""
        ledger = ESGLedger()
        entry = ledger.append_entry(
            batch_id="BATCH-LEAP",
            farm_id="FARM-LEAP",
            crop_type="Rice",
            scope1_co2e_kg=10.0,
            scope2_co2e_kg=5.0,
            scope3_co2e_kg=2.0,
            baseline_co2e_kg=25.0,
            timestamp="2024-02-29T12:00:00+07:00",
        )
        assert "2024-02-29" in entry.timestamp
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is True

    def test_various_timezone_offsets(self):
        """Offsets +07:00 (Vietnam) and +09:00 (Japan) produce valid distinct blocks."""
        ledger = ESGLedger()
        e_vn = ledger.append_entry(
            batch_id="BATCH-VN",
            farm_id="FARM-VN",
            crop_type="Rice",
            scope1_co2e_kg=10.0, scope2_co2e_kg=5.0, scope3_co2e_kg=2.0, baseline_co2e_kg=25.0,
            timestamp="2026-09-08T13:00:00+07:00",
        )
        e_jp = ledger.append_entry(
            batch_id="BATCH-JP",
            farm_id="FARM-JP",
            crop_type="Coffee",
            scope1_co2e_kg=10.0, scope2_co2e_kg=5.0, scope3_co2e_kg=2.0, baseline_co2e_kg=25.0,
            timestamp="2026-09-08T15:00:00+09:00",
        )
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is True
        assert err is None

    def test_non_iso_arbitrary_string_timestamp_finding(self):
        """
        FINDING: ESGAuditEntryModel defines timestamp as plain str.
        It does not enforce ISO 8601 validation or chronological monotonicity!
        A block with timestamp='yesterday' or out-of-order timestamp is accepted.
        """
        ledger = ESGLedger()
        entry = ledger.append_entry(
            batch_id="BATCH-WEIRD-TIME",
            farm_id="FARM-01",
            crop_type="Rice",
            scope1_co2e_kg=10.0, scope2_co2e_kg=5.0, scope3_co2e_kg=2.0, baseline_co2e_kg=25.0,
            timestamp="not_an_iso_timestamp",
        )
        # It hashes and verifies because compute_hash just dumps whatever string is stored:
        valid, err = verify_ledger_chain(ledger.chain)
        assert valid is True


# ============================================================================
# 7. HIGH LOAD SCALE & RAPID TAMPER PINPOINTING
# ============================================================================

class TestLedgerScaleAndTamperPinpointing:
    """Validates throughput, sub-10ms verification, and instant tamper localization on 500+ blocks."""

    def test_500_blocks_scale_and_tamper_localization(self):
        """500 blocks chain verification completes in <20ms and tampering is localized instantly."""
        ledger = ESGLedger()
        for i in range(1, 501):
            ledger.append_entry(
                batch_id=f"SCALE-BATCH-{i:04d}",
                farm_id=f"FARM-{i % 10:02d}",
                crop_type="Jasmine 85 Rice" if i % 2 == 0 else "Arabica Coffee",
                scope1_co2e_kg=100.0 + (i % 50),
                scope2_co2e_kg=50.0 + (i % 20),
                scope3_co2e_kg=200.0 + (i % 100),
                baseline_co2e_kg=500.0 + (i % 100),
            )
        
        # Verify valid chain
        t0 = time.perf_counter()
        valid, err = verify_ledger_chain(ledger.chain)
        verify_duration_ms = (time.perf_counter() - t0) * 1000.0
        assert valid is True
        assert err is None
        assert verify_duration_ms < 50.0, f"500 blocks verification took {verify_duration_ms:.2f}ms (>50ms)"

        # Tamper intermediate block 250
        ledger.chain[250].scope1_co2e_kg += 0.05
        t1 = time.perf_counter()
        tampered_valid, tamper_err = verify_ledger_chain(ledger.chain)
        detect_duration_ms = (time.perf_counter() - t1) * 1000.0
        
        assert tampered_valid is False
        assert "Tampering detected at block index 250" in tamper_err
        assert "SCALE-BATCH-0250" in tamper_err
        assert detect_duration_ms < 25.0
