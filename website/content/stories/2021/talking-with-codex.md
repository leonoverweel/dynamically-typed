---
category: productized-ai
date: 2021-08-15
issue_number: 72
title: Towards talking to computers with Codex
---

**Towards talking to computers with Codex**

About seven years ago, when I was a junior in high school, I built a “self-learning natural language search engine” called [Wykki](https://leonoverweel.com/projects/2014/wykki/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
It used “natural language” in that it was able to separate a user’s prompt like “How old is Barack Obama” into a question stub (“How old is _blank_ ”) and a subject (“Barack Obama”) using some hard-coded tricks and simple heuristics.
It then had a backend that connected those question stubs to properties in Freebase — think Wikipedia-as-a-database — so it could answer that question about Obama with his _person.age_ property.
Wykki was also “self-learning” in that, if it came across a question stub it hadn’t seen before, it had a UI that let users “teach” it which Freebase property that question referred to.

Once you knew about those tricks it wasn’t all that impressive — I wouldn’t use “natural language” or “self-learning” to describe Wykki today — but seeing it work for the first time was a pretty cool experience.
Wykki was never more than a short-lived side project, but it got me really excited about the idea of accessing APIs (Freebase in this case) using natural language — and made me realize how difficult of a problem it is.
Over the past few years I’ve had a lot of shower thoughts about how I’d approach it with the background knowledge I have now — like maybe learning APIs from their docs pages or auto-generated OpenAPI specs — but those never materialized into anything.

**The Codex live demo**

This week, a [thirty-minute Codex demo](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=SGUCcjHTmGY) by OpenAI’s Greg Brockman, Ilya Sutskever and Wojciech Zaremba, showed me we’re now much closer to solving this problem than I could’ve imagined even a year ago.
[As I wrote about last month](https://dynamicallytyped.com/stories/2021/copilot/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Codex is OpenAI’s latest giant language model that can write code, which also powers GitHub’s autocomplete-on-steroids Copilot tool.

Tuesday’s Codex demo started off with a bit of history, mostly about how the [code generation demos that people were doing with GPT-3 last summer](https://dynamicallytyped.com/stories/2020/gpt-3-demos-one-month-in/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) inspired the researchers to build a benchmark capturing those types of tasks, and to then start optimizing a GPT-type model to solve it (mostly by training it on a lot of open-source code).
Thus the initial version of Codex powering Copilot was born, followed quickly by the improved version that was behind the [private beta](https://share.hsforms.com/1Lfc7WtPLRk2ppXhPjcYY-A4sk30?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), a [coding challenge](https://challenge.openai.com?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and the four demonstrations during the presentation.
_(Demo links go to timestamps in the YouTube recording.)_

The [first demo](https://youtu.be/SGUCcjHTmGY?t=219&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) was fairly simple: telling Codex to “say Hello World” produced a Python program that prints “Hello, World!” to the console.
In the next commands, they asked it to “say that with empathy,” “say that five times,” and “wrap it in a web server,” showing that Codex can write some more complex code, but more importantly that it can keep track of the commands and code it received and wrote so far, and use them as context for the next code it wrote.

[Another demo](https://youtu.be/SGUCcjHTmGY?t=820&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) was quite similar, but a lot more complex: writing a simple game in Javascript: “add a person,” “make it 100 pixels tall,” “make it move left and right with the arrow keys,” “stop it from going off-screen,” and “make the person lose when it collides with a boulder.” The key thing here was that Codex works best when you keep asking it to take small steps, and that it’s always easy to go back and try slightly different phrasing to improve your results.
“We think these text instructions will become a type of source code that people can pass around [instead of the actual code].”

The [next demo](https://youtu.be/SGUCcjHTmGY?t=564&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (which actually happend second) is where it gets really interesting.
Viewers were asked to leave their email addresses in a web form.
We then watched as the demonstrators used Codex to create a small python script that looked up the current Bitcoin price and email it to us.
Crucially, they did not explicitly tell Codex how to find out the current Bitcoin price — from training millions of lines of open-source code, it apparently already knew that Coinbase has a world-readable API for querying this.
You could ask Codex to write a program that uses the current Bitcoin price without knowing what Coinbase is, or without even knowing what a REST API is!

They took this idea to the next level in the [fourth and final demo](https://youtu.be/SGUCcjHTmGY?t=1498&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), for which they switched to an iPad running Microsoft Word with a custom Codex plugin.
The plugin mostly consisted of a big button to trigger speech recognition, the output of which got fed into Codex, which then translated it to code and ran it (with a bit of glue to give it access to Word’s APIs).
This enabled some really cool interactions.
After pasting some badly-formatted text, they could for example say “remove initial spaces,” and a few seconds later Codex had written and run code that used the Word API to iterate through each line of text and delete any leading spaces.
Next, they said “make every fifth line bold,” and a few seconds later… every fifth line was bold!

That’s where the demo ended, but this got me really excited.
There is so much functionality in modern software and services that’s hidden three layers deep in some convoluted UI or API, that most people today don’t know how to use.
Codex plugins like this can enable those people to use that functionality — and they won’t even have to know that under the hood it’s doing this by generating code on the fly.
[Brockman on Twitter](https://twitter.com/gdb/status/1425159432648855552?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), a few hours after the demo:

> The history of computing has been moving the computer closer to the human — moving from punch cards to assembly to higher level languages.

> Codex represents a step towards a new interface to computers — being able to talk to your computer and having it do what you intend.

There are a lot of unanswered questions about how well this works with arbitrary APIs and outside of a controlled demo environment, but given OpenAI’s track record with GPT-x I’m not too worried about those.
I really think that during that half hour last Tuesday evening, I witnessed the next big thing in how we’ll interact with our computing devices a few years from now.
Exciting!!