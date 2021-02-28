---
category: ml-research
date: 2021-02-28
emoji: "\u26A1\uFE0F"
issue_number: 60
title: Model Search for TensorFlow
---

Google [has released Model Search](https://ai.googleblog.com/2021/02/introducing-model-search-open-source.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), an open-source AutoML platform for the TensorFlow ecosystem.
The pitch: “Model Search is domain agnostic, flexible and is capable of finding the appropriate architecture that best fits a given dataset and problem, while minimizing coding time, effort and compute resources.” It can run on a single machine or in a distributed setting, and uses a reinforcement learning-inspired “explore & exploit” methodology to find a model architecture that optimizes for user-specified metrics.
For efficiency, Model Search also uses knowledge distillation and weight sharing between experiments runs.
It’s available on GitHub at [google/model_search](https://github.com/google/model_search?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).