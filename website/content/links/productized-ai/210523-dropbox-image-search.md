---
category: productized-ai
date: 2021-05-23
emoji: "\U0001F526"
issue_number: 66
title: How image search works at Dropbox
---

Thomas Verg wrote about [How image search works at Dropbox](https://dropbox.tech/machine-learning/how-image-search-works-at-dropbox?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for the company’s blog.
Their algorithm uses a combination of image classification to extract relevant ImageNet-style labels from photos (like “beach” or “hotdog”), and word vectors to match non-exact search terms to those labels (e.g.
“shore” or “[sandwich](https://cuberule.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)”).
The rest of the post goes into quite some depth on the production architecture and scalability optimizations in the algorithm’s deployment.
Always nice to see these technical deep dives on AI-powered features from product companies!