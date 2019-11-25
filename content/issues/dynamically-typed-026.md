# #26: Chollet's Measure of Intelligence, and BERT in Google Search 

Hey everyone, welcome to Dynamically Typed #26!
Today’s issue is a bit thin on the productized AI and AI for the climate crisis sides, because I mostly focused on François Chollet’s new _The Measure of Intelligence_ paper.
It’s 64-pages long, which took a lot of time to summarize into a few paragraphs for the newsletter, so I pushed some other content to the next issue.
Anyway, let’s dive in.

## Productized Artificial Intelligence 🔌

![Improved natural language understanding in Google Search. (Google)](https://s3.amazonaws.com/revue/items/images/005/199/866/mail/d02534228644aa77f821dc01c5d769aa.jpeg?1573306786)

_Improved natural language understanding in Google Search. (Google)_

**Google Search now uses the BERT language model** to better understand natural language search queries:

> This breakthrough was the result of Google research on [transformers](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter): models that process words in relation to all the other words in a sentence, rather than one-by-one in order.
> BERT models can therefore consider the full context of a word by looking at the words that come before and after it—particularly useful for understanding the intent behind search queries.

The query in the screenshots above is a good example of what BERT brings to the table: its understanding of the word “to” between “brazil traveler” and “usa” means that it no longer confuses whether the person is from Brazil and going to the USA or the other way around.
Google is even using concepts that BERT learns from English-language web content for other languages, which led to “significant improvements in languages like Korean, Hindi and Portuguese.” Read more in Pandu Nayak’s post for Google’s The Keyword blog: [Understanding searches better than ever before](https://www.blog.google/products/search/search-language-understanding-bert?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

## Machine Learning Research 🎛

![From top to bottom: Chollet's hierarchy of intelligence, and two sample tasks from ARC. (François Chollet))](https://s3.amazonaws.com/revue/items/images/005/197/673/mail/c940ac191521a1ebf6ed783a42de131b.png?1573227558)

_From top to bottom: Chollet's hierarchy of intelligence, and two sample tasks from ARC. (François Chollet))_

**Keras creator François Chollet has published his 64-page manifesto on the path “toward more intelligent and human-like” AI** in a paper titled [The Measure of Intelligence](https://arxiv.org/abs/1911.01547?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that “formalizes things [he’s] been talking about for the past 10 years.” This is one of the most inspiring papers I’ve read in a long time, and it has many people around the office very excited too.
Broadly, Chollet covers three topics: (1) the context and history of evaluating the intelligence of humans and machines; (2) a new perspective of what a framework for evaluating intelligence should be; and (3) the Abstraction and Reasoning Corpus (ARC), his implementation of this framework.

**(1) Context and history.**
In cognitive science, there are are two opposing views of how the human mind works:

> One view in which the mind is a relatively static assembly of special-purpose mechanisms developed by evolution, only capable of learning what is it programmed to acquire, and another view in which the mind is a general-purpose “blank slate” capable of turning arbitrary experience into knowledge and skills, and that could be directed at any problem.

Chollet explains that early (symbolic) AI research focused on the former view, creating intricate symbolic representations of problems over which computers could search for solutions, while current (deep learning) AI research focuses on the latter, creating “randomly initialized neural networks that starts blank and that derives its skills from training data.” He argues that neither of these approaches is sufficient for creating human-like intelligence, which, as he introduces through the lense of [psychometrics](https://en.wikipedia.org/wiki/Psychometrics?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), is mostly characterized by the ability to _broadly generalize_ on top of some low-level [core knowledge](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-7687.2007.00569.x?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) that all humans are born with.

**(2) A new perspective.**
Chollet presents a new framework that is meant to be an “actionable perspective shift in how we understand and evaluate flexible or general artificial intelligence.” It evaluates these broad cognitive generalization abilities by modelling an intelligent system as something that can output static “skill programs” to achieve some task.
The system’s intelligence is then measured by how efficiently it can generate these skills.
Formally:

> The intelligence of a system is a measure of its skill-acquisition efficiency over a scope of tasks, with respect to priors, experience, and generalization difficulty.

**(3) Abstraction and Reasoning Corpus (ARC).**
Chollet finally proposes a practical implementation of the framework.
An ARC task, as pictured above, consists of several example _before_ and _after_ grids, and one final _before_ grid for which the intelligent system’s generated skill must figure out the correct _after_ grid.
Each task is designed so that the average human can solve it quite easily, and so that it depends only on core knowledge (and not learned things like the concept of arrows).
Tasks range from simple object counting to more complex things like continuing a line that bounces off edges.
There are 400 tasks to train on and 600 tasks to test on, of which 200 are secret and used to evaluate a competition.

**I’ve barely scratched the surface of the paper here,** and I highly recommend reading it in full and trying out ARC for yourself!

- The Measure of Intelligence on arXiv: [Chollet (2019)](https://arxiv.org/abs/1911.01547?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- The Abstraction and Reasoning Corpus on GitHub, including a version you can test yourself on: [fchollet/ARC](https://github.com/fchollet/ARC?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Chollet’s [twitter thread](https://twitter.com/fchollet/status/1192121587467784192?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) with some more background about how the paper came to be.

**Quick ML resource links ⚡️** ([see all 47](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4))

- arXiv Vanity renders papers from arXiv into HTML pages instead of PDFs, making them easier to read in your browser. Link: [arxiv-vanity.com](https://www.arxiv-vanity.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Gradient Community Notebooks lets you run PyTorch, TensorFlow and Keras models on cloud GPUs for free, similar to Colab. Link: [Gradient Community Notebooks](https://gradient.paperspace.com/free-gpu?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Hypothesis GU Funcs is Uber’s open-source Python package that “allows property-based testing of vectorized NumPy functions” for ML models. GitHub link: [uber/hypothesis-gufunc](https://github.com/uber/hypothesis-gufunc?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Artificial Intelligence for the Climate Crisis 🌍

**Climate Change AI launched its forum.**
CCAI is the organization that came out of the 97-page paper about AI approaches to solving the climate crisis (see [DT #16](https://dynamicallytyped.com/issues/16-finding-whales-with-ai-and-97-pages-of-ml-for-climate-change-183400?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
They’ve now launched a forum for “sharing resources and building teams at the intersection of climate change and machine learning.
See [David Rolnick’s tweet](https://twitter.com/david_rolnick/status/1189655261805305856?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for more information and check out the forum at [forum.climatechange.ai](https://forum.climatechange.ai/login?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
🚂