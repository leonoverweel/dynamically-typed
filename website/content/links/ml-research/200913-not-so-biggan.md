---
category: ml-research
date: 2020-09-13
emoji: "\u270D"
issue_number: 48
title: Not-so-BigGAN
---

When I covered BigGAN in February 2019 ([DT #6](https://dynamicallytyped.com/issues/6-deep-reinforcement-learning-from-an-atari-zoo-to-a-self-driving-car-in-20-minutes-155882?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), its image generation results were very impressive — but the model was also incredibly expensive to train, requiring a cluster of hundreds of TPUs.
Now, just a year and a half later, [Han et al.
(2020)](https://arxiv.org/abs/2009.04433?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) introduced not-so-BigGAN: close-enough image quality trained on just 4 Tesla-V100 GPUs — an order of magnitude less compute.
This speed of this progress is amazing.