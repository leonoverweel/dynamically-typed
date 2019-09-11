# #17: GANPaint Studio, collaborative sketching with AI, and a survey of ML testing 

Hey everyone, welcome to Dynamically Typed #17.
Today’s issue is a bit shorter than usual because I’ve had a busy two weeks working on my MSc thesis—I’m already halfway through my internship at Adyen!
Nevertheless, I found a good few interesting links for the newsletter.

In productized AI news, MIT’s CSAIL showed off an image editing tool called GANPaint Studio, and a US police body cam manufacturer banned the use of facial recognition on its cameras.
On the research side, Microsoft introduced MASS, a new state-of-the-art pre-training technique for sequence-to-sequence models, and Zhang et al.
published a comprehensive study of machine learning testing techniques.
Finally, I found a fun study from Stanford that allows you to take turns with an AI to collaboratively make a drawing.

## Productized Artificial Intelligence 🔌

![GANPaint Studio (MIT CSAIL).](https://s3.amazonaws.com/revue/items/images/004/766/177/mail/c4b238b6dfd0b9fb532dc1f4543ae35d.png?1562316272)

_GANPaint Studio (MIT CSAIL)._

**GANPaint Studio is a tool by MIT CSAIL to modify images of certain categories using a generative adversarial network.**
Using the software, you can take an input image of something like a kitchen or a church and paint over an area you want to change.
You can then tell it to draw extra chairs or windows, or different rooftops or trees, and GANPaint Studio will do its best to realistically fill the areas you marked with your desired objects.
More:

- Demonstration video on YouTube: [GANPaint Studio (SIGGRAPH 2019)](https://www.youtube.com/watch?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=q1K4QWrbCRM)
- Project website: [ganpaint.io](http://ganpaint.io/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Paper to appear at SIGGRAPH 2019: [Semantic Photo Manipulation with a Generative Image Prior](http://ganpaint.io/Bau_et_al_Semantic_Photo_Manipulation_preprint.pdf?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) (PDF)
- Kyle Wiggers for VentureBeat: [GAN Paint Studio uses AI to add, delete, and modify objects in photos](https://venturebeat.com/2019/06/30/gan-paint-studio-uses-ai-to-add-delete-and-modify-objects-in-photos/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**Police body camera company Axon has banned the use of facial recognition technology on its cameras.**
This is the less shiny side of productized artificial intelligence: biased AI systems are being deployed in sensitive areas like policing, where they are likely to reinforce existing societal inequalities and (racial, gender, sexual orientation, …) discrimination.
As [Ben Evans wrote earlier this year](https://www.ben-evans.com/benedictevans/2019/4/15/notes-on-ai-bias?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter):

> [The] scenario for AI bias causing harm that is easiest to imagine is probably not one that comes from leading researchers at a major institution.
> Rather, it is a third tier technology contractor or software vendor that bolts together something out of open source components, libraries and tools that it doesn’t really understand and then sells it to an unsophisticated buyer that sees ‘AI’ on the sticker and doesn’t ask the right questions, gives it to minimum-wage employees and tells them to do whatever the ‘AI’ says.

Indeed, it’s not hard to imagine Evans’ scenario happening in the police body cam setting: nothing is stopping a budget-constrained police department from trying to use body cams to automatically find criminals, without realizing that current commercially-available facial recognition software is much more likely to, for example, misrecognize a person of color than a white person.

That’s why it’s refreshing to see a body cam manufacturer stepping up to take responsibility for the problem.
Charlie Warzel for the New York Times:

> According to [Axon’s independent] ethics board report, in early conversations about facial recognition, Axoninitially argued that it “could not dictate to customers how products were used, nor its customers’ policies, and that it could not feasibly patrol misuse of its product.” That’s Big Tech’s version of “guns don’t kill people, people kill people.” And it’s a view that’s very widely held across the industry.

> Mr.
> Friedman hopes that Axon’s pledge will force other vendors to think about where the new technology might be headed and how it could impact the most vulnerable.
> “We want them to remember that just because you can build it, doesn’t mean you should.”

It’d be great to see technology companies that sell facial recognition APIs, like [Amazon](https://aws.amazon.com/rekognition/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) and [Microsoft](https://azure.microsoft.com/en-us/services/cognitive-services/face/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter), build these principles into their user agreements instead of [waiting for governments](https://blogs.microsoft.com/on-the-issues/2018/12/06/facial-recognition-its-time-for-action/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) to put [regulations](https://www.nytimes.com/2019/05/14/us/facial-recognition-ban-san-francisco.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) in place.
Read more about Axon’s decision in Warzel’s piece here: [A Major Police Body Cam Company Just Banned Facial Recognition](https://www.nytimes.com/2019/06/27/opinion/police-cam-facial-recognition.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter#click=https://t.co/PlHpwHuiad).

## Machine Learning Technology 🎛

![Figures from Machine Learning Testing: Survey, Landscapes and Horizons. (Zhang et al.)](https://s3.amazonaws.com/revue/items/images/004/766/792/mail/ce953ab95c1dfb9f69b5bfa6ab5de611.png?1562324430)

_Figures from Machine Learning Testing: Survey, Landscapes and Horizons. (Zhang et al.)_

**Zhang et al.
published a comprehensive survey of machine learning testing research on arXiv.**
The paper is a collaboration between CREST (University College London), FAIR (Facebook), Kyushu Univeristy, and Nanyang Technological University, and it covers “any activity aimed at detecting differences between existing and required behaviours of machine learning systems.” This includes:

- Testing workflows (how to test), such as test generation, analysis, reporting and debugging.
- Testing components (where and what to test), such as data, model, and framework testing.
- Testing properties (what to test), such as correctness, overfitting, robustness, efficiency, fairness, and interpretability.

It looks like a very useful reference resource for both researchers and industry practitioners.
Read the paper on arXiv: [Machine Learning Testing: Survey, Landscapes and Horizons](https://arxiv.org/abs/1906.10742?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter).

**Microsoft Asia researchers have introduced Masked Sequence to Sequence Pre-training (MASS),** which outperforms previous state-of-the-art methods on tasks like unsupervised machine translation, low-resource machine translation, abstractive summarization, and conversational response generation.
Modern systems for these natural language tasks use an encoder-attention-decoder system, and with previous techniques like BERT and GPT, the encoder and decoder sides had to be pre-trained separately.
MASS uses masking to pre-train the two sides jointly, which significantly boosts performance on the aforementioned tasks.
More:

- Xu Tan wrote an in-depth (but easy to follow) explanation of MASS for Microsoft’s AI blog: [Introducing MASS – A pre-training method that outperforms BERT and GPT in sequence to sequence language generation tasks](https://www.microsoft.com/en-us/research/blog/introducing-mass-a-pre-training-method-that-outperforms-bert-and-gpt-in-sequence-to-sequence-language-generation-tasks/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Paper by Song et al. on arXiv: [MASS: Masked Sequence to Sequence Pre-training for Language Generation](https://arxiv.org/abs/1905.02450?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**Quick ML resource links ⚡️** ([see all 25](https://www.notion.so/adab36fecaea4306880898f41dcb9cb3?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter&v=cb3a74562c914234ac171931dad6c2e4))

- Jay Alammar created a great visual introduction to NumPy and data representation; wish I had this when I was trying to wrap my head around ndarrays. Link: [visual intro to NumPy](https://jalammar.github.io/visual-numpy/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Steve Grunwell wrote a nice introduction to regular expressions, which I’ve started using more and more for things like data cleaning. Link: [Demystifying regular expressions](https://stevegrunwell.com/blog/demystifying-regular-expressions/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)
- Related, RegExr is an online tool to build and test regular expressions. Link: [RegExr](https://regexr.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

## Cool Things ✨

![Drawing an octopus together; peach lines are me, yellow lines are the AI. (Stanford Department of Psychology)](https://s3.amazonaws.com/revue/items/images/004/766/718/mail/c38e36707557631ea229371297618f5e.png?1562322419)

_Drawing an octopus together; peach lines are me, yellow lines are the AI. (Stanford Department of Psychology)_

**Let’s draw together!
__** is a fun online study where you collaborate with an AI to draw different things.
The site tells you something to draw, like an elephant or an octopus, and then invites you to make the first line.
You then take turns drawing the next line until the sketch is complete, after which the AI checks your collaborative work by trying to guess what the drawing was.

The site is a part of “a study being performed by cognitive scientists in the Stanford Department of Psychology,” but I haven’t been able to find out much more about the research online.
You can try it out here: [Let’s draw together!](https://cogtoolslab.org:8888/collab96/collab.html?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter)

**Thanks for reading!**
As usual, you can let me know what you thought of today’s issue using the buttons below or by replying to this email.
If you’re new here, check out the [Dynamically Typed archives](https://dynamicallytyped.com/?utm_campaign=Dynamically%20Typed&utm_medium=email&utm_source=Revue%20newsletter) or subscribe below to get a new issues in your inbox every second Sunday.

**If you enjoyed this issue of Dynamically Typed, why not forward it to a friend?**
It’s by far the best thing you can do to help me grow this newsletter.
😁