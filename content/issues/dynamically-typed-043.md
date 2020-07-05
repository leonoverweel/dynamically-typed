# #43: One AI model, four competing services 

Hey everyone, welcome to Dynamically Typed #43.
For the first time ever, this newsletter is now going out to more than 200 people!

In today’s edition, I’m focusing mostly on a story in the productized AI space: how one company’s open-source ML model spawned four competing, independent online services.
I didn’t end up covering the open-source model when I originally came across it a few months ago; but when a friend sent me a link to one of the services built on top of it, I realized it may actually be part of a much bigger trend forming in the industry.
I found it pretty fascinating to discover, and I’d love to know what you think about it.

Beyond that, I have a few quick links and some follow-up in all the other usual sections.

## Productized Artificial Intelligence 🔌

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

**Quick productized AI links 🔌**

* 👁 As we feared following the news that IBM, Microsoft, and Amazon are no longer selling facial recognition technology to police departments in the United States (see [DT #42](https://dynamicallytyped.com/issues/42-facial-recognition-exodus-openai-s-new-gpt-3-language-model-and-oil-in-the-cloud-254772?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), companies that aren’t tied to large consumer-facing brands—and that aren’t under the level of scrutiny that comes with being a household name—[are now doubling down on the space](https://www.wsj.com/articles/facial-recognition-companies-commit-to-police-market-after-amazon-microsoft-exit-11591997320?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter). The only real solution to this problem is regulation.
* 👁 In related news, a Michigan man was [arrested because a facial recognition algorithm misidentified him](https://www.nytimes.com/2020/06/24/technology/facial-recognition-arrest.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter). This is the first time a facial-recognition-induced wrongful arrest has been reported, which actually slightly surprises me because the technology has been rolled out much more widely in China (although cases like this may not make the news there). What’s less surprising is that this first case happened to a Black man, given that commercial facial recognition algorithms have been shown to make more mistakes on people with darker skin (see [DT #41](https://dynamicallytyped.com/issues/41-black-lives-matter-highlighting-ml-ai-products-research-and-climate-projects-by-black-creators-251381?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).

## Machine Learning Research 🎛

**Quick ML research + resource links** 🎛 ([see all 65 resources](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4))

* 💱 Today in gargantuan language models: Google’s new state-of-the-art model for translating from 100 languages to English has _600 billion parameters_. Compare this to OpenAI’s GPT-3 at 175 billion parameters from June (see [DT #42](https://dynamicallytyped.com/issues/42-facial-recognition-exodus-openai-s-new-gpt-3-language-model-and-oil-in-the-cloud-254772?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) and Microsoft’s Turing-NLG at 17 billion parameters from February ([DT #33](https://dynamicallytyped.com/issues/33-billie-eilish-answers-ai-generated-interview-questions-visual-search-for-aerial-imagery-and-the-tech-won-t-drill-it-pledge-224742?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)). Google’s 600 billion-parameter Transformer took four days to train on 2048 (!) TPUs, which is actually relatively little for that model size. This training process is therefore also the focus of the paper describing the model: [Lepikhin et al. (2020)](https://arxiv.org/abs/2006.16668?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) introduce GShard, “an elegant way to express a wide range of parallel computation patterns with minimal changes to the existing model code.”
* 🧙‍♀️ In a paper to be published at ICSE 2020, [Liem and Panichella (2020)](https://pure.tudelft.nl/portal/en/publications/oracle-issues-in-machine-learning-and-where-to-find-them\(01091b30-9b8e-46eb-972e-e5b90e509a60\).html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) introduce two heuristics that can be used to semi-automatically uncover high-level issues in data labels and representations. In ImageNet for example, they find that the synonymous “laptop” and “notebook” labels consistently confuse models, and argue that such oracle issues warrant closer collaboration between the machine learning and software testing communities. The paper, called [Oracle Issues in Machine Learning and Where to Find Them](https://www.youtube.com/watch?feature=youtu.be&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=4KUgMOREzjs), also comes with an amazing video where the authors—animated as talking portrait paintings from the wizarding world—describe their “potion for better Defense Against the Dark ML Arts.” It may be the most perfect thing I’ve ever shared in this section.

## Artificial Intelligence for the Climate Crisis 🌍

**Quick climate AI links** 🌍

* 🌞 SunDown is a “a sensorless approach designed to detect per-panel faults in residential solar arrays” by [Feng et al. (2020)](https://arxiv.org/abs/2005.12181?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter). Trained on years of solar generation data from homes, it “leverages correlations between the power produced by adjacent panels to detect deviations from expected behavior,” detecting faults and electrical failures with > 99% accuracy. This also sounds like an app waiting to happen!

## Cool Things ✨

**Quick cool things links ✨**

* 🎞 [Broxton et al. (2020)](https://storage.googleapis.com/immersive-lf-video-siggraph2020/ImmersiveLightFieldVideoWithALayeredMeshRepresentation.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) extended [DeepView](https://augmentedperception.github.io/deepview/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), their previous gradient-based method to render new perspectives of 3D scenes, into the video domain with [DeepViewVideo](https://augmentedperception.github.io/deepviewvideo/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter). This is very cool: as you’re watching a video, you can virtually pan and tilt the “camera” through which you’re watching the scene to see it from different angles. Their method enables doing this efficiently enough that it can run in browsers and on mobile phones. Check out the sample video at the top of [the excellent webpage for the paper](https://augmentedperception.github.io/deepviewvideo/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to get a feel for the effect.

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
🎞