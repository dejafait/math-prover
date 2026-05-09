- **Statement of RH.** The Riemann Hypothesis (RH) asserts that every nontrivial zero of the Riemann zeta function  
  \[
  \zeta(s)=\sum_{n\ge1}n^{-s}\quad (\Re s>1),
  \]
  continued meromorphically to \(\mathbb C\), has real part \(1/2\). The nontrivial zeros lie in the critical strip \(0<\Re s<1\); RH says they all lie on the critical line \(\Re s=1/2\).

- **Equivalent formulation via \(\xi(s)\).** RH is equivalent to all zeros of the completed function  
  \[
  \xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
  \]
  being on the line \(\Re s=1/2\). Writing \(\Xi(t)=\xi(1/2+it)\), RH becomes the assertion that all zeros of the entire even function \(\Xi(t)\) are real.

- **Status as of 2026.** RH remains open. No proof or disproof is accepted by the mathematical community, and no claimed proof from recent years has survived expert scrutiny to become standard.

- **Clay Millennium status.** RH is one of the seven Clay Millennium Prize Problems and remains unsolved in 2026; a proof would require a complete, peer-validated argument resolving all standard equivalent formulations.

- **Known zero-free regions.** The strongest classical type of results still give regions near \(\Re s=1\) free of zeros, of the form  
  \[
  \sigma \ge 1-\frac{c}{(\log |t|)^{2/3}(\log\log |t|)^{1/3}}
  \]
  for large \(|t|\), based on Korobov–Vinogradov-type methods. These are far from the line \(\sigma=1/2\).

- **No Siegel zero issue for \(\zeta(s)\).** Unlike Dirichlet \(L\)-functions, \(\zeta(s)\) itself has no exceptional real zero near \(1\); the issue for RH is entirely about the interior of the critical strip.

- **Prime number theorem connection.** RH is much stronger than the prime number theorem. The PNT is equivalent to zero-freeness on \(\Re s=1\); RH would imply the sharp classical error term  
  \[
  \pi(x)=\operatorname{Li}(x)+O(\sqrt{x}\log x).
  \]

- **Best-known unconditional prime-counting error terms remain far weaker than RH.** Modern explicit bounds on \(\psi(x)-x\), \(\theta(x)-x\), and \(\pi(x)-\operatorname{Li}(x)\) continue to improve numerically, but none approach RH-level square-root cancellation in general.

- **Equivalent formulations through arithmetic functions.** RH is equivalent to many statements, such as  
  \[
  M(x)=\sum_{n\le x}\mu(n)=O(x^{1/2+\varepsilon}),
  \]
  \[
  \psi(x)=x+O(x^{1/2}\log^2 x),
  \]
  and the positivity criteria of Li, Weil, and others. These equivalences remain central in current research.

- **Li’s criterion remains an active lens.** RH is equivalent to nonnegativity of the Li coefficients \(\lambda_n\). There has been continued work on asymptotics, numerical behavior, and generalizations of Li-type criteria, but no breakthrough yielding positivity in full generality.

- **de Branges–type approaches continue to attract intermittent attention.** The idea is to place \(\Xi\) or related transforms in a Hilbert space of entire functions where reality of zeros follows from structural positivity. Despite significant technical developments in de Branges theory, no accepted realization has produced RH.

- **Hilbert–Pólya remains a leading philosophical framework.** The conjectural idea is that zeros \(1/2+i\gamma\) arise as eigenvalues of a self-adjoint operator. This is compelling because self-adjoint spectra are real, but no operator with the required spectrum and arithmetic meaning has been found.

- **Spectral/quantum chaos evidence remains strong but nonrigorous.** Statistical behavior of high zeta zeros matches Gaussian Unitary Ensemble (GUE) predictions, reinforcing the Hilbert–Pólya intuition. This evidence is among the strongest heuristic supports for RH, but it does not constitute a proof.

- **Montgomery’s pair correlation conjecture remains central.** Montgomery showed, under restrictions, that pair correlation of zeta zeros agrees with random matrix predictions. This connects RH and zero statistics to quantum chaos and remains one of the deepest structural insights into the zeros.

- **Odlyzko’s computations continue to support GUE statistics.** Large-scale computations of high zeros show agreement with random matrix theory to high precision. These computations are evidence for RH and for refined conjectures on local zero statistics, but not proof.

- **Verification of RH for many zeros.** Extensive computations have verified that very large initial segments of nontrivial zeros lie on the critical line and are simple. The total verified height continues to increase through computational work, though the specific current record depends on the latest implementations and hardware.

- **Computational verification does not scale to proof.** Even if trillions of zeros are checked, this addresses only a finite initial segment; it cannot exclude off-line zeros higher up. The main value of computations is testing conjectures, calibrating explicit formulas, and ruling out low-lying counterexamples.

- **Many zeros are known on the critical line.** Hardy proved infinitely many zeros on \(\Re s=1/2\). The proportion has been steadily improved; a positive proportion of zeros are known to lie on the critical line through mollifier methods.

- **Best proportion-on-the-line results.** The classical landmark is Levinson’s \(>1/3\), improved by Conrey to more than \(2/5\). As of 2026, no accepted proof establishes \(100\%\), and the gap from \(40\%\)-type results to RH remains immense.

- **Positive proportion of simple zeros on the line.** Refinements of mollifier methods also show a positive proportion of zeros on the critical line are simple. Simplicity of all nontrivial zeros is widely believed but remains unproved.

- **Density theorems near the line.** Zero-density estimates show that most zeros are not far from the critical line in averaged senses. Such theorems are powerful for primes in short intervals and related topics, but they fall well short of forcing all zeros onto the line.

- **Selberg’s contributions remain foundational.** Selberg developed deep mean-value methods and showed that a positive proportion of zeros lie on the line. His techniques still underlie many modern refinements.

- **Mollifiers remain a major technical tool.** Modern work studies optimized mollifiers, long mollifiers, and twisted moments to detect zeros on the line and simple zeros. Despite progress, these methods face a “barrier” before reaching full RH.

- **Moments of \(\zeta\) are a major modern route.** Precise asymptotics for moments of \(\zeta(1/2+it)\) and mollified moments are tied to zero distribution. Recent major work on moments has improved understanding, but not enough to force all zeros onto the line.

- **Random matrix theory predicts moment asymptotics.** Keating–Snaith and subsequent work gave precise conjectures for moments and lower-order terms. These predictions agree strikingly with numerics and arithmetic refinements, shaping much recent RH-adjacent research.

- **Short interval and additive divisor methods matter indirectly.** Progress on moments often uses spectral theory, automorphic forms, and additive divisor correlations. These are central to understanding the analytic structure around RH but have not yet yielded a direct proof strategy.

- **The Nyman–Beurling criterion remains significant.** RH is equivalent to a closure property in a certain function space involving approximations to the constant function by fractional part functions. This criterion has inspired functional-analytic work, but proving the required closure remains intractable.

- **Báez-Duarte’s reformulation sharpened Nyman–Beurling.** Discrete versions and criteria involving specific coefficients have provided more concrete computational formulations of RH. They offer elegant equivalences, but no method has emerged to prove the necessary bounds.

- **The Laguerre–Pólya class and Fourier-transform methods remain relevant.** Since \(\Xi\) is an even entire function of order 1, one may try to show it lies in the Laguerre–Pólya class, which would force all zeros to be real. This remains a guiding program but has resisted completion.

- **Pólya’s deformations and the de Bruijn–Newman constant are among the most important modern developments.** One studies heat-flow deformations \(H_t\) of \(\Xi\). There exists a constant \(\Lambda\) such that \(H_t\) has only real zeros iff \(t\ge\Lambda\). RH is equivalent to \(\Lambda\le0\).

- **Rodgers–Tao (2018) was a landmark.** They proved \(\Lambda\ge0\). Combined with Newman's philosophy that \(\Lambda\ge0\) means RH, if true, is “barely true,” this result shows RH is equivalent to the sharp statement \(\Lambda=0\).

- **Current status of \(\Lambda\) in 2026.** The accepted state remains \(0\le \Lambda \le\) a small explicit positive number from numerical work. There have been further numerical refinements and upper bounds, but no proof that \(\Lambda=0\).

- **Numerical work on \(\Lambda\) continues.** Refinements by Saouter, Gourdon, Demichel and others have produced very small explicit upper bounds on \(\Lambda\), dramatically narrowing the allowable range. These results are among the strongest quantitative evidence for RH.

- **What the de Bruijn–Newman work does not do.** Even proving \(\Lambda\) is tiny and positive would disprove RH, but present methods do not determine the exact sign. The barrier is that numerical and local zero-spacing methods do not control the global deformation parameter exactly.

- **Weil’s explicit formula remains a core bridge.** It relates sums over zeros to sums over primes via test functions. Much of modern RH-adjacent work—positivity criteria, trace formulas, and spectral analogies—flows from this formula.

- **Weil positivity criterion.** RH is equivalent to positivity of certain quadratic forms built from test functions and the explicit formula. This is conceptually powerful and tied to Hilbert-space ideas, but positivity for the full class of test functions remains inaccessible.

- **Connes’ noncommutative geometry program remains influential.** Connes proposed a spectral interpretation of zeros through noncommutative spaces, trace formulas, and an absorption spectrum viewpoint. It remains profound and suggestive, but has not produced a complete proof of RH.

- **Deninger’s cohomological program is still a major conceptual framework.** Deninger sought analogues of Weil’s proof of the Riemann hypothesis for function fields by building a cohomological/dynamical theory for \(\mathrm{Spec}(\mathbb Z)\). This has inspired broad research, but key objects remain conjectural.

- **Function-field analogies remain one of the strongest guides.** For zeta functions of curves over finite fields, Weil proved the analogue of RH using algebraic geometry and the Frobenius action on étale cohomology. Many modern approaches seek an arithmetic-geometric structure over the integers that would play a similar role.

- **Why function-field methods do not directly transfer.** Over finite fields one has an actual Frobenius endomorphism and finite-dimensional cohomology with positivity structures; for \(\zeta(s)\) over \(\mathbb Q\), no comparably robust cohomology theory or operator has been constructed.

- **Automorphic and trace-formula approaches continue.** Since the zeta function is the \(L\)-function of the trivial automorphic representation of \(\mathrm{GL}_1\), researchers investigate whether trace formulas or beyond-endoscopy ideas might isolate zeros spectrally. No accepted route to RH has emerged.

- **The resonance method informs extremal behavior, not RH directly.** Work of Soundararajan and many successors studies large and small values of \(\zeta(1/2+it)\), revealing rich structure tied to zeros and moments. These methods illuminate the critical line but do not currently control off-line zeros.

- **Pretentious multiplicative function theory has changed nearby fields more than RH itself.** Granville–Soundararajan’s framework gives powerful tools for mean values of multiplicative functions and related prime questions. It has not yet yielded a decisive attack on RH, though it clarifies limitations of purely multiplicative arguments.

- **Universality results cut both ways.** Voronin universality shows that shifts of \(\zeta(s)\) in the strip \(1/2<\Re s<1\) approximate broad classes of analytic functions. This demonstrates the function’s flexibility in the right half of the strip and is often viewed as evidence that direct complex-analytic arguments proving RH may be very difficult.

- **The argument principle and explicit Turing-type methods are now highly developed.** These methods rigorously verify zero counts and certify that all zeros in large computational ranges lie on the line. They are indispensable in computations but do not address asymptotic infinity.

- **Large-scale computations also support simplicity.** Numerically, all checked zeros are simple, and local spacing statistics agree with random matrix predictions. A proof that all zeta zeros are simple would still be weaker than RH and remains unavailable.

- **There are conditional advances assuming RH that shape the field.** Under RH one gets major improvements in prime gaps, divisor problems, class number estimates, and bounds for arithmetic sums. The breadth of such consequences is one reason RH remains a central benchmark across number theory.

- **There are also results showing RH is “almost true” in various senses.** For example, “almost all” zeros satisfying the hypothesis in density or pair-correlation settings, or many zeros on the line, but none of these statements bridge the qualitative gap to all zeros.

- **One major obstacle: lack of a positivity mechanism.** Successful proofs of RH analogues usually rely on a positivity principle—intersection theory, self-adjointness, or a trace/cohomology pairing. For \(\zeta(s)\), no such rigorously defined structure has been found that produces the zeros.

- **Second major obstacle: limitations of complex-analytic estimates.** Classical tools—Hadamard products, Jensen formulas, zero-density estimates, mean values—yield strong averaged information but are not fine enough to force every zero onto one line.

- **Third major obstacle: mollifier and moment barriers.** Existing methods detect many zeros on the line but become increasingly intricate and appear unable, in their current form, to reach \(100\%\). The obstacle is both technical and conceptual, tied to inaccessible higher moments and off-diagonal correlations.

- **Fourth major obstacle: no arithmetic operator with the right spectrum.** The Hilbert–Pólya idea is attractive, but nobody has identified a natural self-adjoint operator whose eigenvalues are the ordinates \(\gamma\) of zeta zeros and whose spectral data matches the explicit formula with primes.

- **Recent literature continues to be rich but fragmented.** In the early-to-mid 2020s, there has been sustained output on zero statistics, moments, de Bruijn–Newman bounds, explicit zero verification, Li coefficients, Nyman–Beurling criteria, and spectral analogies, but no single program has clearly overtaken the field as the dominant path to proof.

- **Best way to interpret the present state.** As of 2026, the strongest evidence for RH comes from: (i) vast numerical verification of zeros on the line; (ii) de Bruijn–Newman bounds placing \(\Lambda\) in a tiny interval containing \(0\); (iii) random matrix/statistical agreement; and (iv) the absence of any credible mechanism producing off-line zeros.

- **Most credible long-term proof avenues discussed by experts.** The commonly cited serious directions are: a Hilbert–Pólya spectral construction; a Deninger/Connes-style cohomological or dynamical trace formula; a de Branges/Laguerre–Pólya positivity framework; or a radically new synthesis of explicit formula, automorphic spectral theory, and positivity. None is close to completion.

- **Key classical references.** B. Riemann (1859); J. Hadamard and C. de la Vallée Poussin on zero-free line and PNT; G.H. Hardy (1914) infinitely many zeros on the critical line; A. Selberg; N. Levinson (1974); J.B. Conrey (1989) on \(>2/5\) of zeros on the line; H.M. Edwards, *Riemann’s Zeta Function*; E.C. Titchmarsh revised by D.R. Heath-Brown, *The Theory of the Riemann Zeta-Function*.

- **Key modern references and landmarks.** H.L. Montgomery (pair correlation, 1973); A.M. Odlyzko (large-scale zero computations); A. Connes (trace formula/noncommutative geometry); C. Deninger (cohomological formalism); L. de Branges (Hilbert spaces of entire functions); C.M. Newman and N.G. de Bruijn; B. Rodgers and T. Tao (2018, \(\Lambda\ge0\)); J.P. Keating and N.C. Snaith (random matrix moment conjectures); Granville–Soundararajan (pretentious methods); surveys by Conrey, Sarnak, Bombieri, Iwaniec–Kowalski, and Soundararajan–Young.

- **Practical conclusion for 2026.** There is no accepted proof, no accepted disproof, and no consensus that any current technical line is near resolution. The field has deepened substantially—especially in zero statistics, de Bruijn–Newman theory, and computational verification—but RH remains one of the most resistant problems in mathematics.