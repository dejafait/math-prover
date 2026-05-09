# Final Report on the Riemann Hypothesis (2026)

*Note:* This report synthesizes established literature reliably known through mid-2024, together with the broad 2026 consensus that no proof or disproof of the Riemann Hypothesis (RH) has been accepted. It does **not** rely on live web access.

---

## Executive Summary

The Riemann Hypothesis remains open in 2026. No claimed proof or disproof has been accepted by the mathematical community, and the Clay Millennium Prize remains unclaimed.

The strongest established facts are still the classical ones:

- RH is equivalent to several exact reformulations, including:
  - the prime-number error term
    \[
    \psi(x)=x+O\!\left(x^{1/2}\log^2 x\right),
    \]
  - the Möbius cancellation bound
    \[
    M(x)=\sum_{n\le x}\mu(n)=O_\varepsilon(x^{1/2+\varepsilon}),
    \]
  - Robin’s inequality for divisor sums,
  - Lagarias’s harmonic-number criterion,
  - positivity of Li coefficients,
  - positivity in Weil’s explicit-formula criterion,
  - the Nyman–Beurling–Báez-Duarte closure criterion,
  - Speiser’s theorem on zeros of \(\zeta'(s)\),
  - and the de Bruijn–Newman condition \(\Lambda\le 0\).

- Major proven progress includes:
  - infinitely many zeros on the critical line (Hardy),
  - a positive proportion on the line (Selberg, Levinson, Conrey, Bui–Conrey–Young),
  - extensive zero-density bounds,
  - large-scale rigorous computation of zeros on the line,
  - and Rodgers–Tao’s theorem that the de Bruijn–Newman constant satisfies \(\Lambda\ge 0\), implying that if RH is true, it is “barely true.”

- Numerical evidence is overwhelming but not decisive:
  - trillions of zeros have been rigorously checked,
  - all checked zeros are simple and on the critical line,
  - Odlyzko’s computations strongly support random matrix/GUE statistics,
  - and the best numerical lower bound places \(\Lambda\) extremely close to \(0\).

- The three most credible broad research programs remain:
  1. spectral / Hilbert–Pólya ideas,
  2. Weil-style arithmetic geometry or cohomology over \(\operatorname{Spec}\mathbb Z\),
  3. analytic approaches through explicit formulas, moments, mollifiers, and RH-equivalent positivity criteria.

This report also compiles a set of speculative new ideas. A small minority look like serious long-shot directions; many others are best viewed as heuristics, reformulations, or likely dead ends. The sharpest lesson is that most proposals fail because they either:
- do not constrain the real parts of zeros,
- replace RH by a stronger unsupported conjecture,
- assume the existence of an object whose existence would itself almost amount to a proof,
- or mistake a suggestive analogy for a theorem-producing mechanism.

---

## Current State of Research

### 1. Core statement and exact reformulations

The Riemann Hypothesis states that every nontrivial zero of the Riemann zeta function \(\zeta(s)\) has real part \(1/2\).

The most important exact equivalents in current use are:

- **Prime-number error term**  
  RH is equivalent to
  \[
  \psi(x)=x+O\!\left(x^{1/2}\log^2 x\right),
  \]
  and similarly to the expected square-root error in \(\pi(x)-\operatorname{Li}(x)\) (von Koch).

- **Möbius cancellation**  
  RH is equivalent to
  \[
  M(x)=O_\varepsilon(x^{1/2+\varepsilon})
  \quad\text{for every }\varepsilon>0.
  \]

- **Robin’s criterion**  
  RH is equivalent to
  \[
  \sigma(n)<e^\gamma n\log\log n \quad (n>5040).
  \]

- **Lagarias’s criterion**  
  RH is equivalent to an inequality involving \(\sigma(n)\), \(H_n\), and \(e^{H_n}\log H_n\).

- **Li’s criterion**  
  RH is equivalent to the positivity of all Li coefficients \(\lambda_n\).

- **Weil explicit-formula positivity**  
  RH is equivalent to positivity of a quadratic form built from test functions and the explicit formula.

- **Nyman–Beurling–Báez-Duarte criterion**  
  RH is equivalent to a closure statement in \(L^2(0,1)\).

- **Speiser’s theorem**  
  RH is equivalent to \(\zeta'(s)\) having no zeros in \(\Re(s)<1/2\).

- **de Bruijn–Newman reformulation**  
  RH is equivalent to \(\Lambda\le 0\), where \(\Lambda\) is the de Bruijn–Newman constant.

These equivalences are central because they define the main directions any serious new approach must engage with.

### 2. Established partial results

The major unconditional theorems remain far from RH but are structurally important:

- **Hardy (1914):** infinitely many zeros lie on the critical line.
- **Selberg:** a positive proportion lie on the critical line.
- **Levinson (1974):** at least one-third lie on the line.
- **Conrey (1989):** more than two-fifths lie on the line.
- **Bui–Conrey–Young (2011):** slightly above 41% on the line.

This 41% result is **not** considered close to RH. Experts regard the gap from “some positive proportion” to “all zeros” as requiring a qualitatively new idea.

Other established directions:

- **Zero-density theorems** give upper bounds on the number of zeros with \(\Re(s)\ge \sigma\), but they are far too weak to imply RH.
- **Zero-free regions near \(\Re(s)=1\)** remain useful for prime distribution, but they do not approach \(\Re(s)=1/2\).
- **Positive proportion of simple zeros** is known, but simplicity of all nontrivial zeros remains open.
- **Lindelöf** remains open and is much weaker than RH.

### 3. Major modern developments

Several developments since the late 20th century strongly shape current thinking:

- **de Bruijn–Newman constant:**  
  Rodgers and Tao proved \(\Lambda\ge 0\). Since RH is equivalent to \(\Lambda\le 0\), this means RH, if true, sits exactly at the boundary \(\Lambda=0\).

- **Jensen polynomials:**  
  Griffin, Ono, Rolen, and Zagier proved asymptotic hyperbolicity for certain Jensen polynomials attached to \(\xi\), for fixed degree and large shift. This is significant, but it falls far short of the full uniform real-rootedness needed for RH.

- **Mesoscopic zero statistics:**  
  Rigorous work by Bourgade, Kuan, Rodgers, Radziwiłł, Lester, Milinovich, and others has strengthened the statistical understanding of zeros at mesoscopic scales.

- **Moments and large values:**  
  Twisted moments, divisor correlations, resonance methods, and log-correlated field heuristics have advanced substantially, but none has produced a route to RH.

### 4. Numerical and computational status

Numerical evidence remains overwhelmingly favorable to RH:

- Gourdon verified the first \(10^{13}\) zeros on the line.
- Later rigorous work by Platt and Trudgian extended certified verification much further.
- Every rigorously checked zero is on the critical line and simple.
- Odlyzko’s high-height computations strongly match GUE predictions.
- The best published lower bound for the Newman constant remains
  \[
  \Lambda>-1.14541\times 10^{-11}.
  \]

The main computational tools are:

- Turing’s method,
- Odlyzko–Schönhage algorithms,
- Hiary’s fast evaluation methods,
- interval arithmetic and certified enclosures.

These are powerful for verification, but finite computation cannot prove RH.

### 5. Main heuristic frameworks

Three heuristic languages dominate current understanding:

- **Random matrix theory**  
  Especially the GUE analogy, Keating–Snaith moment heuristics, and the ratios conjecture.

- **Spectral/Hilbert–Pólya philosophy**  
  The hope of a self-adjoint operator whose eigenvalues are the zero ordinates.

- **Function-field analogy**  
  RH over finite fields follows from Frobenius + cohomology + positivity. The absence of a number-field analogue remains one of the deepest structural obstacles.

### 6. Known structural barriers

The main reasons current methods have not reached RH are now fairly clear:

- zero-density and mollifier methods do not scale to 100%,
- sieve and bilinear methods hit parity-type barriers,
- statistical information about zeros usually controls averages, not every zero,
- random matrix theory predicts behavior but does not prove location,
- no accepted self-adjoint operator for zeta zeros is known,
- no accepted cohomology theory over \(\operatorname{Spec}\mathbb Z\) with Frobenius/weights/polarization exists,
- and Voronin universality warns against naive local positivity arguments.

### 7. Standard references

The standard foundational references remain:

- Titchmarsh–Heath-Brown, *The Theory of the Riemann Zeta-Function*
- Edwards, *Riemann’s Zeta Function*
- Bombieri’s Clay lecture/surveys
- Conrey, *The Riemann Hypothesis* (*Notices AMS*)
- Iwaniec–Kowalski, *Analytic Number Theory*

---

## Novel Ideas Proposed

All ideas in this section are speculative. They are included because they touch exact RH criteria, major existing programs, or potentially useful structural analogies.

### A. Spectral, operator-theoretic, and dynamical ideas

1. **Adelic quantum graph conjecture**  
   Build a quantum graph with prime-length edges \(\log p\) whose secular determinant is \(\xi(s)\).  
   **Initial status:** conceptually attractive, but likely too rigid in closed self-adjoint form.

2. **Global scattering realization of \(\xi\)**  
   Realize \(\xi\) as a global scattering determinant formed from local factors at primes and infinity.  
   **Initial status:** one of the more serious structural ideas.

3. **Hermitian doubling of the Berry–Keating \(xp\) model**  
   Upgrade the semiclassical \(xp\) model to a doubled self-adjoint system encoding the functional equation.  
   **Initial status:** useful only if arithmetic can be inserted canonically.

4. **Almost-periodic Schrödinger operator with frequencies \(\log p\)**  
   Seek an operator whose spectrum or resonances match zeta zeros.  
   **Initial status:** probably too unconstrained unless canonical.

20. **Dyson-gas model for zero ordinates**  
   Model zero ordinates as an equilibrium Coulomb gas with arithmetic external field.  
   **Initial status:** good statistics heuristic, weak RH mechanism.

26. **Thermodynamic formalism for primes**  
   Build a Ruelle transfer operator with periodic orbits corresponding to prime powers.  
   **Initial status:** meaningful only if a real underlying system is found.

27. **Gauss map / Fredholm determinant bridge**  
   Refine Mayer-type transfer operators until their determinants factor through \(\xi\).  
   **Initial status:** partially grounded in existing math; still missing a critical-line mechanism.

28. **Hyperbolic surface with geodesic lengths \(\log p\)**  
   Search for a Selberg-style geometric realization of prime logarithms.  
   **Initial status:** likely impossible in literal classical form.

40. **Prime-energy minimization on the critical line**  
   Define an energy from primes and prove that off-line zeros increase it.  
   **Initial status:** only useful if the energy is canonical.

41. **Electrostatic mirror principle**  
   Treat the functional equation as mirror symmetry and zeros as charges.  
   **Initial status:** potentially useful as intuition for Speiser-type arguments.

42. **Magnetic quantum graph encoding Möbius signs**  
   Use graph phases to reproduce \(\mu(n)\) by interference.  
   **Initial status:** structurally mismatched to Möbius and likely dead.

43. **PT-symmetry-to-self-adjointness route**  
   Treat the functional equation as PT symmetry and search for a hidden quasi-Hermitian structure.  
   **Initial status:** adds little without a concrete operator.

### B. Functional-analytic, positivity, and entire-function ideas

8. **Mellin-version fractal uncertainty principle**  
   Adapt fractal uncertainty principles to the Mellin setting of zeta.  
   **Initial status:** potentially useful only with a real operator/dynamical model.

9. **Wavelet upgrade of the Nyman–Beurling criterion**  
   Replace raw generators by a Mellin-wavelet frame to make the closure problem constructive.  
   **Initial status:** credible for partial progress.

10. **Prime-adic multiresolution in \(L^2(0,1)\)**  
   Try to Euler-factorize the Nyman–Beurling space.  
   **Initial status:** probably forcing the wrong structure.

11. **Sonine/de Branges Jacobi-matrix model**  
   Build a tridiagonal self-adjoint model from Burnol/de Branges spaces.  
   **Initial status:** one of the most serious long-shot ideas.

12. **Total positivity kernel behind Weil’s criterion**  
   Search for a totally positive kernel underlying Weil positivity.  
   **Initial status:** elegant, but likely too strong to hold in naive form.

13. **Li coefficients as moments of a positive measure**  
   Seek a moment-sequence interpretation of normalized Li coefficients.  
   **Initial status:** appealing, but likely false as stated.

14. **Hankel positivity strengthening of Li’s criterion**  
   Replace scalar positivity by positivity of all Hankel matrices.  
   **Initial status:** almost certainly too strong without modification.

15. **Uniform hyperbolicity of Jensen polynomials via stability preservers**  
   Try to upgrade fixed-degree asymptotic hyperbolicity to a uniform theorem.  
   **Initial status:** one of the best concrete long-shot ideas.

16. **Laguerre–Pólya flow to \(\xi\)**  
   Construct a real-zero-preserving flow ending at \(\xi\).  
   **Initial status:** conceptually meaningful, but at risk of hiding RH in the setup.

17. **Entropy monotonicity under de Bruijn–Newman flow**  
   Define a Lyapunov or entropy functional for the zero set of \(\xi_t\).  
   **Initial status:** serious, technically difficult, and directly relevant to \(\Lambda=0\).

18. **Optimal transport formulation of zero motion**  
   Reinterpret Newman flow as a gradient flow in measure space.  
   **Initial status:** probably a reformulation, not a breakthrough.

19. **Burgers/KPZ-type PDE for \(\xi'/\xi\)**  
   Derive PDE control on zero motion from the heat deformation.  
   **Initial status:** analytically respectable, but may not solve the endpoint problem.

46. **Computer-assisted semidefinite positivity for Weil’s criterion**  
   Use rigorous SDP/sum-of-squares certificates on growing test-function spaces.  
   **Initial status:** one of the most concrete and testable proposals.

### C. Arithmetic, Möbius, and Robin-style ideas

23. **Möbius multiplicative-chaos model**  
   Model \(M(x)\) using log-correlated chaos ideas.  
   **Initial status:** good heuristic language, weak deterministic control.

24. **Universal short-interval nonpretentiousness principle**  
   Reformulate RH as sharp nonpretentiousness/cancellation in every short interval.  
   **Initial status:** serious if formulated non-tautologically.

25. **Nilsequence amplification of the explicit formula**  
   Replace simple phases by nilsequence weights in explicit-formula testing.  
   **Initial status:** may be too far from the actual Mellin structure of RH.

38. **Renormalization flow on superabundant numbers**  
   Treat Robin extremals as a dynamical system on exponent profiles.  
   **Initial status:** concrete but likely difficult to push to a full proof.

39. **Large-deviation principle for Robin’s inequality**  
   Analyze near-counterexamples probabilistically.  
   **Initial status:** useful heuristically, weak as a deterministic proof tool.

### D. Geometric, cohomological, noncommutative, and family-level ideas

5. **Prime quasicrystal diffraction conjecture**  
   Study renormalized diffraction of weighted prime logarithms.  
   **Initial status:** currently in the wrong geometric category.

6. **Fractal string inverse problem for \(\zeta\)**  
   Seek a canonical fractal object forcing zeta zeros as its complex dimensions.  
   **Initial status:** explanatory rather than proof-producing.

29. **Arakelov Hodge index theorem for \(\operatorname{Spec}\mathbb Z\)**  
   Formulate Weil positivity as an arithmetic intersection/Hodge-index theorem.  
   **Initial status:** philosophically strongest geometric program.

30. **Prismatic cohomology shadow of zeta**  
   Search for a global prismatic-type object with determinant \(\xi\).  
   **Initial status:** visionary but currently remote.

31. **Tropicalization of the explicit formula**  
   Translate primes and zeros into tropical balancing data.  
   **Initial status:** probably too lossy analytically.

32. **Noncommutative polarized Hodge structure on the adèle class space**  
   Supply the positivity missing in Connes’s spectral program.  
   **Initial status:** serious, but foundationally incomplete.

33. **Tensor-category of \(L\)-functions with positivity-preserving convolution**  
   Embed zeta in a family/category where positivity is stable under convolution.  
   **Initial status:** too schematic at present.

34. **Rankin–Selberg square descent**  
   Prove positivity at a larger level and descend it to zeta.  
   **Initial status:** descent step is the real obstacle.

35. **Universal Weil kernel across families**  
   Define a family-level version of Weil’s quadratic form.  
   **Initial status:** plausible for infrastructure, weak for eliminating outliers.

### E. Statistical, geometric, and inverse-problem ideas

7. **Multifractal symmetry of the prime error term**  
   Detect off-line zeros through multifractal asymmetry.  
   **Initial status:** likely poetic reformulation rather than method.

21. **Rigidity upgrade from GUE statistics to exact localization**  
   Try to infer RH from stronger zero-rigidity results.  
   **Initial status:** flawed because ordinate statistics do not determine real parts.

22. **Reverse universality contradiction**  
   Use Voronin universality to contradict off-line zeros.  
   **Initial status:** no credible contradiction mechanism.

36. **Derivative-zero rigidity via Speiser’s theorem**  
   Attack RH through geometry of zeros of \(\zeta'\).  
   **Initial status:** one of the better targeted ideas.

37. **Curvature/winding law for \(\xi(1/2+it)\)**  
   Study geometric behavior of the critical-line trace.  
   **Initial status:** ill-posed in its raw form.

44. **Band-limited Mellin Paley–Wiener theorem for primes**  
   Treat prime logarithms as a sampling set in Mellin space.  
   **Initial status:** likely incompatible with classical sampling density constraints.

45. **Arithmetic compressed sensing viewpoint**  
   Regard primes as sparse measurements of the zero set.  
   **Initial status:** mostly metaphorical.

---

## Numerical Testing & Potential Failures

### 1. What numerical evidence already says

Current computation supports RH very strongly:

- Rigorous verification of enormous zero ranges shows all checked zeros on the critical line.
- All checked zeros are simple.
- Zero spacings at high height closely match GUE predictions.
- The Newman constant is numerically forced extremely close to \(0\) from below.

This evidence is powerful for calibration, but it is not proof. Finite verification cannot exclude a first counterexample at very large height.

### 2. Numerical tests that are meaningful for the speculative ideas

The following test programs are mathematically sensible and could separate promising directions from empty analogies.

#### A. For spectral and scattering models

- Check whether a toy graph/scattering model reproduces:
  - the gamma factor exactly,
  - a finite Euler product exactly,
  - and the correct orbit amplitudes for prime powers.
- Attempt no-go theorems showing that closed self-adjoint graphs cannot realize the needed weights.
- Test whether any proposed spectral determinant reproduces the Riemann–von Mangoldt main term before worrying about finer structure.

#### B. For Nyman–Beurling and wavelet approaches

- Compute Gram matrices in candidate Mellin-wavelet frames.
- Measure whether the new basis significantly reduces long-range correlations.
- Track numerical approximation rates to the constant function \(1\).
- Compare observed rates with known zero-free regions or partial RH-type bounds.

#### C. For de Branges / Sonine / Jacobi ideas

- Truncate Burnol-type spaces and run Lanczos or Jacobi tridiagonalization numerically.
- Examine whether recurrence coefficients stabilize or display hidden positivity.
- Test whether any candidate spectral measure looks positive without smuggling RH into the construction.

#### D. For Li, Hankel, and total-positivity proposals

- Compute large batches of Li coefficients to high precision.
- Test low-order and medium-order Hankel minors.
- Test minors of kernels derived from smoothed Weil forms.
- A single robust numerical failure can kill an overly strong conjecture such as naive Hankel positivity.

#### E. For Newman-flow ideas

- Evolve polynomial or truncated Hadamard approximations under heat deformation.
- Test candidate entropy or Lyapunov functionals numerically.
- Check whether monotonicity persists across truncation scale.
- If a candidate entropy is unstable under truncation, it is probably not canonical enough.

#### F. For Robin and Lagarias routes

- Push exhaustive verification along superabundant and colossally abundant numbers.
- Model extremal exponent profiles and search for monotonic quantities.
- Compare deterministic near-extremizers with probabilistic heuristics.

#### G. For Speiser/derivative-zero ideas

- Compute zeros of \(\zeta'\) at large height with high precision.
- Study local configurations around zeros of \(\zeta\) and \(\zeta'\).
- Search numerically for forbidden patterns that an off-line zero pair would force.

#### H. For SDP/Weil-positivity ideas

- Fix a nested basis of test functions adapted to the functional equation.
- Produce interval-arithmetic-certified semidefinite positivity on growing subspaces.
- Track whether positivity margins remain stable or collapse under basis enlargement.

### 3. The most common failure modes

Across both classical and speculative programs, the same logical pitfalls recur.

#### Failure mode 1: the idea does not control \(\Re(\rho)\)

This is the biggest problem in the entire collection. Many proposals say something about:

- the imaginary parts of zeros,
- local spacing statistics,
- average behavior,
- resonance density,
- or geometric analogies,

without any mechanism that forces every zero to lie on the vertical line \(\Re(s)=1/2\).

This affects, in particular:

- random matrix or Dyson-gas style models,
- GUE rigidity upgrades,
- many dynamical analogies,
- quasicrystal and diffraction proposals.

#### Failure mode 2: replacing RH by a stronger unmotivated conjecture

Several ideas demand statements that are prettier than RH but probably false or at least unmotivated, such as:

- total positivity of a kernel,
- moment-sequence behavior of Li coefficients,
- full Hankel positivity.

A stronger statement is only useful if there is serious evidence it is true.

#### Failure mode 3: assuming the missing object already exists

Some proposals say, in effect:

- “Find the canonical self-adjoint operator,”
- “Find the canonical cohomology theory,”
- “Find the canonical polarized structure,”
- “Find the canonical graph or energy.”

But the existence of exactly such an object is already almost the whole RH problem.

#### Failure mode 4: confusing analogy with mechanism

Fractals, tropical geometry, PT symmetry, compressed sensing, and quasicrystals can be illuminating metaphors. But without a hard implication to an RH-equivalent criterion, they remain metaphors.

#### Failure mode 5: finite-dimensional numerics do not imply infinite-dimensional positivity

This is especially dangerous in:

- SDP attacks on Weil positivity,
- basis-dependent functional-analytic formulations,
- kernel positivity programs.

A proof must bridge the finite-to-infinite gap rigorously.

#### Failure mode 6: probabilistic typicality does not imply deterministic worst-case control

This undermines:

- multiplicative chaos models,
- large-deviation Robin heuristics,
- most probabilistic Möbius arguments.

RH requires a deterministic bound, not “with high probability” behavior.

---

## Critical Assessment

### 1. The most serious long-shot directions

These are the only speculative ideas from the list that presently look like plausible sources of genuine mathematical progress, even though all remain remote from a proof.

#### 2. Global scattering realization of \(\xi\)
- **Strength:** naturally accommodates local Euler factors and the functional equation.
- **Fatal weakness:** scattering resonances are not automatically forced onto the critical line.
- **Assessment:** conceptually serious, technically nowhere near completion.

#### 9. Wavelet/Nyman–Beurling upgrade
- **Strength:** attacks an exact RH-equivalent criterion.
- **Fatal weakness:** may only repackage the same arithmetic obstruction.
- **Assessment:** one of the better infrastructure directions.

#### 11. Sonine/de Branges Jacobi-matrix model
- **Strength:** deeply connected to existing exact Hilbert-space frameworks.
- **Fatal weakness:** positivity/self-adjoint spectral interpretation may already be equivalent to RH.
- **Assessment:** one of the strongest structural ideas.

#### 15. Uniform Jensen-polynomial hyperbolicity
- **Strength:** grows directly from a genuine breakthrough.
- **Fatal weakness:** uniformity in degree and shift is vastly harder than the known theorem.
- **Assessment:** precise, high-value, still a long shot.

#### 17. Entropy monotonicity for Newman flow
- **Strength:** targets the sharp modern reformulation \(\Lambda=0\).
- **Fatal weakness:** endpoint control at \(t=0\) is exactly where the problem lives.
- **Assessment:** serious and difficult.

#### 24. Short-interval nonpretentiousness
- **Strength:** points directly at the Möbius cancellation equivalent to RH.
- **Fatal weakness:** can collapse into tautology if not formulated carefully.
- **Assessment:** promising if sharpened into explicit, weaker-than-RH hypotheses.

#### 29. Arakelov Hodge index program
- **Strength:** matches the shape of successful proofs over function fields.
- **Fatal weakness:** the required theory over \(\operatorname{Spec}\mathbb Z\) does not yet exist.
- **Assessment:** philosophically strongest, practically remote.

#### 32. Noncommutative polarized Hodge structure
- **Strength:** correctly targets the missing positivity in Connes-type approaches.
- **Fatal weakness:** remains foundational rather than operational.
- **Assessment:** serious but long-term.

#### 36. Speiser / derivative-zero route
- **Strength:** targets an exact equivalent of RH.
- **Fatal weakness:** missing deterministic geometry linking an off-line zero to a forbidden derivative-zero pattern.
- **Assessment:** one of the cleanest reformulations and worth sustained attention.

#### 46. SDP attack on Weil positivity
- **Strength:** directly attacks an RH-equivalent criterion and is computationally testable.
- **Fatal weakness:** finite-dimensional positivity is not the theorem.
- **Assessment:** among the best chances for meaningful partial progress.

### 2. Intermediate directions that may produce useful partial results but are unlikely to finish RH alone

These ideas have some mathematical content, but currently lack a realistic path to a complete proof:

- 1. Adelic quantum graph
- 8. Mellin FUP
- 16. Laguerre–Pólya flow
- 19. PDE for \(\xi'/\xi\)
- 23. Möbius multiplicative chaos
- 27. Gauss-map determinant bridge
- 35. Universal Weil kernel across families
- 38. Superabundant-number dynamical flow
- 40. Prime-energy minimization
- 41. Electrostatic mirror principle

Their main value is exploratory: they could produce new lemmas, partial criteria, no-go theorems, or sharper formulations.

### 3. Weak directions: overfitted, too vague, or probably stronger than RH

These proposals are not absurd, but they currently look unlikely to matter for a full proof:

- 4. Almost-periodic Schrödinger operator
- 5. Prime quasicrystal diffraction
- 6. Fractal string inverse problem
- 10. Prime-adic multiresolution
- 12. Total positivity kernel
- 13. Li coefficients as moments
- 14. Hankel positivity for Li coefficients
- 18. Optimal transport of zeros
- 20. Dyson-gas model
- 25. Nilsequence explicit-formula amplification
- 26. Thermodynamic formalism for primes
- 30. Prismatic shadow of zeta
- 33. Tensor category of \(L\)-functions
- 34. Rankin–Selberg square descent
- 39. Large deviations for Robin
- 43. PT-symmetry route

The common issue is that they either:
- impose extra structure with no evidence,
- rely on an undefined canonical object,
- or provide heuristic organization without theorem-level force.

### 4. Likely dead ends as stated

These proposals are currently not credible routes to RH:

- 7. Multifractal symmetry of the prime error term
- 21. Rigidity upgrade from GUE statistics to exact localization
- 22. Reverse universality contradiction
- 28. Hyperbolic surface with lengths \(\log p\)
- 31. Tropicalization of the explicit formula
- 37. Curvature/winding law for \(\xi(1/2+it)\)
- 42. Magnetic quantum graph encoding Möbius signs
- 44. Band-limited Mellin Paley–Wiener theorem for primes
- 45. Arithmetic compressed sensing viewpoint

The reasons are straightforward:
- they do not target the real parts of zeros,
- they are ill-posed,
- or they rely on analogies that do not survive precise scrutiny.

### 5. Cross-cutting judgment

Taken together, the idea set shows a useful pattern:

- The only proposals with real potential are those tied to exact RH criteria:
  - Weil positivity,
  - Nyman–Beurling closure,
  - Speiser’s derivative-zero criterion,
  - Newman flow,
  - or genuinely structural Hilbert-space/cohomology programs.

- Ideas based only on:
  - zero statistics,
  - random matrix behavior,
  - geometric metaphor,
  - or generic inverse-problem language  
  almost never reach the core of RH.

This is the central lesson of the entire exercise.

---

## Recommendations for Next Steps

### 1. Focus on exact RH-equivalent criteria, not loose heuristics

The highest-value directions are those where success would immediately imply RH:

- Weil explicit-formula positivity,
- Nyman–Beurling–Báez-Duarte closure,
- Speiser’s criterion,
- de Bruijn–Newman endpoint analysis,
- Robin/Lagarias extremal arithmetic.

A proposal should be deprioritized unless it clearly interfaces with one of these.

### 2. Prioritize the following research shortlist

If resources are limited, the best speculative directions to pursue are:

1. **SDP / rigorous positivity attack on Weil’s criterion**
2. **Wavelet/Mellin reformulation of Nyman–Beurling**
3. **de Branges / Sonine / Jacobi-matrix constructions**
4. **Uniform Jensen-polynomial hyperbolicity**
5. **Entropy/Newman-flow endpoint analysis**
6. **Speiser/derivative-zero geometry**
7. **Short-interval nonpretentiousness in a non-tautological form**
8. **Arakelov Hodge-index formulations**
9. **Polarized noncommutative-geometric refinements**
10. **Global scattering models, but only with an explicit positivity supplement**

### 3. Build no-go theorems, not only positive conjectures

Negative results are badly needed. In particular:

- prove impossibility results for naive quantum-graph realizations,
- rule out classical hyperbolic surfaces with prime logarithmic length spectra,
- test and likely kill naive Li-Hankel/moment-sequence conjectures,
- clarify when random-matrix or Dyson-gas models cannot constrain \(\Re(\rho)\).

This will save effort and sharpen future proposals.

### 4. Separate short-term, medium-term, and long-term goals

#### Short-term
- Rigorous numerical experiments for Weil positivity and Li/Hankel behavior
- Mellin-wavelet Gram-matrix studies in Nyman–Beurling space
- High-precision computation of zeros of \(\zeta'\)
- Truncated de Branges/Jacobi experiments
- Superabundant-number optimization studies

#### Medium-term
- Analytic closure theorems bridging finite-dimensional positivity to full positivity
- Geometric theorems linking off-line zeros to forbidden \(\zeta'\)-zero patterns
- Explicit implications from short-interval Möbius cancellation to zero-density improvements
- Entropy candidates for Newman flow with stable truncation behavior

#### Long-term
- A genuine Hilbert–Pólya operator or scattering system with positivity
- A viable cohomology/intersection-theoretic framework over \(\operatorname{Spec}\mathbb Z\)
- A polarization principle for noncommutative or adelic spectral realizations

### 5. Use computation strategically, not symbolically

Computation cannot prove RH, but it can do four important things:

- kill bad conjectures quickly,
- detect hidden positivity patterns,
- reveal canonical structures,
- and guide theorem statements.

The strongest computational targets are:

- Weil-kernel positivity on nested bases,
- Li/Hankel and total-positivity tests,
- zero motion under Newman-type flows,
- \(\zeta'\)-zero configuration studies,
- extremal sequences in Robin/Lagarias criteria.

### 6. Maintain high proof-discipline standards

Any serious RH program should be checked against the most common failure modes:

- Does it actually control \(\Re(\rho)\)?
- Is it merely stronger than RH without evidence?
- Does it assume the existence of the key object?
- Is it heuristic or theorem-producing?
- Does finite-dimensional evidence truly pass to the infinite setting?
- Is a probabilistic claim being mistaken for a deterministic one?

This standard should be applied ruthlessly.

---

## Final Conclusion

As of 2026, the Riemann Hypothesis remains open. The deepest accepted progress lies in exact reformulations, partial critical-line results, zero-density theory, modern moment technology, extensive computation, and the de Bruijn–Newman breakthrough \(\Lambda\ge 0\).

The speculative directions explored here vary widely in seriousness. Most fail because they do not genuinely attack the location of every zero. A small core, however, deserves sustained attention:

- Weil positivity,
- Nyman–Beurling structure,
- de Branges/Sonine models,
- Jensen-polynomial uniformity,
- Newman-flow endpoint analysis,
- Speiser/derivative-zero geometry,
- short-interval Möbius nonpretentiousness,
- and long-range structural programs in arithmetic geometry and noncommutative spectral theory.

The honest overall verdict is:

- **There is no accepted proof path in view.**
- **There are a handful of mathematically serious long-shot programs.**
- **Most other ideas are best treated as heuristics, diagnostic tools, or dead ends unless they can be tied to an exact RH-equivalent criterion.**

That is the clearest current state of the problem.