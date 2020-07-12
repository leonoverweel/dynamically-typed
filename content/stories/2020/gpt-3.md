---
category: ml-research
data: 2020-06-21
issue_number: 42
title: 'OpenAI''s GPT-3: a language model that doesn''t need finetuning'
---

**OpenAI announced GPT-3, the next generation of its language model.**
As we’re used to by now, it’s another order of magnitude bigger than previous models, at 175 billion parameters—compared to 1.5 billion for GPT-2 and 17 billion for Microsoft’s Turing NLG ([DT #33](https://dynamicallytyped.com/issues/33-billie-eilish-answers-ai-generated-interview-questions-visual-search-for-aerial-imagery-and-the-tech-won-t-drill-it-pledge-224742?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
It’s not the model’s size that’s interesting, though, but what this enables.
From the abstract of the 74-page paper by [Brown et al.
(2020)](https://arxiv.org/abs/2005.14165?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) detailing GPT-3:

> Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches.
> … For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model.

This is super cool!
Where GPT-2 could only complete a passage from a given input in a natural-sounding way, GPT-3 can now do several tasks just from being shown examples.
Instead of fine-tuning the model for specific tasks like translation, question-answering, or [generating podcast episode titles that do not exist](https://twitter.com/layon_overwhale/status/1271350574815088643?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (👀), the model can do everything out of the box.
For example, if you feed it several questions and answers prefixed with “Q:” and “A:” respectively, followed by a new question and “A:”, it’ll continue the passage by answering the question—without ever having to update its weights!
Other example include parsing unstructured text data into tables, improving English-language text, and even turning natural language into Bash terminal commands (but can it do git?).

OpenAI rolled out its previous model in stages, starting with a 117-million parameter version (“117M”) in February 2019 ([DT #8](https://dynamicallytyped.com/issues/8-should-openai-open-source-their-impressive-new-language-model-161119?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), followed by 345M in May of that year ([DT #13](https://dynamicallytyped.com/issues/13-caption-this-new-ai-powered-features-at-google-i-o-and-openai-s-staged-gpt-2-release-175669?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), 774M in September with a six-month follow up blog post ([DT #22](https://dynamicallytyped.com/issues/22-mobile-apps-that-identify-plant-species-ai-powered-posture-correction-and-my-new-job-197292?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), and finally the full 1.5-billion parameter version in November ([DT #27](https://dynamicallytyped.com/issues/27-google-s-teachable-machine-2-0-openai-s-gpt-2-xl-and-capturing-solar-energy-with-ai-209719?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
The lab is doing the same for GPT-3, which is also the first model that it’s making commercially available [in the form of an API](https://beta.openai.com/?demo=2&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Just a few vetted organizations have had access to the API so far.
Ashlee Vance [for Bloomberg](https://www.bloomberg.com/news/articles/2020-06-11/trillions-of-words-analyzed-openai-sets-loose-ai-language-colossus?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

> To date, Casetext has been using the technology to improve its legal research search service, MessageBird has tapped it for customer service, and education software maker Quizlet has used it to make study materials.

Janelle Shane als has access to GPT-3, and she has used the API [to make some “spookily good Twitter bots”](https://aiweirdness.com/post/620645957819875328/this-is-the-openai-api-it-makes-spookily-good/amp?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) on her AI Weirdness blog.

I’m glad OpenAI staging the release of their API this way again, since valid criticism has already started popping up: Anima Anandkumar [pointed out on Twitter](https://twitter.com/AnimaAnandkumar/status/1271137176529416193?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that the GPT-2 has “produced shockingly racist and sexist paragraphs without any cherry picking.” (Also see [this follow-up discussion](https://twitter.com/erikbryn/status/1271544917412610048?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) with OpenAI policy director Jack Clark.) These type of bias problems have to be worked out before the model can responsibly be released beyond a few trusted partners, which OpenAI CEO Sam Altman also acknowledged this in Vance’s piece:

> As time goes on, more organizations will gain access, and then the API will be public.
> “I don’t know exactly how long that will take,” Altman said.
> “We would rather be on the too-slow than the too-fast side.
> We will mistakes here, and we will learn.”

As the OpenAI API gets released more broadly and integrated into more products, I’ll keep following its progress.