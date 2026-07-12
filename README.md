# Is-It-Prime

[English](./README.md) · [中文](./wiki/README_zh.md)

> How can we quickly tell whether a number is prime?

For over two thousand years, people have wrestled with a deceptively simple question: given an integer $n$, how can we quickly determine whether it's prime? (eg. n = 170141183460469231731687303715884105727)

![Is-It-Prime](./wiki/2026-07-05%2019.25.14.png)

### Trial Division: The Most Naive Approach

The oldest method is to try dividing $n$ by every number smaller than it and see if any of them divide evenly. It's about as naive as it gets, but it also leaves obvious room for optimization—for instance, you can rule out all even numbers and multiples of 3 up front, only checking candidates of the form $6k \pm 1$ (this is sometimes called the "6k optimization").

We can push further: there's no need to test every number smaller than $n$. If $n$ has a factor greater than $\sqrt{n}$, it must pair with a corresponding factor smaller than $\sqrt{n}$—factors always come in pairs. So it's enough to check up to $\sqrt{n}$, bringing the overall time complexity down to $O(\sqrt{n})$.

### The Rise of RSA: Why Primality Testing Suddenly Became a Big Deal

The security of the RSA public-key cryptosystem rests on the difficulty of factoring large numbers:

$$n = p \times q$$

Pick two large primes $p$ and $q$, multiply them to get $n$—this step is **fast**. But going the other way, given only $n$, recovering $p$ and $q$ has no known efficient classical algorithm. This assumption—that factoring large integers is hard—is the very foundation RSA's security is built on.

That's exactly why primality testing suddenly mattered so much: $p$ and $q$ have to actually be prime (otherwise $n$ can be factored easily and the encryption breaks), and they need to be found *efficiently*. Even the optimized $O(\sqrt{n})$ trial division is hopeless once you're dealing with primes hundreds of digits long.

With the arrival of RSA, "is this number prime?" stopped being a purely academic curiosity and became a question the real world urgently needed answered.

### Fermat's Little Theorem: The First Efficient (but Imperfect) Test

Fermat's Little Theorem is one of the earliest and most important results in number theory.

> Before diving in, a quick note on notation you'll see repeatedly: $\equiv$ means "congruent to" for modulo, not "equal to."
>
> $$b^m \equiv b \pmod{m}$$
>
> This doesn't mean $b^m$ and $b$ are the same value—it means $b^m$ and $b$ leave **the same remainder** when divided by $m$.

The full statement of Fermat's Little Theorem is: if $p$ is prime and the integer $a$ is coprime to $p$ (written $\gcd(a, p) = 1$), then:

$$a^{p-1} \equiv 1 \pmod{p}$$

Equivalently, for any integer $a$:

$$a^{p} \equiv a \pmod{p}$$

What a primality test actually needs is the contrapositive: if there exists some $a$ satisfying the equation below, then $n$ is definitely not prime.

$$a^{n-1} \not\equiv 1 \pmod{n}$$

So for an unknown integer $n$, it's natural to flip this property around and use it as a test.

Given a candidate $n$, randomly pick several values of $a$ and check whether $a^{n-1} \bmod n$ equals $1$:

- If some $a$ satisfies $a^{n-1} \not\equiv 1 \pmod n$, then $n$ is **definitely composite**.
- If $a^{n-1} \equiv 1 \pmod n$ holds for every $a$ tested, then $n$ is **probably** prime.

Thanks to fast modular exponentiation, a single check only takes $O(\log n)$ multiplications—far more efficient than trial division.

#### A Probabilistic Algorithm

**Why only "probably"?** Because there's a class of composite numbers $n$ for which *every* integer $a$ coprime to $n$ satisfies:

$$a^{n-1} \equiv 1 \pmod{n}$$

In other words, these numbers fool the Fermat test no matter which base you throw at them. They're called **Carmichael numbers**, the smallest being $561$. Worse still, although sparse, they've been proven to be **infinite in number**. This means the Fermat test can, in principle, never be more than a **probabilistic algorithm**.

### Miller–Rabin (1976): Closing the Loophole

Miller–Rabin builds on the Fermat test by additionally checking for nontrivial modular square roots of 1, closing the loophole that Carmichael numbers exploit.

> First, a bit of background on **modular square roots**:
>
> If $p$ is prime and $a$ is any integer with $a^2 \equiv 1 \pmod{p}$, then either $a = 1$ or $a = p - 1$.
>
> Here's an example: with $p = 7$, take $a = 1$: $a^2 = 1$, which mod 7 is 1. Take $a = 7 - 1 = 6$: $a^2 = 6^2 = 5 \times 7 + 1$, which mod 7 is again 1. But for other values, say $a = 4$: $a^2 \bmod 7 = 2$, not 1. So only $a = 1$ and $a = 6\ (= p - 1)$ satisfy the condition.

**Why is this property so useful?**

If $p$ is an odd prime and $a$ is coprime to $p$, Fermat's Little Theorem tells us $a^{p-1} \equiv 1 \pmod{p}$. Since $p$ is odd, $p - 1$ is even, so we can write $p - 1 = 2k$, giving us:

$$a^{2k} \equiv 1 \pmod{p}$$

This means $a^k$ is a modular square root of $1$. And by the property above, the only square roots of $1$ are $\pm 1$, so:

$$a^k \equiv 1 \pmod{p} \quad \text{or} \quad a^k \equiv -1 \pmod{p}$$

**The core insight of Miller–Rabin**: if $a^k$ turns out to be neither $1$ nor $-1$, the modulus can't be prime—because in the world of primes, there's no such thing as an "unexpected" square root.

Now let's apply this to the actual candidate $n$ we're testing. For odd $n > 2$, write $n - 1$ as:

$$n - 1 = 2^s \times d, \quad d \text{ odd}$$

Then, starting from $a^d$, repeatedly square to compute the sequence:

$$a^d,\ a^{2d},\ a^{4d},\ \ldots,\ a^{2^{s-1}d}$$

Check this sequence: if some term equals $1$, look at the term right before it—it must be $\pm 1$. If it isn't, then $n$ has an "unexpected" square root of $1$, and $n$ must be composite.

Putting it together, $n$ passes the test with witness $a$ if and only if:

$$a^d \equiv 1 \pmod n \quad \text{or} \quad a^{2^i d} \equiv -1 \pmod n \ \text{for some } 0 \le i < s$$

#### A Probabilistic Algorithm

For a composite $n$, the probability that a randomly chosen $a$ makes $n$ **pass** the test (i.e., $a$ is a "liar") is **at most $1/4$**. Repeating the test independently $k$ times (typically $k = 40$) drives the error rate down to:

$$\left(\frac{1}{4}\right)^{40} \approx 10^{-24}$$

That's more than reliable enough in practice, and it's the default algorithm used by industry (e.g., OpenSSL) for generating large primes. But fundamentally, Miller-Rabin is still a **probabilistic algorithm**—it can't offer a 100% certain proof.

### AKS (2002): Finally, a Deterministic Algorithm

In August 2002, Manindra Agrawal, Neeraj Kayal, and Nitin Saxena published *PRIMES is in P*, presenting the first **deterministic** primality test that doesn't rely on any unproven conjecture and runs in polynomial time with respect to the number of digits of $n$—finally settling a question that had stood open for over two thousand years.

#### The Starting Point: Extending Fermat's Little Theorem to Polynomial Rings

$$(x + a)^p \equiv x^p + a \pmod{p}, \qquad \gcd(a, p) = 1,\ p \text{ prime}$$

This is essentially Fermat's Little Theorem, $a^p \equiv a \pmod p$, lifted to the polynomial level—replacing $a$ with $x + a$.

**Necessity** ($p$ prime $\Rightarrow$ the identity holds): This follows directly from the binomial theorem—when $p$ is prime, every binomial coefficient $\binom{p}{k}$ for $0 < k < p$ is divisible by $p$, so all the middle terms in the expansion of $(x+a)^p$ vanish, leaving just $x^p + a^p \equiv x^p + a \pmod p$.

**Sufficiency** (the identity holds $\Rightarrow$ the number is prime): The converse holds too. Agrawal et al. proved this reverse direction as well.

But verifying it directly is far too costly: you'd need to check every value of $a$, and expanding $(x+a)^n$ produces $n$ terms—an exponential blowup. This is exactly the problem AKS needed to solve next.

#### The Key Improvement: Why Reduce Modulo $x^r - 1$

The cleverness of AKS is that **you don't need to check the full identity for every $a$**. Specifically, you pick a suitable $r$, which serves two purposes:

1. It's used to construct a smaller quotient ring, compressing polynomials of degree as high as $n$ down to degree at most $r$;
2. It's used to compute an upper bound on the values of $a$ that need checking: $L = \left\lfloor \sqrt{r} \cdot \log_2 n \right\rfloor$.

You only need to verify a **small range** of values of $a$ against:

$$(x + a)^n \equiv x^n + a \pmod{x^r - 1,\ n}$$

By reducing modulo $x^r - 1$, the degree of every polynomial is capped at $r$ (this essentially turns exponentiation into cyclic convolution). A single check now costs $\tilde{O}(r)$ modular coefficient multiplications instead of an exponential amount, bringing the whole algorithm into polynomial time.

#### Choosing $r$

> Before explaining how $r$ is chosen, let's define the **multiplicative order**.
>
> For an integer $n$ coprime to $r$, keep raising $n$ to successive powers—$n^1, n^2, n^3, \ldots$—and reduce each modulo $r$. Since the multiplicative group is finite, these remainders are guaranteed to eventually cycle back to $1$. The **smallest** exponent at which this first happens is called the multiplicative order of $n$ modulo $r$, written $\text{ord}_r(n)$.
>
> Example: $r = 5$, $n = 7$. First reduce $7 \bmod 5 = 2$, then look at powers of $2$: $2^1 = 2, 2^2 = 4, 2^3 = 8 \equiv 3, 2^4 = 16 \equiv 1 \pmod 5$. It takes 4 steps to get back to 1, so $\text{ord}_5(7) = 4$.

$r$ needs to satisfy: the **order** of $n$ modulo $r$ is large enough:

$$\text{ord}_r(n) > (\log_2 n)^2$$

It can be proven that such an $r$ always exists, with an upper bound of:

$$r = O(\log^5 n)$$

So the algorithm simply tries $r = 2, 3, 4, \ldots$ in order, checking $\text{ord}_r(n) > (\log_2 n)^2$ each time, and stops at the first $r$ that satisfies the condition. This search adds negligible cost to the overall complexity.

#### The AKS Algorithm, Step by Step

1. Is $n$ a perfect power? → Yes: $n$ is composite, done.
2. Starting from $r = 2$, search upward:
   - Check $\gcd(n, r)$ first—if it turns up a nontrivial factor → $n$ is composite, done;
   - Otherwise check whether $\text{ord}_r(n) > (\log_2 n)^2$; once satisfied, stop searching and keep this $r$.
3. Using this $r$, compute the upper bound for $a$: $L = \lfloor \sqrt{r} \cdot \log_2 n \rfloor$.
4. For $a$ from 1 to $L$, check each one against $(x+a)^n \equiv x^n + a \pmod{n,\ x^r-1}$:
   - If any $a$ fails the check → $n$ is composite, done.
5. If every $a$ passes → $n$ is prime.

### Closing Thoughts

From trial division to Fermat, to Miller–Rabin and finally AKS, the story of primality testing has always revolved around two competing goals: speed and certainty. In practice, engineers almost always reach for the faster Miller–Rabin test. AKS's significance is mostly theoretical—it proved that primality can be determined deterministically in polynomial time, making it a landmark result in computational complexity theory.