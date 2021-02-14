---
category: ml-research
date: 2021-02-14
emoji: "\u2699\uFE0F"
issue_number: 59
title: DeepMind on JAX
---

_AI lab tooling long read #1:_ DeepMind published a blog post about [using JAX to accelerate their research](https://deepmind.com/blog/article/using-jax-to-accelerate-our-research?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
JAX is a modern take on the NumPy API that “includes an extensible system of composable transformation that help support machine learning research” by taking care of differentiation, vectorization (like abstracting batching away from the researcher), and JIT-compilation (for GPUs and TPUs).
The Python library now underpins many of DeepMind’s recent publications, and they’ve also open-sourced several components of their internal ecosystem on top of JAX: [Haiku](https://github.com/deepmind/dm-haiku?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Optax](https://github.com/deepmind/optax?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [RLax](https://github.com/deepmind/rlax?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Chex](https://github.com/deepmind/chex?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and [Jraph](https://github.com/deepmind/jraph?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (“it’s pronounced _gif_ ”).