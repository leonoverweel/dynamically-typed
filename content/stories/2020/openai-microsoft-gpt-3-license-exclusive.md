---
category: productized-ai
date: 2020-10-11
issue_number: 50
title: 'OpenAI and Microsoft: GPT-3 and beyond'
---

![](https://s3.amazonaws.com/revue/items/images/006/633/129/mail/21d2ff8f0bae6f095178ef6386589964.jpeg?1602274609)

**OpenAI is exclusively licensing GPT-3 to Microsoft.
What does this mean for their future relationship?**

GPT-3 is OpenAI’s latest gargantuan language model (see [DT #42](https://dynamicallytyped.com/issues/42-facial-recognition-exodus-openai-s-new-gpt-3-language-model-and-oil-in-the-cloud-254772?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) that’s uniquely capable of performing many different “text-in, text-out” tasks — demos range from imitating famous writers to generating code ([#44](https://dynamicallytyped.com/issues/44-one-month-in-gpt-3-powered-openai-api-demos-take-the-web-by-storm-261577?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) — without needing to be fine-tuned: its crazy scale makes it [a few-shot learner](https://arxiv.org/abs/2005.14165?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

In July 2019, OpenAI announced it got a $1 billion investment from Microsoft.
Back then, this raised some eyebrows in the (academic) machine learning community, which can sometimes be a bit allergic to the commercialization of AI ([#19](https://dynamicallytyped.com/issues/19-microsoft-s-1b-openai-investment-lyft-s-dataset-and-what-makes-a-peacock-a-peacock-190545?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
The exact terms of the investment were never disclosed, but some key elements of the deal were.
[Tom Simonite for WIRED](https://twitter.com/tsimonite/status/1153340994986766336?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

> Most interesting bit of the OpenAI announcement: “we intend to license some of our pre-AGI technologies, with Microsoft becoming our preferred partner.”

Now, a year and a bit later, that’s exactly what happened.
From the [OpenAI blog](https://openai.com/blog/openai-licenses-gpt-3-technology-to-microsoft/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

> In addition to offering GPT-3 and future models via the OpenAI API, and as part of a multiyear partnership announced last year, OpenAI has agreed to license GPT-3 to Microsoft for their own products and services.

What does that mean?
[Nick Statt for The Verge](https://www.theverge.com/2020/9/22/21451283/microsoft-openai-gpt-3-exclusive-license-ai-language-research?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

> A Microsoft spokesperson tells _The Verge_ that its exclusive license gives it unique access to the underlying code of GPT-3, which contains technical advancements it hopes to integrate into its products and services.

In their [blog post](https://blogs.microsoft.com/blog/2020/09/22/microsoft-teams-up-with-openai-to-exclusively-license-gpt-3-language-model/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Microsoft pitches this as a way to “expand [their] Azure-powered AI platform in a way that democratizes AI technology,” to which the community again[ reacted negatively](https://thegradient.pub/ai-democratization-in-the-era-of-gpt-3/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter): if you want to democratize AI, why not just open-source GPT-3’s code and training data?* I agree that “democratizing” is a bit of a stretch, but I think there’s a much more interesting discussion to be had here than the one on a self-congratulatory word choice in a corporate press release.
Perhaps ironically, that discussion also starts from overanalyzing another few words in that very same press release.

According to Microsoft’s blog post about the licensing deal, GPT-3 “is trained on Azure’s AI supercomputer.” I wonder if that means OpenAI is now using Microsoft’s open-source [DeepSpeed library](https://github.com/microsoft/DeepSpeed?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) ([#34](https://dynamicallytyped.com/issues/34-google-s-app-for-detecting-fake-news-memes-an-ai-for-logical-reasoning-and-microsoft-s-library-for-training-trillion-parameter-models-227577?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) to train its GPT models.
DeepSpeed is a library for distributed training of enormous ML models that has specific features to support training large Transformers; Microsoft Research claimed in May that it’s capable of training models with up to 170 billion parameters ([#40](https://dynamicallytyped.com/issues/40-pinterest-s-ml-for-board-organization-gan-aided-pixel-art-and-bayesian-optimization-gets-the-distill-treatment-247582?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
GPT-3 is a 175-billion-parameter Transformer that was released in June, just one month later.
That seems unlikely to be a coincidence, and Microsoft’s [latest DeepSpeed update](https://www.microsoft.com/en-us/research/blog/deepspeed-extreme-scale-model-training-for-everyone/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) ([#49](https://dynamicallytyped.com/issues/49-movement-in-autonomous-trucking-microsoft-s-deepspeed-update-and-transformers-as-graph-neural-networks-277883?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) even includes some experimental work using the GPT-3 architecture.

So this suggests that the partnership goes beyond just the exchange of Microsoft’s money and compute for OpenAI’s trained models and ML brand strength (an exchange of cloud for clout, if you will) that we [previously expected](https://twitter.com/soumithchintala/status/1153308199610511360/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Are the companies actually also deeply collaborating on ML and systems engineering research?
I’d love to find out.

If so, this could be an early indication that Microsoft — who I’m sure is at least a little bit envious of Google’s ownership of DeepMind — will eventually want to acquire OpenAI.
And it could be a great fit.
Looking at Microsoft’s recent acquisition history, it has so far let GitHub (which it acquired two years ago) continue to operate largely autonomously.
This makes it an attractive potential parent company for OpenAI: the lab probably wouldn’t have to give up too much of its independence under Microsoft’s stewardship.
So unless OpenAI actually invents and monetizes some form of artificial general intelligence (AGI) in the next five to ten years — which I don’t think they will — I wouldn’t be surprised if they end up becoming Microsoft’s DeepMind.

\* One big reason for not open-sourcing GPT-3’s code and data is security; see my coverage of OpenAI’s staged release strategy for GPT-2 ([#8](https://dynamicallytyped.com/issues/8-should-openai-open-source-their-impressive-new-language-model-161119?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [#13](http://%20http://dynamicallytyped.com/issues/13-caption-this-new-ai-powered-features-at-google-i-o-and-openai-s-staged-gpt-2-release-175669), [#22](https://dynamicallytyped.com/issues/22-mobile-apps-that-identify-plant-species-ai-powered-posture-correction-and-my-new-job-197292?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [#27](https://dynamicallytyped.com/issues/27-google-s-teachable-machine-2-0-openai-s-gpt-2-xl-and-capturing-solar-energy-with-ai-209719?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).