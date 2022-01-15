---
title: Text-to-speech based on deep learning for Web site using Amazon Polly and Ruby
description: Amazon Polly, Text-to-speech service from AWS was announced at today
  ‘s re:Invent. Amazon Polly is speech synthesize system based on deep…
date: '2016-12-01T15:00:02+09:00'
categories: []
keywords: [polly, amazon, speech, english, aws, voice, sounds, joanna, characters,
  text]
authors: [aki]
recommendations: [/blog/2017-05-02_An-easy-way-to-get-URL-list-of-your-Medium-publication-c60c61244101/,
  /blog/2019-04-24_Ruby-for-Data-Science-and-Machine-Learning-9f03e99125e0/, /blog/2017-08-03_Why-OSS-based-machine-learning-is-good--3ab45a1a5e52/]
---

Amazon Polly, Text-to-speech service from AWS was announced at today ‘s re:Invent. Amazon Polly is speech synthesize system based on deep learning.

[Amazon Polly — Text to Speech in 47 Voices and 24 Languages](https://aws.amazon.com/blogs/aws/polly-text-to-speech-in-47-voices-and-24-languages/)

**\[updated\] I added generated speech of this article.**

**\[updated2\] I created simple CLI tools and rubygems of polly**

[https://rubygems.org/gems/pollynomial](https://rubygems.org/gems/pollynomial)

The great thing about Amazon Polly is that we can use TTS easily with AWS CLI. The price is free for up to 5 million characters a month, if over that limitation, it is very cheap with $ 0.000004/character. If you synthesize [Adventures of Huckleberry Finn](https://en.wikipedia.org/wiki/Adventures_of_Huckleberry_Finn), it costs about only $2.4.

Here is the example code of Polly with AWS CLI tool.

$ aws polly synthesize-speech \\  
  --output-format mp3 --voice-id Joanna \\  
  --text "Hello my name is Joanna." \\  
  joanna.mp3

As of December 1, 2016, they support the following 24 languages mainly in European languages.

*   Icelandic
*   Italian
*   Welsh
*   Dutch
*   Swedish
*   Spanish (Castile)
*   Spanish (USA)
*   Danish
*   Turkish
*   German
*   Norwegian
*   French
*   French (Canada)
*   Portuguese
*   Portuguese (Brazil)
*   Polish
*   Romanian
*   Russian
*   Japanese
*   English (India)
*   English (Welsh)
*   English (Australia)
*   English (US)
*   English (UK)

I think Japanese speech sounds very natural. Sometime it will be a strange accent, but if I register a word with Lexicon, we can improve the quality by myself. Japanese sample voice as following:

I often find interesting articles in Medium, but since reading long English article is a bit tough for non native English speaker like me. So I came up with if I made the article to voice, I would listen it easily. That’s why I wrote the code to convert articles to speech with Ruby like following:

There are some important restrictions of API:

*   The number of characters per API is 1500 characters
*   Long voice is truncated after 5 minutes

Read more in detail…

[**Limits in Amazon Polly - Amazon Polly**  
_Limits when using Amazon Polly._docs.aws.amazon.com](http://docs.aws.amazon.com/polly/latest/dg/limits.html "http://docs.aws.amazon.com/polly/latest/dg/limits.html")[](http://docs.aws.amazon.com/polly/latest/dg/limits.html)

Actually, I tried to convert the following article just found in Hckr news. I can hear it comfortably.

[**How the Circle Line rogue train was caught with data**  
_Data science meets the Marey Chart_blog.data.gov.sg](https://blog.data.gov.sg/how-we-caught-the-circle-line-rogue-train-with-data-79405c86ab6a "https://blog.data.gov.sg/how-we-caught-the-circle-line-rogue-train-with-data-79405c86ab6a")[](https://blog.data.gov.sg/how-we-caught-the-circle-line-rogue-train-with-data-79405c86ab6a)

If I did a bit more hard work, I can generate sounds of the latest articles on a specific site from RSS and play back the sounds from mobile saved in Dropbox.

Honestly, Amazon Polly is cheap, multilingual and natural as it is, and API is easy to use like other AWS services. It makes me feel that companies in Japan that have worked hard for existing TTS systems are in very difficult time. As a developer, I am looking forward to using various purpose and get more better services using Polly.