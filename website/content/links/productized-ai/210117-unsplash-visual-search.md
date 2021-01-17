---
category: productized-ai
date: 2021-01-17
emoji: "\U0001F4F8"
issue_number: 57
title: Visual Search in Unsplash
---

Creative Commons photo sharing site [Unsplash](https://unsplash.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (where I also [have a profile](https://unsplash.com/@leonoverweel?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)!) has launched a new feature: Visual Search, similar to Google’s search by image.
If you’ve found a photo you’d like to include in a blog post or presentation, for example, but the image is copyrighted, this new Unsplash feature will help you find similar-looking ones that are free to use.
The [launch post](https://unsplash.com/blog/introducing-visual-search/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) doesn’t go into detail about how Visual Search works, but I’m guessing some (convolutional) classification model extracts features from all images on Unsplash to create a high-dimensional embedding; the same happens to the image you upload, and the site can then serve you photos that are close together in this embedding space.
(Here’s an example of [how you’d build that in Keras](https://keras.io/examples/vision/metric_learning/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).)