import os

latex_content = r'''\documentclass[11pt,a4paper]{article}

% =============================================================================
% PREAMBLE: PACKAGES, GEOMETRY & TYPOGRAPHY
% =============================================================================
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=1in]{geometry}
\usepackage{microtype}
\usepackage{fancyhdr}
\usepackage{lastpage}

% Mathematical Formatting Suites
\usepackage{amsmath,amssymb,amsfonts,amsthm,mathtools}
\usepackage{bm}

% Graphics & Visualization
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}

% Algorithms & Pseudocode
\usepackage[ruled,vlined,linesnumbered]{algorithm2e}
\usepackage{xcolor}

% Tables & Typography
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{enumitem}

% Cross-Referencing & Hyperlinks
\usepackage[colorlinks=true,linkcolor=blue!75!black,citecolor=green!50!black,urlcolor=blue!80!black]{hyperref}
\usepackage[capitalize,nameinlink]{cleveref}

% =============================================================================
% THEOREM ENVIRONMENTS & MATHEMATICAL DEFINITIONS
% =============================================================================
\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{framework}{Framework}[section]
\newtheorem{example}{Example}[section]
\newtheorem{prompt}{Diagnostic Prompt}[section]

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{remark}
\newtheorem*{remark}{Remark}
\newtheorem*{pedagogynote}{Pedagogical Note}

% Custom Math Operators & Notation
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}
\DeclareMathOperator{\E}{\mathbb{E}}
\DeclareMathOperator{\Var}{Var}
\DeclareMathOperator{\Cov}{Cov}
\DeclareMathOperator{\Tr}{Tr}
\DeclareMathOperator{\sign}{sign}
\DeclareMathOperator{\softmax}{softmax}
\newcommand{\norm}[1]{\left\lVert#1\right\rVert}
\newcommand{\abs}[1]{\left\lvert#1\right\rvert}
\newcommand{\R}{\mathbb{R}}
\newcommand{\KL}[2]{D_{\mathrm{KL}}\left(#1 \parallel #2\right)}

% =============================================================================
% RUNNING HEADERS & FOOTERS
% =============================================================================
\setlength{\headheight}{14.5pt}
\addtolength{\topmargin}{-2.5pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textsc{IMLC 2026} --- Theoretical Study Guide}
\fancyhead[C]{\textbf{Qualification Round Analytical Monograph}}
\fancyhead[R]{\textit{Senior Division}}
\fancyfoot[L]{\textit{DeepTutor Scaffolding --- Strict R3 Non-Solution Firewall}}
\fancyfoot[R]{Page \thepage\ of \pageref{LastPage}}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.4pt}

% =============================================================================
% DOCUMENT METADATA
% =============================================================================
\title{\vspace{-1.2cm}\Large\textbf{INTERNATIONAL MACHINE LEARNING COMPETITION (IMLC 2026)}\\[0.3cm]
\large\textbf{Qualification Round Theoretical Study Guide \& Analytical Monograph}\\[0.1cm]
\normalsize\textit{Senior Division \& Advanced Olympiad Preparation Track}}

\author{\textbf{IMLC Pedagogical Faculty \& Academic Jury Advisory} \\
\textit{Governing Body: Edu.Harbour GbR (Hamburg, Germany)} \\
\textit{Academic Direction: Dr. Rami Aly (University of Cambridge) \& Fabian Schneider} \\
\textit{Global Portal: \url{https://imlco.org}}}

\date{Academic Season 2026--2027}

\begin{document}
\maketitle
\thispagestyle{fancy}

\begin{abstract}
This monograph serves as the authoritative theoretical companion for scholars, mentors, and educators preparing for the Senior Division of the \textbf{International Machine Learning Competition (IMLC 2026)}. Governed by Edu.Harbour GbR under the Muhammad Yunus Social Enterprise model, IMLC bridges the critical divide between discrete competitive programming and empirical black-box machine learning by demanding rigorous continuous optimization, statistical learning theory, and peer-reviewed scientific paper deconstruction. This document systematically exposes the theoretical foundations of the qualification curriculum across five core domains: (1) production machine learning lifecycles and non-parametric drift detection; (2) orthogonal decision tree partitioning and information theory; (3) polynomial regression, Tikhonov $L_2$ regularization, SVD spectral shrinkage, and bias-variance tradeoff proofs; (4) frontier alignment, Bradley-Terry reward modeling, reverse KL divergence penalties, Gibbs optimal policies, and Riemannian Fisher information geometry; and (5) trustworthy AI, algorithmic fairness, Kleinberg's impossibility theorem, and conformal prediction coverage. In strict compliance with the \textbf{R3 Non-Solution Firewall}, this guide provides zero direct answers to contest problems, focusing entirely on first-principles conceptual scaffolding and mathematical formulation.
\end{abstract}

\tableofcontents
\newpage

% =============================================================================
% SECTION 1: IMLC LANDSCAPE, ARCHITECTURE & STRATEGY
% =============================================================================
\section{IMLC Competition Architecture, Ecosystem \& Comparative Framework}

\subsection{Institutional Genesis \& The Yunus Social Enterprise Model}
The International Machine Learning Competition (IMLC 2026) is governed by \textbf{Edu.Harbour GbR} (Postfach 762135, 22069 Hamburg, Federal Republic of Germany). Academic governance is spearheaded by:
\begin{itemize}[noitemsep]
    \item \textbf{Dr. Rami Aly (Academic Director)}: Artificial Intelligence and NLP researcher at the University of Cambridge (Department of Computer Science and Technology), specialized in automated fact checking, scientific claim verification, and robust evaluation benchmarks.
    \item \textbf{Fabian Schneider (Managing Director)}: Expert in international educational administration and digital examination architecture.
\end{itemize}

Edu.Harbour operates strictly under the \textbf{Social Enterprise Model} articulated by Nobel Peace Prize Laureate Professor Muhammad Yunus:
\begin{enumerate}[noitemsep]
    \item \textbf{Non-Loss, Non-Dividend Principle}: All operational activities are financially self-sustaining without distributing commercial dividends.
    \item \textbf{100\% Revenue Reinvestment}: All proceeds---primarily the single 12~EUR fee for the Pre-Final round---are reinvested into cloud infrastructure, AI proctoring, a global \$1,500 USD cash prize pool, physical certificates, and \textbf{100\% need-based fee waivers} for scholars from developing nations.
    \item \textbf{Geopolitical Independence}: Independent of sovereign funding and corporate lock-in, ensuring universal access across 80+ countries and 3,500+ educators.
\end{enumerate}

\subsection{The Three-Stage Sequential Funnel}
IMLC partitions the evaluation of machine learning mastery into three sequential stages:
\begin{enumerate}
    \item \textbf{Stage I: Qualification Round (Open Research \& Derivation)}:
    \begin{itemize}[noitemsep]
        \item 5 comprehensive technical problems (5.0 pts each, 25.0 pts total).
        \item 100\% Free entry worldwide; untimed take-home format.
        \item Submission deadline: \textbf{Sunday, 13 December 2026, 23:59 UTC+0}.
        \item Senior qualification threshold: $\ge 17.0$ points ($\ge 20.0$ for High Distinction).
    \end{itemize}
    \item \textbf{Stage II: Pre-Final Round (The Research Paper Paradigm)}:
    \begin{itemize}[noitemsep]
        \item 48 hours prior to the exam (\textbf{Friday, 22 January 2027}), an authentic peer-reviewed paper from NeurIPS, ICML, or ICLR is released for open study.
        \item 60-minute timed written examination comprising 3 problems: Basic (4 pts), Advanced Proof (6 pts), and Research Critique (8 pts).
        \item Proctored via in-person teacher supervision (Track A) or dual-camera online AI monitoring (Track B).
        \item 10-minute dynamic QR-code mobile scanning and upload protocol.
        \item Senior advancement threshold: $\ge 11.0$ points ($\ge 12.0$ for Distinction).
    \end{itemize}
    \item \textbf{Stage III: Final Round (Global Speed Sprint)}:
    \begin{itemize}[noitemsep]
        \item Date: \textbf{Tuesday, 23 February 2027}.
        \item Strictly 40 minutes for $\sim 30$ questions ($\sim 75$--$80$ seconds per question).
        \item Strictly \textbf{non-backtracking navigation engine} with question-level countdown timers.
        \item Tools allowed: strictly blank scratch paper and pen (no calculators, no software).
        \item No negative marking; top 20\% awarded Gold, Silver, and Bronze medals (1:2:3 ratio).
    \end{itemize}
\end{enumerate}

\subsection{Demographics \& The Qualification Age Freezing Rule}
Candidates are categorized into three divisions:
\begin{itemize}[noitemsep]
    \item \textbf{Senior Division}: University and graduate students, or candidates aged $\ge 19$.
    \item \textbf{Youth Division}: High school students (Grades 11--13) or aged 16 to $<19$.
    \item \textbf{Junior Division}: Middle school students (Grades $\le 10$) or aged $<16$.
\end{itemize}
\textbf{The Age Freezing Rule}: Official division eligibility is permanently frozen based on the candidate's chronological age on the Qualification Round deadline (\textbf{13 December 2026, 23:59 UTC+0}). A candidate turning 19 during the Pre-Final window remains in the Youth Division for the entire season.

\subsection{Multi-Dimensional Comparative Landscape}
\cref{tab:competition_matrix} positions IMLC relative to other global competitions across eight fundamental dimensions.

\begin{table}[htbp]
\centering
\small
\caption{Global Competition Topology Matrix across Eight Structural Dimensions.}
\label{tab:competition_matrix}
\begin{tabularx}{\textwidth}{l p{2.8cm} p{2.8cm} p{2.8cm} p{3.2cm}}
\toprule
\textbf{Dimension} & \textbf{IMLC (Edu.Harbour)} & \textbf{Kaggle} & \textbf{IOI / ICPC} & \textbf{NeurIPS Comps} \\
\midrule
\textbf{Core Focus} & Mathematical proofs, optimization, paper critique & Empirical accuracy, feature tuning, stacking & Discrete algorithms, data structures & Frontier research systems, custom benchmarks \\
\textbf{Problem Domain} & Continuous math, statistical learning & Tabular, CV, NLP datasets & Pure synthetic discrete puzzles & Novel challenge tasks (agents, biology) \\
\textbf{Compute Needed} & \textbf{Zero GPU}; pen, paper, LaTeX, browser & Multi-GPU/TPU clusters & Standard CPU sandbox & Massive distributed compute clusters \\
\textbf{Evaluation} & Multi-tier jury rubric, proof validity & Private test set scalar metric (LogLoss) & Automated black-box unit test execution & Benchmark test sets, peer review, audits \\
\textbf{Paper Mining} & \textbf{Mandatory 48h paper deconstruction} & None; public kernels and forums & None; pure algorithmic statements & High; literature survey required \\
\textbf{Integrity} & 2-Camera proctoring, teacher supervision & Automated code audit & On-site hall supervision & Code reproducibility checks \\
\textbf{Time Profile} & Untimed QR $\to$ 60m PF $\to$ 40m sprint & Multi-month marathon & 5 hours for 3--4 problems & Multi-month challenge ending at workshop \\
\textbf{Key Competency} & Foundational research, math derivation & Applied ML engineering, tuning & Bug-free discrete implementation & Frontier AI systems engineering \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Strategic Preparation Playbook: The 3-Pass Literature Mining Protocol}
In Stage II, candidates receive an unseen peer-reviewed paper with 48 hours to prepare. To extract maximum information efficiently, apply the \textbf{3-Pass Protocol}:
\begin{itemize}
    \item \textbf{Pass 1: Bird's-Eye Survey (5--10 min)}: Read title, abstract, section headings, figures, and conclusion. Construct the \emph{5 Cs Matrix}: Category, Context, Correctness, Contributions, and Clarity.
    \item \textbf{Pass 2: Conceptual \& Mathematical Audit (20--25 min)}: Build an exact mathematical notation dictionary. Trace the loss function to the gradient update, verify lemma conditions, and audit baseline comparability.
    \item \textbf{Pass 3: Critical Dissection \& Falsification (20 min)}: Stress-test extreme boundary conditions ($\lambda \to 0, \infty$), interrogate unstated assumptions, identify failure modes, and design a counter-experiment.
\end{itemize}

% =============================================================================
% SECTION 2: TOPIC 1 - ML LIFECYCLE & DRIFT
% =============================================================================
\section{Theoretical Foundations: ML Production Lifecycle \& Distributional Drift}

\subsection{Epistemological Formulation: What Constitutes Learning?}
In formal computational learning theory, ``learning'' is not equivalent to executing software or generating predictions. Under Tom Mitchell's classical formulation \cite{mitchell1997machine}:
\begin{definition}[Learning Axiom]
A computer program is said to learn from experience $E$ with respect to some class of tasks $T$ and performance measure $P$, if its performance at tasks in $T$, as measured by $P$, improves with experience $E$.
\end{definition}

Let hypothesis $f_\theta \in \mathcal{H}$ be parameterized by $\theta \in \Theta \subseteq \R^d$. In statistical learning theory \cite{vapnik1998statistical}, the true generalization risk is:
\begin{equation}
R(\theta) = \int_{\mathcal{X} \times \mathcal{Y}} \ell(f_\theta(x), y) \, d\mathbb{P}(x, y)
\end{equation}
which is estimated via the Empirical Risk over training sample $S = \{(x_i, y_i)\}_{i=1}^n$:
\begin{equation}
\hat{R}_n(\theta) = \frac{1}{n} \sum_{i=1}^n \ell(f_\theta(x_i), y_i)
\end{equation}

\begin{theorem}[Parameter State Transition Principle]
A machine learning system is actively in a learning state at time step $t$ if and only if an optimization operator $\mathcal{T}$ alters its parameter vector:
\begin{equation}
\theta_{t+1} = \mathcal{T}(\theta_t, \mathcal{D}_{\mathrm{batch}}) \quad \text{such that} \quad \Delta \theta = \theta_{t+1} - \theta_t \neq \mathbf{0}
\end{equation}
During frozen production inference, $\Delta \theta = \mathbf{0}$; hence, inference is deterministic computation, not learning.
\end{theorem}

\subsection{Mathematical Taxonomy of Distribution Shift}
When joint probability distributions drift between training and deployment, $\mathbb{P}_{\mathrm{train}}(X, Y) \neq \mathbb{P}_{\mathrm{deploy}}(X, Y)$. Factorization reveals three distinct shift regimes:
\begin{enumerate}
    \item \textbf{Covariate Shift (Feature Drift)}:
    \begin{equation}
    \mathbb{P}_{\mathrm{train}}(X) \neq \mathbb{P}_{\mathrm{deploy}}(X) \quad \text{while} \quad \mathbb{P}_{\mathrm{train}}(Y \mid X) = \mathbb{P}_{\mathrm{deploy}}(Y \mid X)
    \end{equation}
    The input feature distribution shifts, but the underlying physical labeling law remains invariant.
    \item \textbf{Concept Shift (Concept Drift)}:
    \begin{equation}
    \mathbb{P}_{\mathrm{train}}(Y \mid X) \neq \mathbb{P}_{\mathrm{deploy}}(Y \mid X) \quad \text{while} \quad \mathbb{P}_{\mathrm{train}}(X) = \mathbb{P}_{\mathrm{deploy}}(X)
    \end{equation}
    The underlying semantic relationship or mapping changes over time.
    \item \textbf{Prior Probability Shift (Label Drift)}:
    \begin{equation}
    \mathbb{P}_{\mathrm{train}}(Y) \neq \mathbb{P}_{\mathrm{deploy}}(Y) \quad \text{while} \quad \mathbb{P}_{\mathrm{train}}(X \mid Y) = \mathbb{P}_{\mathrm{deploy}}(X \mid Y)
    \end{equation}
    Marginal class frequencies shift while class-conditional appearances remain invariant.
\end{enumerate}

\subsection{Non-Parametric Statistical Drift Detection}
\begin{definition}[Two-Sample Kolmogorov-Smirnov Test]
For continuous 1D features, given ECDFs $F_1(x)$ and $F_2(x)$ from baseline and target windows, the test statistic is \cite{massey1951kolmogorov}:
\begin{equation}
D_{\mathrm{KS}} = \sup_{x \in \R} \abs{F_1(x) - F_2(x)}
\end{equation}
The null hypothesis of equal distributions is rejected at significance $\alpha$ if $D_{\mathrm{KS}} > c(\alpha)\sqrt{\frac{n_1 + n_2}{n_1 n_2}}$.
\end{definition}

\begin{definition}[Population Stability Index (PSI)]
Discretizing a continuous feature into $B$ quantiles with baseline proportions $P_b$ and target proportions $Q_b$:
\begin{equation}
\mathrm{PSI} = \sum_{b=1}^B (P_b - Q_b) \ln\left( \frac{P_b}{Q_b} \right)
\end{equation}
Thresholds: $\mathrm{PSI} < 0.10$ indicates stability; $0.10 \le \mathrm{PSI} < 0.25$ indicates moderate shift; $\mathrm{PSI} \ge 0.25$ triggers mandatory model retraining.
\end{definition}

\subsection{DeepTutor Socratic Diagnostic Suite: Topic 1}
\begin{prompt}[Tier 1: Observation]
When an onboard autonomous vehicle neural network executes inference on a rainy evening, does its model weights file on disk change? Does this mean the system is actively learning to drive in the rain?
\end{prompt}
\begin{prompt}[Tier 4: Mathematical Pattern]
Under covariate shift $\mathbb{P}_{\mathrm{deploy}}(x, y) = q(x)\mathbb{P}(y \mid x)$, show that the importance-weighted empirical risk $\hat{R}_w(\theta) = \frac{1}{n}\sum_{i=1}^n w(x_i)\ell(f_\theta(x_i), y_i)$ is an unbiased estimator of deployment risk when $w(x) = \frac{q(x)}{\mathbb{P}_{\mathrm{train}}(x)}$.
\end{prompt}

\begin{remark}[Self-Study Keywords]
Empirical Risk Minimization, Mitchell Learning Axioms, Covariate Shift, Concept Drift, Prior Shift, Kolmogorov-Smirnov Test, Population Stability Index, Continual Learning, Catastrophic Forgetting, Importance Weighting.
\end{remark}

% =============================================================================
% SECTION 3: TOPIC 2 - DECISION TREES
% =============================================================================
\section{Theoretical Foundations: Decision Trees \& Information-Theoretic Partitioning}

\subsection{Orthogonal Space Partitioning Geometry}
A decision tree recursively partitions the feature space $\mathcal{X} \subseteq \R^d$ into disjoint axis-aligned hyper-rectangles $\{R_m\}_{m=1}^M$ fitting local models:
\begin{equation}
f(x) = \sum_{m=1}^M c_m \mathbb{I}(x \in R_m)
\end{equation}
Because splits are strictly axis-aligned ($x_j \le \tau$), representing linear oblique boundaries requires deep staircase approximations.

\subsection{Mathematical Formulations of Impurity Metrics}
Let node $S$ contain $|S|$ samples across $K$ classes with empirical probabilities $p_k = \frac{1}{|S|}\sum_{i \in S} \mathbb{I}(y_i = k)$.
\begin{definition}[Shannon Entropy]
The Shannon entropy \cite{quinlan1986induction} is defined as:
\begin{equation}
H(S) = -\sum_{k=1}^K p_k \log_2(p_k), \quad \text{with } 0 \log_2 0 \equiv 0
\end{equation}
Information Gain for split attribute $A$ with children $\{S_v\}$:
\begin{equation}
IG(S, A) = H(S) - \sum_{v \in \mathrm{Val}(A)} \frac{|S_v|}{|S|} H(S_v)
\end{equation}
\end{definition}

\begin{definition}[Gini Impurity]
The Gini impurity \cite{breiman1984classification} is defined as:
\begin{equation}
I_G(S) = 1 - \sum_{k=1}^K p_k^2
\end{equation}
Gini impurity reduction (Gini Gain) for binary split $s = (j, \tau)$:
\begin{equation}
\Delta I_G(S, s) = I_G(S) - \left[ \frac{|S_L|}{|S|} I_G(S_L) + \frac{|S_R|}{|S|} I_G(S_R) \right]
\end{equation}
\end{definition}

\begin{proposition}[Computational Efficiency Comparison]
For binary classification ($K=2$ with $p \in [0, 1]$), both $H(p) = -p \log_2 p - (1-p)\log_2(1-p)$ and $I_G(p) = 2p(1-p)$ are strictly concave with identical maxima at $p = 0.5$. However, computing Gini impurity requires only basic multiplications and subtractions ($1 - p_1^2 - p_2^2$), bypassing transcendental logarithmic operations and yielding substantially higher computational throughput.
\end{proposition}

\subsection{Continuous Feature Splitting Algorithm}
For a continuous attribute $x_j \in \R$:
\begin{enumerate}[noitemsep]
    \item Sort observed distinct values: $u_{(1)} < u_{(2)} < \dots < u_{(m)}$.
    \item Construct candidate split thresholds at adjacent midpoints: $\tau_i = \frac{u_{(i)} + u_{(i+1)}}{2}$.
    \item Evaluate $\Delta I$ only where adjacent sample labels differ (boundary pruning).
    \item Select $(j^*, \tau^*) = \argmax_{j, \tau} \Delta I(S, (j, \tau))$.
\end{enumerate}

\subsection{Minimal Cost-Complexity Pruning (CART)}
Unconstrained trees exhibit near-zero bias but extreme variance. CART post-pruning minimizes:
\begin{equation}
R_\alpha(T) = R(T) + \alpha |T|
\end{equation}
where $R(T)$ is empirical tree error, $|T|$ is the number of terminal leaves, and $\alpha \ge 0$ is the complexity cost. The weakest-link sequence collapses subtrees with minimal effective cost:
\begin{equation}
\alpha_{\mathrm{eff}}(t) = \frac{R(t) - R(T_t)}{|T_t| - 1}
\end{equation}
generating nested candidate subtrees $T_0 \supset T_1 \supset \dots \supset T_{\mathrm{root}}$ optimized via cross-validation.

\begin{remark}[Self-Study Keywords]
Recursive Partitioning, Shannon Entropy, Information Gain, C4.5 Gain Ratio, Gini Impurity, CART Pruning, Weakest Link, Minimal Cost-Complexity $R_\alpha(T)$, Midpoint Thresholding, Ensembles (Random Forests, Gradient Boosting).
\end{remark}

% =============================================================================
% SECTION 4: TOPIC 3 - REGULARIZATION MECHANICS
% =============================================================================
\section[Polynomial Regression and Regularization Mechanics]{Theoretical Foundations: Polynomial Regression \& Regularization Mechanics}

\subsection{Runge's Phenomenon \& The OLS Pathologies}
Fitting a degree-$p$ polynomial $\phi(x) = [1, x, \dots, x^p]^T$ via unconstrained Ordinary Least Squares (OLS) minimizes $\text{RSS}(w) = \frac{1}{2n}\|y - \Phi w\|_2^2$. The normal equations:
\begin{equation}
w_{\mathrm{OLS}} = (\Phi^T \Phi)^{-1} \Phi^T y
\end{equation}
suffer catastrophic breakdown when features are collinear or $p+1 > n$. As $p$ increases, the condition number $\kappa(\Phi^T \Phi)$ explodes, leading to \textbf{Runge's Phenomenon}: wild polynomial oscillations between sample points, creating zero training error but massive test error.

\subsection{Ridge Regularization (L2 Tikhonov Regularization)}
\begin{pedagogynote}[Conceptual Explanation]
Ridge regression combats overfitting by adding an isotropic Euclidean penalty on parameter magnitudes to the prediction loss. Conceptually, while empirical loss pulls weights to interpolate sample points, the $L_2$ penalty acts as an elastic spring pulling all weights toward the origin. Quadratic penalization severely punishes large coefficient magnitudes, damping high-frequency oscillations and restoring function smoothness. The intercept $w_0$ is unpenalized as it simply reflects baseline target offset.
\end{pedagogynote}

The mathematical Ridge loss functional is:
\begin{equation}
J_{\mathrm{Ridge}}(w) = \frac{1}{2n} \|y - \Phi w\|_2^2 + \frac{\lambda}{2} \|w_{1:p}\|_2^2 = \frac{1}{2n} \|y - \Phi w\|_2^2 + \frac{\lambda}{2} w^T I^* w
\end{equation}
where $I^* = \mathrm{diag}(0, 1, 1, \dots, 1)$.

\subsubsection{Matrix Gradient \& Closed-Form Normal Equations}
Differentiating with respect to $w$:
\begin{equation}
\nabla_w J_{\mathrm{Ridge}}(w) = -\frac{1}{n} \Phi^T (y - \Phi w) + \lambda I^* w
\end{equation}
Setting the gradient to zero yields the regularized normal equations:
\begin{equation}
\left( \frac{1}{n}\Phi^T \Phi + \lambda I^* \right) w = \frac{1}{n}\Phi^T y \implies \mathbf{w_{\mathrm{Ridge}} = (\Phi^T \Phi + n\lambda I^*)^{-1} \Phi^T y}
\end{equation}

\begin{proposition}[Guaranteed Invertibility]
Because $\Phi^T \Phi$ is symmetric positive semi-definite (eigenvalues $\mu_i \ge 0$), adding $n\lambda I^*$ shifts every non-intercept eigenvalue to $\mu_i + n\lambda > 0$ for $\lambda > 0$. Hence, $(\Phi^T \Phi + n\lambda I^*)$ is strictly positive definite and always invertible.
\end{proposition}

\subsubsection{Gradient Descent Dynamics \& Weight Decay}
Under gradient descent with learning rate $\eta$:
\begin{equation}
w_j^{(t+1)} = (1 - \eta \lambda) w_j^{(t)} + \eta \left[ \frac{1}{n} \Phi^T (y - \Phi w^{(t)}) \right]_j \quad (\forall j \ge 1)
\end{equation}
The factor $(1 - \eta \lambda) < 1$ directly executes \textbf{weight decay}, geometrically contracting weights at every step.

\subsection{Lasso Regularization (L1 Norm) \& Geometric Duality}
Lasso minimizes $J_{\mathrm{Lasso}}(w) = \frac{1}{2n}\|y - \Phi w\|_2^2 + \lambda \|w_{1:p}\|_1$.
Under orthogonal design ($\Phi^T \Phi = I$), the solution is governed by the \textbf{soft-thresholding operator}:
\begin{equation}
\hat{w}_j^{\mathrm{Lasso}} = \mathcal{S}_\lambda(\hat{w}_j^{\mathrm{OLS}}) = \sign(\hat{w}_j^{\mathrm{OLS}}) \max\left(0, |\hat{w}_j^{\mathrm{OLS}}| - \lambda\right)
\end{equation}
\textbf{Geometric Duality}: Lasso's constraint set is a cross-polytope ($L_1$ diamond) with sharp corners on the coordinate axes. Elliptical loss contours make first contact at these vertices, setting coefficients \textbf{identically to zero} (sparsity). Ridge's constraint set is a smooth Euclidean sphere, where contact occurs tangentially without forcing exact zeros.

\subsection{SVD Spectral Shrinkage Factors}
Let $\Phi = U \Sigma V^T$ be the SVD of the centered design matrix with singular values $\sigma_j$.
Substituting into the Ridge estimator:
\begin{equation}
w_{\mathrm{Ridge}} = \sum_{j=1}^p \left( \frac{\sigma_j^2}{\sigma_j^2 + n\lambda} \right) \frac{u_j^T y}{\sigma_j} v_j
\end{equation}
Ridge introduces spectral filter factors $f_j = \frac{\sigma_j^2}{\sigma_j^2 + n\lambda} \in (0, 1]$. Directions with high variance ($\sigma_j^2 \gg n\lambda$) have $f_j \approx 1$ (unperturbed signal); directions with small variance ($\sigma_j^2 \ll n\lambda$) have $f_j \to 0$ (aggressive noise filtering).

\subsection{Algebraic Proof of the Bias-Variance Decomposition}
Let $y = \Phi w_{\mathrm{true}} + \epsilon$ with $\E[\epsilon] = \mathbf{0}, \Cov(\epsilon) = \sigma^2 I$.
For Ridge estimator $w^* = (\Phi^T \Phi + \lambda I)^{-1}\Phi^T y$:
\begin{enumerate}
    \item \textbf{Squared Bias strictly increases with $\lambda$}:
    \begin{equation}
    \|\mathrm{Bias}(w^*)\|_2^2 = \sum_{j=1}^p \left( \frac{\lambda}{\sigma_j^2 + \lambda} \right)^2 (v_j^T w_{\mathrm{true}})^2 \implies \frac{\partial}{\partial \lambda} \|\mathrm{Bias}\|_2^2 > 0 \quad (\forall \lambda > 0)
    \end{equation}
    \item \textbf{Variance strictly decreases with $\lambda$}:
    \begin{equation}
    \Var(w^*) = \sigma^2 \sum_{j=1}^p \frac{\sigma_j^2}{(\sigma_j^2 + \lambda)^2} \implies \frac{\partial}{\partial \lambda} \Var(w^*) = \sigma^2 \sum_{j=1}^p \frac{-2\sigma_j^2}{(\sigma_j^2 + \lambda)^3} < 0 \quad (\forall \lambda > 0)
    \end{equation}
\end{enumerate}
Evaluating total error $\mathrm{MSE}(\lambda) = \|\mathrm{Bias}\|^2 + \Var$ at $\lambda = 0$:
\begin{equation}
\left. \frac{\partial \mathrm{MSE}}{\partial \lambda} \right|_{\lambda = 0} = 0 - 2\sigma^2 \sum_{j=1}^p \frac{1}{\sigma_j^4} < 0
\end{equation}
Hence, \textbf{there always exists an optimal $\lambda^* > 0$ achieving strictly lower prediction error than unconstrained OLS}.

\begin{remark}[Self-Study Keywords]
Runge's Phenomenon, Tikhonov Regularization ($L_2$), Lasso ($L_1$), Soft-Thresholding $\mathcal{S}_\lambda$, Gram Matrix Invertibility, Weight Decay $(1-\eta\lambda)$, SVD Spectral Shrinkage, Bias-Variance Tradeoff, Gaussian vs. Laplace Priors.
\end{remark}

% =============================================================================
% SECTION 5: TOPIC 4 - RLHF & POLICY DIVERGENCE
% =============================================================================
\section{Theoretical Foundations: Frontier Alignment, RLHF \& Policy Divergence}

\subsection{The Alignment Challenge \& Goodhart's Law}
Pretrained foundation models optimize for next-token prediction probability, not truthfulness or helpfulness. RLHF trains a neural reward model $r_\psi(x, y)$ on human pairwise preferences \cite{ouyang2022training}:
\begin{equation}
P(y_w \succ y_l \mid x) = \sigma(r_\psi(x, y_w) - r_\psi(x, y_l))
\end{equation}
However, under Goodhart's Law (``When a metric becomes a target, it ceases to be a good metric''), unconstrained policy optimization triggers \textbf{reward hacking}: verbosity, sycophancy, and nonsensical adversarial loops that maximize proxy reward while degrading language quality.

\subsection{The KL Penalty Objective}
\begin{pedagogynote}[Conceptual Explanation]
To prevent reward hacking, alignment pipelines augment the reward objective with a relative entropy penalty anchoring active policy $\pi_\theta$ to a frozen reference model $\pi_{\mathrm{ref}}$. Conceptually, this acts as an information-theoretic leash: the policy seeks to satisfy human preference instructions, but is penalized proportionally to how far its token probabilities diverge from natural linguistic priors.
\end{pedagogynote}

The mathematical composite objective is:
\begin{equation}
\max_\theta \mathcal{J}_{\mathrm{RLHF}}(\theta) = \E_{x \sim \mathcal{D}, y \sim \pi_\theta} [r_\psi(x, y)] - \beta \E_{x \sim \mathcal{D}} [\KL{\pi_\theta(\cdot \mid x)}{\pi_{\mathrm{ref}}(\cdot \mid x)}]
\end{equation}
where $\beta > 0$ is the regularization coefficient.
In PPO \cite{schulman2017proximal}, the token-level surrogate reward is:
\begin{equation}
R_{\mathrm{surrogate}}(x, y) = r_\psi(x, y) - \beta \left( \log \pi_\theta(y \mid x) - \log \pi_{\mathrm{ref}}(y \mid x) \right)
\end{equation}

\subsection{First-Principles Proof: The Optimal Gibbs Policy}
\begin{theorem}[Optimal Aligned Gibbs Policy]
Fix prompt $x$. Optimizing non-parametric distribution $\pi(y)$ on the probability simplex with Lagrange multiplier $\mu$ enforcing $\sum_y \pi(y) = 1$:
\begin{equation}
\mathcal{L}(\pi, \mu) = \sum_{y} \pi(y) r(x, y) - \beta \sum_{y} \pi(y) \log\left(\frac{\pi(y)}{\pi_{\mathrm{ref}}(y)}\right) + \mu \left( 1 - \sum_y \pi(y) \right)
\end{equation}
Setting $\frac{\partial \mathcal{L}}{\partial \pi(y)} = r(x, y) - \beta\left(\log\frac{\pi(y)}{\pi_{\mathrm{ref}}(y)} + 1\right) - \mu = 0$ yields:
\begin{equation}
\pi^*(y \mid x) = \frac{1}{Z(x)} \pi_{\mathrm{ref}}(y \mid x) \exp\left( \frac{r(x, y)}{\beta} \right)
\end{equation}
where $Z(x) = \sum_{y'} \pi_{\mathrm{ref}}(y' \mid x) \exp\left( \frac{r(x, y')}{\beta} \right)$ is the partition function.
\end{theorem}

\begin{corollary}[Direct Preference Optimization Reparameterization]
Rearranging $\pi^*(y \mid x)$ gives $r(x, y) = \beta \log \frac{\pi^*(y \mid x)}{\pi_{\mathrm{ref}}(y \mid x)} + \beta \log Z(x)$. Substituting into the Bradley-Terry loss cancels out $Z(x)$, allowing direct policy training without an explicit reward model \cite{rafailov2023direct}.
\end{corollary}

\subsection{Information Geometry: Taylor Expansion \& The Fisher Metric}
Expanding $\KL{\pi_\theta}{\pi_{\theta_{\mathrm{ref}}}}$ around $\theta = \theta_{\mathrm{ref}}$:
\begin{itemize}[noitemsep]
    \item Value at anchor: $\KL{\pi_{\theta_{\mathrm{ref}}}}{\pi_{\theta_{\mathrm{ref}}}} = 0$.
    \item Gradient: $\nabla_\theta \KL{\pi_\theta}{\pi_{\theta_{\mathrm{ref}}}} \big|_{\theta = \theta_{\mathrm{ref}}} = \mathbf{0}$.
    \item Hessian: $\nabla_\theta^2 \KL{\pi_\theta}{\pi_{\theta_{\mathrm{ref}}}} \big|_{\theta = \theta_{\mathrm{ref}}} = \mathcal{F}(\theta_{\mathrm{ref}})$, the \textbf{Fisher Information Matrix}.
\end{itemize}
Thus, the local Riemannian Taylor expansion is:
\begin{equation}
\KL{\pi_\theta}{\pi_{\theta_{\mathrm{ref}}}} = \frac{1}{2}(\theta - \theta_{\mathrm{ref}})^T \mathcal{F}(\theta_{\mathrm{ref}})(\theta - \theta_{\mathrm{ref}}) + \mathcal{O}(\|\theta - \theta_{\mathrm{ref}}\|^3) \propto \frac{1}{2} t^2
\end{equation}
This proves that quadratic drift penalties $\beta t^2$ are canonical local approximations of relative entropy.

\subsection{Regularized Policy Optimization \& Bounded Divergence Dynamics}
In frontier alignment, policy optimization balances expected preference reward $\mathcal{R}(\pi)$ against an anchor divergence penalty $\mathcal{D}(\pi \,\|\, \pi_{\mathrm{ref}})$:
\begin{equation}
\min_{\pi} \mathcal{L}_{\mathrm{drift}}(\pi; \beta) = -\mathbb{E}_{x \sim \mathcal{D}, y \sim \pi}[r(x, y)] + \beta \, \mathcal{D}(\pi \,\|\, \pi_{\mathrm{ref}})
\end{equation}
where $\beta > 0$ acts as a Lagrange multiplier governing the exchange rate on the Pareto frontier:
\begin{itemize}[noitemsep]
    \item \textbf{Under-Regularized Regime ($\beta \to 0^+$)}: $\pi^* \to \arg\max_y r(x, y)$. Without divergence anchoring, the policy degenerates into reward hacking and exploitation of proxy model artifacts (Goodhart's Law).
    \item \textbf{Over-Regularized Regime ($\beta \to \infty$)}: $\pi^* \to \pi_{\mathrm{ref}}$. Divergence penalty dominates, freezing the policy at the reference anchor with zero adaptation.
    \item \textbf{Safe Operational Governance}: To prevent catastrophic distribution drift, deployment standards enforce bounded divergence $\mathcal{D}(\pi \,\|\, \pi_{\mathrm{ref}}) \le T_{\mathrm{drift}}$ across worst-case disturbance envelopes.
\end{itemize}

\begin{remark}[Self-Study Keywords]
Bradley-Terry Model, Goodhart's Law, Reward Hacking, PPO Surrogate Objective, Reverse KL Divergence, Gibbs Policy, Direct Preference Optimization (DPO), Fisher Information Metric, Policy Divergence Bounds, Alignment Tax.
\end{remark}

% =============================================================================
% SECTION 6: TOPIC 5 - AI ETHICS & DEPLOYMENT
% =============================================================================
\section{Theoretical Foundations: Trustworthy AI, Algorithmic Fairness \& Responsible Deployment}

\subsection{Mathematical Formulations of Algorithmic Fairness}
Let $A \in \{0, 1\}$ be a protected demographic attribute, $Y \in \{0, 1\}$ ground-truth label, and $\hat{Y} \in \{0, 1\}$ prediction:
\begin{enumerate}
    \item \textbf{Demographic Parity}: $\mathbb{P}(\hat{Y}=1 \mid A=0) = \mathbb{P}(\hat{Y}=1 \mid A=1) \iff \hat{Y} \perp A$.
    \item \textbf{Equalized Odds}: $\hat{Y} \perp A \mid Y$, requiring equal TPR ($\text{TPR}_0 = \text{TPR}_1$) and equal FPR ($\text{FPR}_0 = \text{FPR}_1$).
    \item \textbf{Predictive Parity}: $Y \perp A \mid \hat{Y}$, requiring equal PPV ($\text{PPV}_0 = \text{PPV}_1$).
\end{enumerate}

\subsection{Proof of Kleinberg's Impossibility Theorem}
\begin{theorem}[Kleinberg's Impossibility Theorem]
If base rates differ ($p_0 = \mathbb{P}(Y=1 \mid A=0) \neq p_1 = \mathbb{P}(Y=1 \mid A=1)$), no non-trivial classifier can simultaneously satisfy Equalized Odds and Predictive Parity \cite{kleinberg2016inherent}.
\end{theorem}
\begin{proof}
By Bayes' Theorem:
\begin{equation}
\mathrm{PPV}_a = \frac{\mathrm{TPR}_a \cdot p_a}{\mathrm{TPR}_a \cdot p_a + \mathrm{FPR}_a \cdot (1 - p_a)} = \frac{1}{1 + \left( \frac{\mathrm{FPR}_a}{\mathrm{TPR}_a} \right) \left( \frac{1 - p_a}{p_a} \right)}
\end{equation}
Under Equalized Odds, $\mathrm{TPR}_0 = \mathrm{TPR}_1$ and $\mathrm{FPR}_0 = \mathrm{FPR}_1$, so ratio $c = \frac{\mathrm{FPR}}{\mathrm{TPR}}$ is constant.
Then $\mathrm{PPV}_a = \left[ 1 + c \left( \frac{1 - p_a}{p_a} \right) \right]^{-1}$. Because base rates differ ($p_0 \neq p_1$), odds ratios $\frac{1 - p_a}{p_a}$ differ. Unless $c = 0$ (which requires $\mathrm{FPR} = 0$, implying perfect deterministic separation), $\mathrm{PPV}_0 \neq \mathrm{PPV}_1$, violating Predictive Parity.
\end{proof}

\subsection{Conformal Prediction \& Certified Coverage}
Conformal prediction generates set-valued predictions $C(x) \subseteq \mathcal{Y}$ satisfying distribution-free coverage:
\begin{equation}
\mathbb{P}(Y \in C(X)) \ge 1 - \alpha
\end{equation}
When instances are ambiguous or OOD, $|C(x)| \ge 2$ or predictive entropy $H(Y \mid X) > \tau_{\mathrm{safe}}$, triggering automated abstention and Human-in-the-Loop (HITL) triage.

\subsection{Regulatory Frameworks}
\begin{itemize}[noitemsep]
    \item \textbf{EU AI Act}: Partitions AI into Unacceptable (prohibited), High-Risk (strictly audited for data governance, human oversight, logging), Limited, and Minimal Risk tiers.
    \item \textbf{NIST AI RMF 1.0}: Structured around Govern, Map, Measure, and Manage functions.
\end{itemize}

\begin{remark}[Self-Study Keywords]
Demographic Parity, Equalized Odds, Predictive Parity, Kleinberg's Impossibility Theorem, Disparate Impact, Conformal Prediction Coverage ($1-\alpha$), Grounded RAG, Hallucination Mitigation, EU AI Act High-Risk Compliance, Human-in-the-Loop Triage.
\end{remark}

% =============================================================================
% SECTION 7: CROSS-PILLAR VARIATIONAL SYNTHESIS
% =============================================================================
\section{Cross-Pillar Variational Synthesis \& Grand Unified Framework}

\subsection{The Unified Variational Principle}
Both Ridge regression and RLHF alignment solve instances of a universal information projection:
\begin{equation}
\min_{\psi \in \Psi} \left[ \mathcal{L}_{\mathrm{task}}(\psi) + \kappa \cdot \mathcal{D}(\psi, \psi_{\mathrm{anchor}}) \right]
\end{equation}

\subsection[Proof: L2 Ridge as Gaussian Relative Entropy]{Proof: $L_2$ Ridge as Gaussian Relative Entropy}
Assume an adapted parameter distribution $P = \mathcal{N}(w, \sigma^2 I_p)$ and a zero-mean reference prior $Q = \mathcal{N}(\mathbf{0}, \sigma^2 I_p)$.
The KL divergence between multivariate Gaussians with identical covariance is:
\begin{equation}
\KL{P}{Q} = \frac{1}{2} (\mathbf{0} - w)^T (\sigma^2 I)^{-1} (\mathbf{0} - w) = \frac{1}{2\sigma^2} \|w\|_2^2
\end{equation}
Rearranging yields the fundamental identity:
\begin{equation}
\mathbf{\|w\|_2^2 = 2\sigma^2 \cdot \KL{\mathcal{N}(w, \sigma^2 I)}{\mathcal{N}(\mathbf{0}, \sigma^2 I)}}
\end{equation}
\textbf{Unification Theorem}: The $L_2$ Ridge penalty is algebraically identical to the Relative Entropy from an uninformative Gaussian prior. Both classical regularization and modern RLHF enforce \textbf{Minimum Relative Entropy (Information Projection)}.

\subsection{Master 6-Dimension Comparative Matrix}
\begin{table}[htbp]
\centering
\scriptsize
\caption{Cross-Pillar Theoretical Matrix across all Five Qualification Syllabus Topics.}
\label{tab:master_matrix}
\begin{tabularx}{\textwidth}{l p{2.2cm} p{2.2cm} p{2.2cm} p{2.2cm} p{2.2cm}}
\toprule
\textbf{Dimension} & \textbf{Topic 1: Lifecycle} & \textbf{Topic 2: Trees} & \textbf{Topic 3: Regularization} & \textbf{Topic 4: RLHF Drift} & \textbf{Topic 5: Ethics} \\
\midrule
\textbf{Domain} & Statistical Learning & Information Theory & Convex Matrix Calculus & Functional Calculus & Probability \& Fairness \\
\textbf{Objective} & Non-stationary ERM & Maximize Information Gain & Minimize RSS + Penalty & Maximize Reward - KL & Balance Errors \& Risk \\
\textbf{Inductive Bias} & Distribution stationarity & Axis-aligned partitions & Parameter Euclidean norm & Proximity to base $\pi_{\mathrm{ref}}$ & Calibrated error parity \\
\textbf{Failure Mode} & Silent drift decay & Memorization of noise & Runge boundary oscillation & Reward hacking gibberish & Bias \& hallucinations \\
\textbf{Mitigation} & KS-test, PSI, retraining & Cost-complexity pruning & Ridge / Lasso penalty & KL divergence penalty & Conformal sets, RAG \\
\textbf{Evaluation} & OOD generalization & Test Gini drop, OOB & Cross-validated MSE & Win-rate, Perplexity & Equalized odds ratio \\
\bottomrule
\end{tabularx}
\end{table}

\section*{Conclusion}
The IMLC Senior Division demands deep foundational synthesis: understanding that machine learning algorithms are unified mathematical systems anchored in continuous optimization, information geometry, and ethical responsibility. As emphasized throughout: \textbf{``Understand AI. Don't just use it.''}

% =============================================================================
% BIBLIOGRAPHY
% =============================================================================
\bibliographystyle{plain}
\bibliography{references}

\end{document}
'''

with open('latex/imlc_study_guide.tex', 'w', encoding='utf-8') as f:
    f.write(latex_content)

print(f"Updated LaTeX study guide written successfully! Total bytes: {len(latex_content.encode('utf-8'))}")
