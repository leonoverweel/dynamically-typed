---
category: ml-research
date: 2021-01-03
emoji: "\U0001F47E"
issue_number: 56
title: 'DeepMind''s new RL SOTA: MuZero'
---

New from DeepMind, in Nature: _Mastering Atari, Go, chess and shogi by planning with a learned model_ by [Schrittwieser et al.
(2020)](https://www.nature.com/articles/s41586-020-03051-4?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
The paper describes DeepMind’s new games-playing reinforcement learning algorithm [MuZero](https://deepmind.com/blog/article/muzero-mastering-go-chess-shogi-and-atari-without-rules?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which is the latest evolution of the lab’s previous [AlphaGo](https://deepmind.com/research/case-studies/alphago-the-story-so-far?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (2016), [AlphaGo Zero](https://deepmind.com/blog/article/alphago-zero-starting-scratch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (2017), and [AlphaZero](https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (2018) algorithms.
The key improvement in MuZero is that it doesn’t need to be explicitly told the rules of the games it plays: it’s model-free, and “just models aspects that are important to the agent’s decision-making process.” This helps it achieve state-of-the-art (and superhuman) results on the Atari suite, Go, chess, and shogi.