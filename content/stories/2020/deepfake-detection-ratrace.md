---
category: productized-ai
date: 2020-09-13
issue_number: 48
title: The deepfake detection ratrace
---

![](https://s3.amazonaws.com/revue/items/images/006/499/462/mail/1b6f5cdb2d383c1993c1d76546c3d679.png?1599928722)

[**Microsoft is launching Video Authenticator**](https://blogs.microsoft.com/on-the-issues/2020/09/01/disinformation-deepfakes-newsguard-video-authenticator/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **, an app that helps organizations “involved in the democratic process” detect deepfakes** — videos that make people look like they’re saying things they’ve never said by superimposing automatically-generated voice tracks and face movements over real videos.
Deepfakes are usually made using generative adversarial networks (GANs) like those in [Samsung AI’s neural avatars project](https://arxiv.org/abs/1905.08233?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (see [DT #15](https://dynamicallytyped.com/issues/15-neural-avatars-ai-on-the-edge-and-apple-s-new-create-ml-app-180967?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) and in the popular open-source [DeepFaceLab app](https://github.com/iperov/DeepFaceLab?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

Because of all the obvious ways in which deepfakes can be abused, this has been a popular research area for technology platform companies: a bit over a year ago, Facebook launched their [deepfake detection challenge](https://ai.facebook.com/datasets/dfdc/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and Google contributed to TU Munich’s [FaceForensics benchmark](http://kaldir.vc.in.tum.de/faceforensics_benchmark/index.php?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) ([#23](https://dynamicallytyped.com/issues/23-robotic-raspberry-and-lettuce-pickers-2-5-billion-objects-in-pinterest-lens-and-an-analysis-of-the-ai-reproducibility-crisis-199555?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
Microsoft has now productized these research efforts with Video Authenticator.
The app checks photos and videos for the “subtle fading or greyscale elements” that may occur at a deepfake’s blending boundary — where the fake facial movements mix in with the real background media — and gives users a confidence score for whether a face is manipulated.
This happens in real-time and frame-by-frame for videos, which I imagine will be particularly useful for detecting subtle fakery, like a mostly-real video with a few small tweaks that change its message.

Video Authenticator initially won’t be made publicly available.
Instead, Microsoft is privately distributing it to news outlets, political campaigns, and media companies through the AI Foundation’s [Reality Defender 2020](https://rd2020.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) program, “which will guide organizations through the limitations and ethical considerations inherent in any deepfake detection technology.” This makes sense, since deepfakes represent a typical cat-and-mouse AI security game — new models will surely be trained specifically to fool Video Authenticator, which this limited release approach attempts to slow down.

I’d be interested to learn about how organizations integrate Video Authenticator into their existing workflows for validating the veracity of newsworthy videos.
I haven’t really come across any examples of big-name news organizations getting fooled by deepfakes yet, but I imagine it’s much more common on social media where videos aren’t vetted by journalists before being shared.