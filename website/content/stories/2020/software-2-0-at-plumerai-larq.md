---
category: productized-ai
date: 2020-03-29
issue_number: 36
title: Software 2.0 at Plumerai
---

![The stacked layers of Plumerai's Larq ecosystem: Larq Compute Engine, Larq, and Larq Zoo.](https://s3.amazonaws.com/revue/items/images/005/738/442/mail/e258d2c35f85915cd06789baaa2ea06b.png?1585392392)

_The stacked layers of Plumerai's Larq ecosystem: Larq Compute Engine, Larq, and Larq Zoo._

A few days ago, we published a new blog post about **software 2.0 at Plumerai** , which touches on some points that are interesting for productized artificial intelligence at large.
As a reminder, Plumerai—and my day-to-day research there—is centered around Binarized Neural Networks (BNNs): deep learning models in which weights and activations are not floating-point numbers but can only be -1 or +1.
[Larq](https://larq.dev?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is our ecosystem of open-source packages for BNN development: [larq/zoo](https://github.com/larq/zoo?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) has pretrained, state-of-the-art models; [larq/larq](https://github.com/larq/larq?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) integrates with TensorFlow Keras to provide BNN layers and training tools; and [larq/compute-engine](https://github.com/larq/compute-engine?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is an optimized converter and inference engine for deploying models to mobile and edge devices.

[Andrej Karpathy](https://twitter.com/karpathy?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), who was previously at OpenAI and is now [developing Tesla’s self-driving software](https://www.youtube.com/watch?t=6676s&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=Ucp0TTmvqOE), first wrote about his [vision for Software 2.0](https://medium.com/@karpathy/software-2-0-a64152b37c35?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) back in 2017.
I recommend reading the whole essay, but it boils down to the idea that large chunks of currently human-written software will be replaced by learned neural networks—something we already see happening in areas like computer vision, machine translation, and speech recognition/synthesis.
Let’s look at two benefits Karpathy notes about this shift that are relevant to our work on Larq.

First, neural networks are agile.
Depending on computational requirements—running on a high-power chip vs.
an energy-efficient one—deep learning models can be scaled by trading off size for accuracy.
Take one of the BNN families in our Zoo package, for example: the XL version of [QuickNet](https://docs.larq.dev/zoo/api/sota/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) achieves 67.0% top-1 ImageNet classification accuracy at a size 0f 6.2mb, but it can also be scaled down to get 58.6% at just 3.2mb.
Depending on the power and accuracy requirements of your application, you can swap in one for the other without having to otherwise change your code.

Second, deep learning models constantly get better.
If we think of a cool new training trick or other optimization for BNNs, we can push it out in an updated version of the QuickNet family.
In fact, that’s exactly what we did last week:

> A great example of the power of this integrated approach is the recent addition of one-padding across the Larq stack.
> Padding with ones instead of zeros simplifies binary convolutions, reducing inference time without degrading accuracy.
> We not only enabled this in [Larq Compute Engine], but also implemented one-padding in Larq and retrained our QuickNet models to incorporate this feature.
> All you need to do to get these improvements is update your pip packages.

I’m super excited about the idea of Software 2.0, and—as you can probably tell from the paragraphs above—I’m pumped to be working on it every day at Plumerai, both on the research side (making better models) and the software engineering side (improving Larq).
You can read more about our Software 2.0 aspirations in this blog post: [The Larq Ecosystem: State-of-the-art binarized neural networks and even faster inference](https://blog.larq.dev/2020/03/larq-ecosystem/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).