# #12: OpenAI introduces Mozart to Lady Gaga, and Google takes your best duck-face selfies for you 

Hey everyone, welcome to the 12th edition of Dynamically Typed!
In the past two weeks, both Google and OpenAI showed off new research ranging from complex deep learning architectures to charming machine learning applications: Google open-sourced a network architecture shrinking tool called MorphNet, and automated taking selfies with Photobooth; OpenAI improved on the concept of _attention_ with Sparse Transformers, and generated music with MuseNet.
Other news includes remove.bg’s new Photoshop plugin, Ben Evan’s notes on AI bias, and a few more useful ML resources I found.

## Productized Artificial Intelligence 🔌

!["Photobooth automatically captures group shots, when everyone in the photo looks their best." (Google)](https://s3.amazonaws.com/revue/items/images/004/522/713/mail/c58d481578f6dd7e00a7b511f8177a03.png?1556388688)
_"Photobooth automatically captures group shots, when everyone in the photo looks their best." (Google)_

**Google’s Pixel phones have a new feature called Photobooth that captures selfies at exactly the right time.**
The app tracks people in the frame of your selfie and makes sure that everyone is looking at the camera and that no one is blinking.
It then uses an [Image Content Model](https://ai.googleblog.com/2018/05/automatic-photography-with-google-clips.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that looks for five expressions (smiles 😀, tongue-out 😝, duck face 😙, puffy-cheeks 🐡, and surprise 😮) and triggers an image capture when it sees one.
This is just the latest of all the machine learning-powered photography features that Google has been adding to its Pixel phones (see also [Night Sight](https://www.theverge.com/2018/11/14/18092660/google-night-sight-review-pixel-2-3-camera-photos-image-quality?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), and it’s definitely the biggest thing I’m jealous of as an iPhone user.
More details of how Photobooth works are on Google’s AI blog: [Take Your Best Selfie Automatically, with Photobooth on Pixel 3](https://ai.googleblog.com/2019/04/take-your-best-selfie-automatically.html?m=1&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Remove.bg, which automatically removes backgrounds from photos, now has a Photoshop plugin.**
The service launched with a demo site about four months ago (see [DT #3](https://www.getrevue.co/profile/dynamically-typed/issues/3-happy-holidays-149573?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), and quickly after also added a paid tier for processing high-resolution images (see [DT #6](https://dynamicallytyped.com/issues/6-deep-reinforcement-learning-from-an-atari-zoo-to-a-self-driving-car-in-20-minutes-155882?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
Previously, you had to go to [remove.bg](https://remove.bg?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), upload an image, wait for it to process, and then download it again.
Now with the new extension, Photoshop users can simply click a button inside the app to automatically remove the background of the current layer and generate a transparency mask.
I’ve loved following this product’s evolution—it’s the perfect example of the kind of productized AI I try to cover here—and it’s great to see its creators continuing to ship cool features like this one.
Read their blog post here: [Announcing remove.bg for Photoshop](https://www.remove.bg/b/remove-bg-photoshop?ref=producthunt&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Benedict Evans published some of his notes on AI bias.**
He lays out a clear perspective of where bias in productized machine learning systems comes from—"a system for finding patterns in data might find the wrong patterns, and you might not realise"—and what to do about it:

> You can divide thinking in the field into three areas: (1) methodological rigour in the collection and management of the training data; (2) technical tools to analyse and diagnose the behavior of the model; and (3) training, education and caution in the deployment of ML in products.

He also argues that the big-name companies and research groups should probably worry us less than “third-tier vendors” that sell ML-powered technology to non-technical customers: the former group is full of people who know (and worry) about AI bias, while the latter’s customers may not even know the right questions to ask about the limitations of the systems they’re buying.
Read Evan’s full post here: [Notes on AI Bias](https://www.ben-evans.com/benedictevans/2019/4/15/notes-on-ai-bias?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Machine Learning Technology 🎛

![Image completions by the Sparse Transformer model. (OpenAI)](https://s3.amazonaws.com/revue/items/images/004/522/961/mail/d15e3063efb7b34a83465b4042c92159.png?1556400476)
_Image completions by the Sparse Transformer model. (OpenAI)_

**OpenAI’s Sparse Transformers model set records at sequence prediction tasks in text, image and sound data.**
It’s an attention-based model:

> In Transformers, every output element is connected to every input element, and the weightings between them are dynamically calculated based upon the circumstances, a process called _attention_.
> While it is believed that this allows Transformers to be more flexible than models with fixed connectivity patterns, in practice it requires the creation of an _N_ × _N_ _attention matrix_ for every layer and attention head, which can consume large amounts of memory when applied to data types with many elements, like images or raw audio.

One of the biggest contributions by authors Rewon Child et al.
is an O(N×sqrt(N)) reformulation of Transformer self-attention, compared to the previous O(N×N) formulation.
This allowed them to attack problems with larger data sizes (like images and audio) and longer-distance dependencies within the data, beating the state of the art for the density estimation task on CIFAR-10, Enwik8, and Imagenet 64.
Although this is an impressive improvement, the authors think it can be taken further in combination with multi-scale approaches.
More:

- Rewon Child and Scott Gray on the OpenAI blog: [Generative Modeling with Sparse Transformers](https://openai.com/blog/sparse-transformer/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Paper by Child et al. (2019): [Generating Long Sequences with Sparse Transformers](https://arxiv.org/pdf/1904.10509.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (PDF)
- Code: [openai/sparse_attention](https://github.com/openai/sparse_attention?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (GitHub)

**Google has open-sourced a TensorFlow implementation of MorphNet,** a tool that “takes an existing neural network as input and produces a new neural network that is smaller, faster, and yields better performance tailored to a new problem.” MorphNet works in a cycle of two phases: a _shrinking_ phase that prunes inefficient neurons from the network, and an _expanding_ phase that uniformly grows all layers using a width multiplier.
Together, these two phases result in computation (in terms of FLOPs or model size) being reallocated to places where it is most effective.
When applied to the [Inception V2 network](https://arxiv.org/abs/1502.03167?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) trained on [Imagenet](http://www.image-net.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), MorphNet reduces FLOPs per inference by 11-15% without degrading the accuracy.
More:

- Andrew Poon on the Google AI Blog: [MorphNet: Towards Faster and Smaller Neural Networks](http://ai.googleblog.com/2019/04/morphnet-towards-faster-and-smaller.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Paper by Gordon et al. (2018): [MorphNet: Fast & Simple Resource-Constrained Structure Learning of Deep Networks](https://arxiv.org/pdf/1711.06798.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (PDF)

**Adam King wrote an in-depth explanation of how GauGAN works.**
NVIDIA’s GauGAN tool that can automatically transform sketches into photorealistic landscapes (see [DT #10](https://dynamicallytyped.com/issues/10-a-turing-award-for-deep-learning-and-a-bitter-lesson-for-ai-research-166903?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) is powered by a recent Generative Adversarial Network (GAN) architecture called SPADE.
King’s excellent post explains everything from the original Goodfellow GAN and pix2pixHD, to the problems with these methods and how SPADE solves them.
Read it here: [Photos from Crude Sketches: NVIDIA’s GauGAN Explained Visually](https://adamdking.com/blog/gaugan/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Quick ML resource links ⚡️**

- Andrej Karpathy (director of AI + Autopilot Vision at Tesla) shared some practical deep learning tips: [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
- Rachel Thomas (cofounder of [fast.ai](https://www.fast.ai/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) shared two sets of pragmatic tips for improving AI ethics in your organization: [16 Things You Can Do to Make Tech More Ethical, part 1](https://www.fast.ai/2019/04/22/ethics-action-1/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); [part 2](https://www.fast.ai/2019/04/25/ethics-action-2/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Cool Things ✨

![My favorite clip generated by MuseNet: Lady Gaga's Poker Face, continued in the style of Mozart. (OpenAI)](https://s3.amazonaws.com/revue/items/images/004/523/026/mail/d5221ee470c6057aa1006b2c23d06c14.png?1556404969)
_My favorite clip generated by MuseNet: Lady Gaga's Poker Face, continued in the style of Mozart. (OpenAI)_

**Christine Payne (OpenAI) released MuseNet, “a deep neural network that can generate 4-minute musical compositions with 10 different instruments,** and can combine styles from country to Mozart to the Beatles.” It uses the same unsupervised technology as OpenAI’s GPT-2 language model (see [DT #8](https://dynamicallytyped.com/issues/8-should-openai-open-source-their-impressive-new-language-model-161119?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) and it’s super fun to play around with.
Check it out here:

- The main interactive site on OpenAI’s blog: [MuseNet](https://openai.com/blog/musenet/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- A “concert” of things generated using the model, live streamed on the day MuseNet was released: [MuseNet Concert](https://www.twitch.tv/videos/416276005?t=&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Twitch)

**@eukaryote trained OpenAI’s GPT-2 language model on r/ShowerThoughts,** where Reddit users share odd realizations they’ve had in the shower, and set up a site that generates new such thoughts.
Some of my favorites:

> The last time you ate a hot dog was during dinner

> The internet would be very different if all of us had a phone for our eyes.

> If there was an AI/machine learning/machine learning and artificial intelligence, i bet most of the people i know were probably scared of it.

Check it out at [BotThoughts](https://eukaryote31.github.io/bot-thoughts/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
(Thanks for sharing, [Steinar](https://twitter.com/SteinarLaenen?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)!)

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
😁