---
category: productized-ai
data: 2020-07-05
issue_number: 43
title: One AI model, four competing services
---

[Melody ML](https://melody.ml?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Acapella Extractor](https://www.acapella-extractor.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Vocals Remover](https://www.remove-vocals.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and [Moises.ai](https://moises.ai?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) are all **services that use AI to separate music into different tracks by instrument.**
Like many of these single-use AI products, they wrap machine learning models into easy-to-use UIs and APIs, and sell access to them as a service (after users exceed their free tier credits).
Here’s a few examples of their outputs:

* Bill Withers - Lean On Me: [original](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=fOZ-MySzAac) vs. [vocals extracted](https://youtu.be/01YrXUChqCI?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) using Acapella Extractor.
* The Beatles - Yellow Submarine: [original](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=m2uTFF_3MaA) vs. [instrumental extracted](https://youtu.be/PviSf_deGyE?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) using Vocals Remover.
* Etnia - Estrella Síria: [original and isolated tracks](https://moises.ai?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) on the Moses.ai landing page.

As you can tell, these services all have pretty similar-quality results.
That’s no accident: all four are in fact built on top of [Spleeter](https://github.com/deezer/spleeter?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), an open-source AI model by French music service [Deezer](https://www.deezer.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)—but none of them are actually _by_ Deezer.
So these services are basically just reselling Amazon’s or Google’s GPU credits at a markup—not bad for what I imagine to be about a weekend’s worth of tying everything together with a bit of code.
There’s a lot of low-hanging fruit in this space, too: even just within the audio domain, there are 22 different task on [Papers with Code](https://paperswithcode.com/area/audio?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for which you can find pretrained, state-of-the-art models that are just waiting to be wrapped into a service.
(And for computer vision, there are 807 tasks.)

I actually quite like the idea of this.
You need a whole different skillset to turn a trained model into a useful product that people are willing to pay for: from building out a thoughtful UI and the relevant platform/API integrations, to finding a product/market fit and the right promotional channels for your audience.
As long as the models are open-source and licensed to allow commercial use, I think building products like this and charging money for them is completely fair game.

Since the core technology is commoditized by the very nature of the underlying models being open-source, the competition shifts to who has the best execution around those same models.

For example, the Melody ML service restricts both free and paid users to a maximum length of 5 minutes per song.
Moises.ai saw that and thought they could do better: for $4/month, they’ll process songs up to 20 minutes long.
Similarly, the person who built both Vocals Remover and Acapella Extractor figured the pitch worked better in the form of those two separate, specialized websites.
They even set up namesake YouTube channels that respectively post instrumentals-only and vocals-only versions of popular songs—some with [many thousands of views](https://youtu.be/01YrXUChqCI?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)—and of course link those back to the websites.
Clever!

It’s really cool to see how the open-source nature of the AI community, along with how easy it is to build websites that integrate with cloud GPUs and payments services nowadays, is enabling these projects to pop up more and more.
So who’s picking up something like this as their next weekend project?
Let me know if you do!

(Thanks for the link to Acapella Extractor, [Daniël](https://www.linkedin.com/in/daniel-vos/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)!
Update: I previously thought the Melody ML service was _by_ Deezer, but someone at Deezer pointed out it was built by a third party.)