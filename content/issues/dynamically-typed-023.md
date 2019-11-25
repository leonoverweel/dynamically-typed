# #23: Robotic raspberry and lettuce pickers, 2.5 billion objects in Pinterest Lens, and an analysis of the AI reproducibility crisis 

Hey everyone, welcome to Dynamically Typed #23!

I’m covering a lot in today’s issue.
For productized artificial intelligence, Pinterest Lens can now recognize 2.5 billion objects; CNN Business had a piece on computer vision-powered agriculture robots; and Google released a big report on their AI Impact Challenge.

On the research side, lots of cool stuff came out of Interspeech 2019, the biggest conference on spoken language processing, including an ML approach to recognizing killer whale calls!
There was also a large industry push into detecting deepfake images and videos, and a data-based analysis of the AI reproducibility crisis.
As usual, I’m closing today’s newsletter off with climate and art projects.

Let’s jump in.

## Productized Artificial Intelligence 🔌

![Visual search through the camera or existing Pins in the updated Pinterest Lens. (Pinterest)](https://s3.amazonaws.com/revue/items/images/005/044/190/mail/2c1e15e7b57a42027766ab5d6ade307b.png?1569696806)

_Visual search through the camera or existing Pins in the updated Pinterest Lens. (Pinterest)_

**Social search and discovery app Pinterest updated their Lens feature to recognize 2.5 billion objects.**
Similar to Google Lens—but capable of recognizing 2.5x more home and fashion “somethings"—Pinterest Lens identifies objects in photos and links users to similar things previously pinned on the site.
It works on photos taken by the camera or, in a clever bit of UI, when a user pinches to zoom into a part of an existing image that contains recognizable objects.
From the Pinterest newsroom:

> Today we’re rolling out improvements to Lens and bringing shoppable Pins to visual search results.
> If you see it — online or off — you can shop it.

I love this business model.
Instead of creepily tracking you across the internet and interrupting your newsfeed or video playback with ads,* Pinterest actually shows you where to shop for something _when you’re searching for it—_ and presumably then earns a referral bonus with the store.
So now when you see that cute IKEA shelf in a friend’s home, they won’t have to remember whether it’s a _Billy,_ a _Svalnäs_ , or a _Bror_ : the Pinterest Lens can tell you, and link you straight through to the purchase page.
(Can you tell I’ve been decorating my apartment?) Anyway, for more details, see the announcement on the Pinterest Newsroom: [Upgrading Lens for more online to offline inspiration](https://newsroom.pinterest.com/en/post/upgrading-lens-for-more-online-to-offline-inspiration?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

_* I don’t use Pinterest, so for all I know they do this too, but at least they’re trying alternative approaches to making money as well._

![A raspberry picking robot by Fieldwork Robotics. (CNN Business)](https://s3.amazonaws.com/revue/items/images/005/044/988/mail/7c438bb7b09ee240ec5adef571a0268d.jpeg?1569742352)

_A raspberry picking robot by Fieldwork Robotics. (CNN Business)_

**Nell Lewis wrote about agriculture robots hitting the market in the U.K.**
Robots that pick fruit and vegetables are a good example of productized AI because they use computer vision to see where a piece of fruit is, to decide whether it’s ripe enough to pick, and to figure out how it’s oriented before harvesting it.
Lewis’ piece covers four robots in different stages of production:

- A strawberry-picking robot that is currently used in production in Belgium and the Netherlands, by Belgian company Octinion
- An apple-picking robot currently used in California, by Abundant Robotics
- A raspberry-picking robot that it expects to go into production with Hall Hunter growers next year, by Fieldwork Robotics
- Vegabot, a robot that picks iceberg lettuce and is currently still in development, by the University of Cambridge

As the world population and food demand grows, and as farming becomes more difficult in the face of climate change and shifting labor interests, I can see the agri-robots industry becoming huge in the coming decades.
Read Lewis’ CNN Business story for more: [Why robots will soon be picking soft fruits and salad](https://edition.cnn.com/2019/09/04/business/robot-farmers/index.html?_hsenc=p2ANqtz-8HCoir0GLOsl4_Q5PLUpJ1-xl2yf3Wr4xrJV-ZIEV_C-vbm_tSsPwLYZEK4P3pD3LGw7RKs36NUYTD5t_sWi-hyQhWxg&_hsmi=77004961&utm_campaign=The%20Batch&utm_content=77004961&utm_medium=email&utm_source=hs_email).

**“Machine learning is not always the answer”** for social impact products and projects.
This is the primary takeaway from Google’s 47-page report on their AI Impact Challenge, which awarded $25 million in funding to 20 grantees (see [DT #13](https://dynamicallytyped.com/issues/13-caption-this-new-ai-powered-features-at-google-i-o-and-openai-s-staged-gpt-2-release-175669?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [DT #15](https://dynamicallytyped.com/issues/15-neural-avatars-ai-on-the-edge-and-apple-s-new-create-ml-app-180967?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
Google received 2,602 proposal from 119 countries and analyzed them for “a view of the AI for social good landscape,” which they present in the report.
Assuming grant proposals are an unbiased estimator:

- The most common area for social good AI projects is health (27% of proposals), followed by environment, conservation, and energy (16%), and education (12%).
- The most common AI capability for such projects is computer vision (41%), followed by general “analytics” (26%) and deep learning (18%); noticeably, reinforcement learning, which is a big focus of Alphabet’s DeepMind research group, is used by very few real-world projects (2%).
- Academic institutions are most likely to already be using AI in some way (85%), where not-for-profit organizations are least likely (44%).

Digging deeper, Google noted that for many social impact projects, machine learning just isn’t applicable.
Hopefully this report will help poke a hole in the “sprinkle some AI on top and call it a day” enterprise hype that has been growing in the past few years:

> Some organizations submitted proposals that might be better implemented without machine learning by leveraging other methods that could result in faster, simpler, and cheaper execution.
> Other applicants underestimated the complexity of the work required, and in still other instances, machine learning is not yet sophisticated enough to make the proposed solution viable.

That definitely corroborates the notion that the current AI hype is giving a lot of people wrong ideas about the usefulness of machine learning in their domains.
The report’s overall seven main insights are:

I’m not going to dig into all of these here, so check out the full report for detailed descriptions and specific recommendations for funders, organizations using AI, and policymakers:

- Brigitte Hoyer Gosselink (Head of Product Impact, Google.org) and Carla Bromberg (Program Lead, Google AI) for Google’s The Keyword blog: [2,602 uses of AI for social good, and what we learned from them](https://www.blog.google/outreach-initiatives/google-org/2602-uses-ai-social-good-and-what-we-learned-them/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- The full report (PDF): [Accelerating social good with artificial intelligence: Insights from the Google AI Impact Challenge](https://services.google.com/fh/files/misc/accelerating_social_good_with_artificial_intelligence_google_ai_impact_challenge.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Machine Learning Research 🎛

![Automatically transcribing a meeting using multiple synced phones. (Microsoft Research)](https://s3.amazonaws.com/revue/items/images/005/043/629/mail/58266075426fc2618a0dd4259c5e8d16.png?1569679953)

_Automatically transcribing a meeting using multiple synced phones. (Microsoft Research)_

**Microsoft Research demonstrated fusing mobile phone microphones to improve meeting transcription.**
The idea is that, instead of using expensive conferencing equipment, participants can all have their phones out recording a meeting in parallel.
A central server then transcribes and combines this data to produce a more accurate transcript than any of the phones could do individually.
The method by [Yoshioka et al.
(2019)](https://www.microsoft.com/en-us/research/publication/meeting-transcriptions-using-virtual-microphone-arrays/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which outperforms single-phone transcripts by 14.8% or 22.4% respectively with three or seven microphones, is part of [Project Denmark](https://www.microsoft.com/en-us/research/project/project-denmark/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), Microsoft’s longer-term project “to move beyond the need for traditional microphone arrays.” More:

- Takuya Yoshioka (Principal Researcher) et al. for the Microsoft Research Blog: [Bring your phones to the conference table: creating ad hoc microphone arrays from personal devices](https://www.microsoft.com/en-us/research/blog/bring-your-phones-to-the-conference-table-creating-ad-hoc-microphone-arrays-from-personal-devices/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Paper by Yoshioka et al. (2019): [Meeting Transcription Using Asynchronous Distant Microphones](https://www.microsoft.com/en-us/research/publication/meeting-transcription-using-asynchronous-distant-microphones/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**_Aloha Phone_ , was there any related research this month?**
Yes!
The work by Yoshioka et al.
is being published as part of [Interspeech 2019](https://interspeech2019.org/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), the largest conference on spoken language processing, which was held earlier this month.
The big tech companies all have voice assistants that are key to their platforms, and they’ve all posted overviews of their recent advances published at Interspeech 2019: see the research blog posts from [Amazon](https://www.amazon.jobs/en/landing_pages/interspeech2019?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Apple](https://machinelearning.apple.com/2019/09/15/interspeech.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Facebook](https://ai.facebook.com/blog/facebook-research-at-interspeech-2019/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [Google](https://ai.googleblog.com/2019/09/google-at-interspeech-2019.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), and [Microsoft](https://www.microsoft.com/en-us/research/event/interspeech-2019/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
My favorite summary of the conference comes from Cognito Corporation, who highlighted ten papers ranging from methods to improve speech recognition for deaf people, to deep learning for orca call identification.
Read their post on Medium here: [Interspeech 2019 — Machine Learning-enabled Creativity and Innovation In Speech Tech](https://medium.com/@CogitoCorp/interspeech-2019-machine-learning-enabled-creativity-and-innovation-in-speech-tech-30d46df482e8?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Facebook, Microsoft, and Google have launched initiatives to push deepfake detection research.**
Deepfakes are realistic-looking fake images or videos where one person’s face has been superimposed over someone else’s body using generative adversarial networks (GANs, see [DT #15](https://dynamicallytyped.com/issues/15-neural-avatars-ai-on-the-edge-and-apple-s-new-create-ml-app-180967?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)).
They’ve previously been used to create fake nudes of celebrities and to make politicians look like they’ve said things they haven’t.
If social media sites can robustly detect that a photo or video has been deepfaked, they could alert their users of this fact, but this is a very difficult problem.
Now, seemingly independently and in parallel, two initiatives have popped up to push this research forward:

- Facebook and Microsoft have launched the [Deepfake Detection Challenge](https://deepfakedetectionchallenge.ai/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), which starts next month and “invites people around the world to build innovative new technologies that can help detect deepfakes and tampered media.”
- Google has [released](https://ai.googleblog.com/2019/09/contributing-data-to-deepfake-detection.html?m=1&utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) a [dataset of deepfakes](https://github.com/ondyari/FaceForensics/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) generated using different techniques, along with the [FaceForensics benchmark](http://kaldir.vc.in.tum.de/faceforensics_benchmark/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

As nation states and other actors are putting increasing effort into spreading fake news on these companies’ platforms, it’s good to see them putting resources into this problem.
Especially with the U.S.
elections coming up next year, this work will be very important.

**Edward Raff attempted to reproduce 255 machine learning papers.**
He succeeded for 63.5% of papers, meaning that about 1/3rd of published results he surveyed were not easily reproducible.
Some (statistically significant) results I found interesting:

> Papers with detailed pseudocode and no pseudocode were equally reproducible.

> No relation between reproduction and [publication year].
> Does this imply the [reproducibility] “crisis” has been ever present, overblown, or something else?

The AI reproducibility crisis has been making headlines recently ([WIRED](https://www.wired.com/story/artificial-intelligence-confronts-reproducibility-crisis/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), [BBC](https://www.bbc.com/news/science-environment-47267081?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)), so this new data-based analysis is an interesting new insight: much ado about nothing, or has ML research just never been peer reviewed critically enough?
More:

- Paper by Raff (2019) on arXiv: [A Step Toward Quantifying Independently Reproducible Machine Learning Research](https://arxiv.org/abs/1909.06674?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- NeurIPS poster (PDF) on GitHub: [Quantifying Reproducible Machine Learning Research](https://github.com/EdwardRaff/Quantifying-Independently-Reproducible-ML/blob/master/QIRML_NeurIPS_poster.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Data on GitHub: [EdwardRaff/Quantifying-Independently-Reproducible-ML](https://github.com/EdwardRaff/Quantifying-Independently-Reproducible-ML?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Artificial Intelligence for the Climate Crisis 🌍

![Common project type submissions for Google's AI Impact Challenge. (Google.org)](https://s3.amazonaws.com/revue/items/images/005/043/496/mail/531b9977faeb02c522347d881e763357.png?1569674260)

_Common project type submissions for Google's AI Impact Challenge. (Google.org)_

**Google’s AI Impact Challenge report also summarized climate-related projects proposed for the grant.**
Most of these look like they’re related to air quality: estimating where air pollution happens and what it effects.
Interestingly, things like solar PV prediction or other energy-related projects didn’t make the list, suggesting there’s still a gap there to fill.

## Cool Things ✨

![3D Ken Burns effect from a single image. (Niklaus et al.)](https://s3.amazonaws.com/revue/items/images/005/045/162/mail/366e3f05f9d4ae046a436f7795656605.png?1569746738)

_3D Ken Burns effect from a single image. (Niklaus et al.)_

**For his internship at Adobe, Simon Niklaus managed to create a parallax effect from a single image.**
The still screenshot I embedded above doesn’t really get the effect across, so check out his [tweet with several demos](https://twitter.com/SideOverride/status/1173502120969920514?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).
Niklaus explains that their framework estimates the depth of different parts of the image, generates a point cloud, and then synthesizes video frames by moving a virtual camera through the point cloud.
Read more about it on his website: [3D Ken Burns Effect from a Single Image](http://sniklaus.com/papers/kenburns?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
🏡