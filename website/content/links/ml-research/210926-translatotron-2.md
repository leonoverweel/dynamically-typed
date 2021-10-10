---
category: ml-research
date: 2021-09-26
emoji: "\U0001F4B1"
issue_number: 75
title: Translatotron 2
---

In 2019, Google AI introduced [Translatotron](https://ai.googleblog.com/2019/05/introducing-translatotron-end-to-end.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), “the first ever model that was able to directly [end-to-end] translate speech between two languages,” instead of chaining together separate speech recognition, machine translation, and speech synthesis models (see [DT #14](https://dynamicallytyped.com/issues/014/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
[Jia et al.
(2021)](https://arxiv.org/abs/2107.08661?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) updated the model to create [Translatotron 2](https://ai.googleblog.com/2021/09/high-quality-robust-and-responsible.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which is newly able to do voice transfer — making the translated speech sound like it was spoken by the same voice as the input speech — “even when the input speech contains multiple speakers speaking in turns.” (Check out [the blog post](https://ai.googleblog.com/2021/09/high-quality-robust-and-responsible.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for some samples of generated audio.) One significant change from the original Translatotron is that both the voice and content of the input speech are now captured using a single encoder, which the authors claim makes the model less likely to be abused for spoofing arbitrary audio content (making someone’s voice say something they never said).
But I’m a bit surprised that this is such a central part of the blog post, since there are plenty of dedicated voice-mimicking speech generation models out there already that would be easier to use for this purpose anyway.