- **Statement of RH.** The Riemann Hypothesis (RH) asserts that every nontrivial zero of the Riemann zeta function \(\zeta(s)\) has real part \(1/2\). Equivalently, all zeros in the critical strip \(0<\Re s<1\) lie on the critical line \(\Re s=1/2\).

- **Why RH matters.** RH is central because it gives near-optimal error terms in the distribution of primes and controls many arithmetic quantities through explicit formulas linking zeros of \(\zeta(s)\) to prime counting functions.

- **Classical equivalent formulations.** Standard equivalents include: sharp bounds for the Mertens/prime counting error terms; \(M(x)=O(x^{1/2+\varepsilon})\) for the Möbius summatory function; \(\psi(x)=x+O(x^{1/2}\log^2 x)\); and certain growth estimates for \(\zeta(s)\), \(\xi(s)\), and related Mellin transforms.

- **Current consensus in 2026.** RH remains unproved and unrefuted. There is no broadly accepted proof, and no claimed proof from 2020–2026 has survived expert scrutiny to become part of the literature as a settled theorem.

- **Status of numerical verification.** Extensive computations continue to verify that very large numbers of initial nontrivial zeros lie on the critical line and are simple. These computations strongly support RH but do not constitute a proof. Large-scale verifications rely on Turing’s method, Odlyzko–Schönhage-type algorithms, interval arithmetic, and rigorous certification.

- **Simplicity of zeros numerically.** All zeros checked numerically to very high height are simple. This supports the “simple zeros conjecture,” often studied alongside RH, but simplicity also remains unproved in general.

- **Hardy’s theorem remains foundational.** Hardy (1914) proved infinitely many zeros lie on the critical line. This was the first major positive result toward RH and remains a cornerstone.

- **Positive proportion results.** Levinson proved more than one-third of zeros lie on the critical line, and Conrey improved this to more than two-fifths. No unconditional improvement beyond Conrey’s proportion has been universally accepted as of 2026.

- **Density theorems off the line.** Zero-density estimates show that not too many zeros can lie far from the critical line. These are powerful in applications to primes in short intervals and arithmetic progressions but fall far short of RH.

- **Vinogradov–Korobov zero-free region.** The strongest classical unconditional zero-free region near \(\Re s=1\) remains of Vinogradov–Korobov type:
  \[
  \sigma \ge 1 - \frac{c}{(\log |t|)^{2/3}(\log\log |t|)^{1/3}},
  \]
  for large \(|t|\). This is vastly weaker than RH but central in prime number theory.

- **De la Vallée Poussin and the PNT.** The prime number theorem follows from the fact that \(\zeta(s)\neq 0\) on \(\Re s=1\). This historic result remains the prototype of how zero-free regions imply prime distribution results.

- **Best unconditional prime gap consequences remain limited.** Without RH, one still obtains weaker bounds on prime gaps and error terms than under RH. Many conditional theorems in analytic number theory explicitly assume RH or GRH for their sharpest form.

- **GRH context.** The Generalized Riemann Hypothesis (GRH) extends RH to Dirichlet \(L\)-functions and, more broadly, automorphic \(L\)-functions. Most modern work treats RH as one case of a larger \(L\)-function zero problem.

- **Function field analogue is solved.** For zeta functions of curves over finite fields, the analogue of RH was proved by Weil. More generally, Deligne’s proof of the Weil conjectures is the model of a successful RH-type theorem, but its geometric tools do not presently transfer to the classical zeta function over \(\mathbb{Q}\).

- **Hilbert–Pólya remains a leading philosophical approach.** The idea is to realize zeros as eigenvalues of a self-adjoint operator, which would force them onto the critical line. This remains inspirational but incomplete: no accepted operator with the correct spectrum for \(\zeta(s)\) is known.

- **Berry–Keating program.** The Berry–Keating conjectural Hamiltonian \(H=xp\) and related semiclassical ideas attempt to explain the zero statistics and explicit formula. These ideas remain influential, especially in mathematical physics, but have not produced a proof.

- **Random matrix theory (RMT) evidence.** Montgomery’s pair correlation conjecture and Odlyzko’s computations strongly support GUE statistics for high zeta zeros. Katz–Sarnak philosophy extends this to families of \(L\)-functions. This is among the strongest heuristic evidence for RH-like behavior, but it does not prove RH.

- **Keating–Snaith moment conjectures.** Conjectures for moments of \(\zeta(1/2+it)\) derived from RMT remain a major guide. They fit known data and connect to deep arithmetic factors, but even proving the exact asymptotics of higher moments is open.

- **Selberg class / converse-theorem viewpoint.** RH is often studied in the broader setting of \(L\)-functions satisfying analytic continuation, functional equation, Euler product, and Ramanujan-type conditions. Progress here clarifies what structural input might force zeros onto the line, but no general criterion is known.

- **Li’s criterion remains equivalent, not a proof.** RH is equivalent to positivity of the Li coefficients. This has inspired numerical work and explicit inequalities, yet no method has proved positivity for all coefficients in a way yielding RH.

- **Nyman–Beurling criterion.** RH is equivalent to a closure problem in certain \(L^2\) spaces involving fractional part functions. Báez-Duarte sharpened aspects of this framework. It provides a beautiful functional-analytic reformulation, but the key closure estimate remains out of reach.

- **de Branges approach.** de Branges developed Hilbert spaces of entire functions and proposed several routes to RH over decades. These ideas yielded important analysis but have not led to an accepted proof of RH; claimed proofs in this circle have not convinced the expert community.

- **Lagarias criterion.** RH is equivalent to an elementary-looking inequality involving the divisor sum \(\sigma(n)\) and harmonic numbers. This is conceptually striking but has not led to decisive new progress on RH itself.

- **Robin’s theorem and superabundant numbers.** RH is equivalent to Robin’s inequality \(\sigma(n)<e^\gamma n\log\log n\) for all \(n>5040\). Recent work continues to test Robin-type inequalities on special integer sequences and abundant/superabundant/colossally abundant numbers, but no proof or counterexample has emerged.

- **Möbius randomness and RH.** Strong forms of cancellation in the Möbius function, such as square-root cancellation in partial sums, are tightly connected to RH. The modern “Möbius disjointness” program (Sarnak) is related philosophically, though not equivalent in its standard form.

- **Pretentious multiplicative number theory.** Granville–Soundararajan’s pretentious framework has transformed understanding of multiplicative functions and can reprove or sharpen many classical results. However, it has not yet supplied a route to RH; it seems better adapted to average results and structure theorems than to locating every zeta zero.

- **Resonance method and extreme values.** Work by Soundararajan, Bondarenko–Seip, Heap and others on large values of \(\zeta(1/2+it)\) and resonators deepens understanding of the critical line. These methods reveal complex behavior of \(\zeta\) but currently do not constrain zeros strongly enough to prove RH.

- **Universality is a conceptual obstacle.** Voronin universality shows that \(\zeta(s)\) in the strip can approximate many analytic functions. This flexibility suggests that \(\zeta\) may be too wild for naive positivity or monotonicity arguments and is one reason many simple-looking approaches fail.

- **No obvious positivity principle.** Unlike in the Weil/Deligne finite-field setting, the classical \(\zeta(s)\) lacks a known cohomological interpretation yielding positivity and spectral bounds. This absence is one of the deepest conceptual obstacles.

- **The Euler product is only conditionally useful in the critical strip.** The Euler product converges only for \(\Re s>1\), so using “prime-side positivity” directly in the critical strip is highly nontrivial. Many failed proofs incorrectly manipulate divergent products or logarithms there.

- **Explicit formula methods are powerful but insufficient.** The Riemann–von Mangoldt formula and explicit formulas connect zeros and primes exquisitely. Yet they allow many zero configurations compatible with current unconditional estimates; they do not by themselves isolate the critical line.

- **The argument principle plus computation is robust but limited.** Modern verification combines the Riemann–Siegel formula, Turing’s method, and interval arithmetic to count zeros exactly in large height ranges. This confirms RH up to enormous finite heights but cannot bridge the infinite tail.

- **Recent computational work remains active through 2026.** Ongoing projects continue refining certified zero tabulations, checking pair correlation, spacing statistics, and simplicity at increasing heights. The trend is toward more rigorous, formally verified, and high-performance computation, rather than toward a proof strategy.

- **Improved understanding of low-lying zeros in families.** Through 2020–2026, work on one-level density, symmetry type, and low-lying zeros of families of automorphic \(L\)-functions continued to support the Katz–Sarnak picture. This is major progress in the broader RH ecosystem, though not direct progress on RH for \(\zeta\).

- **Subconvexity and RH are different scales of difficulty.** Major advances in subconvexity for automorphic \(L\)-functions show deep control of \(L\)-values, but these estimates are still much weaker than the pointwise and zero-location conclusions implied by RH.

- **Lindelöf Hypothesis remains open.** RH implies the Lindelöf Hypothesis, which predicts \(\zeta(1/2+it)\ll_\varepsilon |t|^\varepsilon\). Considerable progress on moments and bounds has occurred, but Lindelöf remains unproved, highlighting how far current methods are from RH.

- **Large gaps and small gaps between zeros.** Research on normalized zero spacings, including results conditional on RH and unconditional average statements, has progressed. Statistical properties fit RMT, but such spacing information has not translated into full zero-line localization.

- **The de Bruijn–Newman constant \(\Lambda\).** RH is equivalent to \(\Lambda\le 0\); Newman showed \(\Lambda\) exists, and Rodgers–Tao proved \(\Lambda\ge 0\), implying RH, if true, is “barely true.” Numerical work places increasingly tight upper bounds near \(0\). This is one of the deepest structural results related to RH in recent decades.

- **Meaning of Rodgers–Tao.** The theorem \(\Lambda\ge 0\) does not prove RH, but it shows the heat-flow deformation of the xi function cannot become hyperbolic significantly before time \(0\). It transformed understanding of RH’s stability and sharpened the sense that proving RH requires exceptionally delicate structure.

- **There has been no accepted breakthrough on \(\Lambda\le 0\).** Through 2026, numerical and theoretical work continues to narrow bounds and study deformations, but the decisive inequality equivalent to RH remains unresolved.

- **Zero repulsion and Lehmer pairs matter.** Near-colliding zeros (“Lehmer pairs”) are linked to lower bounds on the de Bruijn–Newman constant and to the instability of hyperbolicity. Their study has intensified the view that zeta zeros can behave in an extremely delicate way, complicating proof attempts.

- **Autocorrelation and ratios conjectures.** The Conrey–Farmer–Keating–Rubinstein–Snaith ratios conjectures and related formulas predict fine correlations among zeros and values. These give remarkably accurate heuristics, but remain conjectural and do not provide a rigorous route to RH.

- **Trace formulas and spectral analogies.** Selberg’s trace formula proves RH analogues for Selberg zeta functions in geometric settings because zeros correspond to spectral data of the Laplacian. This remains a strong source of analogy, but no trace formula of comparable power for the classical \(\zeta(s)\) over \(\mathbb{Q}\) is known.

- **Noncommutative geometry approach.** Connes proposed a spectral/noncommutative framework interpreting the explicit formula as a trace formula. It has profoundly influenced the conceptual landscape, but as of 2026 it has not yielded a proof accepted by the number theory community.

- **Arithmetic statistics and RH heuristics.** Developments in arithmetic statistics, especially over function fields and in families of \(L\)-functions, continue to reinforce the expectation that zero distributions are governed by symmetry principles. These advances offer strong indirect support but not a direct attack on RH.

- **Machine-assisted and formal methods are increasing.** Recent years have seen more computer-verified inequalities, interval arithmetic proofs, and formalization efforts around zeta computation and zero counting. These improve trust in numerical evidence and local arguments, but there is no computer-assisted proof of RH.

- **Common failure mode in claimed proofs.** Most alleged proofs mishandle analytic continuation, interchange infinite sums/products illegitimately, assume positivity where none exists, or infer global zero information from finite computations. Expert vetting remains essential.

- **Key obstacle: controlling sign/cancellation globally.** RH can be reformulated as square-root cancellation in several arithmetic sums. Current methods, even the strongest exponential sum and bilinear-form techniques, do not uniformly achieve this level of cancellation across the full range needed.

- **Key obstacle: no spectral object with the right arithmetic.** The Hilbert–Pólya dream needs a self-adjoint operator whose spectrum matches the zeros and whose trace formula matches the primes. Constructing such an object with both the correct local factors and global functional equation remains completely open.

- **Key obstacle: zeros are a global phenomenon.** Many techniques localize in \(t\), average over families, or prove density results. RH requires pointwise control for every zero at every height, a leap beyond the reach of current averaging methods.

- **Most credible active directions in 2026.** The research front is not centered on one imminent proof strategy; rather it is spread across: spectral/Hilbert–Pólya ideas, de Bruijn–Newman analysis, random matrix and integrable structures, refined zero-density estimates, moments and ratios conjectures, Nyman–Beurling-type reformulations, and high-rigor computation.

- **What would count as significant progress now.** Experts would view as major advances any of the following: an unconditional improvement beyond the \(2/5\) critical-line proportion; a genuinely new zero-free region mechanism; a canonical self-adjoint operator producing the zeta zeros; decisive progress on the de Bruijn–Newman constant; or a new positivity/cohomological framework over \(\mathbb{Q}\).

- **Best short conclusion for 2026.** RH remains one of mathematics’ central open problems. The evidence for truth is overwhelming from computation, statistics, and structural analogies, but the main obstacle is not lack of data: it is the absence of a mechanism forcing all zeros onto the critical line.

- **Core classical references.** B. Riemann (1859); G.H. Hardy (1914); A. Selberg; N. Levinson (1974); J.B. Conrey (1989); H. Montgomery (pair correlation, 1973); A. Odlyzko (large-scale computations); E.C. Titchmarsh, revised by D.R. Heath-Brown, *The Theory of the Riemann Zeta-Function*; H.M. Edwards, *Riemann’s Zeta Function*.

- **Core modern references and surveys.** P. Sarnak surveys on RH and randomness; J.B. Conrey, “The Riemann Hypothesis” (notable survey); A. Ivić on \(\zeta(s)\); Soundararajan and Harper on moments and extreme values; Granville–Soundararajan on pretentious methods; Rodgers–Tao on the de Bruijn–Newman constant; Katz–Sarnak on random matrices and families; de Branges’ monographs for the Hilbert-space approach; Báez-Duarte and subsequent work on Nyman–Beurling.