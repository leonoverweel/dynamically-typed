---
category: ml-research
date: 2020-06-07
issue_number: 41
title: Datasheets for datasets and Model Cards for model reporting
---

![Google's model card for their face detection model. (Google)](https://s3.amazonaws.com/revue/items/images/006/082/344/mail/10fd363eed5e0ff5a46c9dc1af36a194.png?1591519380)

_Google's model card for their face detection model. (Google)_

[**Datasheets for Datasets**](https://arxiv.org/abs/1803.09010?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **and**[ **Model Cards for Model Reporting**](https://dl.acm.org/doi/abs/10.1145/3287560.3287596?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) **.**
These two papers aim to improve transparency and accountability in machine learning models and the datasets that were used to create them.

From the abstract of the first paper by [Gebru et al.
(2018)](https://arxiv.org/abs/1803.09010?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

> The machine learning community currently has no standardized process for documenting datasets, which can lead to severe consequences in high-stakes domains.
> To address this gap, we propose datasheets for datasets.
> In the electronics industry, every component, no matter how simple or complex, is accompanied with a datasheet that describes its operating characteristics, test results, recommended uses, and other information.
> By analogy, we propose that every dataset be accompanied with a datasheet that documents its motivation, composition, collection process, recommended uses, and so on.

The paper goes on to provide a set of questions and a workflow to properly think through and document each of these aspects of a dataset in a dataseheet.
It also has example datasheets for two standard datasets: [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and the [Movie Review Data](http://www.cs.cornell.edu/people/pabo/movie-review-data/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

From the abstract of the second paper by [Mitchell et al.
(2019)](https://dl.acm.org/doi/abs/10.1145/3287560.3287596?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

> Model cards are short documents accompanying trained machine learning models that provide benchmarked evaluation in a variety of conditions, such as across different cultural, demographic, or phenotypic groups (e.g., race, geographic location, sex, Fitzpatrick skin type) and intersectional groups (e.g., age and race, or sex and Fitzpatrick skin type) that are relevant to the intended application domains.
> Model cards also disclose the context in which models are intended to be used, details of the performance evaluation procedures, and other relevant information.

This is essentially the same principle, but now applied to a trained model instead of a dataset.
The paper also includes details on how to fill in each part of a model card, as well as two examples: a smile detection model and a text toxicity classifier.
I’ve also seen some model cards in the wild recently: Google has them for their [face detection](https://modelcards.withgoogle.com/face-detection?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [object detection](https://modelcards.withgoogle.com/object-detection?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) APIs and OpenAI has one for their [GPT-2 language model](https://github.com/openai/gpt-2/blob/master/model_card.md?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (but not yet for GPT-3, as far as I can tell).

I’m excited to try creating a dataset datasheet and a model card at work—which also makes me think: practicing making these should really have been part of my AI degree.
I’ve also added both papers to [my machine learning resources list](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4).