---
category: ml-research
date: 2020-04-26
issue_number: 38
title: 'Report: Toward Trustworthy AI Development'
---

![That's a lot of authors and institutions.](https://s3.amazonaws.com/revue/items/images/005/879/701/mail/7f61f26e1ce8ae8bd86ac42f593f001b.png?1587894977)

_That's a lot of authors and institutions._

A large coalition of big-name ML researchers and institutions published [**Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims**](https://arxiv.org/abs/2004.07213?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
The 80-page report recognizes “that existing regulations and norms in industry and academia are insufficient to ensure responsible AI development” and presents a set of recommendations for providing evidence of the “safety, security, fairness, and privacy protection of AI systems.” Specifically, they outline two types of mechanisms:

1. Mechanisms for AI developers to substantiate claims about their AI systems—going beyond just saying a system is “privacy-preserving” in the abstract, for example.
2. Mechanisms that users, policy makers, and regulators can use to increase the specificity and diversity of demands they make to AI developers—again, going beyond abstract, unenforceable requirements.

The two-page executive summary and single-page list of recommendations (categorized across institutions, software, and hardware) are certainly worth a read for anyone who is to some extent involved in AI development, from researchers to regulators:

![Recommendations from the report by Brundage et al. (2020).](https://s3.amazonaws.com/revue/items/images/005/879/720/mail/85a6a88b914de55b62c42765449774dc.png?1587896163)

_Recommendations from the report by Brundage et al. (2020)._

On the software side, I found the audit trail recommendation especially interesting.
The authors state the problem as such:

> AI systems lack traceable logs of steps taken in problem-definition, design, development, and operation, leading to a lack of accountability for subsequent claims about those systems’ properties and impacts.

Solving this will have go far beyond just saving a git commit history that traces the development of a model.
For the data collection, testing, deployment, and operational aspects, there are no reporting or verification standards in widespread use yet.

I don’t think these standards can be sensibly defined for “AI” at large, so they’ll have to be implemented on an industry-by-industry basis.
There are a whole different set of things to think about for self-driving cars than for social media auto-moderation, for example.

(Also see OpenAI’s [short write-up of the report](https://openai.com/blog/improving-verifiability/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).)