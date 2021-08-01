---
category: ml-research
date: 2021-08-01
emoji: "\u2699\uFE0F"
issue_number: 71
title: OpenAI Triton
---

[OpenAI has released v1.0 of Triton](https://openai.com/blog/triton?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), its Python-like GPU programming language for neural networks.
“Triton makes it possible to reach peak hardware performance with relatively little effort; for example, it can be used to write FP16 matrix multiplication kernels that match the performance of cuBLAS—something that many GPU programmers can’t do—in under 25 lines of code.
Our researchers have already used it to produce kernels that are up to 2x more efficient than equivalent Torch implementation.” It’s interesting to see how many different intermediate languages have popped up in recent years — [JAX](https://github.com/google/jax?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [MLIR](https://mlir.llvm.org?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) are the other big ones — that sit somewhere between the abstraction level of frameworks (TensorFlow/PyTorch) and of bare-metal GPU languages (CUDA), all trying to find an architectural balance in what bits to keep flexible and what bits to abstract away from developers.
I always find it very hard to estimate which of these things are going to be mainstream and which will mostly be used as “glue” by framework- and low-level language builders.
I guess time will tell.
Triton is available on GitHub at [openai/triton](https://github.com/openai/triton?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).