# #16: Finding whales with AI, and 97 pages of ML for climate change 

Hey everyone, welcome to the 16th edition of Dynamically Typed!

In some personal news, I’ve moved to Amsterdam and started my MSc thesis internship at [Adyen](https://www.adyen.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Adyen is a payments processing company (like PayPal, Stripe, and WorldPay) that takes care of the online and in-store payments for merchants like Spotify, Netflix, Uber, and Bonobos.
For the next few months, I’m working on transfer learning for credit card fraud prediction models, as part of their Risk team.
So far, both Amsterdam and Adyen have been a blast and I’m super excited about my project!

Today’s edition of Dynamically Typed covers a new 97-page paper on how machine learning can help with the climate crisis, a tool for automatically filtering out background noise from conference calls, and an interactive website that visualizes thousands of hours of whale song.
On the research side, Facebook investigated cultural bias in commercial object detection systems, and Google launched a new football reinforcement learning environment.

## Artificial Intelligence for the Climate Crisis 🌍

![Tackling Climate Change with Machine Learning (Rolnick et al.)](https://s3.amazonaws.com/revue/items/images/004/721/750/mail/09dd3ca5fc53e8e5c3f4164793f2c045.png?1561188657)

_Tackling Climate Change with Machine Learning (Rolnick et al.)_

Researchers from several big AI institutions (see the author list above) have published **a 97-page paper on tackling the climate crisis with machine learning.**
It came out of its [namesake workshop](https://www.climatechange.ai/ICML2019_workshop.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) at the [2019 International Conference on Machine Learning](https://icml.cc/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (ICML), but it is aimed at a much broader audience than just AI researchers:

* Entrepreneurs and investors (to fill this “wide-open space” with companies)
* Corporate leaders (to make their companies greener)
* Local and national governments (to help decision-making)
* Researchers and engineers (to solve outstanding problems)

The paper is organized in sections for different application domains in which machine learning may be able to impact climate change, from electricity systems and transportation to tools for individuals and society.
Each solution is labeled as _high leverage_ , _long-term_ , and/or _high-risk_ , and includes references to relevant previous research that can be used to implement it.
More:

* Paper by Rolnick et al. on arXiv: [Tackling Climate Change with Machine Learning](https://arxiv.org/abs/1906.05433?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Website for the project: [Climate Change + AI](https://www.climatechange.ai/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* The workshop talks on SlidesLive: [Climate Change: How can AI Help?](https://slideslive.com/38917142/climate-change-how-can-ai-help?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

_Are you working on any of these solutions, or do you know a company that is?_[ _Please reach out!_](https://leonoverweel.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Productized Artificial Intelligence 🔌

![Krisp runs as a passthrough for your laptop's microphone and speaker, filtering out background noise. (Krisp)](https://s3.amazonaws.com/revue/items/images/004/722/231/mail/2bc65d8e568d86a293c21a2cf257b2b1.png?1561198048)

_Krisp runs as a passthrough for your laptop's microphone and speaker, filtering out background noise. (Krisp)_

**Krisp is a Mac and Windows app that removes background noise during calls.**
This is one of those rare tools that’s a perfect example of productized AI: its core technology is KrispNet, a deep neural network trained on 20,000 noises, 10,000 distinct speakers, and 2,500 hours of audio.
By running this network directly on your laptop (so no audio is ever sent to a server!), Krisp filters background noise—like screaming children and coffee shop commotion—from any app’s audio input and output.
It works with all video and audio conferencing tools and costs $10 per user per month.
Seems like a no-brainer expense to me.
Check it out here: [Krisp | Noise Cancelling App](https://krisp.ai/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**remove.bg added support for cats.**
This is still one of my favorite AI products (see [DT #3](https://www.getrevue.co/profile/dynamically-typed/issues/3-happy-holidays-149573?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [DT #6](https://dynamicallytyped.com/issues/6-deep-reinforcement-learning-from-an-atari-zoo-to-a-self-driving-car-in-20-minutes-155882?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and [DT #12](https://dynamicallytyped.com/issues/12-openai-introduces-mozart-to-lady-gaga-and-google-takes-your-best-duck-face-selfies-for-you-173114?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), and today it added a new feature: the service can now automatically remove the backgrounds from photos of animals and common everyday objects like food, furniture, bicycles, and airplanes.
More in remove.bg’s blog post: [Cats, Animals and more](https://www.remove.bg/b/cats-animals-more?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Machine Learning Technology 🎛

!["Photos from the Dollar Street data set, showing soap, spices, and toothpaste in different countries. Below each image are examples of labels generated by different object-recognition cloud services." (Facebook AI)](https://s3.amazonaws.com/revue/items/images/004/722/206/mail/f95a20872495f5d44a05c0f2a75ab93d.jpeg?1561195600)

_"Photos from the Dollar Street data set, showing soap, spices, and toothpaste in different countries. Below each image are examples of labels generated by different object-recognition cloud services." (Facebook AI)_

**Facebook AI researchers have done a comprehensive study of cultural bias in object-recognition systems.**
As computer vision systems today are often trained on labeled datasets containing just one culture’s version of an object or event (like toothpaste or a wedding), they fail to recognize other cultures’ versions of those things.

> Facebook AI researchers have published the first systematic study that measures the accuracy of object-recognition systems for different communities across the world.
> … Using a publicly available third-party data set of photos of household items in 50 countries, we found accuracy for all these systems was indeed significantly lower for images from certain regions and from households with lower income levels.

Relative to the distribution of where people live, events and objects from North America and Europe are overrepresented in datasets, while those from South America, Africa, and Asia are underrepresented.
Terrance DeVries et al.
for Facebook’s AI research blog: [Does object recognition work for everyone?
A new method to assess bias in CV systems](https://ai.facebook.com/blog/new-way-to-assess-ai-bias-in-object-recognition-systems/?mc_cid=fe89d15d88&mc_eid=2ce07ab429&utm_campaign=fe89d15d88-Benedict%27s%20Newsletter%20291&utm_medium=email&utm_source=Benedict%27s%20newsletter&utm_term=0_4999ca107f-fe89d15d88-70536657).

**Google Brain has released a new football (soccer) reinforcement learning (RL) environment.**
Currently, there are popular frameworks by OpenAI and DeepMind that RL researchers use to teach computers to play [Go](https://deepmind.com/research/alphago/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Dota 2](https://openai.com/five/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Starcraft 2](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and [Atari console games](https://arxiv.org/abs/1207.4708?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
The Google Research Football Environment joins this lineup as a new challenge for RL agents to tackle, with a highly optimized C++ physics-based 3D football engine that serves as environment.
It contains three Football Benchmarks to pit an agent against hand-engineered easy, medium and hard opponent teams, as well as a Football Academy meant for [curriculum learning](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.149.4701&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) research.
This looks like it’ll be much nicer to use than the deprecated football environment I had to use in my RL course this year ([HFO](https://github.com/LARG/HFO?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
More:

* Karol Kurach and Olivier Bachem for the Google AI blog: [Introducing Google Research Football: A Novel Reinforcement Learning Environment](https://ai.googleblog.com/2019/06/introducing-google-research-football.html?m=1&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Code on GitHub: [google-research/football](https://github.com/google-research/football?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

Thanks for the link, [Art](https://www.linkedin.com/in/atharvadeshmukh/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)!

**Chris Olah wrote a post about collaboration in ML research.**
The TL;DR biggest actionable items are:

1. Be generous.
2. Use author contribution statements.
3. Put “author order not finalized” if it hasn’t been.

Beyond that, it’s also a very good read that touches on the links between credit issues and privilege/power, and that goes deeper into Olah’s own core collaboration principles.
This one seems especially useful:

> In drafts, keep a running list of people to acknowledge.
> This reduces the risk of you forgetting to acknowledge someone.
> It also signals to them that you’re taking this stuff seriously.

I’ve added this to my thesis draft, and I encourage everyone reading this to do the same for their current projects!
Read Olah’s full post here for more tips: [Collaboration & Credit Principles](https://colah.github.io/posts/2019-05-Collaboration/index.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Quick ML resource links ⚡️** ([see all 20](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4))

* _The Matrix Calculus You Need For Deep Learning_ is a 33-page reference PDF that does exactly what it says on the can. Link: [arXiv abstract](https://arxiv.org/abs/1802.01528?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Texar is a TensorFlow toolkit designed for fast prototyping of a broad set of machine learning text generation tasks like translation, dialog, summarization, and language modelling. Link: [asyml/texar](https://github.com/asyml/texar?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* PyTorch Hub is an API and workflow that can be used to improve machine learning research reproducibility, with support for Colab and Papers With Code. Link: [PyTorch docs](https://pytorch.org/hub?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Cool Things ✨

![Pattern Radio detecting a humpback whale song (Google)](https://s3.amazonaws.com/revue/items/images/004/722/016/mail/426014e0cd51a8e219271b7c36752574.png?1561191222)

_Pattern Radio detecting a humpback whale song (Google)_

Google AI and the [US NOAA Pacific Islands Fisheries Science Center](https://www.fisheries.noaa.gov/about/pacific-islands-fisheries-science-center?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) have partnered to **map more than 8,000 hours of ocean sound recordings.**
By pattern matching on a spectrogram of the recording, an interactive site hosting the audio can automatically highlight clips that contain whale songs and visualize repeated sounds within the songs.
The site also contains guided tours through the audio, which are really cool to explore as the scientists explain aspects of different clips.
More:

* The website: [Pattern Radio: Whale Songs](https://patternradio.withgoogle.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Google video about the project on YouTube: [Whale Songs and AI, for everyone to explore](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=JE3-LkMqBfM)
* In-depth, pun-filled post on how the project came to be, by Ann Allen for NOAA Fisheries: [OK Google: Find the Humpback Whales](https://www.fisheries.noaa.gov/science-blog/ok-google-find-humpback-whales?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
🤗