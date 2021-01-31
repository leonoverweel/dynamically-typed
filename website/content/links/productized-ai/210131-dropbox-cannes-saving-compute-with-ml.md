---
category: productized-ai
date: 2021-01-31
emoji: "\U0001F4D1"
issue_number: 58
title: 'Dropbox Cannes: saving compute with ML'
---

Win Suen wrote about a machine learning system running in production at Dropbox that decides for which files previews should be rendered: [Cannes: How ML saves us $1.7M a year on document previews](https://dropbox.tech/machine-learning/cannes--how-ml-saves-us--1-7m-a-year-on-document-previews?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
She goes into two design considerations for building a highly performant AI system: the cost-benefit tradeoff of ML-powered infrastructure savings (rendering fewer previews to save compute vs.
hurting user experience by not having previews) and the model complexity tradeoff (prediction accuracy vs.
interpretability and cost of deployment).
The final model is a gradient-boosted classifier that can “predict previews up to 60 days after time of pre-warm with >70% accuracy.”