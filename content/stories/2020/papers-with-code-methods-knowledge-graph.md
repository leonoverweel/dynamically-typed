---
category: ml-research
date: 2020-08-02
issue_number: 45
title: Methods is Papers with Code's machine learning knowledge graph
---

![Papers with Code's Methods page for the residual block (cropped).](https://s3.amazonaws.com/revue/items/images/006/327/202/mail/89e64db1fc5224078510ebc25c376d65.png?1596303561)

_Papers with Code's Methods page for the residual block (cropped)._

A few weeks ago, [**Papers with Code**](https://paperswithcode.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **launched**[ **Methods**](https://paperswithcode.com/methods?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **, a knowledge graph of hundreds of machine learning concepts:**

> We are now tracking 730+ building blocks of machine learning: optimizers, activations, attention layers, convolutions and much more!
> Compare usage over time and explore papers from a new perspective.

I’ve started using Methods as my go-to reference for many things at work.
Sitting at a more abstracted level than the documentation for your ML library of choice, it’s an incredibly useful resource for anyone doing ML research or engineering.
Each Methods page contains the following sections:

* A concise description of what the method is and how it works, including math and a diagram where relevant
* A chronological list of papers that use the method
* A breakdown of tasks from the site’s [State-of-the-Art](https://paperswithcode.com/sota?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) leaderboards for which the method is used
* A graph of how the method’s use changed over time, compared to other methods of the same category (for example, Adam vs. SGD for optimizers)
* A list of components: other methods that contribute to this method (for example, 1x1 convolutions and ReLUs are components of residual blocks)
* A list of categories for the method

I’ve found the last of those sections to be especially handy for answering those hard-to-Google “what’s the name of that other thing that’s kind of like this thing again?” questions.
(Also see [this Twitter thread](https://twitter.com/rosstaylor90/status/1280889854264594432?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) by the project’s co-creator Ross Taylor for a few example uses of the other sections.) Methods launched just a month ago, and given how useful it already is, I’m very excited to see how it grows in the future.

One additional feature I’d find useful is the inverse of the components section: I also want to know which methods build on top of the method I’m currently viewing.
Another thing I’d like to see is an expansion of code links for methods to also include TensorFlow snippets—but since [Facebook AI Research bought Papers with Code late last year](https://medium.com/paperswithcode/papers-with-code-is-joining-facebook-ai-90b51055f694?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), I’m guessing that keeping these snippets exclusive to (FAIR-controlled) PyTorch may be a strategic decision rather than a technical one.