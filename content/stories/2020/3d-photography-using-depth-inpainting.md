---
category: cool-things
date: 2020-04-12
issue_number: 37
title: 3D photography using depth inpainting
---

![Layered depth inpainting. (Shih et al., 2020)](https://s3.amazonaws.com/revue/items/images/005/809/755/mail/aeb49373886c4e9513730e682e292d7c.png?1586634824)

_Layered depth inpainting. (Shih et al., 2020)_

Here’s another cool AI art piece that can’t be done justice using just the static screenshot above: Shih et al. (2020) published [**3D Photography using Context-aware Layered Depth Inpainting**](https://shihmengli.github.io/3D-Photo-Inpainting/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) at this year’s CVPR conference.
Here’s what that means:

> We propose a method for converting a single RGB-D input image into a 3D photo, i.e., a multi-layer representation for novel view synthesis that contains hallucinated color and depth structures in regions occluded in the original view.

Based on a single image (plus depth information), they can generate a 2.5-dimensional representation, realistically re-rendering the scene from slightly different perspectives from which it was originally taken.
Contrast that with recent work on neural radiance fields, which requires on the order of 20 - 50 images to work (see [DT #36](https://dynamicallytyped.com/issues/36-google-releases-tensorflow-quantum-software-2-0-at-plumerai-and-encoding-scenes-in-neural-networks-233576?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).

Shih et al. set up [a website with some fancy demos](https://shihmengli.github.io/3D-Photo-Inpainting/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which is definitely worth a look; see [these gifs on Twitter too](https://twitter.com/genekogan/status/1248650281249673217?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
One of the authors also works at Facebook, so I wonder if we’ll one day see Instagram filters with this effect—or if it’ll be a part of Facebook’s virtual reality ambitions.
Since the next generation of iPhones will likely have a depth sensor on the back too, I expect we’ll see a lot of this 2.5D photography stuff in the coming years.