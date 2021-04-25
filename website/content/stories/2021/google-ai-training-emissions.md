---
category: climate-ai
date: 2021-04-25
issue_number: 64
title: Google's tips for reducing AI training emissions
---

David Patterson wrote a blog post for Google’s The Keyword blog on [how the company is minimizing AI’s carbon footprint](https://blog.google/technology/ai/minimizing-carbon-footprint/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), mostly covering his new paper on the topic: [Carbon Emissions and Large Neural Network Training](https://arxiv.org/abs/2104.10350?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Patterson et al.
2021).
The paper went live on arXiv just half a week ago, but coming in at 22 data-dense pages, I think it’ll become a key piece of literature for sustainable AI.
My two main takeaways from the paper were: (1) retroactively estimating AI training emissions is difficult, so researchers should measure it during model development; and (2) where, when and on what hardware models are trained can make an enormous difference in emissions.

**Emissions estimates**

Patterson et al.
calculate the carbon footprint of several recent gargantuan models ([T5](http://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Meena](https://ai.googleblog.com/2019/06/applying-automl-to-transformer.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [GPT-3](https://dynamicallytyped.com/stories/2020/gpt-3/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), etc.) more precisely than previous work, which they found to be off by up to two orders of magnitude in some cases: the previous estimate for [The Evolved Transformer](https://arxiv.org/abs/1901.11117?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)‘s Neural Architecture Search (NAS), for example, was 88 times too high (see Appendix D).
This shows that, without knowing the exact datacenter, hardware, search algorithm choices, etc., it’s pretty much impossible to accurately estimate how much CO2 was emitted while training a model.

Because of this, one of the authors’ recommendations is for the machine learning community to include CO2 emissions estimates as a standard metric in papers: a measurement by the people training the models, who have much better access to all relevant information (see e.g.
Table 4 in the paper and the [Google Cloud page on their different datacenters’ carbon intensities](https://cloud.google.com/sustainability/region-carbon?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), will always be more accurate than a retroactive estimate by another researcher.
If conferences and journals start requiring emissions metrics in paper submissions and include them in acceptance criteria, it’ll encourage individual researchers and AI labs to take steps to reduce their emissions.

(As an aside, this is an interesting comparison that makes “tons of CO2-equivalent greenhouse gas emissions” a bit easier to think about: a whole passenger jet round trip flight between San Francisco and New York emits about 180 tons of CO2e; relative to that, “T5 training emissions are ~26%, Meena is 53%, Gshard-600B is ~2%, Switch Transformer is 32%, and GPT-3 is ~305% of such a round trip.” Puts it all in perspective quite well.)

**Emissions reductions**

Patterson et al.
also have some specific recommendations for reducing the CO2 emissions caused by training AI models:

> * Large but sparsely activated DNNs can consume <1/10th the energy of large, dense DNNs without sacrificing accuracy despite using as many or even more parameters.
> * Geographic location matters for ML workload scheduling since the fraction of carbon-free energy and resulting CO2e vary ~5X-10X, even within the same country and the same organization.
> * Specific datacenter infrastructure matters, as Cloud datacenters can be ~1.4-2X more energy efficient than typical datacenters, and the ML-oriented accelerators inside them can be ~2-5X more effective than off-the-shelf systems.

Adding all these up, “remarkably, the choice of DNN, datacenter, and processor can reduce the carbon footprint up to ~100-1000X.” _Two to three orders of magnitude!_ Since this research happened inside Google, its teams are now already optimizing where and when large models are trained to take advantage of these ideas.
Another cool aspect of the paper is that each of the four specific focus points for reducing emissions (improvements in algorithms, processors, datacenters, and the grid’s energy mix) is accompanied by a business rationale for implementing it as a cloud provider — I’m guessing the researchers also used some of these arguments to push for change internally at Google.
(Maybe, as a next step, they can also look into [ramping model training based on signals from the intraday electricity market](https://dynamicallytyped.com/stories/2021/gargantuan-ai-model-climate-opportunity/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)?)

It’s great to see a paper on AI sustainability with so much measured data and actionable advice.
I haven’t seen it going around much yet on Twitter, but I hope it’s read widely — [here’s the PDF link again](https://arxiv.org/pdf/2104.10350.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); the fallacy debunks in section 4.5 (page 12) are an interesting bit I haven’t summarized above, so give it a click!
I also hope that the paper’s recommendations are implemented: even just the relatively low-effort change of shifting our training workloads to different datacenters can already make a big difference.
And of course it’ll be interesting to see if there are any specific critiques on the paper’s emissions measurement methodology, since of course this is all still just a preprint and half the paper’s authors work at Google.