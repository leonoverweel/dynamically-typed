---
category: ml-research
date: 2021-06-06
emoji: "\U0001F41B"
issue_number: 67
title: DeepDebug for Python code fixing
---

Cool new paper from [Drain et al.
(2021)](https://arxiv.org/abs/2105.09352?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) at Microsoft Research: DeepDebug is a Transformer-based model that can fix Python bugs using stack traces, back translation and code skeletons.
One interesting contribution is their “neural bugs” injection model, which was trained to revert bug-fixing commits and “can generate near arbitrary edits that are drawn from the distribution of mistakes developers actually make.” On the QuixBugs benchmark, DeepDebug increases the number of bug fixes found by 50% while reducing false positives from 35% to 5%, all while decreasing the run timeout from six hours to one minute.
Can I get this in PyCharm?