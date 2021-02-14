---
category: productized-ai
date: 2021-02-14
emoji: "\U0001F4B1"
issue_number: 59
title: 'Speller100 in Bing: AI for input validation'
---

Jingwen Lu, Jidong Long and Rangan Majumder wrote [a blog post about Speller100](https://www.microsoft.com/en-us/research/blog/speller100-zero-shot-spelling-correction-at-scale-for-100-plus-languages/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Microsoft’s zero-shot spelling correction models that now collectively work across 100+ languages.
Speller100 is currently live in production as part of Microsoft’s Bing search engine, where it corrects typos in search queries — it’s what powers the “did you mean…” prompt.
Although this feature has been around for English-language search queries for a very long time, Speller100 newly enables it for a whole host of smaller languages.
It’s also an interesting case study of how an AI-powered refinement step of user input can significantly improve a product’s overall experience.
By A/B testing Speller100 against not having spelling correction, the researchers found that it reduced the number of pages with no results by 30%, and manual query reformatting by 5%; and that it increased the number of clicks on spelling suggestions by 67%, and clicks on any item on the page by 70%.