---
category: productized-ai
data: 2020-08-16
issue_number: 46
title: Snapchat's platform for creative ML models
---

![](https://s3.amazonaws.com/revue/items/images/006/383/892/mail/3ad60a6dab191b0421bba5cd9f7577f6.png?1597579662)

**SnapML is a software stack for building Lenses that use machine learning models to interact with the Snapchat camera.**
You can build and train a model in any ONNX-compatible framework (like TensorFlow or PyTorch) and drop it straight into Snapchat’s [Lens Studio](https://lensstudio.snapchat.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) as a SnapML component.
SnapML can then apply some basic preprocessing to the camera feed, run it through the model, and format the outputs in a way that other Lens Studio components can understand.
A segmentation model outputs a video mask, an object detection outputs bounding boxes, a style transfer model outputs a new image, etc.
You even have control over how the model runs: once every frame, in the background, or triggered by a user action.
(More details in the [docs](https://lensstudio.snapchat.com/guides/machine-learning/ml-overview/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).)

Matthew Moelleman has written some great in-depth coverage on SnapML for the [Fritz AI Heartbeat blog](https://heartbeat.fritz.ai?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), including a [technical overview](https://heartbeat.fritz.ai/exploring-snapml-a-technical-overview-45d37114fe81?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and a [walkthrough of making a pizza segmentation Lens](https://heartbeat.fritz.ai/exploring-snapml-working-with-custom-neural-networks-in-lens-studio-57459a51cb3d?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
As he notes, SnapML has the potential to be super interesting as a platform:

> Perhaps most importantly, because these models can be used directly in Snapchat as Lenses, they can quickly become available to millions of users around the world.

Indeed, if you create an ML-powered Snapchat filter in Lens Studio, you can easily [publish and share it using a Snapcode](https://lensstudio.snapchat.com/guides/sharing/sharing-your-lens/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which users can scan to instantly use the Lens in their snaps.
I don’t think any other platform has such a streamlined (no-code!) system for distributing trained ML models directly to a user base of this size.
Early SnapML user Hart Woolery, also [speaking to Heartbeat](https://heartbeat.fritz.ai/lens-studio-3-0-introduces-snapml-for-adding-custom-neural-networks-directly-to-snapchat-c2c32ed95b2b?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

> It’s a game-changer.
> At least within the subset of people working on live-video ML models.
> This now becomes the easiest way for ML developers to put their work in front of a large audience.
> I would say it’s analogous to how YouTube democratized video publishing.
> It also lowers the investment in publishing, which means developers can take increased risks or test more ideas at the same cost.

Similar to YouTube, the first commercial applications of SnapML have been marketing-related: there’s already a [process for submitting sponsored Lenses](https://lensstudio.snapchat.com/guides/submission/sponsored-lenses/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which can of course include an ML component.
It’s not too hard to imagine that some advertising agencies will specialize in building SnapML models that, for example, segment Coke bottles or classify different types of Nike shoes in a Lens.
I bet you can bootstrap a pretty solid company around that pitch.

Another application could be Lenses that track viral challenges: count and display how many pushups someone does, or whether they’re getting all the steps right for a TikTok dance.
Snapchat is [building many of these things itself](https://www.theverge.com/2020/8/13/21365330/snapchat-augmented-reality-lens-tiktok-dance-dixie-damelio?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), but the open platform leaves lots of room for creative ML engineers to innovate—and even get a share of this year’s [$750,000 Official Lens Creators fund](https://adage.com/article/digital/snapchat-commits-750000-ar-influencers/2216611?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
(See some of the creations that came out of the fund [here](https://lensstudio.snapchat.com/news/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).)

The big question for me is whether and how Snapchat will expand these incentives for creating ML-powered Lenses.
The Creators fund tripled in size from 2019 to 2020; will we see it grow again next year?
Or are we going to get an in-app Snapchat store for premium Lenses with revenue sharing for creators?
In any case, I think this will be a very exciting space to follow over the next few years.