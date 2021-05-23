---
category: productized-ai
date: 2021-05-23
emoji: "\U0001FA7A"
issue_number: 66
title: 'Google''s dermatology app: high potential, with a catch'
---

[Google previewed its AI-powered dermatology assist tool](https://blog.google/technology/health/ai-dermatology-preview-io-2021/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) at I/O, its yearly developer conference.
Integrated with Search, the app guides you through taking photos of your skin at different angles, and then uses [a deep learning model published in _Nature Medicine_](https://www.nature.com/nm/volumes/26/issues/6?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to potentially detect one of 288 skin conditions.
(See how it works [in this GIF](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/derm-web-cropped-white-bg.gif?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).) The tool is explicitly not intended to provide a diagnosis or as a substitute to medical advice.
Although this theoretically sounds incredible — internet-scale access to early-stage detection of e.g.
skin cancer could be an amazing global [DALY](https://en.wikipedia.org/wiki/Disability-adjusted_life_year?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) booster — experts have raised some serious concerns.
Google Ethical AI researcher [Dr.
Alex Hanna](https://twitter.com/alexhanna/status/1395423337036193795?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Stanford Medicine dermatologist [Roxanna Daneshjou MD/PhD](https://twitter.com/RoxanaDaneshjou/status/1394745183015641091?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and Vice journalist [Todd Feathers](https://www.vice.com/en/article/m7evmy/googles-new-dermatology-app-wasnt-designed-for-people-with-darker-skin?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) have pointed out that, although Google claims to have tested the app across all _demographics,_ it has not sufficiently tested it across all ([Fitzpatrick](https://dermnetnz.org/topics/skin-phototype/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)) _skin types:_ the darkest V and VI types — [where skin conditions are already misdiagnosed relatively often](https://twitter.com/RoxanaDaneshjou/status/1395768505010589705?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) — were severely underrepresented in the dataset.
The app isn’t live yet, and Google Health spokesperson Johnny Luu told Vice that the dataset has been expanded since the _Nature_ paper was published, but this issue must be properly addressed before the app can responsibly be launched.
I’d be disappointed to see it go live without at the very least [a Datasheet and a Model Card](https://dynamicallytyped.com/stories/2020/datasheets-for-datasets-and-model-cards-for-model-reporting/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) explaining its limitations.