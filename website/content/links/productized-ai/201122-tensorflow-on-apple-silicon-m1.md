---
category: productized-ai
date: 2020-11-22
emoji: "\U0001F34E"
issue_number: 53
title: TensorFlow on Apple Silicon M1
---

[Apple has forked TensorFlow 2](https://blog.tensorflow.org/2020/11/accelerating-tensorflow-performance-on-mac.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to optimize it for their new crazy-fast M1 Macs!
This came as a pretty big surprise, and it makes the new M1 Macs even more attractive to ML developers: for the first time, this’ll enable using the internal GPU to train TensorFlow models on Mac laptops, leadings to ~5x speedups (!) compared to the previous generation.
I’ll probably hold until for the next generation — by which time Apple’s optimizations should also be upstreamed to the main TensorFlow branch instead of only being available on their own fork — but it’s clear that even now these laptops are already huge game changers.