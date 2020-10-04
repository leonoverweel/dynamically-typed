---
category: ml-research
date: 2020-04-12
issue_number: 37
title: 'Distill: Early Vision in CNNs'
---

![The largest neuron groups in the `mixed3a` layer of InceptionV1. (Olah et al., 2020)](https://s3.amazonaws.com/revue/items/images/005/808/130/mail/1b22ed14889a1b09c65af4e07fce2b66.png?1586603190)

_The largest neuron groups in the `mixed3a` layer of InceptionV1. (Olah et al., 2020)_

**Chris Olah and his OpenAI collaborators published a new Distill article:**[ **An Overview of Early Vision in InceptionV1**](https://distill.pub/2020/circuits/early-vision?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **.**
This work is part of Distill’s [_Circuits_ thread](https://distill.pub/2020/circuits/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which aims to understand how convolutional neural networks work by investigating individual features and how they interact through the formation of logical circuits (see [DT #35](https://dynamicallytyped.com/issues/35-completely-automatic-video-background-removal-with-unscreen-and-circuits-for-understanding-neural-networks-230458?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
In this new article, Olah et al.
explore the first five layers of Google’s [InceptionV1](https://arxiv.org/abs/1409.4842?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) network:

> Over the course of these layers, we see the network go from raw pixels up to sophisticated [boundary detection](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3b_boundary), basic shape detection (eg.
> [curves](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3b_curves), [circles](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3b_circles_loops), [spirals](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3b_curve_shapes), [triangles](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3a_angles)), [eye detectors](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3b_eyes), and even crude detectors for [very small heads](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3b_proto_head).
> Along the way, we see a variety of interesting intermediate features, including [Complex Gabor detectors](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#conv2d1_discussion_complex_gabor) (similar to some classic “complex cells” of neuroscience), [black and white vs color detectors](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#mixed3a_discussion_BW), and [small circle formation from curves](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#mixed3a_discussion_small_circle).

Each of these five layers contains dozens to hundreds of features (a.k.a.
channels or filters) that the authors categorize into human-understandable groups, which consist of features that detect similar things for inputs with slightly different orientations, frequencies, or colors.
This goes from `conv2d0`, the first layer where 85% of filters fall into two simple categories (detectors [for lines](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_conv2d0_gabor_filters) and [for contrasting colors](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_conv2d0_color_contrast), in various orientations), all the way up to `mixed3b`, the fifth layer where there are over a dozen complex categories (detectors [for small heads](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3b_proto_head), [for circles/loops](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3b_circles_loops), and much more).
We’ve known that there are line detectors in early network layers for a long time, but this detailed taxonomy of later-layer features is novel—and it must’ve been an enormous amount of work to create.

![A cicuits-based visualization of the black & white detector neuron group in layer `mixed3a` of InceptionV1. (Olah et al., 2020)](https://s3.amazonaws.com/revue/items/images/005/808/297/mail/359e82fcba2c004daa134d52da10992b.png?1586611023)

_A cicuits-based visualization of the black & white detector neuron group in layer `mixed3a` of InceptionV1. (Olah et al., 2020)_

For a few of the categories, like black & white and small circle detectors in `mixed3a`, and boundary and fur detectors in `mixed3b`, the article also investigates the “circuits” that formed them.
Such circuits show how strongly the presence of a feature in the input positively or negatively influences (“excites” or “inhibits”) different regions of the current feature.
One of the most interesting aspects of this research is that some of these circuits—which were learned by the network, not explicitly programmed!—are super intuitive once you think about them for a bit.
The black & white detector above, for example, consists mostly of negative weights that inhibit colorful input features: the more color features in the input, the less likely it is to be black & white.

The simplicity of many of these circuits suggests, to me at least, that Olah et al.
are currently exploring one of the most promising paths in AI explainability research.
(Although there is an alternate possibility, as pointed out by the authors: that they’ve found a “taxonomy that might be helpful to humans but [that] is ultimately somewhat arbitrary.”)

Anyway, [An Overview of Early Vision in InceptionV1](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#group_mixed3b_proto_head) is one of the most fascinating machine learning papers I’ve read in a long time, and I spent a solid hour zooming in on different parts of the taxonomy.
[The groups for layer `mixed3a`](https://distill.pub/2020/circuits/early-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#mixed3a) are probably my favorite.
I’m also curious about how much these early-layer neuron groups generalize to other vision architectures and types of networks—to what extent, for example, do these same neuron categories show up in the first layers of binarized neural networks?

If you read the article and have more thoughts about it that I didn’t cover here, I’d love to hear them.
:)