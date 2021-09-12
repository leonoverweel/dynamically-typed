---
category: ml-research
date: 2021-09-12
emoji: "\U0001F50E"
issue_number: 74
title: DeepMind's multimodal Perceiver IO
---

[Perceiver IO](https://deepmind.com/blog/article/building-architectures-that-can-handle-the-worlds-data?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is DeepMind’s new general-purpose architecture for processing a wide variety of input modalities — like images, videos, 3D point clouds, and sounds — into output vectors.
First, [Perceiver](https://arxiv.org/abs/2103.03206?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (without the IO) scaled Transformers’ concept of attention to much larger input sizes, “without introducing domain-specific assumptions,” by first encoding the inputs to a small fixed-size latent array and attending over that.
Now, Perceiver IO ([arXiv](https://arxiv.org/abs/2107.14795?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [GitHub](https://github.com/deepmind/deepmind-research/tree/master/perceiver?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) extends this by also applying attention to the decoding side, so that one input can produce multiple outputs and both the inputs and outputs can be a mix of modalities.
“This opens the door for all sorts of applications, like understanding the meaning of a text from each of its characters, tracking the movement of all points in an image, processing the sound, images, and labels that make up a video, and even playing games, all while using a single architecture that’s simpler than the alternatives.” With OpenAI releasing [DALL·E and CLIP](https://dynamicallytyped.com/stories/2021/openai-dall-e-clip/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and Stanford HAI launching [the Foundation Models research center](https://crfm.stanford.edu?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), both also this year, these large multimodal networks have become a central focus of leading AI labs.