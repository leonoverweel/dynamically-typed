# #6: Deep reinforcement learning, from an Atari zoo to a self-driving car in 20 minutes 

Reinforcement learning (RL) is a type of machine learning where an “agent” learns to achieve a task by continuously trying new things and observing the feedback it gets from its environment.
Deep RL, the combination of this concept with deep neural nets, has been a big research focus in the last two years.
This issue of DT features some of this recent research, in applications from self-driving cars to playing complicated video games, and of course much more ML and AI news from the last two weeks.
Let’s dive in.

## Productized Artificial Intelligence 🔌

![Mapillary's map of Amsterdam, with green lines indicating available street-level imagery, and icons indicating tags. (Mapillary)](https://s3.amazonaws.com/revue/items/images/004/198/786/mail/mapillary-2.jpg?1549189934)

_Mapillary's map of Amsterdam, with green lines indicating available street-level imagery, and icons indicating tags. (Mapillary)_

**Swedish startup Mapillary is an open platform that crowdsources images of streets** and then uses computer vision to identify and tag objects like stop signs, traffic lights, and manhole covers on the map – what OpenStreetMap is to Google Maps, Mapillary is to Street View.
It’s free for personal and non-profit use, and cities around the world are already using it for things like checking streets for potholes; in the future, Mapillary hopes to sell access to their database to self-driving car companies.
As with any crowd-sourced product, it’ll be interesting whether Mapillary can reach critical mass and how it’ll incentivize contributors (who don’t get paid) to help them get there.
More:

- Browse around the map yourself: [Mapillary](https://www.mapillary.com/app/?focus=map&lat=52.35310195496024&lng=4.883763916141675&menu=false&pKey=psvLqgY-VhkVViZDlgMrkg&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&x=0.6216437437477728&y=0.5139292283493687&z=11.345079927556345&zoom=0)
- Charlotte Jee at MIT Technology Review: [Crowdsourced maps should help driverless cars navigate our cities more safely](https://www.technologyreview.com/s/612825/open-source-maps-should-help-driverless-cars-navigate-our-cities-more-safely/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Mapillary isn’t alone in this field: [The Golden Age of HD Mapping for Autonomous Driving](https://medium.com/syncedreview/the-golden-age-of-hd-mapping-for-autonomous-driving-b2a2ec4c11d?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Medium)

**Waymo has received approval to build a factory for its self-driving cars in Michigan.**
The factory won’t be building cars from scratch, but rather retrofitting existing models from other manufacturers with the sensors etc.
required to make them drive themselves.
It’ll be interesting whose cars they’ll use for this, since I imagine existing car companies would much rather be building self-driving tech in-house than becoming just a parts supplier for Waymo.
Jon Fingas’ report at Engadget: [Waymo will build self-driving cars in Michigan](https://www.engadget.com/2019/01/22/waymo-to-build-self-driving-cars-in-michigan/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Remove.bg, the site that automatically removes backgrounds from images** (see [DT #4](https://www.getrevue.co/profile/dynamically-typed/issues/4-gan-you-feel-the-love-tonight-151860?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [DT #5](https://www.getrevue.co/profile/dynamically-typed/issues/5-hey-google-what-s-a-golden-kitty-153366?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), has now launched its API, along with paid tiers for high resolution images.
Prices range from $2 for a single HD image to $0.15 per image on the $749 per month business subscription plan.
I’ve really enjoyed following this project: it’s the perfect combination of a technically impressive machine learning feat and a great product launch.
Check it out at [remove.bg](https://www.remove.bg/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Sam Byford at The Verge wrote about all the ways AI has changed mobile photography.**
It’s a detailed overview that covers everything from Google Photos auto-tagging pictures of your dog to Night Sight making it possible to take pictures in the dark.
Check it out here: [How AI is changing photography](https://www.theverge.com/2019/1/31/18203363/ai-artificial-intelligence-photography-google-photos-apple-huawei?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Machine Learning Technology 🎛

![512x512 pixel images generated using BigGAN models. (Brock et al.)](https://s3.amazonaws.com/revue/items/images/004/196/926/mail/screenshot-2019-02-02-at-12-07.jpg?1549109620)

_512x512 pixel images generated using BigGAN models. (Brock et al.)_

**Andrew Brock et al.
DeepMind pre-published a new GAN paper.**
Their work, which involved optimizing Generative Adversarial Networks “at the largest scale yet attempted,” has resulted in some stunningly realistic-looking images that beat previous methods on metrics for both output variety and fidelity.
They trained the networks on hundreds of Google’s TPUs in parallel, which has also caused [one reviewer](https://openreview.net/forum?id=B1xsqj09Fm&noteId=HklmZ1xqhm&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to raise the issue of reproducibility, since this would require massive computational budgets.
The paper will be published at [ICLR 2019](https://iclr.cc/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), but it’s already available on arXiv: [Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/pdf/1809.11096.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (PDF).

**Google released a new benchmark and dataset for open domain question answering.**
Lots of AI-powered products, like voice assistants, need to answer complex natural-language questions using relatively unstructured data.
The new Natural Questions dataset includes questions from real Google users, along with Wikipedia articles that contain the answers to these questions.
The goal of benchmark is to extract the answer from page.
Read the announcement here: [Natural Questions: a New Corpus and Challenge for Question Answering Research](http://ai.googleblog.com/2019/01/natural-questions-new-corpus-and.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Wayve demonstrated a deep reinforcement learning approach to autonomous driving.**
Their approach requires only a single video feed as input (and not the usual expensive 3D mapping sensors), and learns to follow a lane from scratch in just 20 minutes.
The authors [claim in a blog post](https://wayve.ai/blog/learning-to-drive-in-a-day-with-reinforcement-learning?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that “the potential implications of [their] approach are huge,” but it’s important to remember that this is a preliminary result: this demonstration is on an empty road at slow speeds, while other approaches are already deployed on real roads.
On the other hand, it is exciting to see a company trying a novel approach in this field.
Read the full paper by Kendall et al.
here: [Learning to Drive in a Day](https://arxiv.org/pdf/1807.00412.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (PDF).

**Speaking of deep reinforcement learning: Uber just released a “zoo” of Atari-playing RL agents.**
They worked together with Google Brain and OpenAI (famous for [their RL gym](https://gym.openai.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) to create an open-source repository of trained deep RL agents that play different Atari games, along with tools to analyze how they work.
Their post includes two case studies on the sorts of questions that can be explored using this “zoo” of trained agents: creating high-level visualizations of deep RL algorithms, and examining whether different deep RL algorithms learn different game strategies.
They hope the zoo will encourage more research into understanding deep RL.

- Uber’s blog post: [Creating a Zoo of Atari-Playing Agents to Catalyze the Understanding of Deep Reinforcement Learning](https://eng.uber.com/atari-zoo-deep-reinforcement-learning/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- The accompanying paper on arXiv: [An Atari Model Zoo for Analyzing, Visualizing, and Comparing Deep Reinforcement Learning Agents](https://arxiv.org/pdf/1812.07069?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (PDF)
- The repository on GitHub: [uber-research/atari-model-zoo](https://github.com/uber-research/atari-model-zoo?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**DeepMind’s AlphaStar has mastered StarCraft II:** in a demonstration game, DeepMind’s software beat one of the strongest players of the game 5-0.
StarCraft is considered more difficult than other games (from Chess and Go to Atari games and Dota) because of its long-term planning, real time, and game theory aspects, and because it provides the player with incomplete information and a large action space.
DeepMind tackled this using a multi-agent RL process: they trained a bunch of bots up to a certain level, and then made them compete with each other to get better and better.
Both the ML and video game aspects of this go right over my head, but their blog post has some good visual explanations: [AlphaStar: Mastering the Real-Time Strategy Game StarCraft II](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/?utm_campaign=ea5bfae276-Benedict%27s%20Newsletter_COPY_01&utm_medium=email&utm_source=Benedict%27s%20newsletter&utm_term=0_4999ca107f-ea5bfae276-70536657)

## Tech and Startups 🚀

![The distribution of car trips by distance in the US. What happens to car sales when the first 3-5 miles of these trips shift to micromobility? (Horace Dediu, Micromobility)](https://s3.amazonaws.com/revue/items/images/004/197/828/mail/blogpost_disruption-01.png?1549144837)

_The distribution of car trips by distance in the US. What happens to car sales when the first 3-5 miles of these trips shift to micromobility? (Horace Dediu, Micromobility)_

**The second micromobility conference happened this week.**
What’s micromobility?
Horace Dediu (who runs the conference) defines it as utility transportation using powered vehicles that weigh less than 500kg: electric bikes and scooters.
Lime’s, Jump’s and Bird’s scooters became huge in the US in 2018, and they’re driving what Dediu envisions as “the unbundling of the car” – from the bottom (short trips) up, more and more trips will be micromobility-powered, which will decrease car utilization and eventually car sales.
As someone from the Netherlands, where getting in a car for any trip shorter than 5km is extremely unusual, this prediction makes perfect sense to me.
I’ve been living it for years, with human-pedalled bicycles instead of electric scooters.
(See [Modacity’s Building the Cycling City](http://www.modacitylife.com/building-the-cycling-city/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for a good primer on this.)

One problem that’s popped up with micromobility has been crashes: it’s dangerous for scooter riders to be around cars on the road, and dangerous for pedestrians to be around scooter riders on the sidewalk.
Some US cities have responded to this by banning or severely restricting the use of scooters.
This seems crazy to me.
Cities should be building cycling infrastructure, which will further enable transportation that’s both healthier for people and better for the environment, whether the bike lanes are used for micromobility or cycling.

This intersection of micromobility and cycling infrastructure is something that’s been both fascinating and frustrating to me in the past year, so I might write more about it in the future.
In the mean time, check out these posts (especially the first):

- Florent Crivello (product manager at Uber, which owns Jump): [Five Promises of Micromobility](https://florentcrivello.com/index.php/2019/01/28/five-promises-of-micromobility/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Horace Dediu’s blog posts: [Micromobility, an Introduction](https://micromobility.io/latest-news/2019/1/21/micromobility-an-introduction?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [Part 2: Disruption](https://micromobility.io/latest-news/2019/1/22/part-2-disruptionnbsp?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); also see the [Micromobility.io’s vision](https://micromobility.io/about/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Michal Naka: [Micromobility conference 2017 vs. 2019](https://twitter.com/michalnaka/status/1091062602866671616?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Twitter)

**Sony’s 3D cameras might be in the next iPhone.**
The 3D smartphone cameras that are coming to Huawai’s next generation of phones (see [DT #4](https://www.getrevue.co/profile/dynamically-typed/issues/4-gan-you-feel-the-love-tonight-151860?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) are now rumored to be coming to Apple’s next flagship phones too.
Apple has been pushing augmented reality a lot in the past few years, and this could bring the long-distance equivalent of the iPhone’s front-facing TrueDepth camera (used for FaceID and Memoji) to its main, rear camera.
It should make current apps that use the iOS ARKit framework much better, but, again, the real question is what cool new usecases developers will come up with as the sensor spreads to more phones.
Mark Gurman and Debby Wu’s report at Bloomberg: [Apple Is Planning 3-D Cameras for New iPhones in AR Push](https://www.bloomberg.com/news/articles/2019-01-30/apple-is-said-to-prep-new-3-d-camera-for-2020-iphones-in-ar-push?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Cool Things ✨

![Mobula rays in the Sea of Cortez. (OceanX)](https://s3.amazonaws.com/revue/items/images/004/198/916/mail/uploads_2F2019_2F1_2F16_2FOceanX_Mashable_01.09.19_20.jpg_2Ffit-in__1440x1440.jpg?1549194699)

_Mobula rays in the Sea of Cortez. (OceanX)_

**Mark Kaufman at Mashable did a deep dive deep-sea exploration.**
This is the kind of sci-fi technology story I love: OceanX is a company that builds submarines that have gone down to the deepest, darkest places of the sea to observe what goes on down there:

> Perhaps the greatest endorsement of the submersible’s reliability comes from the maker himself, Patrick Lahey, the creator of Triton Submarines.
> The subs aren’t released into the wild until he actually takes them to depth.

> “I dive in every one of the subs we build,” said Lahey, who said he’s made tens of thousands of dives.
> […] The OceanX submersibles are built to make thousands of dives.
> Like NASA’s now-retired Space Shuttles, they incur extreme environments, but are designed to be used repeatedly in some of the most extreme places humans can go.

> “To me, they really are spaceships,” said Lahey.

Read Kaufman’s full story here: [Uncharted Worlds: Descending into the dark sea is like exploring deep space](https://mashable.com/feature/deep-sea-exploration-space-oceanx/?europe=true&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#S7tkUM_5Saq7).

**Thanks for reading!**
Let me know what you thought of this issue using the buttons below or by sending me a message.
If you’re new here, subscribe for a new issue of Dynamically Typed every second Sunday!