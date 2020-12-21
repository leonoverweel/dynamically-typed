---
category: ml-research
date: 2020-03-15
issue_number: 35
title: 'Distill: Zoom in on Circuits'
---

!["By studying the connections between neurons, we can find meaningful algorithms in the weights of neural networks."](https://s3.amazonaws.com/revue/items/images/005/677/755/mail/b9001d85efe0632acb4a0193c5d105fb.png?1584286554)

_"By studying the connections between neurons, we can find meaningful algorithms in the weights of neural networks."_

**Chris Olah et al.
wrote a fascinating new Distill article about “circuits” in convolutional neural networks.**
The authors aim to reposition the field of AI interpretability as a natural science, like biology and chemistry:

> There are two common proposals for dealing with this [lack of shared evaluation measures in the field of interpretability], drawing on the standards of adjacent fields.
> Some researchers, especially those with a deep learning background, want an “interpretability benchmark” which can evaluate how effective an interpretability method is.
> Other researchers with an HCI background may wish to evaluate interpretability methods through user studies.

> But interpretability could also borrow from a third paradigm: natural science.
> In this view, neural networks are an object of empirical investigation, perhaps similar to an organism in biology.
> Such work would try to make empirical claims about a given network, which could be held to the standard of falsifiability.

Olah et al.
do exactly this by investigating the Inception v1 network architecture in detail and presenting three speculative claims about how convolutional neural networks work:

1. Features are the fundamental unit of neural networks. They correspond to directions. These features can be rigorously studied and understood.
2. Features are connected by weights, forming circuits. These circuits can also be rigorously studied and understood.
3. Analogous features and circuits form across models and tasks.

For the former two claims, they present substantive evidence: examples of curve detectors, high-low frequency detectors, and pose-invariant dog head detectors for their claim about features; and examples of again curve detectors, oriented dog head detection, and car + dog superposition neurons for the circuits claim.

As always, the article is accompanied by very informative illustrations, and even some interesting tie-backs to the historical invention of microscopes and discovery of cells.
I found it a fascinating read, and it made me think about how these findings would look in the context of binarized neural networks.
You can read the article by Olah et al.
(2020) on Distill: [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#d-footnote-9).