---
category: productized-ai
date: 2020-05-10
issue_number: 39
title: Cloudflare's ML-powered bot blocking
---

![Cloudflare's overview of good and bad bots.](https://s3.amazonaws.com/revue/items/images/005/946/458/mail/c90c3afcf896580ebd3a4efe81ee4540.png?1589095680)

_Cloudflare's overview of good and bad bots._

Web infrastructure company **Cloudflare is using machine learning to block “bad bots” from visiting their customers’ websites.**
Across the internet, malicious bots are used for content scraping, spam posting, credit card surfing, inventory hoarding, and much more.
Bad bots account for an astounding 37% of internet traffic visible to Cloudflare (humans are responsible for 60%).

To block these bots, Cloudflare built a scoring system based on five detection mechanisms: machine learning, a heuristics engine, behavior analysis, verified bots lists, and JavaScript fingerprinting.
Based on these mechanisms, the system assigns a score of 0 (probably a bot) to 100 (probably a human) to each request passing through Cloudflare—about 11 million requests per second, that is.
These scores are exposed as fields for [Firewall Rules](https://blog.cloudflare.com/announcing-firewall-rules/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), where site admins can use them in conjunction with other properties to decide whether the request should pass through to their web servers or be blocked.

Machine learning is responsible for 83% of detection mechanisms.
Because support for categorical features and inference speed were key requirements, Cloudflare went with gradient-boosted decision trees as their model of choice (implemented using [CatBoost](https://github.com/catboost/catboost?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
They run at about 50 microseconds per inference, which is fast enough to enable some cool extras.
For example, multiple models can run in shadow mode (logging their results but not influencing blocking decisions), so that Cloudflare engineers can evaluate their performance on real-world data before deploying them into the Bot Management System.

Alex Bocharov [wrote about the development of this system](https://blog.cloudflare.com/cloudflare-bot-management-machine-learning-and-more/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) for the Cloudflare blog.
It’s a great read on adding an AI-powered feature to a larger product offering, with good coverage of all the tradeoffs involved in that process.