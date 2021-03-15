---
category: climate-ai
date: 2021-03-14
issue_number: 61
title: The climate opportunity of gargantuan AI models
---

**Climate change and the energy transition**

Climate change is our generation’s biggest challenge, and the transitions needed to reduce emissions and prevent it from becoming catastrophic will affect almost every part of society in the coming decades.
On their excellent _Our World in Data_ page on [CO2 and Greenhouse Gas Emissions](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#how-do-we-make-progress-in-reducing-emissions), Hannah Ritchie and Max Roser write:

> To make progress in reducing greenhouse gas emissions, there are two fundamental areas we need to focus on: energy (this encapsulates electricity, heat, transport, and industrial activities) and food and agriculture (which includes agriculture and land use change, since agriculture dominates global land use).

The biggest of these is energy: it’s responsible for [almost three quarters of global greenhouse gas emissions](https://ourworldindata.org/emissions-by-sector?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Decarbonizing energy involves two parallel transitions: (1) electrifying sectors powered by fossil fuels, and (2) shifting our electricity generation to low-emissions sources like solar, wind, hydro and nuclear.

Take road transport for example: cars need to be powered by electricity, and that electricity needs to be green.
Replacing all internal combustion engine cars with electric ones will take at least two decades, as will replacing all gas- and coal-fired electricity plants with low-carbon power generation — so if we want to be climate-neutral by 2050, neither transition can wait for the other.
Road transport is responsible for [about 12% of overall emissions](https://ourworldindata.org/emissions-by-sector?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#transport-16-2), but the same dual transition applies for other energy-intensive sectors like iron and steel production ([7%](https://ourworldindata.org/emissions-by-sector?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#energy-use-in-industry-24-2)) or lighting and heating in buildings ([17.5%](https://ourworldindata.org/emissions-by-sector?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#energy-use-in-buildings-17-5)).

That’s the energy transition in a nutshell: we need to move energy demand towards electricity, and the electricity supply toward low-carbon sources.

But there’s one less-discussed thing linking these two: how do we move this low-carbon electricity from the supply to the demand?
That’s where electrical grids — the focus of this post — come in.

**A quick primer on electrical grids**

Let’s start with a short, hopefully not too technical, primer on electrical grids — they play a huge role in all our lives, but I personally didn’t really know how they worked until [I started working at a renewables optimization software company](https://dynamicallytyped.com/issues/056/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) in January.
On the most basic level, grids are very large systems — all of Europe is a single grid, and North America is divided into an eastern and a western grid (plus the smaller Texas and Quebec grids) — consisting of power lines at different voltages (high for long-distance transmission, low for local distribution), electrical substations which step voltage up or down, and electricity producers and consumers.

As opposed to the direct current (DC) in, for example, a battery-LED system — where electrons flow from one pole of the battery through the LED to the other pole — electricity in grids is in the form of alternating current (AC) — where electrons oscillate back and forth on the power line tens of times a second: at 50 Hz (times a second) in Europe and 60 Hz in North America.
One of the main jobs of a grid operator is to ensure that this frequency remains constant, because [lots of stuff breaks if it is too far from nominal](https://electronics.stackexchange.com/questions/105186/importance-of-keeping-the-electricity-network-frequency-stable?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which can cause grid-wide blackouts in the worst case.
An oversupply of electricity (more generation than consumption) causes the frequency to increase, while an undersupply causes it to decrease; so the operator has to make sure that generation and consumption are equal at all times.

**Electricity markets and renewable generation**

Grid operators keep electricity generation and consumption equal by creating time-based markets for electricity.
For this discussion, the _day-ahead_ and _intraday_ markets are the most important.
On the day-ahead market, producers and consumers place bids to sell and buy the amount of electricity they want to produce or consume during each hour of the following day.
At the end of the day, the operator settles these bids in an optimal way that ensures that, for each hour, the amount sold matches the amount bought.
Problem solved, right?

Sadly, as anyone who has ever been outside knows, the weather (and other factors affecting generation and consumption) can’t be perfectly predicted down to the hour a whole day ahead.
It could happen, for example, that the afternoon is less sunny than expected, which means that a solar farm will produce less electricity than it sold the previous day.
This is where the intraday market — operating on 15-minute intervals instead of hour-long ones — comes in.
In this scenario of an expected underproduction, the solar farm can go to the intraday market and place bids to buy the difference between the amount of electricity it sold on the day-ahead market and the amount it’ll actually produce, from someone who is willing to either consume less power than they bought or produce more power than they already sold.

In practice, it’s usually the latter: someone will jump in and produce the extra electricity.
This is big business for coal and gas plants, because they can ramp their production up (or down if the scenario is reversed) on-demand, and very quickly.
As a larger percentage of electricity on the grid is generated using weather-dependent renewables, this intraday market becomes more valuable — and coal and gas-burning plants can be operated profitably for longer, even as [learning effects make wind and solar power cheaper](https://ourworldindata.org/cheap-renewables-growth?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [CO2 emission prices rise](https://www.bloomberg.com/news/articles/2021-01-19/europe-carbon-market-emissions-permits-set-price-records-in-2021?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

Beyond fossil fuel-burning power plants ramping their generation up and down to meet consumption, another obvious supplier of flexibility is large batteries.
These can be paid to charge when there is an oversupply, and paid again to discharge when there is an undersupply.
Another plausible demand-side response comes from climate-controlled (food) distribution centers that need to run their cooling units a number of hours a day, but can be a bit flexible about exactly when those hours are.
These are both useful, but they’re not happening at scale (yet).

So it’d be great for the planet if these coal and gas plants had some more competition on the intraday electricity balancing market.

(Any imbalance that is not solved on the day-ahead and intraday markets is handled by the [grid operator’s balancing reserves](https://www.tennet.eu/electricity-market/ancillary-services/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter); I won’t go into the details of these FCRs and FRRs here.)

**Datacenters and flexible AI training for demand-side response**

This is — finally — where datacenters and AI models come in.
Here in The Netherlands, there has been some controversy in recent months about how many datacenters are being built (I bike by [this imposing-looking one in Amsterdam](https://www.stedebouwarchitectuur.nl/nieuws/091117/de-tempels-van-deze-tijd-datacenters-van-equinix?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) several times a week) and how much energy they use.
But given the above, I actually think datacenters have the potential to play a positive role in the intraday electricity market.
Although many tasks of a datacenter, like serving websites, facilitating video calls, or powering Netflix streams, can’t really be shifted around in time at will, AI-related tasks often can be — both in research and production.

In a research setting, gargantuan AI models like [DeepMind’s AlphaFold 2](https://dynamicallytyped.com/stories/2020/deepmind-alphafold-2/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) can often take several days or weeks to train on dozens, hundreds or thousands of powerful machines.
And labs like OpenAI already use [highly-customized versions of tools like Kubernetes](https://dynamicallytyped.com/links/ml-research/210214-openai-on-kubernetes/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to orchestrate these machines.
It’s not a stretch to imagine that these tools can be extended to ramp training up or down (in terms of the number of active machines, for example), along with the intraday electricity market.
(In fact, [I tried building a little tool similar to this myself](https://twitter.com/layon_overwhale/status/1236619430681067520?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) last year!)

In production settings, machine learning models are often retrained periodically, once for a whole service or even many times for individual (groups of) users.
This doesn’t happen exactly when the user queries or interacts with the model, but rather in an “offline” way: training happens on some schedule, and the model is saved to be retrieved for inference whenever the user wants to query it — so there’s potential for flexibility there.
Even inference can happen offline: things like tagging photo libraries with the objects present in the photos are not too time-sensitive, and can probably happen flexibly within some period after the photos are uploaded without impacting user experience too much.
It’s also not too crazy to imagine syncing this up to the electricity market.

Luckily, I’m not the first person to come up with this idea — see [the Boden Tech datacenter in Sweden](https://energyplaza.vattenfall.se/how-fcr-became-a-sustainable-win-win-for-the-boden-tech-data-centre?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [Google’s partnership with Electricity Map](https://twitter.com/corradio/status/1253188550201393154?s=20&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), for example — but I do think that it’s under-appreciated, and often missed in discussions about [Green AI](https://arxiv.org/abs/1907.10597?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [the climate risks of large AI models](https://www.washington.edu/news/2021/03/10/large-computer-language-models-carry-environmental-social-risks/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Since these big models can often be scheduled to be trained at any time, perhaps counterintuitively, the more power they use, the more flexibility they can offer to the grid — and the more they can out-compete fossil fuel plants on the intraday electricity market!

I think we have a better shot at getting big tech companies and AI labs to implement ideas like this at scale, than we do at getting them to stop training big AI models.
So instead of looking at gargantuan AI (language) models only as a climate problem, let’s give some more attention to their potential as a climate solution.