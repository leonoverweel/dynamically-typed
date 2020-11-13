---
category: ml-research
date: 2020-05-24
emoji: "\U0001F4E3"
issue_number: 40
title: Data echoing for improved training speed
---

Google also proposed a new optimization technique: [speeding up neural network training with data echoing](https://ai.googleblog.com/2020/05/speeding-up-neural-network-training.html?m=1&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
It’s quite simple: while one bottlenecked part of the training pipeline is getting the next input ready, the current input gets “echoed” through the rest of the model graph, reducing training time while preserving predictive performance.
This is cool work, and hopefully it’ll get upstreamed to TensorFlow for everyone to use.