---
category: productized-ai
date: 2021-05-23
emoji: "\U0001F426"
issue_number: 66
title: 'Removing AI features: Twitter''s biased cropping algorithm'
---

A bit different from usual on DT: the following is a good example of _removing_ an AI-powered feature from a product.
Late last year, Twitter users began to notice that the app’s photo cropping algorithm (which decides what portion of an image to show as preview in the timeline) [seemed to favor white faces over Black faces](https://www.theverge.com/2020/9/20/21447998/twitter-photo-preview-white-black-faces?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
The simple [saliency algorithm](https://arxiv.org/abs/1801.05787?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) doesn’t look for faces specifically but rather tries to predict what part of an image a user would look at first, and no one thought to check it for this bias.
Twitter has now solved the problem by no longer cropping images at all, instead displaying standard aspect ratio images in full (which I think is better anyway.) Director of Software Engineering Rumman Chowdhury wrote [an excellent blog post](https://blog.twitter.com/engineering/en_us/topics/insights/2021/sharing-learnings-about-our-image-cropping-algorithm.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) about how the company handled this issue, including details of its own ([open-source](https://github.com/twitter-research/image-crop-analysis?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) [study](https://arxiv.org/abs/2105.08667?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that confirmed the algorithm’s biases.
“One of our conclusions is that not everything on Twitter is a good candidate for an algorithm, and in this case, how to crop an image is a decision best made by people.”