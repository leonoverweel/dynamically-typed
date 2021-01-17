---
category: ml-research
date: 2021-01-17
issue_number: 57
title: "DALL\xB7E and CLIP: OpenAI's Multimodal Neural Networks"
---

![Two example prompts and resulting generated images from DALL·E](https://s3.amazonaws.com/revue/items/images/007/075/268/mail/Screen_Shot_2021-01-17_at_10.59.57.png?1610877616)

_Two example prompts and resulting generated images from DALL·E_

**OpenAI’s new “multimodal”**[ **DALL·E**](https://openai.com/blog/dall-e/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **and**[ **CLIP**](https://openai.com/blog/clip/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **models combine text and images,** and also mark the first time that the lab has presented two separate big pieces of work in conjunction.
[In a short blog post](https://openai.com/blog/tags/multimodal/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which I’ll quote almost in full throughout this story because it also neatly introduces both networks, OpenAI’s chief scientist [Ilya Sutskever](https://openai.com/blog/authors/ilya?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) explains why:

> A long-term objective of artificial intelligence is to build “multimodal” neural networks—AI systems that learn about concepts in several modalities, primarily the textual and visual domains, in order to better understand the world.
> In our latest research announcements, we present two neural networks that bring us closer to this goal.

These two neural networks are DALL·E and CLIP.
We’ll take a look at them one by one, starting with **DALL·E.**

The name DALL·E is a nod to Salvador Dalí, the surrealist artist known for [that painting of melting clocks](https://en.wikipedia.org/wiki/The_Persistence_of_Memory?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and to WALL·E, the Pixar science-fiction romance about a waste-cleaning robot.
It’s a bit silly to name an energy-hungry image generation AI after a movie in which lazy humans have fled a polluted Earth to float around in space and do nothing but consume content and food, but given how well the portmanteau works and how cute the WALL·E robots are, I probably would’ve done the same.
Anyway, beyond what’s in a name, here’s Sutskever’s introduction of what DALL·E actually does:

> The first neural network, DALL·E, can successfully turn text into an appropriate image for a wide range of concepts expressible in natural language.
> DALL·E uses the same approach used for GPT-3, in this case applied to text–image pairs represented as sequences of “tokens” from a certain alphabet.

DALL·E builds on two previous OpenAI models, combining [GPT-3](https://arxiv.org/abs/2005.14165?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)’s capability to [perform different language tasks without finetuning](https://dynamically-typed.netlify.app/stories/2020/gpt-3/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) with [Image GPT](https://openai.com/blog/image-gpt/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)’s capability to generate coherent image completions and samples.
As input it takes a single stream — first text tokens for the prompt sentence, then image tokens for the image — of up to 1280 tokens, and learns to predict the next token given the previous ones.
Text tokens take the form of [byte-pair encodings](https://en.wikipedia.org/wiki/Byte_pair_encoding?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) of letters, and image tokens are patches from a 32 x 32 grid in the form of latent codes found using a variational autoencoder [similar to VGVAE](https://openai.com/blog/dall-e/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#fn2).
This relatively simple architecture, combined with a large, [carefully designed](https://twitter.com/AlexTamkin/status/1348581947736424448?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) dataset, gives DALL·E the following laundry list of capabilities, each of which have interactive examples in [OpenAI’s blog post](https://openai.com/blog/dall-e?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

* Controlling attributes
* Drawing multiple objects
* Visualizing perspective and three-dimensionality
* Visualizing internal and external structure (like asking for a macro or x-ray view!)
* Inferring contextual details
* Combining unrelated concepts
* Zero-shot visual reasoning
* Geographic and temporal knowledge

A lot of people from the community have written about DALL·E or played around with its interactive examples.
Some of my favorites include:

* DeepMind researcher Felix’s Hill’s [NonCompositional](https://fh295.github.io/noncompositional.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), a blog post on why DALL·E is good at composition without being very systematic (it can draw _a hedgehog-shaped lettuce_ but not _a green cube on a red cube on a blue cube_ )
* Károly Zsolnai-Fehér’s [Two Minute Papers video](https://www.youtube.com/watch?feature=youtu.be&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=C7D5EzkhT6A) on DALL·E, OpenAI’s previous work that led to it, and lots of generation examples
* Fun generations from Twitter and beyond: Janelle Shane’s [dawnings of DALL-E](https://aiweirdness.com/post/640120026320470016/the-drawings-of-dall-e?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); Oriol Vinyals’ [soap dispenser in the shape of a glacier](https://twitter.com/OriolVinyalsML/status/1347219207927320581?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); and Karol Hausman’s [snail made of a corkscrew](https://twitter.com/hausman_k/status/1346642324172861440?s=12&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

I think DALL·E is the more interesting of the two models, but let’s also take a quick look at **CLIP**.

![CLIP's performance on different image classification benchmarks.](https://s3.amazonaws.com/revue/items/images/007/075/525/mail/Screen_Shot_2021-01-17_at_13.13.08.png?1610885638)

_CLIP's performance on different image classification benchmarks._

Sutskever:

> CLIP has the ability to reliably perform a staggering set of visual recognition tasks.
> Given a set of categories expressed in language, CLIP can instantly classify an image as belonging to one of these categories in a “zero-shot” way, without the need to fine-tune on data specific to these categories, as is required with standard neural networks.
> Measured against the industry benchmark ImageNet, CLIP outscores the well-known ResNet-50 system and far surpasses ResNet in recognizing unusual images.

Instead of training on a specific benchmark like ImageNet or ObjectNet, CLIP pretrains on a large dataset of text and images scraped from the internet (so without specific human labels for each images).
It performs a proxy training task: “given an image, predict which out of a set of 32,768 randomly sampled text snippets, was actually paired with it in our dataset.” To then do actual classification on a benchmark dataset, the labels are transformed to be more descriptive (e.g.
a “cat” label becomes “a photo of a cat”), and CLIP calculates for each label how likely it is to be paired with the image.
It predicts the most likely one to be the label.
As you can see from the image above, this approach is highly effective across datasets.
It’s also very efficient because, being a zero-shot model, CLIP doesn’t need to be (re)trained or finetuned for different datasets.

My favorite application so far of CLIP is by [Travis Hoppe](https://twitter.com/metasemantic?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), who used it to [visualize poems using Unsplash photos](https://twitter.com/metasemantic/status/1349446585952989186?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) — worth a click!
Another interesting one is actually how it’s used in combination with DALL·E: after DALL·E generates 512 plausible images for a prompt, CLIP ranks their quality, and only the 32 best ones are returned in the interactive viewer.
Instead of researchers cherry-picking the best results to show in a paper, a different neural net can actually perform this task!