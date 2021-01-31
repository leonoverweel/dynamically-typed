---
category: ml-research
date: 2021-01-31
emoji: "\U0001F99A"
issue_number: 58
title: 'Distill: High-Low Frequency Detectors'
---

Ludwig Schubert, Chelsea Voss and Chris Olah published a new entry to the [Distill Circuits thread](https://distill.pub/2020/circuits/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), in which they model connections in trained convolutional neural networks as logical circuits to figure out how they work; I covered what makes this research so interesting last April in [Distill: Early Vision in CNNs](https://dynamically-typed.netlify.app/stories/2020/distill-early-vision-in-cnns/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Using feature visualization, dataset examples, and synthetic tuning curves, this new article goes in-depth on a relatively unintuitive class of neurons: [High-Low Frequency Detectors](https://distill.pub/2020/circuits/frequency-edges/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which activate when they encounter “directional transitions from low to high spatial frequency.” In [one very cool section](https://distill.pub/2020/circuits/frequency-edges/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#implementation) of the article, the authors combine clusters of high- and low-frequency circuit components into two generic HF- and LF-factors, and show that they play the same roles in the implementation of high-low frequency detectors as their individual components do.
As always, the article is a great weekend long read.