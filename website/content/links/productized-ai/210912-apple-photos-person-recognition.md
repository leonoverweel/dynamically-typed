---
category: productized-ai
date: 2021-09-12
emoji: "\U0001F575\uFE0F\u200D\u2640\uFE0F"
issue_number: 74
title: Person recognition in Apple Photos
---

Apple’s machine learning blog has a detailed new post about their privacy-focused, on-device implementation of [facial recognition in the Photos app](https://machinelearning.apple.com/research/recognizing-people-photos?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Some interesting details, in no particular order: (1) people are identified not only by embeddings of their face, but also by their upper body and metadata from the photo — two photos taken a few minutes apart are relatively likely to contain the same person; (2) an iterative clustering algorithm first groups very certain matches, then groups those groups, etc, and once it’s no longer certain it asks the user whether two clusters are still the same person; (3) constant re-evaluations of bias in the training dataset serve as a guide to what gaps to fill in new rounds of data collection; (4) running on a recent Apple Neural Engine, face embedding generation takes only 4 milliseconds.
I’ve recently switched from Google Photos to Apple Photos, and one thing about their person recognition is definitely impressive: Google thinks two of my friends who are twins are the same person, and Apple can keep them apart.