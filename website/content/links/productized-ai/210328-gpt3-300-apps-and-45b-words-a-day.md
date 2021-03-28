---
category: productized-ai
date: 2021-03-28
emoji: "\U0001F4F1"
issue_number: 62
title: 'GPT-3: 300 apps and 4.5B words a day'
---

After we saw GPT-3 — OpenAI’s [gargantuan language model that doesn’t need finetuning](https://dynamicallytyped.com/stories/2020/gpt-3/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) — used for [lots of cool demos](https://dynamicallytyped.com/stories/2020/gpt-3-demos-one-month-in/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), the model’s API now powers 300+ apps and outputs an average of 4.5 billion (!) words per day.
OpenAI published [a blog post](https://openai.com/blog/gpt-3-apps/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) describing some of these apps, including [Viable](https://askviable.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which summarizes and answers questions about survey responses, and [Agolia](https://www.algolia.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), a website plugin for semantically searching through content.
Cool stuff!
As the OpenAI API scales up to power more products, though, one thing to keep a close eye on will be how often it outputs problematic responses in production systems.
[Abid et al.
(2021)](https://arxiv.org/abs/2101.05783v2?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) have shown that [GPT-3 has a persistent anti-Muslim bias](https://onezero.medium.com/for-some-reason-im-covered-in-blood-gpt-3-contains-disturbing-bias-against-muslims-693d275552bf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and TNW’s Tristan Greene [got a GPT-3-powered chatbot to spit out racist and anti-LGBT slurs](https://thenextweb.com/neural/2020/09/24/gpt-3s-bigotry-is-exactly-why-devs-shouldnt-use-the-internet-to-train-ai/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
The OpenAI API runs a content filter on top of the raw GPT-3 model to prevent such responses from reaching end-users (which is pretty strict in my experience: when I was playing around with the beta, I couldn’t get it to say bad things without labeling them as potentially problematic) but no filter is ever perfect.
We’ll see what happens in the coming few years, but I do expect that the good and useful products will outweigh the occasional bad response.