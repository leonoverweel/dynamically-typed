# #22: Mobile apps that identify plant species, AI-powered posture correction, and my new job! 

Hey everyone, welcome to Dynamically Typed #22!
Today in productized AI, I’m covering mobile apps that recognize plant and flower species from a photograph, as well as the “AI spiders” Pixar used to create set backgrounds for _Toy Story 4_.
On the machine learning research side, there’s a new self-driving car dataset release from Waymo, another GPT-2 release from OpenAI, and an _Eye on A.I._ podcast episode calling for ML researchers to look at climate-related problems.

I also found a super creative website that uses on-device machine learning to watch your posture, so that you can only read it when you’re sitting up straight; as well as an AI art exhibition in Berlin.
Finally, in some ~ personal news ~, I’m starting my first full-time machine learning job in two weeks!
More about that at the end of today’s DT.

## Productized Artificial Intelligence 🔌

![PictureThis apps for Android, iOS, and the web. (Glority Software)](https://s3.amazonaws.com/revue/items/images/004/987/737/mail/b010a24f6d641738f96ace378798bbb3.png?1568464118)

_PictureThis apps for Android, iOS, and the web. (Glority Software)_

**PictureThis is an app and website that identifies plants and flowers from photos.**
I’m moving into my new apartment in Amsterdam soon, and I can’t wait to decorate it with lots and lots of plants.
So every time I was at friends’ houses in the past few weeks, I asked them about their greenery.
For those times when they didn’t remember what a particular one was called, this app would’ve come in useful!
It’s a good example of productized AI because it uses image classification models to try to figure out what plant you’re pointing your phone camera at.
More:

- The app’s website has download links for iOS and Android: [PictureThis - Botanist in your pocket](https://www.picturethisai.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (free 7 day trial and $19.99/year after that).
- iNaturalist is a free alternative (also featuring automatic identification) supported by National Geographic and the California Academy of Sciences. It even allows you to contribute your observations back to scientific data repositories, and it’s what I’m using on my phone now. Link: [A community for Naturalists - iNaturalist.org](https://www.inaturalist.org?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Pixar used “AI spiders” to create the background cobwebs for _Toy Story 4,_ **which features a number of scenes in an antiques store that had to feel old and abandoned.
Beside adding a layer of dust on top of all the objects in the store and sprinkling around some “miscellaneous debris, hair and fur,” the animators wanted to fill the background of the set with cobwebs.
Sets supervisor Thomas Jordan for the Walt Disney Company blog:

> [Traditionally,] animators would have had to make the webs one strand at a time, which would have taken several months.
> … [Instead,] one animator wrote a program simulating an A.I.
> spider building cobwebs: “He guided the spiders to where he wanted them to build cobwebs, and they’d do the job for us.”

> “You have to tell the spider where the connection points of the cobweb should go,” Jordan says, “but then it does the rest.”

I’ve searched around a bit, but I haven’t been able to find any technical details about the spiders.
For example, are they "AI” in the sense that a non-player character in a videogame, which simply follows some handwritten rules to decide its next action, is called an AI?
Or are they “AI” in that they learned their behavior by abstracting it from data observed from real spiders?
Only the latter qualifies as something I’d like to cover in this newsletter, but nonetheless I thought this was a fun story to highlight.
More:

- The Walt Disney Company blog: [Setting the Scene: How Technology Created a Richer Playset in ‘Toy Story 4’](https://www.thewaltdisneycompany.com/setting-the-scene-how-technology-created-a-richer-playset-in-toy-story-4/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Jason Kottke for Kottke.org: [Pixar’s AI Spiders](https://kottke.org/19/09/pixars-ai-spiders?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Machine Learning Research 🎛

**Self-driving car company Waymo has also open-sourced its training data,** following other players in the field like Chinese tech giant Baidu and ride hailing company Lyft (see [DT #19](https://dynamicallytyped.com/issues/19-microsoft-s-1b-openai-investment-lyft-s-dataset-and-what-makes-a-peacock-a-peacock-190545?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
Brad Templeton, who previously worked on Google’s car team, wrote about the significance of this release:

> Waymo is widely hailed as the best in the business.
> Their data is good, and it also contains flat 2-D camera images which have been synchronized with LIDAR 3-D scans of the same scene, something else Waymo is good at.
> … This archive will be a boon for academic researchers, who can’t pay [to collect and label this data themselves].

But there is a catch: the data is strictly licensed for only non-commercial use, so Waymo’s many competitors can’t use it directly.
In the long term, though, supporting academia like this should help advance the basic research (object classification, sensor fusion, optical flow, etc.) on top of which all self-driving systems are being built.
Read Templeton’s full analysis on Forbes: [Waymo Gives Away Free Self-Driving Training Data – But With Restrictions](https://www.forbes.com/sites/bradtempleton/2019/08/22/waymo-gives-away-free-self-driving-training-data-but-with-restrictions/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**OpenAI has posted a 6-month follow-up of their GPT-2 release.**
GPT-2 is OpenAI’s language model that can be used to generate text that convincingly looks like it was written by a human.
It has been controversial from the start, since OpenAI originally—in fear that GPT-2 would be used to automatically generate fake news and propaganda—only released a small, less capable version of the model, which made it hard for other scientists to evaluate or replicate their work.
At the time, I called for them to release the full model to raise public awareness of its capabilities (see [DT #8](https://dynamicallytyped.com/issues/8-should-openai-open-source-their-impressive-new-language-model-161119?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).

Instead, over the past half year, OpenAI has been doing a staged release of progressively larger versions of the model (see [DT #13](https://dynamicallytyped.com/issues/13-caption-this-new-ai-powered-features-at-google-i-o-and-openai-s-staged-gpt-2-release-175669?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), opening it up first to trusted research institutions and then to the public at large.
With their latest release a little over two weeks ago, they also published some of their findings about this approach:

- _Coordination is difficult, but possible:_ OpenAI has worked closely with over five other groups that have replicated GPT-2 and ensured that no one has released a full-size model yet.
- _Humans can be convinced by synthetic text:_ As they feared, fake news written by GPT-2 can be extremely effective; propaganda written by similar language model called GROVER actually seems more “plausible” to humans than human-written propaganda.
- _Detection isn’t that simple:_ The automated systems to detect text written by GPT-2 or similar models are only around 90% effective, not enough to stop potential bad actors.

So what’s next?

> As part of our staged release strategy, our current plan is to release the 1558M parameter model in a few months, but it’s plausible that findings from a partner, or malicious usage of our 774M model, could change this.

> We think that a combination of staged release and partnership-based model sharing is likely to be a key foundation of responsible publication in AI, particularly in the context of powerful generative models.
> The issues inherent to large models are going to grow, rather than diminish, over time.

I think I’ve changed my mind from six months ago and that I agree with this approach now—we need detection systems built by trusted partners to at least catch up to the current publicly available versions of GPT-2 before new, more capable ones become available.
For more analysis and a full timeline, see OpenAI’s blog post: [GPT-2: 6-Month Follow-Up](https://openai.com/blog/gpt-2-6-month-follow-up/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Quick ML resource links ⚡️** ([see all 41](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4))

- Turbo is a color map for visualizing depth images (common in computer vision research) that’s more perceptually uniform, interpretable, and accessible to color blind people. Link: [Turbo](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- _Fairness and machine learning_ is a free online textbook that approaches ML from an anti-discriminatory perspective. Link: [fairmlbook.org](https://fairmlbook.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Artificial Intelligence for the Climate Crisis 🌍

**The _Eye On A.I._ podcast interviewed John Platt about mitigating global warming.**
Platt is a Distinguished Scientist at Google and one of the editors of the 97-page [Rolnick et al.
(2019)](https://arxiv.org/abs/1906.05433?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) paper on _Tackling Climate Change with AI_ that’s the basis of several climate workshops at large machine learning research conferences (see [DT #16](https://dynamicallytyped.com/issues/16-finding-whales-with-ai-and-97-pages-of-ml-for-climate-change-183400?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [DT #19](https://dynamicallytyped.com/issues/19-microsoft-s-1b-openai-investment-lyft-s-dataset-and-what-makes-a-peacock-a-peacock-190545?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).

Craig Smith, who runs _Eye on A.I._ , says this episode is meant as a call to action for his ML researcher and engineer listeners (like many of us!) to take a look at the paper and see if there are any problems where we can contribute.
Platt thinks:

> [ML can be particularly effective for] smart measurements, … trying to understand this very, very complicated sort of geophysics / economic system [that controls our climate].

> [There] won’t be a silver bullet.
> But maybe if we all work on different parts we can make progress.

You can hear to the full episode here: [Episode #020 - Eye on A.I.](https://www.eye-on.ai/podcast-020?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) It’s a good listen that also touches on a number of other projects outside of machine learning, like finding cheap zero-carbon energy sources.

Personally, I spent some time this summer looking into the PV power prediction problem and building [a website for Generation Climate Europe](https://gceurope.org?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), but I haven’t found a really good ML for climate change side project just yet.
If any of you have one that you’re passionate about and that you’d like to work on together (or just have me feature here), please reach out!

## Cool Things ✨

![Fix Posture blurs your screen if your posture is bad. (Olesya Chernyavskaya)](https://s3.amazonaws.com/revue/items/images/004/987/924/mail/5ebc08ff322caa4cbf842f176f982869.png?1568476165)

_Fix Posture blurs your screen if your posture is bad. (Olesya Chernyavskaya)_

**Fix Posture is an experimental website that blurs itself out if it detects that your posture is bad.**
The Glitch site by Olesya Chernyavskaya uses a [TensorFlow.js](https://www.tensorflow.org/js?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) PoseNet implementation to detect your “pose"—the position of your body parts relative to each other—from your laptop’s camera.
It all happens locally without having to send your video to a remote server, so the site reacts instantly to your movements almost instantly.
I had a lot of fun playing around with this, and Chernyavskaya’s site also includes a lot of information about how she designed and built it: [fix-posture.glitch.me](https://t.co/NuJzcm5clr?amp=1&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Gene Kogan launched an exhibit of interactive AI art at the Futurium in Berlin.**
Here’s a rundown of the installations, with links to Kogan’s demo videos / tweets:

- [Invisible Berlin](https://twitter.com/genekogan/status/1170689180890017792?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is a sandbox where you can place colored shapes representing water, buildings, greenery, etc on a surface. An overhead camera feeds that into a generative adversarial network, and a computer renders and displays what a satellite view of an area with that layout would look like.
- [AI Drawing Studio](https://twitter.com/genekogan/status/1170689184954224640?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is a replica of NVIDIA’s GauGAN (see [DT #10](https://dynamicallytyped.com/issues/10-a-turing-award-for-deep-learning-and-a-bitter-lesson-for-ai-research-166903?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) where you can draw shapes on a touchscreen and see them transform into a landscape painting.
- [Cubist Mirror](https://twitter.com/genekogan/status/1170689187894452224?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is a big projection that applies style transfer (generating a version of an image in the style of a particular artists’ paintings) to a live camera feed of the crowd. (You can do this online yourself using sites like [Deep Dream Generator](https://deepdreamgenerator.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which I used to create the purple hero image at the top of this email.)

If you’re near Berlin, this would definitely make for a fun afternoon!

## My Stuff 😁

![Plumerai's landing page features drones and delivery bots. (Plumerai)](https://s3.amazonaws.com/revue/items/images/004/989/248/mail/68de530740c790471221288481e0ae78.png?1568535366)

_Plumerai's landing page features drones and delivery bots. (Plumerai)_

**I’m starting my first full-time machine learning job!**
I’ll be working at Plumerai, a small startup out of London and Warsaw that’s building chips for binarized neural networks (BNNs).
The idea behind BNNs comes from a paper by [Courbariaux et al.
(2016)](https://arxiv.org/abs/1602.02830?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which argues that neural networks with 1-bit activations and weights can be nearly as effective as traditional (8-, 16- and 32-bit) networks, at a fraction of the memory and energy use.

For the past few years, research in the area has faced a bit of a chicken-and-egg problem: to get the energy use benefits from BNNs, you need to run them on specialized chips (which don’t yet exist); and if you build those chips, you’d need a software and research ecosystem to have a market for selling your chips (which also doesn’t yet exist).
The pitch for Plumerai is to attack this problem from both ends: the Warsaw part of the company is building the custom chips, while the London part of the company is working on software (e.g.
the [Larq](https://larq.dev?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) TensorFlow library) and research (e.g.
[Helwegen et al.
(2019)](https://arxiv.org/abs/1906.02107?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
This way, they’ll create both the chip for more energy-efficient deep learning and the surrounding ecosystem to sell it into.

Plumerai has just opened up a new office in Amsterdam to work on the software + research side, which is where I’m going to be working as a Deep Learning Engineer, implementing BNNs and building out Larq.
I can’t wait to start!
(If Plumerai also sounds interesting to you, don’t hesitate to reach out—they’re hiring.)

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.
Also, I’m experimenting with cross-posting this newsletter [to Medium](https://medium.com/dynamically-typed?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to see if that’ll help more people find out about Dynamically Typed.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
🍃