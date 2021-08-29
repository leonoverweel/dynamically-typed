---
category: climate-ai
date: 2021-08-29
emoji: "\U0001F50C"
issue_number: 73
title: Hongyu's thesis on datacenter demand-side response
---

Earlier this year, I wrote about [the climate opportunity of gargantuan AI models](https://dynamicallytyped.com/stories/2021/gargantuan-ai-model-climate-opportunity/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter): like many other types of workloads, the offline training of AI models could be scheduled dynamically based on electricity market signals of over- or under-supply.
This way, these power-hungry datacenters can provide demand-side response for balancing the power grid — an increasingly important problem with the growth of renewables — so that we’ll be less dependent on supply-side balancing from coal and gas plants.
I’m excited to share that over the past few months, I co-supervised [Hongyu He](https://www.linkedin.com/in/hongyuhe/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAC68YsEBXtrKRly9DxChIOEtYaISxg3rA1s&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)’s BSc thesis project at the VU Amsterdam’s [@Large Research group](https://atlarge-research.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) on exactly this topic.
In his 158-page (!) thesis, Hongyu extended [OpenDC](http://opendc.org?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), a datacenter simulator I helped develop during my own BSc, to incorporate electricity price signals from [Dexter’s asset optimization product](https://dexterenergy.ai/services/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#assetdispatching) into the virtual datacenter’s workload scheduler.
He then simulated different ways for datacenters to participate directly in power markets, and found that these could be profitable (and therefore helpful in balancing the grid).
Hongyu’s full thesis is on arXiv: [How Can Datacenters Join the Smart Grid to Address the Climate Crisis?](https://arxiv.org/abs/2108.01776?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) This simulation work is an important step for convincing stakeholders to pilot and deploy this in the real world; I hope to have more to share on that in the future.