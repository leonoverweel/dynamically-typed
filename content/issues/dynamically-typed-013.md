# #13: Caption this: new AI-powered features at Google I/O, and OpenAI's staged GPT-2 release 

This week, Google had their yearly I/O developer conference.
They announced a slew of new AI-powered features for their services, from automatic subtitles for any video on an Android device to an menu-reading AR app that shows you photos of popular dishes at a restaurant.

OpenAI also responded to community concerns by open-sourcing a larger version of their GPT-2 language model, and Dropbox published a deep dive on the process of building a machine learning document recommendation feature into their app.

_(Small note: today’s issue is a bit shorter than usual because I’m in full-on exam crunch mode—I had one last Wednesday, and two more coming up tomorrow and Tuesday.
Final pre-thesis stretch!)_

## Productized Artificial Intelligence 🔌

![Live Caption will add subtitles to any video playing on an Android device. (Vjeran Pavic, The Verge)](https://s3.amazonaws.com/revue/items/images/004/575/072/mail/7b19818d41d642dfe1dcaf71a681b7da.jpeg?1557569545)

_Live Caption will add subtitles to any video playing on an Android device. (Vjeran Pavic, The Verge)_

**Google announced a slew of new features across their products at I/O, their yearly developer conference.**
Here are the ones that jumped out as productized AI to me:

* Google’s augmented reality (AR) camera app, Lens, will be able to understand a restaurant menu you point it at. It’ll highlight popular dishes and show you photos of the dish that were taken at the restaurant. After the meal, it’ll be able to split the bill for you as well.
* Duplex, the “call this restaurant and make a reservation for me” feature that Google demonstrated at I/O last year, will now also work on websites, automatically going through reservation flows to book things like rental cars and hotels.
* Google Search will use AR to place shopping search results into the real world. For example, it’ll show you what a pair of shoes will look like on your feet.
* Android will get a new feature called Live Caption, which uses on-device speech recognition to add subtitles to any video. The feature will also come to phone calls.

All these announcements underline just how much Google is investing in machine learning, both on the research and product sides, and that AI is now a big part of pretty much every part of the company.
More about I/O here:

* CEO Sundar Pichai on Google’s The Keyword blog: [At I/O ‘19: Building a more helpful Google for everyone](https://www.blog.google/technology/developers/io19-helpful-google-everyone/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Natt Guran for The Verge: [The 8 biggest announcements from the Google I/O 2019 keynote](https://www.theverge.com/2019/5/7/18531198/google-io-summary-keynote-news-highlights-recap-2019?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* [Demo video of Live Caption](https://twitter.com/Google/status/1125823197323059200?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Twitter)

**Dropbox is using machine learning to predict what file you need next,** and software engineer [Neeraj Kumar](https://neerajkumar.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) wrote a great post about their journey building this feature for the Dropbox tech blog.
The team started with an initial heuristics-based baseline, which allowed them to design the surrounding infrastructure and front-end code, and to monitor users’ response to the feature: does it actually help them get to the file they’re looking for faster?

With that baseline in place, they figured out what types of file-use patterns the heuristics-based method wasn’t picking up, and used that to design several iterations of a machine learning model.
Kumar’s post dives more into this, as well as some other interesting production issues they ran into, from figuring out what metrics to use to working out how to perform statistically significant experiments while the app’s UI changed.
Read it here: [Using machine learning to predict what file you need next](https://blogs.dropbox.com/tech/2019/05/content-suggestions-machine-learning/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Microsoft is adding an AI-powered upgrade of its spell checker.**
The new feature is called Ideas and it’s available in the online version of Word.
It also does much more than tell you when you’ve misspelled a word; it will:

* Help you rewrite complex sentences into more concise ones
* Point out non-inclusive language and suggest appropriate replacements
* Pick out key points of a text to generate a summary

Read more about it here:

* Frederic Lardinois for TechCrunch: [Word’s new AI editor will improve your writing](https://techcrunch.com/2019/05/06/words-new-ai-features-will-help-you-write-better/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Jon Fingas for Engadget: [Microsoft Word uses AI to improve your writing](https://www.engadget.com/2019/05/06/microsoft-word-online-ideas/?guccounter=2&guce_referrer=aHR0cHM6Ly90LmNvL0d0Zm1xdTk3MFM&guce_referrer_sig=AQAAALDbwBnwOyRTgfhb6spNNhP1y21bHkGPKmuc-r2L6bz_yy5c0sNXVy7fexFAIRk-qb5pmYwfMbl3cBqOHxTnhCyb52k-6cSQq_4i77LBDEhNzXWn9oo9djpaa6U4z1wPUW1LvW2vxGbPeiVISVH8cqpvz6Gzr4jhZB86xpildIdL&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Miltos Allemanis, Marc Brockschmidt and Alex Gaunt for the Microsoft Research Blog (technical): [Beyond spell checkers: Enhancing the editing process with deep learning](https://www.microsoft.com/en-us/research/blog/beyond-spell-checkers-enhancing-the-editing-process-with-deep-learning/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Machine Learning Technology 🎛

**OpenAI has open-sourced a larger version of their GPT-2 language model.**
They previously only released a 117 million parameter version, citing their concerns for abuse of the full-size model by malicious actors, a decision that much of the community disagreed with.
(See [DT #8](https://dynamicallytyped.com/issues/8-should-openai-open-source-their-impressive-new-language-model-161119?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for my take on that debate).
OpenAI has now changed course and released a larger version, GPT-2-345M, which is nearly three times larger than the original release.
Additionally, they’re giving select partners, like established university research labs, access to the even larger 762M and 1.5B parameter versions.
It’s good to see OpenAI responding to the community’s criticism like this, and I’m excited for the art projects and demo sites (such as the one I featured below) that this medium-sized model will spawn.
More here:

* OpenAI’s updated blog post, with a new discussion on their staged release of GPT-2: [Better Language Models and Their Implications](https://openai.com/blog/better-language-models/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#update)
* [OpenAI’s announcement](https://twitter.com/OpenAI/status/1124440412679233536?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Twitter)

**Google announced the winners of the Google AI Impact Challenge.**
The challenge is part of Google’s [AI for Social Good program](https://ai.google/social-good/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and this year it gave out $25 million in grants consisting of cash from Google.org and Google Cloud credits + consulting.
I especially love these three projects:

> [Gringgo Indonesia Foundation](https://gringgo.co/about?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Indonesia): Building an image recognition tool to improve plastic recycling rates, reduce ocean plastic pollution and strengthen waste management in under-resourced communities.

> [Skilllab BV](https://skilllab.io/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Netherlands): Helping refugees translate their skills to the European labor market and recommend relevant career pathways to explore.

> [Rainforest Connection ](https://rfcx.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)(USA): Using deep learning for bioacoustic monitoring and commonplace mobile technology to track rainforest health and detect threats.

Read about all the 20 grantees in this blog post by Google.org President Jacqueline Fuller and Google AI SVP Jeff Dean: [Here are the grantees of the Google AI Impact Challenge](https://www.blog.google/outreach-initiatives/google-org/ai-impact-challenge-grantees/amp/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Quick ML resource links ⚡️**

* BoTorch is a Bayesian Optimization library for the PyTorch ecosystem, which can help with hyperparameter optimization (just like Dragonfly from [DT #11](https://dynamicallytyped.com/issues/11-adobe-and-google-s-new-video-ai-tools-stanford-s-hype-for-gans-and-a-conversation-with-books-170283?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)). Links: [BoTorch website](https://botorch.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); [code](https://github.com/pytorch/botorch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (GitHub)
* DVC is an open-source version control system for machine learning projects. Links: [DVC website](https://dvc.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); [community discussion](https://www.reddit.com//r/MachineLearning/comments/bjszua/r_why_git_and_gitlfs_is_not_enough_to_solve_the/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Reddit)
* Rachel Thomas (cofounder of [fast.ai](https://fast.ai?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) published the final instalment of her AI ethics tips: [16 Things You Can Do to Make Tech More Ethical, part 3](https://www.fast.ai/2019/05/03/ethics-action-3/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Cool Things ✨

![What OpenAI's medium-size GPT-2 model thinks I'm up to this year. (Adam King)](https://s3.amazonaws.com/revue/items/images/004/573/933/mail/391c400aa69ea519e2928d5e49765a13.png?1557528515)

_What OpenAI's medium-size GPT-2 model thinks I'm up to this year. (Adam King)_

**Adam King launched Talk to Transformer, an interactive website for OpenAI’s medium-sized language model.**
Thanks to OpenAI’s open-source release of a larger version of GPT-2 and King’s engineering work building a site around it, anyone can now generate completions of short text prompts.
I tried it out above with a prompt of what I’m currently up to (bold text), and it generated a fairly realistic-sounding biography (regular text).
I don’t think I’ll be writing a PhD thesis during my MSc, though…

I encourage you to play around with Talk to Transformer and share your generated completions with friends: it’s a lot of fun and, more importantly, it spreads awareness of the capabilities of these AI models to a broader audience (see [DT #8](https://dynamicallytyped.com/issues/8-should-openai-open-source-their-impressive-new-language-model-161119?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).

* Try Talk to Transformer here: [talktotransformer.com](https://talktotransformer.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* Follow its creator, Adam King: [blog](https://adamdking.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Twitter](https://twitter.com/adamdanielking?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
* [Some startup ideas I generated with the tool](https://twitter.com/layon_overwhale/status/1126990247622074374?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (Twitter)

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
😇