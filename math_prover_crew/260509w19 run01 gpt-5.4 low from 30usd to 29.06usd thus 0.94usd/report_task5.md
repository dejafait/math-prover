# Final Report on the Riemann Hypothesis

## Executive Summary

The Riemann Hypothesis (RH) remains unproved and unrefuted as of 2026. It asserts that every nontrivial zero of the Riemann zeta function \(\zeta(s)\) has real part \(1/2\), equivalently that all zeros in the critical strip \(0<\Re s<1\) lie on the critical line \(\Re s=1/2\).

RH remains central to mathematics because it would yield near-optimal error terms for prime distribution and sharpen many results across analytic number theory, arithmetic statistics, and the theory of \(L\)-functions. Although no accepted proof has emerged, the evidence for RH is overwhelming from three directions:

- rigorous computation verifying vast numbers of zeros on the critical line,
- statistical behavior of zeros matching random matrix heuristics,
- structural analogies with proven RH-type results in function fields and spectral settings.

At the same time, the main obstacle is conceptual rather than computational. Existing tools can verify finitely many zeros, prove density theorems, obtain zero-free regions, and control average behavior, but they do not supply a mechanism forcing every zero at every height onto a single vertical line.

The current research landscape is therefore divided among several mature themes:
- classical analytic approaches,
- equivalent reformulations such as Li, Nyman–Beurling, Robin, and Lagarias criteria,
- spectral and Hilbert–Pólya programs,
- de Bruijn–Newman analysis,
- random matrix and moment heuristics,
- high-rigor numerical verification.

A large set of novel proposals has been considered, ranging from transfer operators, scattering models, and Arakelov positivity to wavelet formulations of Nyman–Beurling and machine-assisted conjecture discovery. The critical review of these ideas shows a sharp divide:

- A small subset appears conceptually credible because it aims at the sort of mechanism RH likely requires: positivity, self-adjointness/unitarity, or a sharp equivalent criterion.
- Many others are currently heuristic or metaphorical, lacking a precise object or theorem-level route.
- None presently constitutes a proof strategy close to resolution.

The most credible active directions in 2026 are:
1. positivity or cohomological frameworks over \(\mathbb Q\),
2. canonical spectral or scattering realizations of \(\xi(s)\),
3. de Bruijn–Newman and zero-dynamics methods,
4. rigorous reformulations such as Nyman–Beurling approached with modern harmonic analysis,
5. continued certified numerical and formal work.

The overall conclusion is clear: RH remains one of mathematics’ central open problems. The evidence for its truth is extremely strong, but no known method yet explains why all zeros must lie on the critical line.

---

## Current State of Research

### 1. Statement and significance

RH concerns the nontrivial zeros of the Riemann zeta function. It predicts that each such zero has the form
\[
\rho=\tfrac12+it.
\]
Its importance comes from the explicit formulas connecting zeros of \(\zeta(s)\) to prime-counting functions such as \(\pi(x)\), \(\psi(x)\), and related arithmetic sums. Under RH, one obtains essentially best-possible square-root-scale error terms in many prime distribution problems.

### 2. Classical equivalent formulations

Several classical statements are equivalent to RH, including:
- \(M(x)=O(x^{1/2+\varepsilon})\) for the Möbius summatory function,
- \(\psi(x)=x+O(x^{1/2}\log^2 x)\),
- positivity of all Li coefficients,
- the Nyman–Beurling closure condition in a suitable \(L^2\) space,
- Robin’s inequality for divisor sums,
- Lagarias’s elementary inequality involving \(\sigma(n)\) and harmonic numbers.

These equivalences are valuable because they translate RH into problems in harmonic analysis, entire-function theory, elementary inequalities, or divisor-sum optimization. However, none has yet yielded a proof.

### 3. Established unconditional results

Several foundational results remain central:

- Hardy proved infinitely many zeros lie on the critical line.
- Levinson showed more than one-third of the zeros lie on the line.
- Conrey improved this to more than two-fifths.
- Zero-density theorems show that zeros off the line cannot be too numerous.
- The Vinogradov–Korobov zero-free region remains the strongest classical unconditional region near \(\Re s=1\).
- The prime number theorem follows from the absence of zeros on \(\Re s=1\), illustrating how zero-free regions drive prime distribution.

These are important but still far weaker than RH, which requires all zeros to lie on the line.

### 4. Numerical verification

Extensive certified computations continue to verify that enormous numbers of initial nontrivial zeros lie on the critical line and are simple. The main tools are:
- the Riemann–Siegel formula,
- Turing’s method,
- Odlyzko–Schönhage-type algorithms,
- interval arithmetic,
- rigorous certification and increasingly formal verification.

These calculations provide extremely strong evidence for RH and for the simple zeros conjecture, but they remain finite verifications and therefore do not imply RH.

### 5. Zero statistics and random matrix evidence

A major source of heuristic support comes from zero statistics:
- Montgomery’s pair correlation conjecture,
- Odlyzko’s numerical data,
- GUE-like spacing behavior,
- Katz–Sarnak symmetry philosophy for families of \(L\)-functions,
- moment conjectures of Keating–Snaith,
- ratios conjectures of Conrey–Farmer–Keating–Rubinstein–Snaith.

This evidence strongly supports the expectation that zeros behave like eigenvalues of a self-adjoint quantum system. But statistical agreement does not prove exact zero localization.

### 6. Function field analogues and geometric lessons

The analogue of RH for curves over finite fields was proved by Weil, and Deligne’s proof of the Weil conjectures established a much broader geometric RH-type theory. These results show that positivity, cohomology, and spectral purity can force zeros onto critical lines in geometric settings.

However, there is no accepted analogue of this machinery over \(\mathbb Q\). The absence of a cohomological or spectral positivity principle in the number-field setting remains a major obstacle.

### 7. Hilbert–Pólya and spectral approaches

The Hilbert–Pólya philosophy remains one of the leading conceptual programs: if the zeros corresponded to eigenvalues of a self-adjoint operator, RH would follow. Related ideas include:
- Berry–Keating’s \(xp\) Hamiltonian,
- Connes’s noncommutative geometry,
- transfer operators and trace-formula analogies,
- scattering and resonance interpretations.

These directions are influential and structurally appealing, but no canonical self-adjoint operator with the correct arithmetic, local factors, and explicit-formula behavior is known.

### 8. de Bruijn–Newman theory

The de Bruijn–Newman constant \(\Lambda\) has become one of the deepest structural invariants related to RH. RH is equivalent to \(\Lambda\le 0\), while Rodgers–Tao proved \(\Lambda\ge 0\). Thus, if RH is true, it is “barely true.”

This result sharpened understanding of RH’s delicacy. Numerical work continues to push upper bounds for \(\Lambda\) closer to 0, while Lehmer pairs and near-colliding zeros underscore the instability of the problem. No accepted proof of \(\Lambda\le 0\) exists.

### 9. Modern analytic number theory context

From 2020–2026, research continued on:
- low-lying zeros in families,
- symmetry types and one-level densities,
- subconvexity for automorphic \(L\)-functions,
- moments and extreme values of \(\zeta(1/2+it)\),
- resonance methods,
- pretentious multiplicative number theory,
- Möbius randomness and disjointness,
- improved rigorous computation and formal methods.

These developments enrich the RH ecosystem and support its expected truth, but none has produced a decisive mechanism enforcing the critical line.

### 10. Consensus in 2026

The consensus remains:
- RH is unproved and unrefuted.
- No claimed proof from 2020–2026 has become accepted as settled mathematics.
- The evidence for RH is extremely strong.
- The obstacle is not lack of data but lack of a forcing principle.

---

## Novel Ideas Proposed

A set of 48 speculative or exploratory ideas was reviewed. These ideas can be grouped into several themes.

### A. Spectral, dynamical, and trace-formula ideas

These proposals seek a Hilbert–Pólya-type mechanism through operators, flows, or scattering:

1. Fractal transfer-operator conjecture for \(\xi(s)\)
2. Prime geodesic flow on an adelic fractal
3. Noncommutative trace formula with time-reversal symmetry
4. Local-to-global gluing of \(p\)-adic local operators
5. Arithmetic quantum graph model for \(\zeta\)
6. Canonical scattering matrix whose resonances are zeta zeros
7. Berry–Keating with adelic boundary conditions
8. Hidden transfer-operator spectral gap
9. Arithmetic Schrödinger or “zeta crystal” model
10. Selberg-trace-formula analogue on arithmetic moduli spaces

These ideas are strongest when they aim at:
- a canonical self-adjoint operator,
- a unitary scattering problem,
- or a genuine trace formula reproducing the explicit formula.

### B. Positivity, cohomology, and geometric purity ideas

These seek a replacement for the positivity mechanism available in the function-field case:

1. Arakelov-cohomological positivity over \(\mathrm{Spec}\,\mathbb Z\)
2. Motive-at-infinity conjecture
3. Prime-based reproducing-kernel Hilbert spaces
4. Li coefficients as moments of a positive measure
5. Complete monotonicity of a transformed Li generating function
6. Rigidity from the full family of Weil-type explicit formulas
7. Multiplicative uncertainty principle
8. Mellin–Paley–Wiener theory with arithmetic support

These are conceptually significant because they aim at exactly the sort of positivity or self-duality that could force zeros to the line.

### C. de Bruijn–Newman and zero-dynamics ideas

These target the heat-deformed \(\Xi\)-function and the constant \(\Lambda\):

1. de Bruijn–Newman as a phase transition in an integrable PDE
2. Lehmer pairs as localized structures in zero dynamics
3. Hyperbolicity-preserving operators approximating backward heat flow
4. Critical-line bootstrap from natural deformations of \(\xi\)

These are attractive because they attack a sharp equivalent problem rather than RH in its original form.

### D. Reformulations via established RH-equivalent criteria

These try to make exact criteria more tractable:

1. Nyman–Beurling via compressed sensing on multiplicative scales
2. Wavelet bases adapted to fractional-part functions
3. Robin inequality via divisor-tree optimization
4. Superabundant numbers as shadows of zero repulsion
5. Local obstruction search via formal methods

These proposals are strongest when they sharpen a known equivalent condition rather than merely restate it.

### E. Statistical, probabilistic, and physics-inspired ideas

These include:
1. Coulomb gas with arithmetic external field
2. Large-deviation exclusion of off-line zeros
3. Exact GUE plus arithmetic correction implying RH
4. Converse theorem from moments to zero location
5. Free probability model for Euler factors
6. Entropy maximization for Möbius randomness
7. Topological recursion, Painlevé, and isomonodromic frameworks
8. Adelic conformal field theory
9. Optimal transport from primes to zeros

These are often rich heuristic frameworks but generally face difficulty turning statistical or physical analogies into pointwise zero localization.

### F. Geometric-metaphorical or highly speculative frameworks

These include:
1. Minkowski dimension equals critical line
2. Tropical geometry avatar of the explicit formula
3. Renormalization fixed-point principle
4. Category-theoretic functorial RH
5. \(p\)-adic/archimedean interference model

These proposals may offer intuition, but in current form they are not close to theorem-level strategies.

### G. Computational and discovery-oriented proposals

1. Machine-discovered invariants of zeros
2. Formal-proof-guided search for finite obstruction sets

These are not direct proof strategies but may help generate conjectures or certify reductions.

---

## Numerical Testing & Potential Failures

### 1. What computation has actually established

Numerical work has rigorously verified that very large finite sets of zeros lie on the critical line and are simple. It also strongly supports:
- GUE spacing statistics,
- the pair correlation picture,
- the simple zeros conjecture,
- tight upper bounds on the de Bruijn–Newman constant,
- agreement with moment and ratios heuristics.

This computational evidence is among the strongest empirical support for RH.

### 2. Why computation is not enough

Finite verification cannot control the infinite tail. RH is a universal statement about all nontrivial zeros. No amount of checking finitely many zeros, however large the height, can logically exclude a counterexample above that range.

This limitation is fundamental, not merely practical.

### 3. Common failure modes in proof attempts

The critical review identified several recurring ways in which conjectural approaches break down:

#### a. Mistaking statistics for exact localization
Ideas based on random matrix theory, Coulomb gas models, moments, or machine-learned patterns may explain why RH looks true statistically, but they do not force every zero onto the line.

#### b. Smuggling positivity through analytic continuation
Several kernel, Euler-product, or prime-side positivity ideas risk illegitimately carrying positivity from \(\Re s>1\) into the critical strip, where the Euler product does not converge absolutely.

#### c. Assuming the missing operator exists
Many spectral proposals would prove RH if a canonical self-adjoint operator or unitary scattering system existed. But constructing that object is the hard part, and most proposals simply restate this need.

#### d. Repackaging equivalent criteria without new estimates
Restating RH via Li coefficients, Nyman–Beurling, Robin, or Lagarias is valuable only if it yields a tractable new inequality or structure. Otherwise it does not reduce difficulty.

#### e. Overinterpreting finite data
Machine discovery, numerical invariants, and low-lying zero behavior can suggest patterns, but the infinite tail may behave differently. Any proof depending on extrapolation from data alone is invalid.

#### f. Confusing metaphor with theorem
Terms such as “entropy,” “dimension,” “renormalization,” “transport,” or “CFT” do not advance RH unless accompanied by exact objects, rigorous identities, and a clear forcing mechanism.

### 4. Likely failure points for specific proposal classes

#### Spectral models
Potential failure: producing only a determinant representation or semiclassical counting law, without self-adjointness or exact arithmetic matching.

#### Positivity frameworks
Potential failure: defining positivity only formally, or on a domain too small to imply RH.

#### de Bruijn–Newman approaches
Potential failure: zero dynamics may remain too delicate, with local models unable to control the global zero configuration.

#### Nyman–Beurling and Robin-type strategies
Potential failure: equivalent formulations may remain just as hard as RH if no new approximation or extremal monotonicity principle is found.

#### Statistical/physics ideas
Potential failure: average laws and equilibrium pictures may never imply pointwise zero support.

### 5. What numerical work remains useful for

Despite these limitations, numerical testing remains highly valuable for:
- certifying finite results rigorously,
- testing conjectured inequalities and monotonicity,
- probing Li coefficients and de Bruijn–Newman bounds,
- identifying candidate identities or invariants,
- falsifying overstrong speculative claims.

---

## Critical Assessment

### 1. Overall strengths of the current research landscape

The modern RH ecosystem is unusually rich. It combines:
- deep classical theory,
- exact reformulations,
- strong numerical evidence,
- structural analogies from geometry and spectral theory,
- broad interaction with mathematical physics and harmonic analysis.

In particular, the review reveals three genuine strengths:

#### a. Multiple exact reformulations exist
This means RH is not confined to one analytic expression. It can be attacked through Möbius sums, approximation theory, divisor inequalities, entire functions, or positivity criteria.

#### b. There is overwhelming empirical support
Large-scale certified computation and zero statistics strongly suggest RH is true.

#### c. Several directions target the right kind of mechanism
The most credible ideas seek:
- a positivity principle,
- a self-adjoint/unitary spectral model,
- or a rigorous equivalent criterion made more tractable.

These are the right kinds of targets, even if none is currently complete.

### 2. Overall weaknesses

The main weaknesses are structural.

#### a. No forcing mechanism is known
This is the central issue. Existing methods control averages, densities, or finite ranges, but RH requires pointwise control of every zero.

#### b. Many proposals merely rename the problem
A large fraction of the novel ideas are conceptually attractive but do not reduce RH to a simpler or more rigid theorem.

#### c. Positivity is repeatedly invoked but not constructed
In successful RH analogues over finite fields, positivity is genuine and geometric. In the classical case, many approaches hope for positivity without providing a mathematically robust one.

#### d. Statistical theories are too weak
RMT, moments, pair correlation, and equilibrium models strongly support RH, but statistics do not imply exact support on \(\Re s=1/2\).

#### e. Equivalent criteria are not automatically easier
Robin, Li, Nyman–Beurling, and Lagarias criteria are exact, but each hides the same global cancellation difficulty in a different language.

### 3. Ranking of the proposed ideas by credibility

#### Most credible in principle
These are the proposals that align best with what a real proof likely needs:
- Arakelov-cohomological positivity
- Canonical scattering matrix or unitary spectral realization
- Prime-based RKHS or de Branges-type positivity
- de Bruijn–Newman via PDE/integrable zero dynamics
- Li coefficients as moments of a positive measure
- Rigidity from the full family of explicit formulas
- Berry–Keating with genuine arithmetic boundary conditions
- Multiplicative uncertainty principles
- Nyman–Beurling with modern harmonic analysis or wavelet methods

#### Best as partial-progress programs
These may not prove RH directly but could generate meaningful advances:
- Fractal transfer operators
- Lehmer-pair zero dynamics
- Arithmetic quantum graphs
- Pretentious refinements for Möbius cancellation
- Coulomb gas and large-deviation formulations
- Painlevé/isomonodromic formulations
- Robin optimization on divisor trees
- Arithmetic deconvolution of the gamma factor
- Machine-assisted conjecture discovery

#### Mostly heuristic or weak in current form
These currently lack a clear theorem-level route:
- Dimension-equals-critical-line ideas
- Renormalization fixed-point language
- Tropical geometry avatars
- Entropy maximization
- Free probability models for Euler factors
- Universality breakdown as a proof device
- Category-theoretic RH
- Adelic conformal field theory
- Optimal transport from primes to zeros

### 4. The core obstacles, restated

The review repeatedly returns to three genuine obstructions:

#### a. Global cancellation
RH is equivalent to square-root-scale cancellation in several arithmetic sums. Current analytic methods do not reach that uniformly.

#### b. Missing spectral object
The Hilbert–Pólya dream demands an operator with the right spectrum and the right arithmetic trace formula. No such object is known.

#### c. Missing positivity principle
The Weil/Deligne paradigm succeeds through cohomological positivity and purity. No analogous principle over \(\mathbb Q\) has been identified.

### 5. Final critical judgment

The novel proposal set is valuable as a map of possible directions, but not as a collection of near-proof strategies. Most ideas fail because they do not bridge the decisive gap between:
- averaged, finite, or heuristic control,
and
- exact, global, all-zero localization.

The strongest ideas are those that attack this gap directly through positivity, self-adjointness, or exact equivalent criteria. The weakest are those that rely mainly on analogy or metaphor.

---

## Recommendations for Next Steps

### 1. Prioritize mechanisms, not reformulations alone

Future work should focus less on generating new metaphors and more on developing one of the few mechanisms that could plausibly force RH:
- genuine positivity,
- self-adjointness/unitarity,
- rigidity from a full explicit-formula framework,
- or a sharp equivalent criterion with new estimates.

### 2. Highest-priority research clusters

#### A. Positivity and geometric frameworks
Most promising directions:
- Arakelov-cohomological positivity
- de Branges/RKHS positivity tied to \(\xi\)
- Li coefficients as moments of a positive measure
- Rigidity from all Weil-type explicit formulas simultaneously

Why prioritize:
These are among the few approaches that might produce a forcing principle rather than statistical evidence.

Recommended tasks:
- formulate exact positivity criteria,
- build smallest possible candidate spaces/forms,
- test whether Li or Weil quadratic forms can be represented by true positive measures or kernels,
- seek toy analogues in simpler \(L\)-function settings.

#### B. Spectral and scattering realization
Most promising directions:
- canonical scattering determinant equal to \(\xi(s)\),
- Berry–Keating with rigorous arithmetic boundary conditions,
- adelic trace/scattering frameworks.

Why prioritize:
A canonical self-adjoint or unitary object would immediately explain the critical line.

Recommended tasks:
- define exact target determinant identities,
- separate local and archimedean contributions cleanly,
- prove trace or scattering formulas before claiming RH implications,
- require canonicity, not merely engineered models.

#### C. de Bruijn–Newman and zero dynamics
Most promising directions:
- PDE or integrable-structure interpretations of \(\Xi_t\),
- local Lehmer-pair dynamics,
- hyperbolicity-preserving operators.

Why prioritize:
This attacks a sharp equivalent problem where modern progress already exists.

Recommended tasks:
- derive exact zero-motion laws under heat deformation,
- search for conserved quantities or monotone functionals,
- aim first at improved upper bounds on \(\Lambda\),
- study whether local pair geometry yields rigorous global constraints.

#### D. Exact reformulations with modern analysis
Most promising directions:
- Nyman–Beurling via Mellin-adapted harmonic analysis,
- wavelet or frame methods,
- multiplicative uncertainty principles,
- carefully structured Robin optimization.

Why prioritize:
These are rigorous equivalents and may yield incremental but meaningful advances.

Recommended tasks:
- compute and analyze Gram matrices and basis structures,
- identify whether approximation obstructions localize in Mellin coordinates,
- search for new coercive inequalities,
- focus on tractable subproblems rather than broad reformulations.

### 3. Use computation strategically

Computation should continue, but in targeted roles:
- certify zeros and simplicity to higher ranges,
- test candidate positivity/monotonicity statements,
- probe Li coefficients and de Bruijn–Newman functionals,
- generate conjectures for exact identities or inequalities,
- support formal verification of local arguments.

Computation should not be mistaken for a proof route to the full RH.

### 4. Demand exact objects and falsifiable statements

For speculative proposals, a useful screening rule is:
- What exact object is being constructed?
- What known theorem would it recover?
- How does \(\Re s=1/2\) enter mathematically?
- What is the first nontrivial theorem short of RH that the idea predicts?

Ideas that cannot answer these questions should be deprioritized.

### 5. Best concrete milestones that would count as real progress

The community would likely regard any of the following as major advances:
- an unconditional improvement beyond Conrey’s \(2/5\) critical-line proportion,
- a genuinely new zero-free region mechanism,
- a canonical self-adjoint or unitary operator/scattering system producing \(\xi\),
- decisive progress on the de Bruijn–Newman upper bound or \(\Lambda\le 0\),
- a new positivity framework over \(\mathbb Q\),
- a substantial breakthrough on Nyman–Beurling closure estimates,
- a rigorous positive-measure interpretation of Li coefficients.

### 6. Recommended strategic ranking

If effort must be concentrated, the strongest portfolio is:

1. Positivity/cohomological frameworks  
2. Scattering and canonical spectral realization  
3. de Bruijn–Newman and zero dynamics  
4. Nyman–Beurling and multiplicative harmonic analysis  
5. High-rigor computational and formal support

### 7. Final recommendation

The most productive path forward is not to chase ever more varied analogies, but to deepen the few directions that target the real missing structures:
- positivity,
- self-adjointness,
- exact global rigidity,
- and sharp equivalent formulations.

RH does not appear blocked by lack of evidence. It is blocked by lack of a mechanism. Research should therefore prioritize the discovery of a mechanism over the accumulation of further heuristic support.

---

## Concluding Statement

As of 2026, the Riemann Hypothesis remains open. Its truth is supported by overwhelming numerical, statistical, and structural evidence, yet no accepted proof exists. The review of classical theory, modern progress, equivalent criteria, numerical testing, and 48 speculative proposals leads to a single consistent conclusion:

The central challenge is not finding more evidence that RH is true. It is finding a mathematically rigorous principle that forces all zeros onto the critical line.

At present, the most credible candidates for such a principle lie in:
- positivity over number fields,
- canonical spectral or scattering realizations,
- de Bruijn–Newman zero dynamics,
- and deeper exploitation of exact equivalent criteria.

Everything else is secondary unless it can be sharpened into one of those forms.