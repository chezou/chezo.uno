---
title: Why OSS based machine learning is good?
description: This article is translation of Japanese version.
date: '2017-08-03T12:56:59+09:00'
categories: [machine_learning, OSS]
authors: [aki]
aliases: [/blog/why-oss-based-machine-learning-is-good-3ab45a1a5e52, /blog/3ab45a1a5e52]
keywords: [learning, machine, deep, open, algorithms, research, performance, source,
  companies, year]
recommendations: [/blog/2019-06-04_The-first-conference-of-Operational-Machine-Learning--OpML--19-308baad36108/,
  /blog/2019-04-24_Ruby-for-Data-Science-and-Machine-Learning-9f03e99125e0/, /blog/2016-12-01_Text-to-speech-based-on-deep-learning-for-Web-site-using-Amazon-Polly-and-Ruby-adc1923212cb/]
---


_This article is translation of_ [_Japanese version_](https://chezo.uno/post/2017-08-03_oss-48807bbbf13f/)_._

After releasing of TensorFlow, the movement of OSS-based machine learning is accelerating. [François Chollet](https://twitter.com/fchollet), the creator of Keras, says the essential point of this change. I think his phrase is enough, but in this article, I would like to organize why open source machine learning is great, and what recent trends are.

### tl;dr

*   Machine learning and deep learning frameworks have become standard things for software engineers
*   Since arXiv becomes very famous, many papers are published before peer review of international conferences. This change made easier for other companies to validate the algorithm.
*   Many researchers have been started to study machine learning, machine learning researches in academia become Red Oceanic.
*   The strategy, “Make a great algorithm, but the implementation is secret” becomes a thing of the past.

### Halcyon days

Five or ten years ago, almost all players working on advanced machine learning were in laboratories such as universities or large enterprises, or some advanced companies. In particular, the amount of data with a label was smaller than the present, and many researchers had been improving the performance by researching algorithms, by feature engineering.

Many researchers from academia studied state-of-the-art machine learning, posted to international conferences. Most of the insights were shared after peer review. Implementation was not shared as much as now, and each researcher had to reimplement the preceding research from scratch. A typical cycle for releasing new algorithms was a half year, in some cases more than a year.

There were few open source machine learning libraries/frameworks like Weka. scikit-learn, [released in 2010](https://en.wikipedia.org/wiki/Scikit-learn), was not famous among software engineers. Many of us used libraries with single/few algorithms such as libsvm and liblinear.

### Fast moving era

As of 2017, people who work in machine learning have significantly increased compared with 10 years ago. The center of machine learning has been moved from academia to companies with large data. In particular, software engineers, who have never worked on machine learning, entering deep learning world. I was surprised to hear that my friend of the community who had never worked on machine learning in business had started working on Deep Learning. The reasons for this movement are 1) it became general for companies to store large data that can be used for machine learning,   
2) excellent machine learning frameworks have been increased, and 3) the GPU power leverage Deep Learning for efficient calculation.

Many open source libraries became popular not only in the frameworks of Deep Learning such as TensorFlow, Chainer, MXNet, Caffe 2, PyTorch but also by XGBoost, Lightgbm, which are famouse among kaggler. scikit-learn is also common tool as a framework to experiment with multiple algorithms.

### The rise of “open papers”

This movement is supported by machine learning competition site “kaggle”, and by a place to post open papers called “arXiv”. (There is discussion arxiv does not have a peer review process and quality is not assured. So can we call the document as a research paper? But, in this post, I will call the research paper style report as “paper”)

The following article describes the number of paper submissions related to machine learning (especially Deep Learning) submitted to arXiv. According to this article, it is pointed out that the number of papers related to machine learning has more than quadrupled in 2017 compared to five years ago.

[**A Peek at Trends in Machine Learning**  
_Have you looked at Google Trends? It’s pretty cool — you enter some keywords and see how Google Searches of that term…_medium.com](https://medium.com/@karpathy/a-peek-at-trends-in-machine-learning-ab8a1085a106 "https://medium.com/@karpathy/a-peek-at-trends-in-machine-learning-ab8a1085a106")[](https://medium.com/@karpathy/a-peek-at-trends-in-machine-learning-ab8a1085a106)

Papers of arXiv are posted every day. It means, state-of-the-art results from such as Google, Facebook, Microsoft, etc. are published more and more before peer review. This is a challenge for the central laboratories of the traditional large enterprises to research and develop cutting edge algorithms of machine learning itself. Those companies usually set targets for a year or half a year. There is also criticism of “just adding parts”, but it is clear that the speed of developing machine learning algorithms is significantly fast.

> In the field of machine translation, the breakthrough in deep learning was encoder-decoder and attention. The subsequent papers are not interesting, “I just put existing parts here.” I can’t understand why these papers come to the top conference.

Recently, for those who read new arXiv’s paper day and night, there is an system called “ariXiv Times” to better check new arrival documents.

[**arXivTimes Indicator**  
_Edit description_arxivtimes.herokuapp.com](https://arxivtimes.herokuapp.com/ "https://arxivtimes.herokuapp.com/")[](https://arxivtimes.herokuapp.com/)

### Open papers accelerates Open source machine learning

This March, a paper about “Deep Forest” was published at arXiv, and it became a hot topic with the author claims that “performance is better than Deep Learning”.

[**\[1702.08835\] Deep Forest: Towards An Alternative to Deep Neural Networks**  
_Abstract: In this paper, we propose gcForest, a decision tree ensemble approach with performance highly competitive to…_arxiv.org](https://arxiv.org/abs/1702.08835 "https://arxiv.org/abs/1702.08835")[](https://arxiv.org/abs/1702.08835)

This method proposed in this paper, about one week (2017/3/5) after the publication (2017/2 / 28), R implementation came up and Python implementation came out after R one. A discussion was made with the following LightGBM issue on GitHub, and it came out that there was not reproducibility of the article, they can’t confirm the performance.

[**Support gcForest · Issue #331 · Microsoft/LightGBM**  
_LightGBM - A fast, distributed, high performance gradient boosting (GBDT, GBRT, GBM or MART) framework based on…_github.com](https://github.com/Microsoft/LightGBM/issues/331 "https://github.com/Microsoft/LightGBM/issues/331")[](https://github.com/Microsoft/LightGBM/issues/331)

It is a symbolic event where the OSS implementation of the paper   
appeared within a week after published in arXiv and the discussion of the community began.

I hear that it is increasing that the number of international conferences that require disclosing the implementation when a paper is submitted.

### Conclusion

It is an essential task to develop the machine learning algorithm. Thanks to open papers, ML competition web site, and fast implementation of new algorithms as an OSS, we can adopt state-of-the-art knowledge into the business rapidly.

IMHO, it is becoming fun to focus on where we can make use of ML in business rather than developing the algorithm itself.

In other words, now, it is too hard to say “special machine learning algorithms that only our company can do”. Of course, people in academia will push these cutting-edge initiatives if they can prepare data. What is the evidence that one company invents a better algorithm quickly than most state-of-the-art people from tech giants like Google, Facebook, Microsoft, etc.? That is the reason for the strength of open source based machine learning.

Among academia, there is a famous phrase, “[Standing on the shoulders of giants](https://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants)”, it means that we should thank previous research then we can go on to the next step. Even in machine learning based on open source, we can not ignore this phrase. We cannot ignore giants.
