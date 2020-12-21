---
category: ml-research
date: 2020-11-22
emoji: "\U0001F47E"
issue_number: 53
title: Understanding RL Vision
---

Cool new Distill paper from Hilton et al.
(2020): [Understanding RL Vision](https://distill.pub/2020/understanding-rl-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
The authors train a reinforcement learning agent to play a procedurally-generated video game based on single frames as input, and then develop an interactive interface (embedded in the article!) to study what different parts of the network learn.
Using [Circuits](https://distill.pub/2020/circuits/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) editing (see [DT #37](https://dynamicallytyped.com/issues/37-openai-s-neural-network-taxonomy-decoding-text-from-brain-implants-and-models-that-don-t-exist-236677?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), they then make the agent blind to e.g.
left-moving enemies in the game, and experimentally show that this indeed makes it fail more often by missing such enemies.
“Our results depend on levels in CoinRun being procedurally-generated, leading us to formulate a diversity hypothesis for interpretability.
_[Interpretable features tend to arise (at a given level of abstraction) if and only if the training distribution is diverse enough (at that level of abstraction).]_ If it is correct, then we can expect RL models to become more interpretable as the environments they are trained on become more diverse.” As always, [the full article](https://distill.pub/2020/understanding-rl-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is a great Sunday long read.