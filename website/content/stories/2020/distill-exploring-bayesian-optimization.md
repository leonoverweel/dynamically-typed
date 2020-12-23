---
category: ml-research
date: 2020-05-24
issue_number: 40
title: 'Distill: Exploring Bayesian Optimization'
---

![Bayesian optimization of finding gold along a line, using the probability of improvement (PI) acquisition function. (Agnihotri and Batra, 2020.)](https://s3.amazonaws.com/revue/items/images/006/010/478/mail/7957b79fcd3b61d95a8fb937d7eb551f.png?1590231014)

_Bayesian optimization of finding gold along a line, using the probability of improvement (PI) acquisition function. (Agnihotri and Batra, 2020.)_

Apoorv Agnihotri and Nipun Batra wrote an article [**Exploring Bayesian Optimization**](https://distill.pub/2020/bayesian-optimization/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **for Distill.**
This technique is used in hyperparameter optimization, where evaluating any one point—like the combination of a learning rate, a weight decay factor, and a data augmentation setting—is expensive: you need to train your entire model to know how well the hyperparameters performed.

This is where Bayesian optimization comes in.
It centers around answering the question “Based on what we know so far, what point should we evaluate next?” The process uses _acquisition functions_ to trade off exploitation (looking at points in the hyperparameter space that we think are likely to be good) with exploration (looking at points we’re very uncertain about).
Given an appropriate acquisition function and priors, it can help find a good point in the space in surprisingly few iterations.

Bayesian optimization was one of the tougher subjects to wrap my head around in graduate school, so I was very excited to see it get the Distill treatment.
Agnihotri and Batra explain the process through an analogy of picking the best places to dig for gold which, incidentally, was also one of its first real-world applications in the 1950s!
You can [read the full explainer here](https://distill.pub/2020/bayesian-optimization/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); also check out [DragonFly](https://github.com/dragonfly/dragonfly?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [BoTorch](https://botorch.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), two tools for automated Bayesian optimization [from my ML resources list](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4).