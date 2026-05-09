# Final Report on the Riemann Hypothesis

## Executive Summary

The Riemann Hypothesis (RH) remains open as of 2026. No proof or disproof is accepted by the mathematical community, and no recent claimed proof has survived expert scrutiny. RH states that every nontrivial zero of the Riemann zeta function lies on the critical line \(\Re s = 1/2\). Equivalently, all zeros of the completed function \(\xi(s)\) lie on that line, or all zeros of the even entire function \(\Xi(t)=\xi(1/2+it)\) are real.

The present state of evidence strongly favors RH, but none of that evidence reaches proof. The strongest support comes from:
- extensive numerical verification of zeros on the critical line,
- agreement of zero statistics with Gaussian Unitary Ensemble (GUE) predictions,
- de Bruijn–Newman theory, especially the fact that the Newman constant \(\Lambda\) is known to satisfy \(\Lambda \ge 0\) and numerically appears extremely close to \(0\),
- the absence of any credible structural mechanism producing off-line zeros.

At the same time, the main barriers remain unchanged:
- no known positivity mechanism analogous to those in proven RH analogues over function fields,
- no natural self-adjoint operator realizing the zero ordinates spectrally,
- classical complex-analytic methods and zero-density estimates remain too weak to force all zeros onto the line,
- mollifier and moment methods detect many zeros on the line but do not approach 100%.

A large set of speculative or novel ideas has been proposed. A small subset aligns with serious existing frameworks and may be worth long-term development; most others are best understood as heuristic reformulations or exploratory research themes rather than realistic proof strategies. The most credible long-term avenues remain:
1. a Hilbert–Pólya-type spectral construction,
2. a Deninger/Connes-style cohomological or dynamical trace-formula framework,
3. a de Branges/Laguerre–Pólya positivity approach,
4. a sharp de Bruijn–Newman rigidity principle proving \(\Lambda=0\).

## Current State of Research

### Statement and core formulations

The Riemann zeta function is initially defined for \(\Re s>1\) by
\[
\zeta(s)=\sum_{n\ge1} n^{-s},
\]
and extends meromorphically to \(\mathbb C\). Its nontrivial zeros lie in the critical strip \(0<\Re s<1\). RH asserts that all such zeros have real part \(1/2\).

A standard equivalent formulation uses the completed function
\[
\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
Then RH is equivalent to all zeros of \(\xi(s)\) lying on \(\Re s=1/2\). Writing
\[
\Xi(t)=\xi(1/2+it),
\]
RH becomes the statement that all zeros of the entire even function \(\Xi(t)\) are real.

### Status in 2026

RH remains unsolved and is one of the Clay Millennium Prize Problems. A proof would require a complete and peer-validated argument resolving all standard equivalent formulations.

There has been no accepted proof or disproof. The field remains highly active, but fragmented across several major directions:
- zero statistics,
- explicit zero verification,
- de Bruijn–Newman theory,
- Li coefficients and positivity criteria,
- Nyman–Beurling functional-analytic formulations,
- trace-formula and spectral analogies,
- de Branges and Laguerre–Pólya programs,
- noncommutative and cohomological frameworks.

### Classical unconditional results

The strongest classical zero-free regions remain far from RH. For large \(|t|\), one has regions of the form
\[
\sigma \ge 1-\frac{c}{(\log |t|)^{2/3}(\log\log |t|)^{1/3}}
\]
free of zeros, via Korobov–Vinogradov-type methods. These results are important but nowhere near the critical line.

Unlike Dirichlet \(L\)-functions, \(\zeta(s)\) has no Siegel zero issue; the challenge is not an exceptional real zero near 1, but the full geometry of zeros inside the critical strip.

The prime number theorem is equivalent to zero-freeness on \(\Re s=1\), not RH. RH would imply the much sharper error term
\[
\pi(x)=\operatorname{Li}(x)+O(\sqrt{x}\log x).
\]
Best unconditional bounds for \(\psi(x)-x\), \(\theta(x)-x\), and \(\pi(x)-\operatorname{Li}(x)\) remain far weaker than square-root cancellation.

### Equivalent criteria and analytic formulations

RH is equivalent to many deep statements, including:
\[
M(x)=\sum_{n\le x}\mu(n)=O(x^{1/2+\varepsilon}),
\]
\[
\psi(x)=x+O(x^{1/2}\log^2 x),
\]
as well as Li’s criterion, Weil’s positivity criterion, and the Nyman–Beurling closure criterion.

These equivalences remain important because they expose different structural aspects of RH:
- arithmetic cancellation,
- positivity,
- spectral interpretation,
- function-space approximation.

No equivalent criterion has yet yielded a decisive breakthrough.

### Zeros on the critical line

Hardy proved that infinitely many zeros lie on the critical line. Subsequent work, especially by Selberg, Levinson, and Conrey, showed that a positive proportion of zeros lie on the line, with the best landmark results exceeding \(2/5\). As of 2026, no accepted proof gets anywhere close to 100%.

Mollifier methods remain central to these results. They are technically powerful and have also shown that a positive proportion of zeros on the line are simple. But they face well-recognized conceptual and technical barriers before full RH.

Zero-density theorems show that most zeros are close to the line in suitable averaged senses. These theorems are crucial for many applications in analytic number theory, but they do not force all zeros onto the line.

### Statistical and computational evidence

Montgomery’s pair correlation work and the GUE model from random matrix theory remain among the strongest heuristic supports for RH. Odlyzko’s computations of high zeros show striking agreement with GUE statistics.

Large-scale computations have rigorously verified that enormous initial segments of zeros lie on the critical line and are simple. Turing-type zero counting methods and explicit argument-principle implementations are now highly developed. These computations strongly support RH but cannot prove it, because any finite verification leaves open the possibility of off-line zeros farther up.

### de Bruijn–Newman theory

One of the most important modern frameworks studies deformations \(H_t\) of \(\Xi\) under heat flow. There exists a constant \(\Lambda\) such that \(H_t\) has only real zeros if and only if \(t\ge \Lambda\). RH is equivalent to \(\Lambda \le 0\).

Rodgers and Tao proved in 2018 that \(\Lambda \ge 0\). Thus RH is equivalent to the sharp statement
\[
\Lambda=0.
\]
As of 2026, accepted results place \(\Lambda\) in a very small interval of the form
\[
0\le \Lambda \le \text{small explicit positive bound},
\]
with numerical refinements by Saouter, Gourdon, Demichel, and others. This is among the strongest quantitative evidence for RH, but not a proof.

### Major conceptual programs

Several broad frameworks continue to shape expert thinking:

- **Hilbert–Pólya:** find a self-adjoint operator whose eigenvalues are the zero ordinates \(\gamma\).
- **de Branges / Laguerre–Pólya:** place \(\Xi\) in a positivity framework forcing real zeros.
- **Connes / Deninger:** build a spectral, cohomological, or dynamical theory over arithmetic spaces analogous to Weil’s proof for function fields.
- **Weil positivity:** identify a positivity mechanism behind the explicit formula.
- **Nyman–Beurling / Báez-Duarte:** prove an exact closure property in a function space.

All remain active or influential. None is close to resolution.

### Main obstacles

Four obstacles dominate the field:

1. **No positivity mechanism.**  
   Successful RH analogues over finite fields rely on positivity, polarization, self-adjointness, or intersection theory. No analogue is known for \(\zeta(s)\).

2. **Limits of complex analysis.**  
   Classical tools give averaged control, zero-free regions, and density theorems, but not exact line confinement of all zeros.

3. **Mollifier and moment barriers.**  
   Existing methods can detect many zeros on the line, but appear unable in their current form to reach 100%.

4. **No arithmetic spectral operator.**  
   The Hilbert–Pólya vision remains compelling, but no operator with the required spectrum and explicit-formula compatibility has been found.

## Novel Ideas Proposed

The proposed ideas fall into several broad categories. Some are serious variants of major existing programs; others are exploratory or mostly heuristic.

### 1. Spectral, trace-formula, and geometric operator ideas

These ideas seek a self-adjoint or unitary structure whose spectral data reproduces the zeta zeros.

Key proposals included:
- a fractal trace formula for primes,
- a prime geodesic flow on a nonclassical space,
- a quantum graph with bond lengths \(\log p\),
- a supersymmetric Dirac-type operator with regularized determinant \(\Xi\),
- a prime-power scattering matrix whose determinant equals \(\xi\),
- adèlic or singular geometric spaces supporting a Selberg-type trace formula.

**Potential significance:**  
If any exact self-adjoint realization existed, RH would likely follow immediately. These ideas fit naturally with Hilbert–Pólya and with the observed links between zeros, trace formulas, and quantum chaos.

**Common technical target:**  
Reproduce Weil’s explicit formula exactly, including:
- prime-power terms,
- the gamma factor,
- correct spectral density,
- no spurious spectrum.

### 2. Positivity, kernel, and de Branges-style ideas

These proposals aim to force real-rootedness of \(\Xi\) through analytic positivity.

Key proposals included:
- a de Branges space generated by Mellin-wavelet packets,
- total positivity of a theta-derived Riemann kernel,
- Li coefficients as moments of a positive measure,
- RH as a sharp multiplicative uncertainty principle,
- all-scale log-concavity or hyperbolicity of Jensen polynomials,
- Weil positivity realized through reproducing-kernel Hilbert spaces,
- orthogonal polynomial ensembles built from \(\Xi\)-data.

**Potential significance:**  
These ideas target one of the most plausible missing ingredients: a positivity principle strong enough to force \(\Xi\) into the Laguerre–Pólya class.

**Common technical target:**  
Convert RH into positivity of a kernel, measure, moment functional, or operator that is more structured than current criteria.

### 3. de Bruijn–Newman flow and monotonicity ideas

These ideas focus on the sharpened equivalent statement \(\Lambda=0\).

Key proposals included:
- interpreting Newman flow as a renormalization flow,
- finding a stronger positivity-preserving heat flow,
- viewing zeros as particles in an optimal-transport evolution,
- defining a monotone entropy of the zero set under smoothing,
- hybrid \(p\)-adic/archimedean heat equations.

**Potential significance:**  
This is one of the most sharply focused modern directions, because RH becomes a precise threshold statement.

**Common technical target:**  
Find a monotone functional, entropy, or rigidity theorem under the deformation \(H_t\) that forces the threshold to be exactly \(t=0\).

### 4. Cohomological, motivic, and arithmetic-geometric ideas

These proposals try to recreate the function-field proof pattern for \(\zeta\).

Key proposals included:
- an infinite-dimensional polarized Hodge structure over \(\mathrm{Spec}(\mathbb Z)\),
- a noncommutative solenoid with Frobenius-like scaling,
- a Hodge-index-type inequality for explicit-formula pairings,
- a motivic Ruelle zeta function over the integers,
- mirror-duality interpretations of the functional equation.

**Potential significance:**  
This category is conceptually among the strongest. It directly seeks the missing positivity and duality structures analogous to Weil’s proof over finite fields.

**Common technical target:**  
Construct cohomology, pairings, or dynamical trace formulas with enough rigidity and polarization to force critical-line symmetry.

### 5. Functional-analytic, arithmetic, and data-driven reformulations

These proposals rework known criteria or seek new tools around them.

Key proposals included:
- Nyman–Beurling via compressed sensing or frame theory,
- Möbius orthogonality in nonclassical Hilbert spaces,
- hyperuniformity formulations of prime fluctuations,
- Mellin–Paley–Wiener theorems with arithmetic support,
- machine-assisted discovery of invariants involving \(\Xi\), Li coefficients, or Newman flow.

**Potential significance:**  
These may sharpen existing exact criteria or reveal overlooked monotone quantities.

**Common technical target:**  
Make an RH-equivalent formulation more rigid, computationally tractable, or structurally positive.

## Numerical Testing & Potential Failures

### What numerical work currently supports

Numerics remain one of the strongest sources of evidence for RH:
- very large initial segments of zeros have been verified on the line,
- checked zeros are simple,
- local spacing agrees with GUE to high precision,
- explicit bounds on the de Bruijn–Newman constant place \(\Lambda\) extremely close to 0 from above.

These results substantially constrain low-height counterexamples and strongly support the broader statistical framework around RH.

### Why numerical verification does not scale to proof

No finite computation can prove RH. Even if trillions or more zeros are checked:
- this leaves infinitely many zeros untested,
- a single off-line zero at extreme height would disprove RH,
- local or finite-range statistics do not imply global exact truth.

Thus the main value of numerics is:
- falsifying weak conjectural mechanisms,
- calibrating explicit formulas,
- testing candidate positivity statements,
- suggesting monotone quantities or structural invariants.

### Stress-testing the proposed novel ideas

Across the 50 proposals, several recurring failure modes appear.

#### 1. Exactness failure

Many proposals can imitate some aspect of RH—zero counts, approximate statistics, or prime-like orbit expansions—without matching the exact arithmetic structure. In particular, most speculative spectral or geometric models fail to explain:
- the gamma factor,
- exact prime-power amplitudes,
- the full functional equation,
- the absence of extraneous spectrum.

This is the dominant failure mode for trace-formula, quantum graph, fractal, and scattering ideas.

#### 2. Positivity gap

Many proposals identify an appealing object—kernel, measure, flow, graph, category—but do not produce the actual positivity theorem needed. This is the dominant failure mode for:
- de Branges variants,
- kernel methods,
- Li-measure programs,
- cohomological analogies,
- Hodge-like frameworks.

In most cases, the proposal stops just short of the key missing theorem.

#### 3. Statistical-to-pointwise failure

Several ideas rely on random matrix theory, Coulomb gas intuition, pair correlation, repulsion, or universality. These may explain typical behavior, but RH is an all-zeros statement. Statistical regularity does not rule out isolated off-line zeros.

This is the dominant failure mode for:
- free-probability models,
- zero-repulsion rigidity ideas,
- topological recursion for correlations,
- energy-principle approaches not tied to exact identities.

#### 4. Reformulation without leverage

Some ideas restate known equivalent criteria in modern language—compressed sensing, curvature, machine learning kernels, orthogonality frameworks—without yet providing tools stronger than the original formulation.

This is not useless, but it is not progress unless the reformulation yields a new coercive estimate or positivity argument.

### Which ideas seem strongest under current stress tests

The most resilient proposals under criticism are those that align with known deep structures and target the right bottleneck.

#### Strongest conceptual candidates
- Hodge-index-type positivity for explicit-formula pairings
- motivic/dynamical Ruelle-zeta over the integers
- RKHS realization of Weil positivity
- de Branges-type Mellin-adapted positivity frameworks
- de Bruijn–Newman entropy or monotonicity programs
- exact self-adjoint spectral realizations via graphs, Dirac operators, or scattering

#### Ideas most vulnerable to failure
- tropicalization,
- KAM-style prime resonance pictures,
- mirror symmetry slogans without concrete categories,
- generic fractal or Julia-set analogies,
- graph curvature programs,
- nonlinear transforms of Möbius without exact arithmetic structure.

## Critical Assessment

### Overall strengths of the research landscape

The field has several major strengths:

1. **Exceptional structural richness.**  
   RH has many equivalent formulations, giving researchers multiple points of attack.

2. **Strong heuristic coherence.**  
   Numerical evidence, GUE statistics, explicit formulae, and de Bruijn–Newman theory all point in the same direction.

3. **Deep adjacent progress.**  
   Even without proving RH, work on moments, zero statistics, mollifiers, Li coefficients, and Nyman–Beurling theory has significantly deepened understanding.

4. **High-quality conceptual frameworks.**  
   Hilbert–Pólya, de Branges, Weil positivity, Connes, and Deninger remain serious programs, not mere folklore.

### Overall weaknesses and unresolved gaps

Despite this, the central weakness is unchanged: no approach currently supplies the missing decisive mechanism.

#### No known positivity theorem
This remains the central issue. In function fields, positivity of intersection forms or spectral unitarity forces RH analogues. For \(\zeta\), no such theorem is known.

#### No exact spectral object
Many proposals say, in effect, “if we could build the right self-adjoint operator, RH would follow.” True—but this is not progress unless the operator is actually constructed with exact arithmetic compatibility.

#### Classical methods plateau below RH
Zero-density estimates, mean values, and mollifier methods provide strong averaged information but do not approach full line confinement.

#### Computational evidence is inherently finite
The vast verification of zeros supports RH but cannot settle it.

### Assessment of the novel proposals

The 50 proposals are best classified into four levels.

#### Level I: serious long-term frameworks
These align with expert views about plausible proof architectures:
- Hodge-index / explicit-formula positivity
- motivic or dynamical cohomology over \(\mathrm{Spec}(\mathbb Z)\)
- de Branges / Laguerre–Pólya positivity
- exact self-adjoint Hilbert–Pólya constructions
- sharp de Bruijn–Newman rigidity

These are not close to proof, but they target the right bottleneck.

#### Level II: useful reformulations or tool-building programs
These may yield meaningful partial progress:
- Li coefficients as moment problems,
- RKHS/kernel reformulations,
- Nyman–Beurling via frame methods,
- Jensen polynomial hierarchies,
- Möbius orthogonality in refined Hilbert spaces,
- machine-assisted invariant discovery.

Their value depends on producing genuinely new estimates, not just new language.

#### Level III: statistical or heuristic programs
These are helpful for intuition and testing:
- free probability,
- zero repulsion and Coulomb-gas pictures,
- topological recursion for correlations,
- hyperuniformity of primes.

These do not currently offer a path from average behavior to exact RH.

#### Level IV: mostly decorative or weakly grounded ideas
These are currently too vague or structurally mismatched:
- tropical explicit formulas,
- KAM resonance analogies,
- generic mirror-symmetry language,
- curvature on prime graphs,
- quasiconformal bubble exclusion,
- nonlinear Möbius scattering analogies.

### Bottom-line critical judgment

No proposed idea currently qualifies as a credible near-term proof strategy. A small set deserve sustained long-term attention because they seek the actual missing structure. Most of the rest should be treated as exploratory concepts, not breakthroughs.

The strongest intellectual lesson from the entire survey is this:

RH is unlikely to yield to clever estimates alone. A proof probably requires either:
- a genuine positivity/self-adjointness mechanism, or
- a sharp semigroup or deformation principle with exact rigidity at the boundary case.

## Recommendations for Next Steps

### 1. Prioritize positivity-based programs

The most promising research direction is to develop explicit positivity frameworks strong enough to force real-rootedness or critical-line confinement.

Highest-priority subprograms:
- RKHS factorization of Weil’s positivity criterion,
- de Branges spaces adapted to Mellin/theta structure,
- Hodge-index-type formulations of explicit-formula pairings,
- Li-coefficient moment or Hankel-positivity models.

**Recommended goal:** move from abstract equivalence to concrete positive operators, kernels, or pairings.

### 2. Intensify de Bruijn–Newman rigidity research

Given that RH is equivalent to \(\Lambda=0\) and \(\Lambda\ge 0\) is already known, this is one of the sharpest available routes.

Priority tasks:
- search for entropy or Lyapunov functionals monotone under Newman flow,
- study finite-dimensional analogues via Jensen polynomials and heat flow,
- formalize zero-configuration dynamics under smoothing,
- test candidate monotonic quantities computationally and then prove them.

**Recommended goal:** identify a functional whose equality case corresponds exactly to real-rootedness at \(t=0\).

### 3. Demand exactness in spectral models

Hilbert–Pólya-type ideas remain serious, but only exact models matter.

Any spectral proposal should be required to explain:
- the gamma factor,
- prime-power coefficients in the explicit formula,
- self-adjointness or unitarity,
- determinant normalization,
- exclusion of extra spectral components.

**Recommended goal:** build and solve toy models for finite Euler products or local factors before claiming relevance to full RH.

### 4. Build bridges between major frameworks

Several serious approaches may be different facets of the same missing structure. In particular, researchers should actively connect:
- Weil positivity and RKHS methods,
- de Branges theory and Mellin-wavelet decompositions,
- Li coefficients and orthogonal polynomial/Hankel positivity,
- Newman flow and Laguerre–Pólya criteria,
- Deninger/Connes-style cohomology and explicit-formula quadratic forms.

**Recommended goal:** identify statements that are simultaneously meaningful in multiple frameworks.

### 5. Use computation strategically, not rhetorically

Numerics should be used to:
- test low-order total positivity or kernel positivity,
- search for monotone combinations of Li coefficients,
- study Jensen polynomial hyperbolicity under deformation,
- probe entropy-like quantities along de Bruijn–Newman flow,
- eliminate speculative frameworks quickly when exact low-level identities fail.

**Recommended goal:** computationally screen conjectural structures before investing in full theoretical development.

### 6. Be more selective about speculative analogies

Future work should sharply distinguish:
- exact criterion + new tool,
from
- metaphor + repackaging.

Proposals based mainly on imported language—tropical, KAM, curvature, mirror symmetry, ML kernels—should only be pursued if they immediately yield a precise theorem stronger than current knowledge.

**Recommended goal:** raise the evidentiary standard for speculative RH programs.

### 7. Focus on intermediate milestones

Because a full proof remains distant, progress should be measured by concrete achievements such as:
- new positivity theorems for restricted test-function classes,
- propagation results for Jensen hyperbolicity,
- sharper structural results on Li coefficients,
- semigroup monotonicity under de Bruijn–Newman flow,
- exact trace identities in toy spectral or graph models,
- genuine geometric realizations of local factors.

**Recommended goal:** create milestones that meaningfully reduce the conceptual gap to RH.

---

## Final Conclusion

As of 2026, the Riemann Hypothesis remains one of the deepest open problems in mathematics. The strongest evidence still comes from computation, zero statistics, and de Bruijn–Newman theory, but none of these constitute proof. The field has advanced substantially in understanding the zeta function’s behavior, yet the decisive missing ingredient remains a rigorous mechanism of positivity, self-adjointness, or exact rigidity.

Among the many proposed ideas, only a limited group align with what experts would regard as serious long-term proof architectures:
- explicit-formula positivity and Hodge-index analogues,
- cohomological or dynamical trace-formula programs,
- de Branges/Laguerre–Pólya approaches,
- sharp de Bruijn–Newman rigidity,
- exact Hilbert–Pólya spectral constructions.

The clearest practical recommendation is therefore not to multiply analogies, but to deepen the few frameworks that directly target the central obstruction. If RH is eventually solved, it is most likely to be through a new structure that simultaneously explains:
- the explicit formula,
- the functional equation,
- the prime spectrum,
- and the positivity that forces zeros onto the critical line.

At present, that structure is still missing.