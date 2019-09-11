# #20: DeepMind's new podcast, AR navigation in Google Maps, and an AI Sowing App from India 

Hey everyone, welcome to the 20th edition of Dynamically Typed!
In productized artificial intelligence, I’m covering two apps with new AR features today: Socrates and Google Maps.
On the machine learning research side, DeepMind launched a podcast (hosted by Hannah Fry!), Distill experimented with a new type of scientific article, and I found a bunch of useful new resources.
For climate change AI, I’m covering the Microsoft AI for Earth grant-winning Sowing App and CCAI’s newsletter launch.
Finally, Google AI launched a very cool interactive online visualization of a fruit fly brain.

In personal news: I handed in my thesis— _Transfer Learning Random Forests with Different Feature Spaces for Fraud Detection_ —, capping off the MSc Artificial Intelligence I’ve been doing at the University of Edinburgh for the past year.
I did my thesis in collaboration with [Adyen](https://www.adyen.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and I interned at their office in Amsterdam during the duration of the project.
Hopefully I’ll be able to post it publicly soon; I’ll also share a bit more about what’s next for me in DT #21.

## Productized Artificial Intelligence 🔌

![Socratic extracts the underlying concepts of solving and simplifying square root equations from a photo of a math problem. (The Keyword)](https://s3.amazonaws.com/revue/items/images/004/899/821/mail/8d40f47ddcb1ce0252330d183961ccd9.png?1566126063)
_Socratic extracts the underlying concepts of solving and simplifying square root equations from a photo of a math problem. (The Keyword)_

**Socratic is a mobile learning app for high school and university students.**
The app lets you take a picture of something like a textbook page or a homework problem and then “X-rays” it to figure out what it’s about.
For a math problem, for example, it may be able to find step-by-step explanations for the specific exercise, guides for the concepts involved, and related tutoring videos on YouTube.
I think Socrates can be a super useful tool for students, but also something to be careful with: if you fall back to just looking at the Socratic explanation for a problem once you get a little bit stuck, you won’t learn much.
Socratic is available on iOS and is coming to Android soon.
The app got acquired by Google recently, so Shreyans Bhansali wrote about it for their The Keyword blog: [When students get stuck, Socratic can help](https://www.blog.google/outreach-initiatives/education/socratic-by-google/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Google maps AR navigation is launching on iOS and Android,** after it was teased for about two years and rolled out on Pixel phones earlier this year.
By using your phone’s camera to detect landmarks and match them to Street View imagery, Google Maps can now add an overlay a “Live View” with location markers and walking navigation directions over your phone’s camera feed.
Ron Amadeo for Ars Technica: [Google Maps AR Navigation comes to iPhones and Android devices](https://arstechnica.com/gadgets/2019/08/google-maps-ar-navigation-comes-to-iphones-and-android-devices/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Machine Learning Research 🎛

![The DeepMind podcast has 8 episodes that will be posted in the coming months. (DeepMind)](https://s3.amazonaws.com/revue/items/images/004/899/979/mail/1b4f249aadb2b260369350b76be43668.png?1566133064)
_The DeepMind podcast has 8 episodes that will be posted in the coming months. (DeepMind)_

**DeepMind launched its podcast, hosted by Hannah Fry.**
If you’re anything like me, you’ve seen [every Numberphile video featuring Hannah Fry](https://www.youtube.com/watch?list=PLt5AfwLFPxWKlde0YsnDEFXd-dK3dIZYh&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=BkOIw7vAZCQ), and you should probably subscribe to this podcast right now.
Here’s the pitch:

> Communicating a complex topic like AI research is not easy, and we’re grateful that this series is hosted by the brilliant Dr Hannah Fry, a mathematician and broadcaster with a talent for making technical topics accessible and interesting.
> We’ve worked together over the last 12 months to choose topics that we hope will convey the excitement of AI research, whilst also highlighting some of the questions and challenges the whole field is wrestling with today.
> The result is an eight-part series that explores topics such as the link between neuroscience and AI, why we use games in our research, building safe AI and how AI can be used to solve scientific problems.

There’s a three-minute [trailer for the podcast](https://deepmind.com/blog/article/welcome-to-the-deepmind-podcast?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) up on the DeepMind blog, and you can already subscribe to the podcast on [Apple podcasts](https://podcasts.apple.com/gb/podcast/deepmind-the-podcast/id1476316441?l=fr%20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Google podcasts](https://www.google.com/podcasts?feed=aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS9KVDZwYlBrZw%3D%3D&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Spotify](https://open.spotify.com/episode/0yKNxa7pPTt9imKX9XFgzS?si=GH3bY50DS6eYOQUyNnuUjQ&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), or wherever you listen to podcasts.

**Distill experimented with a new format for research discussions.**
Distill is a web-first machine learning journal that focuses on visualizations and explanations of ML models, like the [Activation Atlas](https://distill.pub/2019/activation-atlas/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for image classification networks (see [DT #9](https://dynamicallytyped.com/issues/9-openai-and-google-s-activation-atlases-a16z-s-ml-startup-investments-and-microsoft-s-ai-pipeline-163609?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
All articles published in the journal are responsive, interactive, open-source web pages (they even [accept pull requests](https://github.com/distillpub/post--gan-open-problems/pull/2?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) with updates after publication!), which is a welcome change from the usual process, in which papers are written, are discussed once at a conference, and then live statically in a repository.

Distill recently hosted another new type of publication: an in-depth “discussion article” for [a paper about adversarial examples](http://gradientscience.org/adv/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

> The paper was received with intense interest and discussion on social media, mailing lists, and reading groups around the world.
> How should we interpret these experiments?
> Would they replicate?
> … To explore these questions, Distill decided to run an experimental “discussion article.” We invited a number of researchers to write comments on the paper and organized discussion and responses from the original authors.

In this discussion, other researchers provided critiques and ran additional experiments, to which the original authors also responded.
The topic itself—transferring models trained on adversarial examples to real datasets—is a bit out of my area of expertise, but I find it exciting that Distill is continuing to innovate on the _process_ of machine learning science.
More:

- The discussion hosted by Distill: [A Discussion of _Adversarial Examples Are Not Bugs, They Are Features_](https://distill.pub/2019/advex-bugs-discussion/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Also see Distill’s [tweet](https://twitter.com/distillpub/status/1158862160845426688?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), where Chris Olah discusses the idea of hosting more similar discussions on the platform

**Rebecca Vickery wrote about Python libraries for interpretable machine learning.**
Her post is a brief guide to several visualization techniques that researchers and practitioners can use to inspect their models, to for example investigate whether they are picking up any problematic biases.
Vickery covers [yellowbrick](https://www.scikit-yb.org/en/latest/quickstart.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [ELI5](https://eli5.readthedocs.io/en/latest/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [LIME](https://github.com/marcotcr/lime?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and [MLxtend](https://rasbt.github.io/mlxtend/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), each with installation instructions and code examples.
Read the post on Medium: [Python Libraries for Interpretable Machine Learning](https://towardsdatascience.com/python-libraries-for-interpretable-machine-learning-c476a08ed2c7?sk=8b4f87a7b40c2a6075110fed8920fad4&source=friends_link&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**The Allen Institute for Artificial Intelligence published a best practices guide for crowdsourcing data labels.**
The post covers ethical pricing rates for different worker regions and types of labeling tasks, as well as notes on privacy, transparency, and tooling design.
Read the post on Medium: [Crowdsourcing: Pricing Ethics and Best Practices](https://medium.com/ai2-blog/crowdsourcing-pricing-ethics-and-best-practices-8487fd5c9872?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Quick ML resource links ⚡️** ([see all 38](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4))

- Andrej Karpathy’s arXiv Sanity is an interface for browsing, searching, and filtering recent arXiv submissions. Link: [karpathy/arxiv-sanity-preserver](https://github.com/karpathy/arxiv-sanity-preserver?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- TabNine adds deep-learning-powered autocompletion to code editors like VSCode (see [DT #18](https://dynamicallytyped.com/issues/18-runway-ml-s-app-store-for-ai-google-s-new-youtube-dataset-and-a-trippy-gan-journey-188184?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)). Link: [TabNine](https://tabnine.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Deeplearning.ai has a set of detailed, interactive AI Notes on things like initializing neural networks and parameter optimization in NNs. Link: [AI Notes](https://www.deeplearning.ai/ai-notes/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Artificial Intelligence for the Climate Crisis 🌍

![Infographic explaining the sowing app. (ICRISAT)](https://s3.amazonaws.com/revue/items/images/004/899/796/mail/d1e2f5f97628efa2bae61a971e5eba03.jpeg?1566125748)
_Infographic explaining the sowing app. (ICRISAT)_

**The AI Sowing App is helping farmers in southeast India use their land more efficiently.**
As the world population continues to expand and climate change accelerates, it’ll become increasingly important to use farmland efficiently.
(The alternative—cutting down forests to make more land available to agriculture—is already having [devastating results](https://www.nytimes.com/2019/07/28/world/americas/brazil-deforestation-amazon-bolsonaro.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).) The International Crop Research Institute for Semi-Arid Tropics (ICRISAT), with the help of a Microsoft AI for Earth grant, is helping farmers in Andhra Pradesh, India, do exactly this:

> The AI Sowing App draws on more than 30 years of climate data, real-time weather information, and sophisticated forecasting models powered by Azure AI to determine the optimal time to plant, the ideal sowing depth, how much farm manure to apply, and more.

In the program’s first year, the 175 farmers who were using the app waited three weeks longer than usual to plant their crops—and, on average, they harvested _30% more_ _per hectare_ as a result.
In the most recent year, 3,000 farmers used the app, increasing their yields by 10-30%.
Incredible results.
More:

- Jean-Philippe Courtois wrote a post about the app and a few other projects for the Official Microsoft Blog: [Harnessing the power of AI to transform agriculture](https://blogs.microsoft.com/blog/2019/08/07/harnessing-the-power-of-ai-to-transform-agriculture/?ocid=FY20_soc_omc_br_tw_AIAg2&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
- Microsoft also has [an interactive map](https://msit.powerbi.com/view?r=eyJrIjoiYThkYjFmNTEtOGUwOC00NmViLWIzZTUtNjY2OTU5MzUxOTRhIiwidCI6IjcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0NyIsImMiOjV9&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) with all 124 recipients of the AI for Earth grant (desktop only), as well as [a list of featured projects](https://www.microsoft.com/en-us/ai/ai-for-earth-projects?activetab=pivot1%3Aprimaryr2&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Climate Change AI launched their newsletter.**
CCAI published their 97-page _Tackling Climate Change with Machine Learning_ [paper](https://arxiv.org/abs/1906.05433?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) in June, ran the namesake [ICML 2019 workshop](https://www.climatechange.ai/ICML2019_workshop.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (see DT #16), and will run a [NeurIPS 2019 workshop](https://www.climatechange.ai/NeurIPS2019_workshop.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) on the topic as well.
They’re really firing on all cylinders.
Their newsletter is a bit more aimed at researchers than DT is: the first edition covers links to recently published papers, calls for collaboration, grant opportunities, and academia + industry job openings.
You can read it and subscribe here: [Climate Change AI Newsletter](https://mailchi.mp/47821c475c6f/climate-change-ai-mailing-list-welcome-and-neurips-workshop?e=0799ab1644&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Cool Things ✨

![A 40-nanometer slice of a fly brain with colored sections highlighted (left) and the corresponding 3D networks (right). (Neuroglancer)](https://s3.amazonaws.com/revue/items/images/004/899/414/mail/88180de1fac032b18d02c92eac2e8c92.png?1566113078)
_A 40-nanometer slice of a fly brain with colored sections highlighted (left) and the corresponding 3D networks (right). (Neuroglancer)_

**Researchers at Google AI built Neuroglancer, an interactive 3D visualization tool for a fruit fly brain.**
The Howard Hughes Medical Institute used a transmission electron microscope to image thousands of 40-nanometer slices of a fly brain.
Google AI researchers then used thousands of Cloud TPUs running combination of flood-filling networks (FNNs) and Segmentation-Enhanced CycleGANs (SECGANs), to turn the resulting 40 trillion pixels of brain imagery into a 3D network.
Neuroglancer is an online tool to visualize this network, and although I didn’t really know _what_ I was looking at, I really enjoyed playing around with it.
You can pan and scroll on the left panel to select a slice to look at, click a region of the slice to color it and show its part of the network, and then pan around the entire 3D network on the right panel.
More:

- Peter H. Li and Jeremy Maitin-Shepard for the Google AI Blog: [An Interactive, Automated 3D Reconstruction of a Fly Brain](https://ai.googleblog.com/2019/08/an-interactive-automated-3d.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Try out the demo: [Neuroglancer](https://neuroglancer-demo.appspot.com/fafb.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#!%7B%22layers%22:%5B%7B%22source%22:%22precomputed://gs://neuroglancer-fafb-data/fafb_v14/fafb_v14_orig%22%2C%22type%22:%22image%22%2C%22name%22:%22fafb_v14%22%2C%22visible%22:false%7D%2C%7B%22source%22:%22precomputed://gs://neuroglancer-fafb-data/fafb_v14/fafb_v14_clahe%22%2C%22type%22:%22image%22%2C%22name%22:%22fafb_v14_clahe%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22mesh%22:%22precomputed://gs://neuroglancer-fafb-data/elmr-data/FAFBNP.surf/mesh%22%2C%22segments%22:%5B%221%22%2C%2210%22%2C%2211%22%2C%2212%22%2C%2213%22%2C%2214%22%2C%2215%22%2C%2216%22%2C%2217%22%2C%2218%22%2C%2219%22%2C%222%22%2C%2220%22%2C%2221%22%2C%2222%22%2C%2223%22%2C%2224%22%2C%2225%22%2C%2226%22%2C%2227%22%2C%2228%22%2C%2229%22%2C%223%22%2C%2230%22%2C%2231%22%2C%2232%22%2C%2233%22%2C%2234%22%2C%2235%22%2C%2236%22%2C%2237%22%2C%2238%22%2C%2239%22%2C%224%22%2C%2240%22%2C%2241%22%2C%2242%22%2C%2243%22%2C%2244%22%2C%2245%22%2C%2246%22%2C%2247%22%2C%2248%22%2C%2249%22%2C%225%22%2C%2250%22%2C%2251%22%2C%2252%22%2C%2253%22%2C%2254%22%2C%2255%22%2C%2256%22%2C%2257%22%2C%2258%22%2C%2259%22%2C%226%22%2C%2260%22%2C%2261%22%2C%2262%22%2C%2263%22%2C%2264%22%2C%2265%22%2C%2266%22%2C%2267%22%2C%2268%22%2C%2269%22%2C%227%22%2C%2270%22%2C%2271%22%2C%2272%22%2C%2273%22%2C%2274%22%2C%2275%22%2C%228%22%2C%229%22%5D%2C%22skeletonRendering%22:%7B%22mode2d%22:%22lines_and_points%22%2C%22mode3d%22:%22lines%22%7D%2C%22name%22:%22neuropil-regions-surface%22%2C%22visible%22:false%7D%2C%7B%22type%22:%22mesh%22%2C%22source%22:%22vtk://https://storage.googleapis.com/neuroglancer-fafb-data/elmr-data/FAFB.surf.vtk.gz%22%2C%22vertexAttributeSources%22:%5B%5D%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20emitRGBA%28vec4%281.0%2C%200.0%2C%200.0%2C%200.5%29%29%3B%5Cn%7D%5Cn%22%2C%22name%22:%22neuropil-full-surface%22%2C%22visible%22:false%7D%2C%7B%22source%22:%22precomputed://gs://fafb-ffn1-20190805/segmentation%22%2C%22type%22:%22segmentation%22%2C%22segments%22:%5B%224613663523%22%2C%224628415467%22%2C%225288638170%22%2C%225546405906%22%2C%225676349851%22%5D%2C%22skeletonRendering%22:%7B%22mode2d%22:%22lines_and_points%22%2C%22mode3d%22:%22lines%22%7D%2C%22name%22:%22fafb-ffn1-20190805%22%7D%5D%2C%22navigation%22:%7B%22pose%22:%7B%22position%22:%7B%22voxelSize%22:%5B4%2C4%2C40%5D%2C%22voxelCoordinates%22:%5B124342.859375%2C67671.6015625%2C3069.28271484375%5D%7D%7D%2C%22zoomFactor%22:34.77285366930207%7D%2C%22showAxisLines%22:false%2C%22perspectiveOrientation%22:%5B0.2962014973163605%2C-0.356022447347641%2C-0.765893816947937%2C0.446003794670105%5D%2C%22perspectiveZoom%22:2682.282950255809%2C%22layout%22:%22xy-3d%22%7D)

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
🤩