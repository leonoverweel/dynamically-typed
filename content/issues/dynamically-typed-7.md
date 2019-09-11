# #7: No code, no problem: from indie makers to machine learning 

In this issue of Dynamically Typed, I’m covering the rise of the #nocode movement: digital products built without a single line of code.
This includes Ryan Hoover’s essay on indie makers launching MVPs in a matter of hours, Uber’s new no-code open source deep learning toolbox, and a Google Cloud AI manager’s realization that writing code is only a small part of building ML products.

It’s been a busy two weeks in the world of AI and ML, so there’s lots more to cover as well.
Let’s dive in.

## Productized Artificial Intelligence 🔌

![How much time does each step of building a machine learning product take? (Josh Cogan, Google)](https://s3.amazonaws.com/revue/items/images/004/241/689/mail/0_JPKydbSB9YRzy8k6.png?1550142136)
_How much time does each step of building a machine learning product take? (Josh Cogan, Google)_

**Josh Cogan wrote about about the surprises he encountered building machine learning products at Google.**
The main steps in building an ML project are defining success metrics (KPIs), collecting data, building infrastructure, optimizing the ML algorithm, and finally integrating the resulting model.
Practitioners think that most time goes into coding and optimizing the algorithm, while in reality most work ends up being in data collection, infrastructure, and integration.
I suspect this is largely caused by the environment in which most of us learn to build AI products: in universities, online classes or [Kaggle competitions](https://www.kaggle.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), the algorithm is all we have to worry about.
It’s a good case for getting real-world experience building products as early-on as possible.

- Josh’s post for The Launchpad: [The Surprising Truth About What it Takes to Build a Machine Learning Product](https://medium.com/thelaunchpad/the-ml-surprise-f54706361a6c?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Medium)

**Google has launched an Android feature that transcribes speech in real time for 70 languages,** covering more than 80% of the world’s population.
This kind of applied AI tech can make a real difference in the lives of the estimated 466 million people around the globe who suffer from some kind of hearing issue, especially because Google’s service is free to use.
One caveat is that the transcription isn’t done on-device, so users may be paying for data the app sends back and forth to Google’s servers (although Google says this data usage is minimized and they’re working on on-device recognition).

- Brian Kemler for [Google.org](https://google.org?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Google’s philanthropy arm): [Making audio more accessible with two new apps](https://www.blog.google/outreach-initiatives/accessibility/making-audio-more-accessible-two-new-apps/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Thanks for the link, [Steinar](https://twitter.com/SteinarLaenen?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)!)
- Sagar Salva for the Google AI Blog: [Real-time Continuous Transcription with Live Transcribe](https://ai.googleblog.com/2019/02/real-time-continuous-transcription-with.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**The Verge did a feature on three AI products for music mastering,** the last step in audio post production.
[Landr](https://www.landr.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [MajorDecibel](https://majordecibel.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) completely automate the expensive process, while [Ozone](https://www.izotope.com/en/products/master-and-deliver/ozone.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) automates cleanup work so that mastering professionals “can hone in on the creative side of things.” These products are an interesting example for the conversation around AI and automation in general.
Are Landr and MajorDecibel going to put masting engineers out of a job, or will they expand the market for mastering by making it available to more artists, who will then go to professionals once they can afford it?
(The companies themselves, of course, claim the latter.)

- Dani Deahl’s piece for The Verge: [How AI is solving one of music’s most expensive problems](https://www.theverge.com/2019/1/30/18201163/ai-mastering-engineers-algorithm-replace-human-music-production?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**How does Waymo, Alphabet’s self-driving taxi company, manage its fleet of driverless cars?**
It involves 5:00 am sensor checks, mid-day backup driver switches, 24/7 operations, and much more.
One interesting aspect is that the cars deal with “strange” real-world scenarios (like construction sites) by phoning home to Waymo’s “fleet response team.” These remote operators then make the call whether the car should switch lanes, turn differently, or reroute itself, and pass this information on to the rest of the fleet.
Waymo currently has over 600 cars on the road in Phoenix, Arizona, serving its Early Riders pilot program.

- Read the full story here, by The Verge’s Andrew J. Hopkins: [A Day in the Life of a Waymo Self-Driving Taxi](https://www.theverge.com/2018/8/21/17762326/waymo-self-driving-ride-hail-fleet-management?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
- Bonus: Watch this hour-long talk from Waymo’s chief scientist on what they’re facing in scaling their ML tech: [Drago Anguelov (Waymo) - MIT Self-Driving Cars](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=Q0nGo2-y0xY)

## Machine Learning Technology 🎛

![Over the past 20 years, AI research has shifted from logic and constraints to networks and learning (MIT Technology Review)](https://s3.amazonaws.com/revue/items/images/004/236/211/mail/artboard-12x-2.png?1550010444)
_Over the past 20 years, AI research has shifted from logic and constraints to networks and learning (MIT Technology Review)_

**MIT Technology Review analyzed 16,625 research articles to identify historical trends in AI research.**
They scraped the papers from the artificial intelligence section of [arXiv](http://arxiv.org?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (pronounced “archive”), the canonical online repository for computer science research.
Their main takeaway:

> Through our analysis, we found three major trends: a shift toward machine learning during the late 1990s and early 2000s, a rise in the popularity of neural networks beginning in the early 2010s, and growth in reinforcement learning in the past few years.

This last trend, the growth of reinforcement learning, has definitely been picking up outside of arXiv papers as well; see [DT #6](https://www.getrevue.co/profile/dynamically-typed/issues/6-deep-reinforcement-learning-from-an-atari-zoo-to-a-self-driving-car-in-20-minutes-155882?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for a few recent examples.
Personally, I’m most excited to see how reinforcement learning will be applied outside of games, where most current research achievements seem to be.

- Karen Ho’s full analysis: [We analyzed 16,625 papers to figure out where AI is headed next](https://www.technologyreview.com/s/612768/we-analyzed-16625-papers-to-figure-out-where-ai-is-headed-next/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- A few examples of reinforcement learning outside of games: [Facebook notifications](https://code.fb.com/ml-applications/horizon/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [trading](https://medium.com/@ranko.mosic/reinforcement-learning-based-trading-application-at-jp-morgan-chase-f829b8ec54f2?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and [fleet management](https://arxiv.org/abs/1802.06444?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (via [this tweet by Pablo Samuel Castro](https://twitter.com/pcastr/status/1095047235199553537?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter))

**But are there problems with the trend of approaching most ML problems with neural networks?**
Alan L.
Yuille et al.
argue that the current singular focus on deep nets in vision research is bad for the field because: researchers are chiefly targeting tasks that have lots labeled data available (which may not be the most important tasks); deep nets often don’t generalize well outside of the dataset they’re trained on (especially in terms of viewpoints); and deep nets are overly sensitive to context in a way a human wouldn’t be.
A few of my professors have mentioned similar issues: people are quick to jump straight to complex, recent methods that perform well on benchmark datasets, without trying simpler, older methods first (which may have major computational and explainability benefits).

- Alan L. Yuille et al’s post for The Gradient: [The Limitations of Deep Learning for Vision and How We Might Fix Them](https://thegradient.pub/the-limitations-of-visual-deep-learning-and-how-we-might-fix-them/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Their paper: [Deep Nets: What have they ever done for Vision? ](https://arxiv.org/pdf/1805.04025.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)(PDF)

**Uber has released Ludwig, and open-source toolbox for building deep learning models without writing code.**
The tool is built on top of TensorFlow, Google’s ML library.
It’s centered around _encoders_ that map different data types to tensors (like CNNs for images and RNNs for text), _combiners_ that feed these tensors through neural networks, and _decoders_ that map the tensors back to data.
Uber has used Ludwig in several internal projects over the past two years, and it’ll be interesting to see what the wider community can do with it.

- Blog post by Piero Molino et al. for Uber Engineering, which includes a detailed example of using Ludwig for predicting book genres: [Introducing Ludwig, a Code-Free Deep Learning Toolbox](https://eng.uber.com/introducing-ludwig/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Landing page: [Ludwig](https://uber.github.io/ludwig/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Main repository of GitHub: [uber/ludwig](https://github.com/uber/ludwig?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**Ars Technica surveyed the different approaches 10 companies are taking to make lidar work.**
Lidar is the “laser radar” technology that self-driving cars (and other robots) use to create a 3D map of the world around them.

> The basic idea of lidar is simple: a sensor sends out laser beams in various directions and waits for them to bounce back.
> Because light travels at a known speed, the round-trip time gives a precise estimate of the distance.
> While the basic idea is simple, the details get complicated fast.
> Every lidar maker has to make three basic decisions: how to point the laser in different directions, how to measure the round-trip time, and what frequency of light to use.

The surveys describes the tradeoffs between different techniques for each of these, and then dives deep into the choices that individual companies like Velodyne, Luminar, Blackmore, and several others have made.
I’m surprised they’re publishing this as an online article–it would probably do well in an academic journal as well.

- Timothy B. Lee’s survey for Ars Technica: [How 10 leading companies are trying to make powerful, low-cost lidar](https://arstechnica.com/cars/2019/02/the-ars-technica-guide-to-the-lidar-industry/?utm_campaign=1de959f524-Benedict%27s%20Newsletter_COPY_01&utm_medium=email&utm_source=Benedict%27s%20newsletter&utm_term=0_4999ca107f-1de959f524-70536657)

## Tech and Startups 🚀

![Some tools in the "no code" stack (Ryan Hoover)](https://s3.amazonaws.com/revue/items/images/004/241/553/mail/1_t-KAcvxBmBhiwZbrEJGaUQ.png?1550139393)
_Some tools in the "no code" stack (Ryan Hoover)_

**Ryan Hoover wrote a post about the rise of indie makers who are building their online products without code.**
Ryan runs ProductHunt, a site where users “hunt” the internet for the best new tech products and discuss them on the platform, so he’s been seeing this trend first-hand for a while now.
His main thesis:

> Today anyone with a computer and access to the internet can build a website using tools far more powerful than Dreamweaver from two decades ago.
> But these GUI-based tools have extended far beyond static sites to fully functional applications.

He also lists some of the tools that you can use to build anything from a [single page site](http://carrd.co?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or [web shop](http://shopify.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to a [mobile app](http://thunkable.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or [chatbot](http://octaneai.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
It’s incredible how much you can set up in just a few hours of tinkering using the right tools; and even if many of them won’t scale to millions of users, they’re amazing for building out a minimum viable product (MVPs) to quickly test whether your idea has any footing.
Right now, I’m doing that myself by using [Zapier](http://zapier.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to test [automated Twitter content marketing](https://twitter.com/amazingroomswc?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for [Weekly.Cool](http://weekly.cool?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

- Ryan’s full post: [The Rise of “No Code”](https://medium.com/@rrhoover/the-rise-of-no-code-e733d7c0944d?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Medium)

**Sahil Lavingia wrote a blog post about his eight-year journey building Gumroad,** the online store that allows creators to sell their products directly to their audiences.
It’s a story of raising venture capital, growing a company, failing to meet targets, laying off all employees, and finally rebuilding the business not as a would-be-unicorn, but as a company primarily focused on creating value rather than revenue.
It’s a fascinating story, and definitely one of my favorite reads from the past few weeks.

- Sahil Lavingia: [Reflecting on My Failure to Build a Billion-Dollar Company](https://medium.com/@shl/reflecting-on-my-failure-to-build-a-billion-dollar-company-b0c31d7db0e7?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Medium)

## Cool Things ✨

![Bill & Melinda's 2019 annual letter was one of "surprises" (Gates Foundation)](https://s3.amazonaws.com/revue/items/images/004/241/989/mail/Screenshot_2019-02-14_at_12.05.08.png?1550145942)
_Bill & Melinda's 2019 annual letter was one of "surprises" (Gates Foundation)_

**Bill and Melinda Gates released their 2019 annual letter,** which discusses the philanthropic work they’re doing with the Gates Foundation.
In this year’s letter, Bill and Melinda discuss nine things they learned in the last year that most surprised them.
My favorite from Bill:

> I wish more people fully understood what it will take to stop climate change.
> You have probably read about some of the progress on electricity, as renewables get cheaper.
> But electricity accounts for only a quarter of all the greenhouse gases emitted around the world.
> … Solar panels are great, but we should be hearing about trucks, cement, and cow farts too.

And from Melinda:

> If you’re anything like me, I’m guessing toilets aren’t your favorite topic of conversation.
> But if you care about keeping girls in school, expanding women’s economic participation, and protecting them against violence, then we have to be willing to talk about toilets.

As usual, this year’s annual letter is worth a full read.
The Gates also did some media surrounding it (including a few videos in the article itself).

- Bill and Melinda Gates’ [2019 Annual Letter](https://www.gatesnotes.com/2019-Annual-Letter?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Marques Brownlee’s interview with Bill: [Talking Tech & Saving the World with Bill Gates!](https://www.youtube.com/watch?feature=youtu.be&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=4mxXdCUXSSs) (YouTube)
- The Gates on Colbert: [Bill & Melinda Gates Talk Taxing The Wealthy](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=qG3eNG2rO7o) (YouTube)

**Thanks for reading!**
As always, let me know what you thought of this issue using the buttons below or by sending me a message.
If you’re new here, subscribe for a new issue of Dynamically Typed every second Sunday!