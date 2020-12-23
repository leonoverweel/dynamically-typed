---
category: ml-research
date: 2020-03-29
issue_number: 36
title: Google releases TensorFlow Quantum
---

!["A high-level abstract overview of the computational steps involved in the end-to-end pipeline for inference and training of a hybrid quantum-classical discriminative model for quantum data in TFQ. "](https://s3.amazonaws.com/revue/items/images/005/739/211/mail/c2492b7975ef4cebc1a1c2b3f509bf53.png?1585407979)

_"A high-level abstract overview of the computational steps involved in the end-to-end pipeline for inference and training of a hybrid quantum-classical discriminative model for quantum data in TFQ. "_

**Google has released**[ **TensorFlow Quantum**](https://www.tensorflow.org/quantum?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **(TFQ), its open-source library for training quantum machine learning models.**
The package integrates TensorFlow with [Cirq](https://ai.googleblog.com/2018/07/announcing-cirq-open-source-framework.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Google’s library for working with Noisy Intermediate Scale Quantum (NISQ) computers (scale of ~50 - 100 qubits).
Users can define a quantum dataset and model in Cirq and then use TFQ to evaluate it and extract a tensor representation of the resulting quantum states.
For now Cirq computes these representations (samples or averages of the quantum state) using millions of simulation runs, but in the future it will be able to get them from real NISQ processors.
The representations feed into a classical TensorFlow model and can be used to compute its loss.
Finally, a gradient descent step updates the parameters of both the quantum and classical models.

> A key feature of TensorFlow Quantum is the ability to simultaneously train and execute many quantum circuits.
> This is achieved by TensorFlow’s ability to parallelize computation across a cluster of computers, and the ability to simulate relatively large quantum circuits on multi-core computers.

TensorFlow Quantum is a collaboration with the University of Waterloo, (Google/Alphabet) X, and Volkswagen, which aims to use it for materials (battery) research.
Other applications of quantum ML models include medicine, sensing, and communications.

These are definitely still very much the early days of the quantum ML field (and of quantum computing in general), but nonetheless it’s exciting to see this amount of software tooling and infrastructure being built up around it.
For lots more details and links to sample code and notebooks, check out the Google AI blog post by Alan Ho and Masoud Mohseni here: [Announcing TensorFlow Quantum: An Open Source Library for Quantum Machine Learning](https://ai.googleblog.com/2020/03/announcing-tensorflow-quantum-open.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).