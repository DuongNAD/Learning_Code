import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import json, time, threading
from core.agents.state import create_initial_agent_state
from core.agents.graph import build_agricarbon_graph, run_agent_workflow, stream_agent_execution
from core.agents.supervisor import supervisor_node, route_supervisor_decision
from core.agents.sensing_agent import sensing_agent_node
from core.agents.dispatch_agent import dispatch_agent_node
from core.agents.carbon_agent import carbon_agent_node
from core.agents.critic_agent import critic_agent_node, evaluate_plan_by_critic
from core.tools.ledger_tool import _SESSION_LEDGER, record_esg_audit_entry, reset_session_ledger
from core.domain.esg_ledger import verify_ledger_chain
from core.memory.short_term import ShortTermMemory
from core.memory.vector_store import LongTermVectorMemory

print('CHECK 1: E2E Graph Execution')
s = create_initial_agent_state('audit_task_001', 'an_giang_rice_001', 'Optimize irrigation', dict(crop_type='rice_jasmine_85', use_cache=True, farm_id='an_giang_rice_001'))
app = build_agricarbon_graph()
final = app.invoke(s, config=dict(configurable=dict(thread_id='t1')))
assert final['final_output']['status'] == 'success'
tools = [t['tool'] for t in final.get('tool_calls', []) if 'args' in t]
print('Tools called:', set(tools))
assert len(set(tools)) >= 4

print('CHECK 2: Reflexion Loop')
bad_s = create_initial_agent_state('audit_task_002', 'an_giang_rice_001', 'Test reflexion', dict(crop_type='rice_jasmine_85', use_cache=True))
bad_s = sensing_agent_node(bad_s)
bad_s = dispatch_agent_node(bad_s)
bad_s['dispatch_plan']['water_needed_mm'] = 80.0
bad_s = carbon_agent_node(bad_s)
bad_s = critic_agent_node(bad_s)
assert bad_s['critic_verdict']['approved'] is False
assert route_supervisor_decision(bad_s) == 'dispatch_agent'
bad_s = dispatch_agent_node(bad_s)
assert bad_s['dispatch_plan']['water_needed_mm'] <= 60.0
assert bad_s['carbon_report'] == {}

print('CHECK 3: Circuit Breaker')
cb = create_initial_agent_state('cb_001', 'an_giang_rice_001', 'Circuit breaker')
cb['weather_data'] = dict(et0=4.0)
cb['sensor_telemetry'] = dict(soil_moisture_pct=20.0)
cb['carbon_report'] = dict(total_co2e_kg=10.0)
for _ in range(3):
    cb['dispatch_plan'] = dict(water_needed_mm=99.0, duration_minutes=600)
    cb = critic_agent_node(cb)
assert cb['critic_verdict']['retry_count'] == 3
assert route_supervisor_decision(cb) == 'FINISH'
cb = supervisor_node(cb)
assert cb['final_output']['status'] == 'safe_abort'
assert cb['final_output']['action'] == 'HALT_PUMP_AND_ALERT_OPERATOR'

print('CHECK 4: Short-Term Memory Concurrency')
mem = ShortTermMemory(':memory:')
errs = []
def worker(idx):
    try:
        for st in range(5):
            mem.save_checkpoint(f't_{idx}', dict(val=st), step=st)
            chk = mem.get_latest_checkpoint(f't_{idx}')
            if chk is None or chk['step'] != st: errs.append(f'{idx} mismatch')
    except Exception as e: errs.append(str(e))
ths = [threading.Thread(target=worker, args=(i,)) for i in range(15)]
for t in ths: t.start()
for t in ths: t.join()
assert len(errs) == 0, str(errs)

print('CHECK 5: Vector Store Episodic Isolation')
vmem = LongTermVectorMemory('data/chroma_db_audit_test')
assert vmem.similarity_search('rice AWD', k=3, collection_name='episodic_memory') == []
for i in range(5):
    vmem.add_episodic_reflection('tsk', 'scene', 'identical length!!', 'OK')
assert len(vmem.search_episodic_memory('identical', k=10)) >= 1

print('CHECK 6: Ledger Integrity')
led = reset_session_ledger()
record_esg_audit_entry('r1', 'f1', 'a1', 10.0)
record_esg_audit_entry('r2', 'f1', 'a2', 20.0)
record_esg_audit_entry('r3', 'f2', 'a3', 15.0)
assert len(led.chain) == 4
ok, err = verify_ledger_chain(led.chain)
assert ok is True and err is None
assert led.chain[1].previous_hash == led.chain[0].entry_hash
assert led.chain[2].previous_hash == led.chain[1].entry_hash
assert led.chain[3].previous_hash == led.chain[2].entry_hash

print('ALL 6 CHECKS PASSED EMPIRICALLY!')
