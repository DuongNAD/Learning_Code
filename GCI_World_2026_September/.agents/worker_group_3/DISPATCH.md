# Task Assignment: Worker Group 3

## Assigned Files (Exclusive Write Ownership)
- `d:\02_Learning_Knowledge\GCI_World_2026_September\study_notes\04_Supervised_Regression.md`
- `d:\02_Learning_Knowledge\GCI_World_2026_September\study_notes\05_Supervised_Classification.md`
- `d:\02_Learning_Knowledge\GCI_World_2026_September\study_notes\06_ML_Landscape_and_Strategy.md`

## Mandatory Reading Before Starting Work
- `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\ORIGINAL_REQUEST.md`
- `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\orchestrator_1\PROJECT.md`
- `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\explorer_survey_1\survey_report.md`
- `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\explorer_survey_2\notebooks_report.md`
- `d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\explorer_survey_3\theory_spec.md`

## Required Content & Structure
Each study note must be comprehensive, rigorous, and strictly fulfill:
1. **R1: Core Theory**:
   - For `04_Supervised_Regression.md`: Simple & Multiple Linear Regression, OLS Normal Equations, Loss functions (MSE, RMSE, MAE), Coefficient of determination $R^2$ (including why $R^2 < 0$ can occur), Holdout split vs K-Fold Cross-Validation, Outlier handling progression (univariate IQR vs bivariate scatter filtering), Feature scaling with `StandardScaler` and Data Leakage prevention.
   - For `05_Supervised_Classification.md`: Decision Tree architecture, Recursive binary splitting, Gini Impurity vs Shannon Entropy vs Information Gain equations, Pruning & `max_depth` hyperparameter tuning, One-Hot Encoding and dummy variable trap (`drop_first=True`), Imputation strategies (mode vs conditional group mode with `groupby`), Relational data merging (`pd.merge`), Confusion Matrix metrics (TP, FP, TN, FN, Accuracy paradox, Precision, Recall, F1 score).
   - For `06_ML_Landscape_and_Strategy.md`: ML taxonomy (Supervised, Unsupervised, Reinforcement, Self-Supervised), K-Means clustering (inertia, elbow method), PCA (covariance matrix, eigenvalues, explained variance ratio), Time Series & Autocorrelation, LLM Next Token Prediction, Enterprise AI strategy (Dark Data, Data Flywheel, Moats via Workflow Integration, Seven-Eleven Japan item-by-item loop).
2. **R2: Python Code Extraction**:
   - Extract authentic code patterns with clear inline explanatory comments (`#`).
3. **R3: Active Recall Flashcards**:
   - Conclude each note with at least 5 conceptual Q&A flashcards.
4. **R4: Visual Mindmaps / Flowcharts**:
   - Include at least 1 valid Mermaid.js diagram per note (e.g., Regression ML pipeline, Decision Tree / Confusion matrix trade-offs, Machine Learning Taxonomy).
5. **Edge Cases**:
   - Document domain traps (e.g. data leakage when fitting scaler on test set, accuracy paradox in imbalanced classes, dummy variable multicollinearity).

DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Report results in `handoff.md` and send a message back when complete.

## 2026-09-20T15:09:11Z
You are Worker Group 3 for the GCI World 202609 course study notes project.
Your working directory: d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\worker_group_3
Workspace root: d:\02_Learning_Knowledge\GCI_World_2026_September
Task assignment: d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\worker_group_3\DISPATCH.md
Authoritative request: d:\02_Learning_Knowledge\GCI_World_2026_September\.agents\ORIGINAL_REQUEST.md

MANDATORY FIRST STEP: Read ORIGINAL_REQUEST.md and your DISPATCH.md.
You have exclusive write ownership over:
- d:\02_Learning_Knowledge\GCI_World_2026_September\study_notes\04_Supervised_Regression.md
- d:\02_Learning_Knowledge\GCI_World_2026_September\study_notes\05_Supervised_Classification.md
- d:\02_Learning_Knowledge\GCI_World_2026_September\study_notes\06_ML_Landscape_and_Strategy.md

Implement all three files thoroughly according to requirements R1 (Theory), R2 (Python Code with comments), R3 (Flashcards >= 5 per file), and R4 (Mermaid diagrams >= 1 per file). Refer to the survey reports in .agents/explorer_survey_1, explorer_survey_2, and explorer_survey_3 for complete source materials.
MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Write your handoff.md in your working directory and report completion via send_message to parent.

