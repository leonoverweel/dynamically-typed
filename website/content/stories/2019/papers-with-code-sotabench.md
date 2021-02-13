---
category: ml-research
date: 2019-10-13
issue_number: 24
title: Papers with Code sotabench
---

![The sotabench homepage. (sotabench)](https://s3.amazonaws.com/revue/items/images/005/094/126/mail/040ec11d29f0de972b7a8123ca1517ec.png?1570813096)

_The sotabench homepage. (sotabench)_

**The team behind Papers with Code has launched sotabench.**
The name derives from “state of the art (sota)” + “benchmark”, and its mission is precisely that: to _benchmark every open source model_ —for free!

This is super cool.
A researcher just needs to implement a small Python file that specifies how to run their model on some given test data.
They can then submit their repository to sotabench, which tracks it and runs the model on standardized test data for every commit to the master branch.
This way, it independently keeps track of whether models achieve the performance claimed by the authors (within some benchmark-specific error range).

The project is run by Atlas ML, a company whose mission is to “advance _open source_ deep learning” (emphasis mine).

> We believe the software of the future should be accessible to everyone, not just large technology companies.
> We are realising this future by building breakthrough tooling that allows the world to build and collaborate on ambitious deep learning projects.

Atlas ML was co-founded by [Robert Stojnic](https://twitter.com/rbstojnic?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), one of the first Wikipedia engineers.
It’s therefore not surprising that the team’s main objective is to push the open and collaborative values that also drive Wikipedia.
The meta dataset resulting from sotabench will also surely lead to lots of interesting research on reproducibility and model characteristics vs.
performance.
Check out the project at [sotabench.com](https://sotabench.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).