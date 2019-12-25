# #14: Artificial intelligence for medicine and the climate crisis 

Hey everyone, this is the 14th issues of Dynamically Typed.
Since there are also 14 days between each issue, that means I’ve now been doing this newsletter for 14^2 = 196 days—over half a year!

Recently, I’ve become more interested in how artificial intelligence can be used to fight [the climate crisis](https://www.climaterealityproject.org/climate-101?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), so I’m dedicating a section in today’s DT to a few projects I’ve come across in this space.
Is this something you’d like to see in future editions as well?
Let me know by replying to this email.

Other news I’m covering today includes a lot of research by Google, from end-to-end systems for detecting lung cancer in CT scans and translating speech to speech, to a framework of best practices for applied AI.
Related, there’s new work from Stripe and the Wolfram Language centered around deploying machine learning systems at scale.

## Productized Artificial Intelligence 🔌

**Google’s Devvret Rishi and Margaret Jennings wrote up a framework of best practices for applied AI** based on their work with ten fintech startups through Google’s [Launchpad accelerator](https://developers.google.com/programs/launchpad/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
The framework is divided into three sections:

1. _Framing the problem:_ getting the right team, incentives and expectations in place
2. _Building the model:_ starting simple and focusing on data pipelines over fancy models (“don’t be a hero”)
3. _Deploying, measuring, monitoring:_ testing for performance and biases early and thoroughly

A lot of their main takeaways mirror [Josh Cogan’s earlier post for the Launchpad blog](https://medium.com/thelaunchpad/the-ml-surprise-f54706361a6c?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (see [DT #7](https://dynamicallytyped.com/issues/7-no-code-no-problem-from-indie-makers-to-machine-learning-158462?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)): building and tuning fancy machine learning models is not what takes the most time in productizing AI:

> We can’t stress enough the importance of starting simple, with a clear business goal tied to the model’s output

> Collecting data, cleaning data, augmenting your relatively small dataset, and aligning on a common business value will take the majority of your time

Read their full post here: [Bridging the gap between research and big tech: applied AI/ML best practices for the modern enterprise](https://medium.com/thelaunchpad/bridging-the-gap-between-research-and-big-tech-applied-ai-ml-best-practices-for-the-modern-d962428beb14?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Artificial Intelligence for the Climate Crisis 🌍

![GAN-generated images of houses before and after a flood hits. (Schmidt et al.)](https://s3.amazonaws.com/revue/items/images/004/627/160/mail/81b9dcf978b56925cef01db25a3c9850.jpeg?1558809684)

_GAN-generated images of houses before and after a flood hits. (Schmidt et al.)_

**Victor Schmidt et al.
used Generative Adversarial Networks to visualize the consequences of climate change.**
Their GAN is trained on street-view images of houses before and after catastrophic extreme weather events like floods and forest fires, which the climate crisis will exacerbate.
The trained model takes an image of a house and, if it is located in a region that climate models predict will be hit by the effects of climate change in the next 50 years, transform it into what the house would look like when it is hit by extreme weather.
Schmidt et al.
hope that this will help create “a more visceral understanding of the effects of climate change.” Read more about it here:

* Will Knight for the MIT Technology Review: [AI can show us the ravages of climate change](https://www.technologyreview.com/f/613547/ai-can-show-us-the-ravages-of-climate-change/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Schmidt et al. on arXiv: [Visualizing the Consequences of Climate Change Using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1905.03709?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**Alina Tugend wrote about several artificial intelligence projects around climate change for The New York Times.**
They include:

* Dr. Maria Uriarte of Columbia University is [using AI to analyze how different types of trees are affected by hurricanes](https://uriartelab.org/forest-disturbance-and-regrowth/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter). She trained a network to identify tree species in satellite images, allowing her to use before-and-after images to compare the rates at which different species survive a hurricane.
* Stanford’s [Grid Resilience & Intelligence Platform](https://gismo.slac.stanford.edu/projects/grip.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (GRIP) project uses satellite imagery to “anticipate, absorb and recover from events that cause grid outages, such as extreme weather or a cyberattack.”
* The Australian Commonwealth Scientific and Industrial Research Organization is using machine learning to more efficiently genetically engineer wheat to resist worsening growing conditions caused by climate change.
* [One Concern](https://www.oneconcern.com/blog/2018-the-dawn-of-benevolent-intelligence-5LICUH70ty2cw0owEG2Os4/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) uses artificial intelligence to forecast damage due to earthquakes and flooding.

Read Tugend’s full piece for much more detail about all of the projects above: [How A.I.
Can Help Handle Severe Weather](https://www.nytimes.com/2019/05/12/climate/artificial-intelligence-climate-change.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

_(PS: If you know a better title for this section than “Artificial Intelligence for the Climate Crisis,” let me know!)_

## Machine Learning Technology 🎛

![Google's lung cancer prediction model (Shravya Shetty, The Keyword)](https://s3.amazonaws.com/revue/items/images/004/626/402/mail/3f06ea2cd6272a88cae1cbac92073736.png?1558780967)

_Google's lung cancer prediction model (Shravya Shetty, The Keyword)_

**Google AI’s Health division has published a new end-to-end lung cancer screening system.**
The model, published in Nature Medicine, takes a 3D CT scan as input and outputs a prediction of whether it is a potential cancer case; it does this very effectively:

> When using a single CT scan for diagnosis, our model performed on par or better than the six radiologists.
> We detected five percent more cancer cases while reducing false-positive exams by more than 11 percent compared to unassisted radiologists in our study.

It’s very cool to see advanced ML technology being published outside of the usual AI conferences: besides the obvious scientific and medical value of this specific contribution, hopefully publications like this will help scientists in other fields understand more deeply what types of problems AI is good at tackling.
More:

* Paper by Ardilla et al. in Nature Medicine: [End-to-end lung cancer screening with three-dimensional deep learning on low-dose chest computed tomography](https://www.nature.com/articles/s41591-019-0447-x?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Shravya Shetty, M.S. for Google’s The Keyword blog: [A promising step forward for predicting lung cancer](https://www.blog.google/technology/health/lung-cancer-prediction/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Denise Grady for The New York Times: [A.I. Took a Test to Detect Lung Cancer. It Got an A.](https://www.nytimes.com/2019/05/20/health/cancer-artificial-intelligence-ct-scans.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#click=https://t.co/nNRiK9JU1S)

**Also from Google: Translatotron, an end-to-end speech-to-speech translation model.**
Previous models for translating spoken text would take three steps: (1) automatic speech recognition to turn the spoken source sentence into text, (2) machine translation to turn translate into the target language, and (3) text-to-speech synthesis to “speak” it.
Translatotron does this all in one go, improving translation speed, reducing compounding errors between steps, and making it easier to retain the voice of the original speaker in the translation (which is really, really cool).
Read more here:

* Ye Jia and Ron Weiss for the Google AI Blog (includes speech samples): [Introducing Translatotron: An End-to-End Speech-to-Speech Translation Model](https://ai.googleblog.com/2019/05/introducing-translatotron-end-to-end.html?m=1&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Jia et al. on arXiv (includes model architecture): [Direct speech-to-speech translation with a sequence-to-sequence model](https://arxiv.org/abs/1904.06037?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**Rob Story wrote about Railyard, an API and job manager that payments processor Stripe uses for scalable machine learning.**
Stripe uses machine learning for everything from fraud detection to retrying failed credit card charges, and it has teams training hundreds of new models every day.
Railyard streamlines this process by exposing an API to which data scientists can submit jobs from any ML framework.
Running on top of Stripe’s Kubernetes cluster, Railyard then trains, evaluates and saves the model.
This takes away the cognitive load of having to think about infrastructure, operations, model state, etc., so data scientists can focus just on building and testing their models.
Story’s full post explains how they implemented this at Stripe: [Railyard: how we rapidly train machine learning models with Kubernetes](https://stripe.com/gb/blog/railyard-training-models?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**The Wolfram Engine is now free for developers to encourage its use in production systems;** this engine is what powers the Wolfram Language and [Wolfram|Alpha](https://www.wolframalpha.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
I’ve always wanted to get more into the Wolfram Language because it has implementations of lots of machine learning models, plus an enormous set of built-in “computational knowledge” about the real world:

> There are now altogether 5000+ functions in the language, covering everything from visualization to machine learning, numerics, image computation, geometry, higher math and natural language understanding—as well as lots of areas of real-world knowledge (geo, medical, cultural, engineering, scientific, etc.).

I never thought of a project that I could build end-to-end in the Wolfram Language ecosystem, but this release now makes it possible to run the Wolfram Engine on a server and call into it from other programming languages, opening up a world of possibilities.
More on Stephen Wolfram’s blog: [Launching Today: Free Wolfram Engine for Developers](https://blog.stephenwolfram.com/2019/05/launching-today-free-wolfram-engine-for-developers/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Quick ML resource links ⚡️** ([see all](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4))

* Philip Guo shared ten “research design patterns” for finding research project ideas in technology-related fields, plus what to watch out for when applying them. Link: [Research Design Patterns](http://pgbovine.net/research-design-patterns.htm?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

I’ve now also made a [Notion](https://www.notion.so/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) page with all the quick ML resource links I’ve shared so far, which I’ll keep updating as I send out new issues of Dynamically Typed.
Check it out here: [Machine Learning Resources](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4).

## Cool Things ✨

![Infinite Patterns used the bottom-right image of a butterfly as input to "dream" this pattern. (Damien Henry, The Keyword)](https://s3.amazonaws.com/revue/items/images/004/626/457/mail/784e345b2108f878368a2a20ba0a55e8.png?1558783980)

_Infinite Patterns used the bottom-right image of a butterfly as input to "dream" this pattern. (Damien Henry, The Keyword)_

**Infinite Patterns is a tool to create one-of-a-kind patterns using machine learning.**
It’s made by artist duo Pinar&Viola and engineer Alexander Mordvintsev as part of the [Google Arts & Culture Lab](https://experiments.withgoogle.com/collection/arts-culture?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
You can upload an image to Infinite Patterns and it’ll use a DeepDream algorithm to transform it into a pattern.
Try it here: [Infinite Patterns](https://experiments.withgoogle.com/infinitepatterns?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
💕