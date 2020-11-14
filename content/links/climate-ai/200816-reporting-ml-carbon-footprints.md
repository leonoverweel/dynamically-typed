---
category: climate-ai
date: 2020-08-16
emoji: "\U0001F4A1"
issue_number: 46
title: Reporting ML carbon footprints
---

New paper from Henderson et al. (2020): [Towards the Systematic Reporting of the Energy and Carbon Footprints of Machine Learning](https://arxiv.org/abs/2002.05651?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
The authors propose a framework and [open-source software tool](https://github.com/Breakend/experiment-impact-tracker?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for measuring the energy use of ML models trained on Linux systems with Intel chips and NVIDIA GPUs.
They also use [electricityMap](https://www.electricitymap.org/map?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to estimate carbon emissions based on energy use, but because datacenters increasingly generate their own solar or wind power, and their electricity’s carbon intensity may therefore not be the same as that of the grid in their region, I’d take those numbers with a grain of salt.
Anyway, I first came across the tool about half a year ago, and I’m glad it has picked up some steam since then.
Consider [giving it a star on GitHub](https://github.com/Breakend/experiment-impact-tracker?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and using it for your next paper or integrating into your company’s tooling!