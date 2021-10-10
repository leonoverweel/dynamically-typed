---
category: ml-research
date: 2021-09-26
emoji: "\U0001F4DA"
issue_number: 75
title: OpenAI Summarizing Books
---

[Wu et al.
(2021)](https://arxiv.org/abs/2109.10862?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) at OpenAI used a fine-tuned [GPT-3](https://dynamicallytyped.com/stories/2020/gpt-3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to recursively summarize books.
The model first separately summarizes sections of a book, then concatenates those summaries together and summarizes the result, and continues the process until it converges on a concise summary of the entire book.
This works surprisingly well!
For _Romeo and Juliet_ , as visualized on the [Summarizing Books](https://openai.com/blog/summarizing-books/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) demo page, this process takes it from 25,433 words (the whole play), to 5,809 words (72 summaries of sections), to 692 words (7 summaries of section summaries), to 116 words (the final summary).
The result is usually a bit worse than an “average” human summarizer, but importantly this recursive process allows researchers to trace back how the model constructed the summary: What part of the book was the source of this plot point in the summary?
What parts of lower-level summaries did the model not deem important enough to include in a higher level?
Constructing models in such a way that these kinds of questions can be answered are part of OpenAI’s larger research effort into the _alignment problem:_ to “ensure that machine learning models act in accordance with human intentions.” (A core part of [their mission](https://openai.com/about/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).)