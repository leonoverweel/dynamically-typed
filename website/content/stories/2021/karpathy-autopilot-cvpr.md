---
category: productized-ai
date: 2021-07-18
issue_number: 70
title: Karpathy on Tesla Autopilot at CVPR'21
---

**Karpathy on Tesla Autopilot at CVPR ‘21**

Tesla’s head of AI Andrej Karpathy did [a keynote at the CVPR 2021 Workshop on Autonomous Driving](https://www.youtube.com/watch?index=11&list=PLvXze1V52Yy2OY67mz2Jy-JcnEw8GUZEl&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=g6bOwQdCJrc) with updates on the company’s Autopilot self-driving system.
Just like [his talk last year at Scaled ML 2020](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=hx7BXih7zx8), this was a great watch if you’re interested in productized AI.
The talk kicks off with the value that “incremental autonomy” is already providing today, in the form of automatic emergency braking, traffic control warnings (“there’s a red light ahead!”), and pedal misapplication mitigation (PMM) — stopping the driver from flooring it when they meant to hit the brakes.

![Examples of "incremental autonomy"](https://s3.amazonaws.com/revue/items/images/010/145/781/mail/E4bgtv6WQAY_PWB.jpeg?1626531015)

_Examples of "incremental autonomy"_

Karpathy then goes into details of the next generation of Autopilot: Tesla has “deleted” the radar sensor from recent new cars and is now relying on vision alone.
“If our [human] neural network can determine depth and velocity, can synthetic neural nets do it too?
Internally [at Tesla], our answer is an unequivocal yes.” This is backed by the fact that the new vision-only approach for Autopilot has a higher precision _and_ recall than the previous sensor fusion approach.

Where does the Autopilot team get a large and diverse enough dataset to train a vision model like this?
From the million-car fleet of course!
There are now 221 manually-implemented triggers running on the Tesla fleet to detect scenarios that they may want to look at for training data.
(Could “inactive traffic lights on the back of a moving truck” [be the 222nd](https://twitter.com/layon_overwhale/status/1400522140240252932?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)?) Once collected, these images are labeled offline with a combination of human annotators, the old radar sensors, and very large neural nets — which would be too slow to deploy in the cars, but are very useful in this offline setting.

![](https://s3.amazonaws.com/revue/items/images/010/145/787/mail/E4bjxLUX0As78mS.jpeg?1626531089)

The loop of the Tesla Data Engine is then: (1) deploy models in ghost mode; (2) observe their predictions; (3) fine-tune triggers for collecting new training data; (4) create new unit tests out of wrong predictions; (5) add similar examples to the dataset; (6) retrain; and repeat.
At 1.5 petabytes, the final dataset for this first release of the new Autopilot system went through this shadow mode loop seven times.
It contains six billion labeled objects across one million 10-second videos.

![](https://s3.amazonaws.com/revue/items/images/010/145/846/mail/E4bmg_ZXwAEtWmr.jpeg?1626531654)

The neural network trained on this data has a ResNet-ish backbone for basic image processing, which branches into “heads,” then “trunks,” and then “terminal” detectors.
This amortizes learning into different levels, and allows multiple engineers to first work on different heads in parallel and then sync up to retrain the backbone.
I hadn’t heard of this structure for letting a large (50-ish person) team collaborate on one big neural network before — very cool.

![](https://s3.amazonaws.com/revue/items/images/010/145/851/mail/E4bnYSzWQAwU3_H.jpeg?1626531790)

And finally, on the deployment side, Tesla is now also vertically-integrated: they built their own FSD (“Full Self Driving”) Computer, with their own neural engine.

Karpathy wrapped by re-emphasizing auto-labeling: using a much heavier model than you could ever use in production to do (a first stab at) data labeling offline, to then be cleaned up a bit by a human, is very powerful.
And his overall conclusion remained in line with Tesla’s overall stance on self-driving: no fleet, no go.