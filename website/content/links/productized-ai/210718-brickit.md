---
category: productized-ai
date: 2021-07-18
emoji: "\U0001F9F1"
issue_number: 70
title: Brickit
---

[Brickit](https://brickit.app?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is an [iOS app](https://apps.apple.com/nl/app/brickit-rebuild-your-lego/id1477221636?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that uses computer vision to identify LEGO bricks in a big pile and then [shows you a list of projects you can build with those bricks](https://twitter.com/AlexanderNL/status/1410253599502962692?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) — with instructions!
The most impressive part is that it can detect so many small objects with so many different classes in one photo.
I’d guess it does this by tiling the image or sliding a window over the photo, and then running the smaller images through some custom model powered by [Core ML](https://developer.apple.com/documentation/coreml?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and the iPhone’s neural engine; but I can’t find information much about how the app works exactly.
Brickit is a great example of productized AI: its core functionality is enabled by a highly-complex machine learning, but it abstracts this away into a simple user interface.