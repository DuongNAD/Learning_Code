import os

modules = [
    'docs/modules/module1_imlc_landscape.md',
    'docs/modules/module2_ml_lifecycle.md',
    'docs/modules/module3_decision_trees.md',
    'docs/modules/module4_regularization.md',
    'docs/modules/module5_rlhf_divergence.md',
    'docs/modules/module6_ethics_deployment.md',
    'docs/modules/module7_cross_pillar_synthesis.md'
]

header = """# International Machine Learning Competition (IMLC 2026)
## Comprehensive Theoretical Study Guide & Analytical Preparation Dossier
### Senior Division & Advanced Olympiad Track

**Author**: IMLC Lead Educational Author & LaTeX Architect  
**Governing Institution**: Edu.Harbour GbR, Hamburg, Federal Republic of Germany  
**Academic Director**: Dr. Rami Aly (University of Cambridge) & Fabian Schneider  
**Integrity Mode**: DeepTutor Socratic Scaffolding & Strict R3 Non-Solution Firewall  
**Publication Date**: 2026-2027 Academic Season  
**Official Portal**: [https://imlco.org](https://imlco.org)

---

## Executive Foreword & Educational Philosophy

The International Machine Learning Competition (IMLC 2026) represents a global standard of excellence in assessing the mathematical, algorithmic, and sociotechnical foundations of Artificial Intelligence. Established by Edu.Harbour GbR in Hamburg, Germany, under the social enterprise model of Nobel Peace Prize Laureate Professor Muhammad Yunus, IMLC is dedicated to a transformative academic ethos:

$$\\mathbf{"Understand\\ AI.\\ Don't\\ just\\ use\\ it."}$$

In modern computing, machine learning is frequently reduced to calling pre-packaged software libraries or writing prompts. Yet when models are deployed into high-stakes real-world domains, empirical tinkering without foundational understanding leads to catastrophic failure modes: silent distribution drift, multicollinear weight explosions, adversarial reward hacking, and discriminatory algorithmic bias.

This monograph serves as the authoritative theoretical companion for candidates, educators, and scholars preparing for the IMLC Qualification, Pre-Final, and Final rounds. It combines geometric intuition, rigorous mathematical derivations (loss functions, matrix gradients, closed-form equations, and variational proofs), DeepTutor 5-Tier Socratic scaffolding, and curated keyword taxonomies.

### Strict R3 Non-Solution Firewall
In strict compliance with **Requirement R3** of the curriculum directive, this study guide **does not contain answers, numerical calculations, or specific solutions to the 2026 Qualification Round problem sheet (Problems A through E)**. It establishes pure first-principles knowledge, empowering candidates to deduce, formulate, and verify solutions autonomously.

---

## Table of Contents
1. [Module 1: IMLC Landscape, Architecture & Strategy](#module-1-the-international-machine-learning-competition-imlc-landscape-architecture--strategy)
2. [Module 2: Machine Learning Production Lifecycle & Distributional Drift](#module-2-topic-1--machine-learning-production-lifecycle--distributional-drift)
3. [Module 3: Decision Trees & Information-Theoretic Partitioning](#module-3-topic-2--decision-trees--information-theoretic-partitioning)
4. [Module 4: Polynomial Regression & Regularization Mechanics ($L_1$ vs. $L_2$)](#module-4-topic-3--polynomial-regression--regularization-mechanics-l_1-vs-l_2)
5. [Module 5: Frontier Alignment, RLHF & Policy Divergence Dynamics](#module-5-topic-4--frontier-alignment-rlhf--policy-divergence-dynamics)
6. [Module 6: Trustworthy AI, Algorithmic Fairness & Responsible Deployment](#module-6-topic-5--trustworthy-ai-algorithmic-fairness--responsible-deployment)
7. [Module 7: Cross-Pillar Variational Synthesis & Comparative Framework](#module-7-cross-pillar-variational-synthesis--comparative-framework)

---

"""

full_text = [header]

for mod_path in modules:
    with open(mod_path, 'r', encoding='utf-8') as f:
        mod_content = f.read()
    full_text.append(mod_content)
    full_text.append('\n\n---\n\n')

output_path = 'docs/IMLC_2026_Study_Guide.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(''.join(full_text))

print(f"Unified study guide written to {output_path} successfully! Total bytes: {len(''.join(full_text).encode('utf-8'))}")
