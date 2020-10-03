---
category: ml-research
date: 2020-07-05
emoji: "\U0001F4B1"
issue_number: 43
title: Google Translate 600B transformer
---

Today in gargantuan language models: Google’s new state-of-the-art model for translating from 100 languages to English has _600 billion parameters_.
Compare this to OpenAI’s GPT-3 at 175 billion parameters from June (see [DT #42](https://dynamicallytyped.com/issues/42-facial-recognition-exodus-openai-s-new-gpt-3-language-model-and-oil-in-the-cloud-254772?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) and Microsoft’s Turing-NLG at 17 billion parameters from February ([DT #33](https://dynamicallytyped.com/issues/33-billie-eilish-answers-ai-generated-interview-questions-visual-search-for-aerial-imagery-and-the-tech-won-t-drill-it-pledge-224742?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
Google’s 600 billion-parameter Transformer took four days to train on 2048 (!) TPUs, which is actually relatively little for that model size.
This training process is therefore also the focus of the paper describing the model: [Lepikhin et al.
(2020)](https://arxiv.org/abs/2006.16668?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) introduce GShard, “an elegant way to express a wide range of parallel computation patterns with minimal changes to the existing model code.”