---
category: productized-ai
date: 2020-05-24
issue_number: 40
title: Pinterest's AI-powered automatic board groups
---

![Pinterest's UX flow for ML-based grouping within boards. (Pinterest Engineering Blog.)](https://s3.amazonaws.com/revue/items/images/006/010/868/mail/41cba04a0d8e80572670ebc7f93785aa.png?1590240695)

_Pinterest's UX flow for ML-based grouping within boards. (Pinterest Engineering Blog.)_

**Pinterest has added new AI-powered functionality for grouping images and other pins on a board.**
The social media platform is mostly centered around finding images and collecting (pinning) them on boards.
After working on a board for a while, though, some users may pin so much that they no longer see the forest for the trees.
That’s where this new feature comes in:

> For example, maybe a Pinner is new to cooking but has been saving hundreds of recipe Pins.
> With this new tool, Pinterest may suggest board sections like “veggie meals” and “appetizers” to help the Pinner organize their board into a more actionable meal plan.

Here’s how it works:

1. When a user views a board that has a potential grouping, a suggestion pops up showing the suggested group and a few sample pins.
2. If the user taps it, the suggestion expands into a view with all the suggested pins, where she can deselect any pins she does not want to add to the group. (Which I’m sure is very valuable training data!)
3. The user can edit the name for the section, and then it gets added to her board.

Coming up with potential groupings is a three-step process.
First, [a graph convolutional network called PinSage](https://medium.com/pinterest-engineering/pinsage-a-new-graph-convolutional-neural-network-for-web-scale-recommender-systems-88795a107f48?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) computes an embedding based on text associated with the pin, visual features extracted from the image, and the graph structure.
Then the Ward clustering algorithm (chosen because it does not require a predefined number of clusters) generates potential groups.
Finally, a filtered count of common annotations for pins in the group decides the proposed group name.

Pinterest has really been on a roll lately with adding AI-powered features to its apps, including visual search ([DT #23](https://dynamicallytyped.com/issues/23-robotic-raspberry-and-lettuce-pickers-2-5-billion-objects-in-pinterest-lens-and-an-analysis-of-the-ai-reproducibility-crisis-199555?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) and AR try-on for shopping ([DT #33](https://dynamicallytyped.com/issues/33-billie-eilish-answers-ai-generated-interview-questions-visual-search-for-aerial-imagery-and-the-tech-won-t-drill-it-pledge-224742?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
[This post by Dana Yakoobinsky and Dafang He](https://medium.com/pinterest-engineering/using-machine-learning-to-auto-organize-boards-13a12b22bf5?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) on the company’s engineering blog has the full details on their implementation of this latest feature, as well as some future plans to expand it.