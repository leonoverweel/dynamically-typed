---
category: ml-research
date: 2021-04-11
emoji: "\U0001F308"
issue_number: 63
title: 'Distill: Weight Banding'
---

_Distill #3:_ [Weight Banding](https://distill.pub/2020/circuits/weight-banding/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) by Petrov et al.
(2021), another chapter in the [_Circuits_ thread](https://distill.pub/2020/circuits/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
This article explores why weights in some layers display a very distinct banding pattern when visualized using Nonnegative Matrix Factorization (NMF), with the following process: “For each neuron, we take the weights connecting it to the previous layer.
We then use NMF to reduce the number of dimensions corresponding to channels in the previous layer down to 3 factors, which we can map to RGB channels.” This pattern occurs in the final convolutional layer across InceptionV1, ResNet50, and VGG19 (but not AlexNet, which does not use global average pooling).
The authors hypothesize that this horizontal banding pattern “is a learned way to preserve [vertical] spatial information as it gets lost through various pooling operations,” which is enforced by the fact that, in an experiment in which they rotate input images by 90 degrees, the bands also rotate by 90 degrees to become vertical.
The article concludes that banding is an example of emergent structure in vision models, but that we can’t say much about whether this structure is “good” or “bad” or how its presence should influence architectural decisions; not the most significant conclusions, but a very interesting observation nonetheless.