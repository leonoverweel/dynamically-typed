# #10: A Turing Award for deep learning, and a bitter lesson for AI research? 

Hey everyone, welcome to the 10th (!) issue of Dynamically Typed.
Over the past few weeks, there was a lively debate in the AI research community about the use of brute-force computation vs.
human ingenuity in machine learning systems, sparked by Rich Sutton’s _The Bitter Lesson_ essay.
I dedicated the first section of today’s newsletter to summarizing that debate.
It’s a relatively technical discussion, so if that’s not your jam, feel free to skip forward to the _Productized AI_ section.

Other news this fortnight includes Nvidia’s GauGAN AI-assisted painting tool demo, Stanford’s new AI institute, and a very cool collaboration between The Met, Microsoft and MIT.
Finally, I’m also bringing back _People in AI_ to highlight a story about DeepMind cofounder Demis Hassabis and the three “fathers of deep learning” who just received the ACM Turing Award.

## A Bitter Lesson for AI Research? 🤔

**Rich Sutton wrote _The Bitter Lesson,_ an essay on the ineffectiveness of human knowledge in AI research.**
Sutton is a research scientist at DeepMind who, among other things, wrote the [reinforcement learning textbook](http://incompleteideas.net/book/the-book.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that I used in a course this semester.
He’s a big name in the field.
[In his March 13th essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), he asserts:

> The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation [like search and learning] are ultimately the most effective, and by a large margin.
> … We have to learn the bitter lesson that building in how we think we think does not work in the long run.

He cites examples from systems that beat humans at chess and Go, to current neural-based approaches to computer vision and natural language processing, to show that expertly crafted systems were all beat out by brute force search and learning algorithms once computers became fast enough.
Sutton thinks we should therefore focus on general methods, and that explicitly modelling systems after how we think our mind works is not a good long-term strategy.

Sutton’s essay sparked a lot of debate in the community; I’ve highlighted a few of the most interesting responses to the essay below.

[In a Twitter thread](https://twitter.com/shimon8282/status/1106534178676506624?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Oxford’s Shimon Whiteson points out that state-of-the-art deep learning-based AI approaches all still incorporate human knowledge in how they’re structured: CNNs use convolutions and LSTMs use recurrence, both big “human knowledge” innovations.
He continues:

> So the history of AI is not the story of the failure to incorporate human knowledge.
> On the contrary, it is the story of the success of doing so, achieved through an entirely conventional research strategy: try many things and discard the 99% that fail.

> The 1% that remain are as crucial to the success of modern AI as the massive computational resources on which it also relies.

Other responses include [A Better Lesson](https://rodneybrooks.com/a-better-lesson/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), where Rodney Brooks also asserts that the way humans wrangle increasing compute power is responsible for AI’s success; and [A Meta Lesson](http://andy.kitchen/a-meta-lesson.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), where Andy Kitchen argues that success lies in the combination of these two.
Finally, in [The Wrong Classroom](https://katbailey.github.io/post/the-wrong-classroom/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Katherine Bailey says that using all these well-defined problems as metrics for “AI” will naturally favor Sutton’s search- and learning-based systems, which may accomplish the given tasks, but do so _not_ _by being intelligent_ but “ _in virtue of having behaved intelligently:”_

> With computer chess, was the goal just to win at chess, or was chess chosen as a metric because it was believed that in order to master it you had to [think] the way humans did it?
> … Metrics for AI systems have to be well-defined, and my suspicion is that this makes them almost by definition solvable without something we humans would ever track as “intelligence.” But what does this matter?
> Sometimes the metric and the end goal are aligned, such as in the case of computer vision and speech recognition… But when they’re not, such as when the true end goal is something vague like “solving intelligence,” there may be many lessons learned but at least some AI researchers will simply be in the wrong classroom.

It’s been interesting seeing this debate unfold over the past few weeks, and I think I agree mostly with Brooks and Bailey.
I’d love to know what you all think, so here’s all the posts I mentioned above one more time if you’d like to read them all:

- Rich Sutton: [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Shimon Whiteson: [Twitter thread](https://twitter.com/shimon8282/status/1106534178676506624?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Rodney Brooks: [A Better Lesson](https://rodneybrooks.com/a-better-lesson/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Andy Kitchen: [A Meta Lesson](http://andy.kitchen/a-meta-lesson.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Katherine Bailey: [The Wrong Classroom](https://katbailey.github.io/post/the-wrong-classroom/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Productized Artificial Intelligence 🔌

![A waterfall landscape drawn using Nvidia's image generator (Nvidia).](https://s3.amazonaws.com/revue/items/images/004/422/337/mail/NVIDIA-GauGAN-AI-demo-screenshot.jpg?1554049892)

_A waterfall landscape drawn using Nvidia's image generator (Nvidia)._

**Nvidia unveiled GauGAN, a demo of a tool that can automatically paint photorealistic landscapes.**
In the tool, you draw a landscape using traditional Photoshop tools like a pencil or a paint bucket; but instead of painting with colors, you paint with concepts like _mountain_ , _sea_ and _snow_.
GauGAN then feeds your drawing through a Generative Adversarial Network (GAN) to turn it into a photorealistic painting.
Nvidia trained the GAN on a million images from Flicker to achieve this result and hopes to make the tool available in its [AI playground website](https://www.nvidia.com/en-us/research/ai-playground/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) soon.
Read more about GauGAN here:

- TechCrunch: [Nvidia AI turns sketches into photorealistic landscapes in seconds](https://techcrunch.com/2019/03/18/nvidia-ai-turns-sketches-into-photorealistic-landscapes-in-seconds/?guccounter=1&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- An in-depth explanation of how GauGAN works by Adam D. King: [Photos from Crude Sketches: NVIDIA’s GauGAN Explained Visually](https://adamdking.com/blog/gaugan/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Google demonstrated doing something similar in real time for games. Engadget: [Google Stadia can use AI to change a game’s art in real-time](https://www.engadget.com/2019/03/19/google-stadia-style-transfer/?guccounter=1&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Another simular tool from a few years ago: [Neural Doodle](https://github.com/alexjc/neural-doodle?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (GitHub)

**For Vogue Business, Maghan McDowell wrote about how physical retail is using AI.**
Luxury goods conglomerate Kering used an algorithm to identify likely repeat-customers based on their transactional data and gave those customers coupons to come back to the store, an approach that startup [Custora](https://www.custora.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) says helped them boost the number of “valuable customers” in stores by 20% over last year’s holiday period.
Some companies in China are also trialing tracking customers in stores using facial recognition.
[AI firm Volume](https://volume.ai/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)’s Chris Sykes thinks that people my age are “less concerned” about the privacy implications here, but I personally find both of these quite invasive and a bit too close to [_Minority Report_ -style advertising](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=uiDMlFycNrw) (YouTube).
You can read McDowell’s full piece here: [Stores get smart about AI](https://www.voguebusiness.com/technology/artificial-intelligence-physical-stores-kering-nike-alibaba?utm_campaign=d2b7126611-Benedict%27s%20Newsletter_COPY_01&utm_medium=email&utm_source=Benedict%27s%20newsletter&utm_term=0_4999ca107f-d2b7126611-70536657).

## Machine Learning Technology 🎛

**Stanford launched its new AI lab, the Institute for Human-Centered Artificial Intelligence (HAI).**
Its mission, [according to Stanford News](https://news.stanford.edu/2019/03/18/stanford_university_launches_human-centered_ai/?linkId=65009865&utm_campaign=%23stanfordhumanai&utm_content=university-communications_twitter_stanfordhai_https%3A%2F%2Fnews.stanford.edu%2F2019%2F03%2F18%2Fstanford_university_launches_human-centered_ai%2F%3Flinkid%3D64954743_20190319195900_2198494130&utm_medium=social&utm_source=twitter), is to “advance artificial intelligence (AI) research, education, policy and practice to improve the human condition.” The HAI symposium was incredibly star-studded, featuring speakers like Bill Gates, Reid Hoffman, Demis Hassabis, and Jeff Dean.
The Gradient wrote up all the talks [here](https://thegradient.pub/stanfords-human-centered-ai/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Shortly after the institute’s launch, however, it came under fire in the community.
[Chad Loder on Twitter](https://twitter.com/chadloder/status/1108588849503109120?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

> Stanford just launched their Institute for Human-Centered Artificial Intelligence (@StanfordHAI) with great fanfare.
> The mission: “The creators and designers of AI must be broadly representative of humanity.”

> 121 faculty members listed.

> Not a single faculty member is Black.

This is a pretty bad look for an institution with such lofty ambitions (the Stanford News article mentions the word “diversity” six times), especially considering the many recent examples of racial bias in machine learning algorithms.
Dave Gershgorn had a good take for Quartz, in which he highlights the some of the women of color leading the field of AI bias research: [Stanford’s new AI institute is inadvertently showcasing one of tech’s biggest problems](https://qz.com/1578617/stanfords-new-diverse-ai-institute-is-overwhelmingly-white-and-male/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
After [a similar story](https://gizmodo.com/stanfords-new-institute-to-ensure-ai-is-representative-1833464337?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) by Patrick O'Neill for Gizmodo, HAI updated its page to include one more faculty member: assistant professor of philosophy [Juliana Bidadanure](https://philosophy.stanford.edu/people/juliana-bidadanure?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

It’s a rough start for the institute, but hopefully this news cycle has served as a wakeup call for them.
Beside this issue, though, I think HAI’s cross-disciplinary approach will lead to lots of good and necessary AI fairness research.

**Google has appointed an external advisory council for its AI research.**
The company announced [its AI Principles](https://www.blog.google/technology/ai/ai-principles/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) last June, and this council (ATEAC) is in charge of making sure Google’s research adheres to them:

> This group will consider some of Google’s most complex challenges that arise under our AI Principles, like facial recognition and fairness in machine learning, providing diverse perspectives to inform our work.

From what I can see, Google has put together a council that’s diverse both in background and ([controversially so](https://www.technologyreview.com/s/613203/google-appoints-an-ai-council-to-head-off-controversy-but-it-proves-controversial/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) in perspective.
You can read the bios of ATEAC members on the company’s blog: [An external advisory council to help advance the responsible development of AI](https://www.blog.google/technology/ai/external-advisory-council-help-advance-responsible-development-ai/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
_Update: the council has been disbanded; see_[ _DT #11_](https://dynamicallytyped.com/issues/11-adobe-and-google-s-new-video-ai-tools-stanford-s-hype-for-gans-and-a-conversation-with-books-170283?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) _._

**Quick ML resource links ⚡️**

- Netron is a viewer that can visualize machine learning models from common model specification file types: [Netron](https://github.com/lutzroeder/netron?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (GitHub).

## People in AI 👩‍💻

![DeepMind cofounder Demis Hassabis (1843 Magazine)](https://s3.amazonaws.com/revue/items/images/004/419/813/mail/201904_FE_DEM_02-HEADER.jpg?1553981997)

_DeepMind cofounder Demis Hassabis (1843 Magazine)_

**1843 Magazine’s Hal Hodson did a feature on DeepMind cofounder Demis Hassabis.**[DeepMind](https://deepmind.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) is an AI company famous for reinforcement learning research accomplishments like [AlphaGo](https://deepmind.com/research/alphago/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which was the first computer program to beat a human in the ancient Chinese game of Go.
Hodson’s piece covers Hassabis’ past, from playing chess and Go as a child to building a gaming company and getting a PhD in neuroscience.
It also dives deep on DeepMind’s core mission: to “solve intelligence” and develop Artificial General Intelligence (AGI)—and on how Hassabis structured his company so that Google (which acquired DeepMind in 2014) won’t own the AGI if his team manages to develop it.
The feature is quite long, but definitely worth a read: [DeepMind and Google: the battle to control artificial intelligence](https://www.1843magazine.com/features/deepmind-and-google-the-battle-to-control-artificial-intelligence?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Yoshua Bengio, Geoffrey Hinton, and Yann LeCun received the Turing Award for their work in deep learning.**
The Turing Award is the computer science equivalent of the Nobel Prize in other scientific fields.
These three, sometimes referred to as “the fathers of deep learning,” have accomplished way too much between them for me to list here, so check out the ACM’s awards blog for their bios: [Fathers of the Deep Learning Revolution Receive ACM A.M.
Turing Award](https://awards.acm.org/about/2018-turing?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Cool Things ✨

![Gen Studio in action (The Met, Microsoft, and MIT)](https://s3.amazonaws.com/revue/items/images/004/421/464/mail/screenshot-2019-03-31-at-14-57.png?1554040756)

_Gen Studio in action (The Met, Microsoft, and MIT)_

**Microsoft, MIT and the Metropolitan Museum of Art did a joint hackathon that resulted in some cool projects:**

- _Gen Studio_ is super cool. You select a piece of art from The Met’s collection, and the website finds five pieces of related art and plots them on a map. You can then click any point on the map to generate a new piece of art that has a mix of the abstract features of the existing art works, weighted by how close you place the point to each of them. It’s quite fast and super fun to play with, so I recommend you check it out at [gen.studio](https://gen.studio?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
- _My Life, My Met_ “[turns] an Instagram feed into a work of art” by finding works in the Met that closely resemble the photos in someone’s Instagram. Check out [their pitch](https://www.microsoft.com/inculture/uploads/prod/2019/02/mylife-my-met.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (PDF).
- _Artwork of the Day_ analyzes a user’s location, weather, news and historical data to present a personalized piece of art from The Met’s collection each day. It’s sadly not available yet.

Check out the full post on Microsoft’s culture website for more projects: [Making art accessible to global audiences through artificial intelligence](https://www.microsoft.com/inculture/arts/met-microsoft-mit-ai-open-access-hack/?ocid=AID825421_QSG_PD_SCL_318673&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Thanks for reading!**
As always, let me know what you thought of this issue using the buttons below or by sending me a message.
If you’re new here, subscribe for a new issue of Dynamically Typed every second Sunday!