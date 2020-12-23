---
category: ml-research
date: 2020-12-20
issue_number: 55
title: 'AlphaFold 2: DeepMind''s structural biology breakthrough'
---

![AlphaFold's predictions vs. the experimentally-determined shapes of two CASP14 proteins.](https://s3.amazonaws.com/revue/items/images/006/966/376/mail/Screen_Shot_2020-12-19_at_17.17.34.png?1608396735)

_AlphaFold's predictions vs. the experimentally-determined shapes of two CASP14 proteins._

**﻿DeepMind’s AlphaFold 2 is a major protein folding breakthrough.**
Protein folding is a problem in structural biology where, given the one-dimensional RNA sequence of a protein, a computational model has to predict what three-dimensional structure the protein “folds” itself into.
This structure is much more difficult to determine experimentally than the RNA sequence, but it’s essential for understanding how the protein interacts with other machinery inside cells.
In turn, this can give insights into the inner workings of diseases — “including cancer, dementia and even infectious diseases such as COVID-19” — and how to fight them.

Biennially since 1994, the Critical Assessment of Techniques for Protein Structure Prediction (CASP) has determined the state of the art in computational models for protein folding using a blind test.
Research groups are presented (only) with the RNA sequences of about 100 proteins whose shapes have recently been experimentally determined.
They blindly predict these shapes using their computational models and submit them to CASP to be evaluated with a Global Distance Test (GDT) score, which roughly corresponds to how far each bit of the protein is from where it’s supposed to be.
GDT scores range from 0 to 100, and a model that scores at least 90 across different proteins would be considered good enough to be useful to science (“competitive with results obtained from experimental methods”).

Before CASP13 in 2018, no model had ever scored significantly above 40 GDT.
That year, the first version of AlphaFold came in at nearly 60 GDT — already “stunning” at the time (see [DT #21](https://dynamicallytyped.com/issues/21-deepmind-s-ml-for-drug-discovery-security-leaks-in-neural-networks-and-green-ai-194986?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
At CASP14 this year, AlphaFold 2 blew its previous results out of the water and achieved a median score of _92.4 GDT across all targets._ This was high enough for CASP to [declare the problem as “solved” in their press release](https://predictioncenter.org/casp14/doc/CASP14_press_release.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and to start talking about new challenges for determining the shape of multi-protein complexes.

I’ve waited a bit to write about AlphaFold 2 until the hype died down because, oh boy, was there a lot of hype.
DeepMind released [a slick video about the team’s process](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=gg7WjuFs8F4), their results were covered with glowing features in [Nature](https://www.nature.com/articles/d41586-020-03348-4?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [The New York Times](https://www.nytimes.com/2020/11/30/technology/deepmind-ai-protein-folding.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and high praise came even from the leaders of DeepMind’s biggest competitors, including OpenAI’s [Ilya Sutskever](https://twitter.com/ilyasut/status/1333445199603744768?s=12&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and Stanford HAI’s [Fei-Fei Li](https://twitter.com/drfeifei/status/1333587506055372800?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
It was a pretty exciting few days on ML twitter.

Columbia University’s Mohammed AlQuraishi, who has been [working on protein folding](https://www.aqlab.io/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for over a decade, was one of the first people to [break the CASP14 news](https://twitter.com/MoAlQuraishi/status/1333383634649313280?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
His [blog post about CASP13 and AlphaFold 1](https://moalquraishi.wordpress.com/2018/12/09/alphafold-casp13-what-just-happened/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) was also widely circulated back in 2018, so a lot of people in the field were interested in what he’d have to say this year.
Last week, after the hype died down a bit, AlQuraishi published [his perspective on AlphaFold 2](https://moalquraishi.wordpress.com/2020/12/08/alphafold2-casp14-it-feels-like-ones-child-has-left-home/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
He summarized it by saying “it feels like one’s child has left home:” AF2 got results he did not expect to see until the end of this decade, even when takin into account AF1 — bittersweet for someone whose lab has also been working on this same problem for a long time.

AlQuraishi is overall extremely positive about DeepMind’s results here, but he does express disappointment at their “falling short of the standards of academic communication” — the lab has so far been much more secretive about AF2 than it was about AF1 (which is [open-source](https://github.com/deepmind/deepmind-research/tree/master/alphafold_casp13?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
AlQuraishi’s post is very long and technical, but if you want to know exactly how impressive AlphaFold 2 is, learn the basics of how it works, read about its potential applications in broader biology, or see some of the hot takes against it debunked, the post is definitely worth the ~75 minutes of your time.
(I always find it energizing to see someone excitedly explain a big advancement in their field that they did not directly work on; [here’s the link again](https://moalquraishi.wordpress.com/2020/12/08/alphafold2-casp14-it-feels-like-ones-child-has-left-home/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).)

I personally also can’t wait to see the first practical applications of AlphaFold, which I expect we’ll start to see DeepMind talk about in the coming years.
(Hopefully!) For one, they’ve already released [AlphaFold’s predictions for some proteins associated with COVID-19](https://deepmind.com/research/open-source/computational-predictions-of-protein-structures-associated-with-COVID-19?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).