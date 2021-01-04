---
category: ml-research
date: 2019-11-10
issue_number: 26
title: Chollet's Abstraction and Reasoning Corpus
---

![From top to bottom: Chollet's hierarchy of intelligence, and two sample tasks from ARC. (François Chollet))](https://s3.amazonaws.com/revue/items/images/005/197/673/mail/c940ac191521a1ebf6ed783a42de131b.png?1573227558)

_From top to bottom: Chollet's hierarchy of intelligence, and two sample tasks from ARC. (François Chollet))_

**Keras creator François Chollet has published his 64-page manifesto on the path “toward more intelligent and human-like” AI** in a paper titled [The Measure of Intelligence](https://arxiv.org/abs/1911.01547?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that “formalizes things [he’s] been talking about for the past 10 years.” This is one of the most inspiring papers I’ve read in a long time, and it has many people around the office very excited too.
Broadly, Chollet covers three topics: (1) the context and history of evaluating the intelligence of humans and machines; (2) a new perspective of what a framework for evaluating intelligence should be; and (3) the Abstraction and Reasoning Corpus (ARC), his implementation of this framework.

**(1) Context and history.**
In cognitive science, there are are two opposing views of how the human mind works:

> One view in which the mind is a relatively static assembly of special-purpose mechanisms developed by evolution, only capable of learning what is it programmed to acquire, and another view in which the mind is a general-purpose “blank slate” capable of turning arbitrary experience into knowledge and skills, and that could be directed at any problem.

Chollet explains that early (symbolic) AI research focused on the former view, creating intricate symbolic representations of problems over which computers could search for solutions, while current (deep learning) AI research focuses on the latter, creating “randomly initialized neural networks that starts blank and that derives its skills from training data.” He argues that neither of these approaches is sufficient for creating human-like intelligence, which, as he introduces through the lense of [psychometrics](https://en.wikipedia.org/wiki/Psychometrics?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), is mostly characterized by the ability to _broadly generalize_ on top of some low-level [core knowledge](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-7687.2007.00569.x?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that all humans are born with.

**(2) A new perspective.**
Chollet presents a new framework that is meant to be an “actionable perspective shift in how we understand and evaluate flexible or general artificial intelligence.” It evaluates these broad cognitive generalization abilities by modelling an intelligent system as something that can output static “skill programs” to achieve some task.
The system’s intelligence is then measured by how efficiently it can generate these skills.
Formally:

> The intelligence of a system is a measure of its skill-acquisition efficiency over a scope of tasks, with respect to priors, experience, and generalization difficulty.

**(3) Abstraction and Reasoning Corpus (ARC).**
Chollet finally proposes a practical implementation of the framework.
An ARC task, as pictured above, consists of several example _before_ and _after_ grids, and one final _before_ grid for which the intelligent system’s generated skill must figure out the correct _after_ grid.
Each task is designed so that the average human can solve it quite easily, and so that it depends only on core knowledge (and not learned things like the concept of arrows).
Tasks range from simple object counting to more complex things like continuing a line that bounces off edges.
There are 400 tasks to train on and 600 tasks to test on, of which 200 are secret and used to evaluate a competition.

**I’ve barely scratched the surface of the paper here,** and I highly recommend reading it in full and trying out ARC for yourself!

* The Measure of Intelligence on arXiv: [Chollet (2019)](https://arxiv.org/abs/1911.01547?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* The Abstraction and Reasoning Corpus on GitHub, including a version you can test yourself on: [fchollet/ARC](https://github.com/fchollet/ARC?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Chollet’s [twitter thread](https://twitter.com/fchollet/status/1192121587467784192?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) with some more background about how the paper came to be.