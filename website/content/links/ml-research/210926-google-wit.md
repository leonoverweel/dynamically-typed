---
category: ml-research
date: 2021-09-26
emoji: "\U0001F5C3"
issue_number: 75
title: Wikipedia-based image-text dataset
---

Big AI labs’ focus on multimodal neural networks — architectures that combine different types of input and output data, like images and text — continues.
After OpenAI’s [DALL·E and CLIP](https://dynamicallytyped.com/stories/2021/openai-dall-e-clip/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Stanford HAI’s [Foundation Models](https://crfm.stanford.edu/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and DeepMind’s [Perceiver IO](https://dynamicallytyped.com/links/ml-research/210912-deepmind-perceiver-io-multimodal/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Google AI has now announced [WIT: a Wikipedia-based image-text dataset](https://ai.googleblog.com/2021/09/announcing-wit-wikipedia-based-image.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Bridging the gap between human-annotated image captions (too labor-intensive) and broad web-scraped ones (too messy and English-centric), [Srinivasan et al.
(2021)](https://dl.acm.org/doi/10.1145/3404835.3463257?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) created WIT by “extracting multiple different text selections associated with an image from Wikipedia articles and Wikimedia image links.” This results in a Creative Commons-licensed dataset of 37.5 million image-text examples, across 11.5 million unique images and 108 languages.
Until now these big multimodal models have mostly been trained on proprietary datasets by large private labs; this open dataset should help lower the barrier to entry for university labs to research similar models.