# #29: BNNs and visual abstractions at NeurIPS 2019, and petabytes of climate data on Google Cloud 

Hey everyone, welcome to Dynamically Typed #29!
This week I’m shuffling the order of the newsletter around a bit.
A ton happened in climate change AI—from solar panels in China to NOAA data dropping on Google Cloud—, and lots of research content came out of the the 33rd annual Neural Information Processing Systems (NeurIPS) conference—including some work from my coworkers at Plumerai.
I’m focussing on those this week, and pushing productized AI stuff to the next issue.
So without further ado, let’s dive straight in!

## Artificial Intelligence for the Climate Crisis 🌍

![A map of the over 500 large-scale solar power plants in China detected by SolarNet, which in total cover an area of 2,000 square kilometers.](https://s3.amazonaws.com/revue/items/images/005/357/413/mail/15394e028ffc117fa6ca66484c429c55.png?1576934398)

_A map of the over 500 large-scale solar power plants in China detected by SolarNet, which in total cover an area of 2,000 square kilometers._

**Researchers from the Chinese WeBank AI Group published SolarNet,** “a deep learning framework to map solar power plants in China from satellite imagery.” The paper contains quite a detailed overview of their methods, including their data source, network architecture, training procedure, and several examples of data points where their approach was successful and unsuccessful.
(Their dataset and code are not available though.) This work is important because it can help track the deployment of solar parks over time in different regions, which is valuable information for the policymakers, investors, and power companies who are working on getting renewables quickly and efficiently.
More:

* Paper by Hou et al. (2019) on arXiv: [SolarNet: A Deep Learning Framework to Map Solar Power Plants In China From Satellite Imagery](https://arxiv.org/abs/1912.03685?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* [Open Climate Fix](https://openclimatefix.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is also working on a similar project; see this post by Damien Tanner: [Starting work on solar PV mapping](https://openclimatefix.org/blog/2019-07-09-solar-pv-mapping?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**Google Cloud is now hosting several climate-related datasets in formats easily accessible to AI researchers and ML engineers.**

**The first dataset** is the Coupled Model Intercomparison Project Phase 6 (CMIP6) data archive by the World Climate Research Programme, “aggregating the climate models created across approximately 30 working groups and 1,000 researchers investigating the urgent environmental problem of climate change.” CMIP6 includes historical data, models, high-resolution simulations of rare events covering…

> […] everything from forest transpiration in the Amazon rainforest and thunderstorms in the U.S.
> Midwest to the formation of meltwater ponds on Arctic sea ice.
> […] On Google Cloud, this dataset will be continuously updated and available to researchers around the globe to use for their own projects—without the constraints of downloading terabytes or even petabytes of data.

It’s very cool to see these data being made accessible at this scale, and I’m sure we’ll see more machine learning projects pop up built on top of them.
Shane Glass for the Google Cloud blog: [New climate model data now in Google Public Datasets](https://cloud.google.com/blog/products/data-analytics/new-climate-model-data-now-google-public-datasets?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**The second dataset** comes from the U.S.
National Oceanic and Atmospheric Administration (NOAA), in the form of 5 petabytes of data including…

> […] real-time satellite imagery, more than 20 years’ worth of the National Water Model, historic storm event data, aggregated lighting strike data, precipitation data back to the 1700s, and data on shipping patterns dating back to the 1600s [and more].

The data will be available across Google products such as Cloud Storage and Kaggle.
This makes them easily accessible to ML/AI researchers and engineers because they fit into our existing workflows, from competing in Kaggle competitions to pulling data from Google Cloud into our models using frameworks e.g.
TensorFlow Datasets.
Check out this second post on the Google Cloud blog by Shane Glass for examples of how the data could be used in ML models, including early wildfire detection and real-time disaster information services: [Big data, big world: new NOAA datasets available on Google Cloud](https://cloud.google.com/blog/products/data-analytics/weather-climate-big-data-from-noaa-now-in-cloud?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

![The Discover tab on Mattermore.](https://s3.amazonaws.com/revue/items/images/005/359/361/mail/4abd17565189879bd22f05993b7a1d9a.png?1577020393)

_The Discover tab on Mattermore._

**Mattermore is a community bringing people with data science skills together with organizations working on climate change.**
The platform has posts in several categories, including projects people are working on; people and organizations looking for help on projects; machine learning + climate job posts; and resources.
In just a short time browsing through Mattermore, I’ve already found a ton of interesting projects, some of which I’ll cover in future editions of DT.

The platform is currently still in closed beta, but if you’re interested in applying your data science or machine learning skills to impactful climate projects, drop me an email and I’ll get you an invite link.
In the meantime, you can learn more on their website: [Mattermore - Data Science for the Climate](https://www.mattermore.io/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Machine Learning Research 🎛

**The 33rd annual Neural Information Processing Systems (NeurIPS) conference happened in Vancouver last week.**
NeurIPS is one of the biggest AI conferences, so it’s always a very exciting week.
I’ve gone in depth about two papers from the conference in the _cool things_ and _my stuff_ sections below; look for my coverage of the climate change AI panel and workshop in the next issue of DT!
Here are some links to other interesting stuff from NeurIPS 2019:

* Tiernan Ray wrote a really nice overview of some cool papers from NeurIPS 2019 for ZDNet: [Google, Intel, MIT, and more: a NeurIPS conference AI research tour](https://www.zdnet.com/article/google-intel-mit-and-more-a-neurips-conference-ai-research-guided-tour/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* NeurIPS had a retrospectives section this year where people could reflect on things they learned after publishing a paper. This one by Jonathan Frankle is quite insightful: [A Retrospective for “Lessons Learned from The Lottery Ticket Hypothesis”](https://ml-retrospectives.github.io/neurips2019/accepted_retrospectives/2019/lottery-ticket/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Overviews of papers by the big tech companies: [Apple](https://machinelearning.apple.com/2019/12/02/apple-at-neurips-2019.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Google](https://ai.googleblog.com/2019/12/google-at-neurips-2019.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Cool Things ✨

![Ink prints of visual abstractions of ImageNet categories: "cello, cabbage, hammerhead shark, iron, tick, starfish, binoculars, measuring cup, blow dryer, and jacko-lantern."](https://s3.amazonaws.com/revue/items/images/005/357/417/mail/2a1978f3763b1e798b1b61638ea4b41c.png?1576934479)

_Ink prints of visual abstractions of ImageNet categories: "cello, cabbage, hammerhead shark, iron, tick, starfish, binoculars, measuring cup, blow dryer, and jacko-lantern."_

**Tom White used neural networks to generate abstract art that can be correctly classified by other neural networks.**
Working at New Zealand’s Victoria University of Wellington School of Design, White published his work at NeurIPS 2019 in a paper titled _Shared Visual Abstractions_ :

> This paper presents abstract art created by neural networks and broadly recognizable across various computer vision systems.
> The existence of abstract forms that trigger specific labels independent of neural architecture or training set suggests convolutional neural networks build shared visual representations for the categories they understand.
> Computer vision classifiers encountering these drawings often respond with strong responses for specific labels - in extreme cases stronger than all examples from the validation set.
> By surveying human subjects we confirm that these abstract artworks are also broadly recognizable by people, suggesting visual representations triggered by these drawings are shared across human and computer vision systems.

The paper is a great and quite accessible read, and I really love seeing this kind of work at the intersection of art and actually understanding what goes on inside convolutional neural networks.
Read the White (2019) paper on arXiv: [Shared Visual Abstractions](https://arxiv.org/abs/1912.04217?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); and see the code on GitHub: [dribnet/perceptionengines](https://github.com/dribnet/perceptionengines?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## My Stuff 😁

![Plumerai's poster for "Latent Weights do not Exist: Rethinking Binarized Neural Network Optimization." I did not write this paper, but I did work on the poster.](https://s3.amazonaws.com/revue/items/images/005/357/421/mail/dc9e2c1d489804eef8317e488a4f74fd.png?1576934618)

_Plumerai's poster for "Latent Weights do not Exist: Rethinking Binarized Neural Network Optimization." I did not write this paper, but I did work on the poster._

**Three of my coworkers at Plumerai also went to NeurIPS to present our company’s first paper,** _Latent Weights do not Exist: Rethinking Binarized Neural Network Optimization_.
(See [DT #22](https://dynamicallytyped.com/issues/22-mobile-apps-that-identify-plant-species-ai-powered-posture-correction-and-my-new-job-197292?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for more about BNNs and Plumerai.) In the paper, Helwegen et al.
introduce the first neual network optimizer designed specifically for BNNs, lovingly called [_Bop_](https://larq.dev/api/optimizers/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#bop).
It can train binary networks from the literature to perform better on ImageNet classification than previous latent weights-based optimizers could.
Although all this very cool research was done before I joined Plumerai, I did spend a lot of time with Koen and Lukas designing the poster for the paper.

Inspired by the [#betterposter movement](https://twitter.com/mikemorrison/status/1110191245035479041?lang=en&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), the bold title section in the middle is meant to attract the attention of researchers browsing through a room filled to the brim with dozens to hundreds of posters.
We also tried to limit ourselves in how much text we used, so that the poster could tell a clear story and encourage an interested viewer to look up the full paper for more details of the work.
We made the poster in vector graphics design program [Figma](https://www.figma.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and laid everything out on a grid pattern that made it easy to align all the elements neatly.

We’re super happy with how the poster turned out, and it was [very well-received at at NeurIPS](https://twitter.com/plumeraihq?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) too!
For more info, see the [paper](https://arxiv.org/abs/1906.02107?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [code](https://github.com/plumerai/rethinking-bnn-optimization?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and [poster](https://github.com/plumerai/rethinking-bnn-optimization/blob/master/poster.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
🧙‍♀️