---
category: ml-research
date: 2021-02-14
emoji: "\u2699\uFE0F"
issue_number: 59
title: OpenAI on Kubernetes
---

_AI lab tooling long read #2:_ OpenAI added a blog post about [scaling Kubernetes to 7,500 nodes](https://openai.com/blog/scaling-kubernetes-to-7500-nodes/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Kubernetes is a system for orchestrating Docker containers across a datacenter, and I think most compute-heavy companies use it by now.
Both startups I’ve worked at also use it for their machine learning workloads — but at a scale on the order of tens or hundreds of nodes, not many thousands.
At that scale, a whole load of problems and potential optimizations suddenly become worth their engineer-time to look at, and that’s exactly what OpenAI does in this detailed post.
_(A fun fact I quite enjoy and will probably never have a better excuse to share in DT than now:_ Kubernetes is abbreviated as K8s — “K-then-eight-letters-then-s,” like how internationalization is i18n — and there’s a management tool for Kubernetes called [K9s](https://github.com/derailed/k9s?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
At first sight, the name just looks like a typical programmer move, “K8+1s = K9s,” but it has another level to it: if you pronounce K9s as a word, it sounds like “canines” — dogs!
So the logo for K9s is a dog.
🐩)