---
category: climate-ai
date: 2021-01-03
emoji: "\U0001F3ED"
issue_number: 56
title: Towards Tracking the Emissions of Every Power Plant on the Planet
---

_Towards Tracking the Emissions of Every Power Plant on the Planet_ by [Couture et al.
(2020)](https://www.climatechange.ai/papers/neurips2020/11/paper.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) won the Best Pathway to Impact award at the [NeurIPS 2020 CCAI workshop](https://www.climatechange.ai/events/neurips2020?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Supported by [Al Gore’s Climate TRACE](https://dynamically-typed.netlify.app/stories/2020/al-gore-launches-climate-trace/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (and grants from Google.org and Bloomberg Philanthropies), the project “[uses] machine learning to infer power generation and emissions from visible and thermal power plant signatures in satellite images.” In this initial paper, the authors present models that can predict whether a power plant is currently on or off from a single satellite image; their best model, a convolutional neural network, gets a mean average precision of 81% on this binary classification task.
Interestingly, they find that the “vapor plume” (steam) from a power plant’s cooling system is a better indicator for its emissions than the “smoke plume” (greenhouse gasses) coming out of its main chimney.