---
category: productized-ai
date: 2020-04-26
issue_number: 38
title: Bias reductions in Google Translate
---

![Gender-specific translations from Persian, Finnish, and Hungarian in the new Google Translate.](https://s3.amazonaws.com/revue/items/images/005/878/035/mail/8a2e6600f8b13d8f8d48a4ff11d55c09.png?1587831046)

_Gender-specific translations from Persian, Finnish, and Hungarian in the new Google Translate._

**Google is continuing to reduce gender bias in its Translate service.**
Previously, it might translate “o bir doktor” in Turkish, a language that does not use gendered pronouns, to “he is a doctor"—assuming doctors are always men—and "o bir hemşire” to “she is a nurse"—assuming that nurses are always women.
This is a very common example of ML bias, to the point that it’s covered in introductory machine translation courses like the one I took in Edinburgh last year.
That doesn’t mean it’s easy to solve, though.

Back in December 2018, Google took a first step toward reducing these biases [by providing gender-specific translations in Translate](https://ai.googleblog.com/2018/12/providing-gender-specific-translations.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for Turkish-to-English phrase translations, like the example above, and for single word translations from English to French, Italian, Portuguese, and Spanish ([DT #3](https://dynamicallytyped.com/issues/3-happy-holidays-149573?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
But as they worked to expand this into more languages, they ran into scalability issues: only 40% of eligible queries were actually showing gender-specific translations.

![Google's original and new approaches to gender-specific translations.](https://s3.amazonaws.com/revue/items/images/005/878/845/mail/c4d7d7d487b38df5a92fe0d1d3ab11a5.png?1587883650)

_Google's original and new approaches to gender-specific translations._

[They’ve now overhauled the system](https://ai.googleblog.com/2018/12/providing-gender-specific-translations.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter): instead of attempting to detect whether a query is gender-neutral and then generating two gender-specific translations, it now generates a default translation and, if this translation is indeed gendered, also rewrites it to an opposite-gendered alternative.
This rewriter uses a custom dataset to “reliably produce the requested masculine or feminine rewrites 99% of the time.” As before, the UI shows both alternatives to the user.

Another interesting aspect of this update is how they evaluate the overall system:

> We also devised a new method of evaluation, named _bias reduction,_ which measures the relative reduction of bias between the new translation system and the existing system.
> Here “bias” is defined as making a gender choice in the translation that is unspecified in the source.
> For example, if the current system is biased 90% of the time and the new system is biased 45% of the time, this results in a 50% relative bias reduction.
> Using this metric, the new approach results in a bias reduction of ≥90% for translations from Hungarian, Finnish and Persian-to-English.
> The bias reduction of the existing Turkish-to-English system improved from 60% to 95% with the new approach.
> Our system triggers gender-specific translations with an average precision of 97% (i.e., when we decide to show gender-specific translations we’re right 97% of the time).

The standard academic metrics (recall and average precision) did not answer the most important question about the two different approaches, so the developers came up with a new metric specifically to evaluate relative bias reduction.
Beyond machine translation, this is a nice takeaway for productized AI in general: building the infrastructure and metrics to measure how your ML system behaves in its production environment is at least as important as designing the model itself.

In the [December 2018 post announcing gender-specific translations](https://ai.googleblog.com/2018/12/providing-gender-specific-translations.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), the authors mention that one next step is also addressing non-binary gender in translations; this update does not mention that, but I hope it’s still on the roadmap.
Either way, it’s commendable that Google has continued pushing on this even after the story has been out of the media for a while now.