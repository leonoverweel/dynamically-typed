# #5: Hey Google, what's a Golden Kitty? 

Hi and welcome to issue #5 of Dynamically Typed!
There are 25 of you now, a number that has been approximately doubling for every issue I’ve sent out – so, by a bit over a year from now, if this trend continues, every person in the world should be subscribed.
But how am I ever [going to afford that many grains of wheat](https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)?

This issue covers Uber’s myriad use cases for ML, the 2019 Consumer Electronics Show, Golden Kitties for AI products, and much more.
Let’s dive in.

## Productized Artificial Intelligence 🔌

![OneSoil's AI-generated map of different crop fields in the Netherlands (OneSoil)](https://s3.amazonaws.com/revue/items/images/004/125/382/mail/Screenshot_2019-01-20_at_15.15.34.png?1547997371)
_OneSoil's AI-generated map of different crop fields in the Netherlands (OneSoil)_

**ProductHunt announced the Golden Kitty awards,** which this year included an AI & Machine Learning Product of the Year category.
The winner is [OneSoil Map](https://www.producthunt.com/posts/onesoil-map-2?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (ProductHunt), [an interactive map](https://map.onesoil.ai/2018?about&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#3.6/50.49/4.96) (Web) that detects 60 million fields across the US and Europe and classifies them by one of 20 crop types, all from satellite images.
It’s super cool to scroll around – make sure you zoom in!
More:

- In 2nd place: [remove.bg](https://www.producthunt.com/posts/remove-bg?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (ProductHunt), the image background removal site [I wrote about last month](https://www.getrevue.co/profile/dynamically-typed/issues/3-happy-holidays-149573?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Revue)
- In 3rd place: [Facehub](https://www.producthunt.com/posts/facehub?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (ProductHunt), a real time face-to-face swap app on iPhone
- The full list of the year’s ProductHunt awards: [Winners of the 2018 Golden Kitty Awards are revealed](https://blog.producthunt.com/winners-of-the-2018-golden-kitty-awards-are-revealed-881c205a1e1f?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Medium)

**Jeremy Hermann and Mike Del Balso posted a deep dive on how ML is used at Uber.**
Use cases include personalized Uber Eats rankings, driver/rider marketplace forecasting, customer support automation, crash detection using drivers’ phones, ETAs, “one-click” chat replies for drivers, and self-driving cars.
The post also covers how ML works on both organizational and technical levels at Uber: [Scaling Machine Learning at Uber with Michelangelo](https://eng.uber.com/scaling-michelangelo/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Web)

**Google Assistant** **now has an _interpreter mode_** : ask any Google-powered smart speaker “Hey, Google help me speak Dutch” (or any of the other 27 supported languages), and it’ll translate everything you say.
Then, when the person you’re talking to replies, it’ll translate what they say back to English (or to whichever language you were speaking to begin with).
It’s not perfect, but if I was, say, an Airbnb host who’s receiving foreign guests, I’d want this _yesterday_.
Shannon Liao at The Verge got a demo: [Google Assistant’s new interpreter mode can translate conversations — but it’s not magic ](https://www.theverge.com/2019/1/8/18170806/google-assistant-translate-languages-real-time-interpreter-ces-2019?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)(Web)

**Marques Brownlee got to ride in a driverless taxi** at CES 2019.
This self-driving car by Yandex is another example of a system that’s close to being autonomous in a very restricted geographic area, like we’ve seen before from Google, Waymo and Voyage.
I wouldn’t be surprised to see the first real public deployment of a self-driving taxi fleet in (a small part of) a city sometime this year.
Check out MKBHD’s video here: [Riding in a Driverless Taxi at CES 2019!](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=gfWjsKsEry0) (YouTube)

**Chris Hartland at Textio** (an “augmented writing” service that aims to improve all kinds of writing in businesses) wrote a blog post on how to think about machine learning for products.
The upshot: don’t build a product around your ML model – build a great product that happens to be powered by ML.
The former is something we’ve seen a lot of in recent years ( _cough NoSQL, cough blockchain_ ), so I think it’s a good take: [Machine Learning in Production ](https://hackernoon.com/machine-learning-in-production-ed65c58ffd1e?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)(Medium).

## Machine Learning Technology 🎛

**Jeff Dean has posted a look back at Google’s AI research in 2018** on the Google AI blog.
In a broad overview, it covers everything from Google’s open source datasets and AI ethics principles, to their papers on perception and computational photography.
It’s pretty crazy how many different areas Google’s research touched on last year: [Looking Back at Google’s Research Efforts in 2018](http://ai.googleblog.com/2019/01/looking-back-at-googles-research.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Web)

**Microsoft has launched their Ability Initiative** with the University of Texas at Austin.
They’re aiming to improve automatic image captioning for blind and low-vision people.
See their announcement here: [Microsoft Ability Initiative](https://www.microsoft.com/en-us/research/blog/microsoft-ability-initiative-a-collaborative-quest-to-innovate-in-image-captioning-for-people-who-are-blind-or-with-low-vision/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Web).

**Lionel Gueguen et al.
at Uber Engineering** blogged about their paper speeding up convolutional neural networks (CNNs) that take JPEG images as input.
Their main insight is that (1) the bottom few layers of a typical CNN mostly transforms an image from pixels to a frequency representation and (2) the last steps of JPEG decompression do the exact opposite – so you could strip these both out and feed JPEG’s internal frequency representation straight into the CNN!
Gueguen’s approach yields a slight accuracy improvement on the standard ImageNet classification task, but, amazingly, also a _1.8x speed improvement_.

- [Their post on the Uber Engineering blog](https://eng.uber.com/neural-networks-jpeg/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Web)
- [Their paper at NeurIPS](https://papers.nips.cc/paper/7649-faster-neural-networks-straight-from-jpeg.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (PDF)

## Tech and Startups 🚀

![LG's rollable TV, showed off at CES, hides itself in its speaker bar when you're done using it (LG)](https://s3.amazonaws.com/revue/items/images/004/124/935/mail/lg-rollable-tv-ces-2019_key-visual.jpg?1547986676)
_LG's rollable TV, showed off at CES, hides itself in its speaker bar when you're done using it (LG)_

**Earlier this month, the Consumer Electronics Show (CES) happened.**
Lots of companies showed off their vision for the future, from the coming year’s television sets all the way to far-out visions for self-driving car interiors.
There’s always a lot of coverage of CES, and I’ve collected the best of it right here so you don’t have to dig through the cynical hot takes yourself:

- As usual, Steven Sinofsky of Andreessen Horowitz (a16z) wrote up an extensive show report. Lots of internet-connected home stuff, most of it now capable of talking to voice assistants, and lots of things that call themselves AI but aren’t. Read it here, and scroll about 80% down for the amazing “just have to share” section:[ CES 2019: A Show Report ](https://medium.learningbyshipping.com/ces-85ca9f07c08a?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)(Medium)
- Samuel Axon at Ars Technica has a a good run-down of products announced at CES that will actually come on the market in 2019. From laptops and TVs to smart clocks and VR, it’s mostly iterative improvements on already good products: [The best PCs, gadgets, and future tech of CES 2019](https://arstechnica.com/gadgets/2019/01/the-best-pcs-gadgets-and-future-tech-of-ces-2019/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Web)
- LG’s rollable TVs looks really cool. A lot of people don’t like the look of a big black screen in their living room, and this looks like a much better solution than those TVs that try to pretend a wall when they’re off. Check out Marques Brownlee’s video: [The Rollable OLED TV: The Potential is Real!](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=D1pa3UX89GA) (YouTube)

**Benedict Evans at a16z wrote a post on the promise of 5G,** the successor standard to the 4G we currently have in our phones.
It’ll mostly have lower latency for phones at long distances, and higher speed at short distances (to replace your internet cable).
A lot of the hype in the industry is around 5G-enabled virtual reality, augmented reality and self-driving cars, but out of those Evans thinks it’ll only make a real difference for AR, and maybe for last-mile remote piloting of delivery trucks.
Network slicing is 5G’s most interesting feature:

> One of the cooler features of 5G is that it lets you split out dedicated capacity for particular use cases - so-called ‘network slicing’.
> Today (to simplify hugely), although network operators try to do traffic management, all traffic in the cell is fundamentally using the same capacity.
> 5G lets you create dedicated private capacity in the radios network with specific characteristics.
> So, you could sell a truck operator dedicated capacity on the two miles between a specific freeway exit and a specific warehouse.
> Or, you could offer an IoT operator (or alarm company) much lower bandwidth but over a wider area.

Read Evans’ full post here: [5G: if you build it, we will fill it](https://www.ben-evans.com/benedictevans/2019/1/16/5g-if-you-build-it-we-will-fill-it?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Web)

**Amazon launched DocumentDB** , its MongoDB competitor.
While AWS adds new services pretty much every other week, this launch is interesting because it tells a bigger story about the state of open source software.
Basically, lots of VC-funded open source software companies supported itself by helping big companies install and run their software on their servers, consultancy-style.
But now that everything is moving to the cloud (and mostly Amazon’s cloud), and no one’s running their own servers anymore, where will these software companies make money?
And what does this mean for the open source ecosystem?
Ben Thompson’s take at Stratechery: [AWS, MongoDB, and the Economic Realities of Open Source ](https://stratechery.com/2019/aws-mongodb-and-the-economic-realities-of-open-source/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)(Web)

## Cool Things ✨

![A screenshot about 2/3rds down Cameron's World (cameronsworld.net)](https://s3.amazonaws.com/revue/items/images/004/123/809/mail/Screenshot_2019-01-19_at_19.04.18.png?1547924690)
_A screenshot about 2/3rds down Cameron's World (cameronsworld.net)_

**This isn’t exactly new, but I think it’s _amazing:_** at Cameron’s World, [Cameron Askin](https://twitter.com/cameronaskin/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Twitter) is recreating beautiful, weird websites from the 90s that were created before everything got slurped up into algorithm-ordered news feeds.
This stuff was a little before my time online, but it’s a ton of fun to scroll through.
Check it out at [cameronsworld.net](http://cameronsworld.net?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Web).

**Hossein Derakhshan, who went to jail for blogging in Iran,** wrote a blog post reflecting on the state of the internet today, where the power has shifted from people (hyper)linking to each others’ blogs to big American companies siloing content into their “Streams.” Here’s an excerpt:

> Nearly every social network now treats a link as just the same as it treats any other object — the same as a photo, or a piece of text — instead of seeing it as a way to make that text richer.
> You’re encouraged to post one single hyperlink and expose it to a quasi-democratic process of liking and plussing and hearting: Adding several links to a piece of text is usually not allowed.
> Hyperlinks are objectivized, isolated, stripped of their powers.

The whole post is definitely worth a read, and it made me appreciate platforms (like this one!) where it’s just me and you controlling the conversation.
I choose when to send emails, and you choose whether and when to open them, with no content ranking algorithm in between.
If Revue, the platform I use to send these emails, shuts down or kicks me off, I can use another one and you likely won’t even notice the difference.
That’s very different from Facebook, Twitter, or Instagram.
It’s a bit ironic, then, that Derakhshan’s post is on Medium – a platform that’s great for distributing content to “the Stream,” but that keeps a blogger’s audience and domain under its control.
Read the post here: [The Web We Have to Save](https://medium.com/matter/the-web-we-have-to-save-2eb1fe15a426?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Medium)

**Thanks for reading!**
As always, please let me know what you thought using the buttons below or by sending me a message.
If you enjoyed this issue, why not forward it to a friend or share it somewhere?
:)

PS: In this issue, I started **bolding** the start of new topics, since I’ve started writing multiple paragraphs about some topics, which I thought was a bit confusing in issue #4.
Do you like the change?
Let me know!