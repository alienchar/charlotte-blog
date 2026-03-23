---
title: "AI真的要攻克癌症了吗？"
date: 2026-03-15
description: "\"澳洲程序员，零生物学背景，*用ChatGPT和AlphaFold从头设计mRNA癌症疫苗，救了自己的狗*。\"。"
tags: ["AI", "mRNA", "AlphaFold", "ChatGPT", "fact-check"]
keywords: ["AI", "mRNA", "AlphaFold", "ChatGPT", "fact-check"]
images: ["/images/cover.png"]
readingTime: 7
slug: "ai-cancer"
cover: '/images/Pasted_image_20260315194354.png'
images: ['/images/Pasted_image_20260315194354.png']
---这两天，我的X时间线被一条推文刷屏了。

"澳洲程序员，零生物学背景，*用ChatGPT和AlphaFold从头设计mRNA癌症疫苗，救了自己的狗*。"

七万多转赞，八百万浏览。

**Demis Hassabis**亲自转发说"This is just the beginning of digital biology"。Greg Brockman也转了。
![](/images/Pasted_image_20260315194354.png)
说实话，我看到的时候也被击中了。一个人，一条狗，两个AI工具，对抗**癌症**。

但我这个人有个毛病——越是好听的故事，越想扒一扒细节。

所以今天这篇，我不打算复述那条病毒式推文。我要做的是：拉出原始报道，一条一条对着看看，哪些是真的，哪些被简化了，哪些是传播过程中被悄悄放大的。这到底是——怎么个一回事儿？

## 故事本身

![配图1](/images/illustration-2.png)

先说事情经过。这部分是真的，而且确实动人。

Paul Conyngham，澳洲悉尼人，2019年从动物收容所收养了一只叫Rosie的杂交犬——Staffy和沙皮的混血。五年后，Rosie确诊癌症。化疗、传统治疗都试过了，没用。
![](/images/Pasted_image_20260315204047.png)
然后Paul决定自己动手。

他花了3000澳元（约14000人民币），在UNSW Ramaciotti基因组中心给Rosie做了肿瘤DNA测序。拿到数据之后，他用ChatGPT制定分析计划，用AlphaFold预测突变蛋白质结构，匹配药物靶点。

他自己的比喻挺好懂的："*就像把车的原始引擎和跑了30万公里的引擎对比，看哪里有损坏*。"

基因组中心的Smith副教授后来回忆说："Paul was relentless. 他打电话告诉我，他已经分析了数据，找到了突变，用AlphaFold预测了蛋白质结构，还匹配了潜在靶点和药物。我当时的反应是——'Woah, that's crazy!'"
![](/images/Pasted_image_20260315204152.png)
之后，UNSW RNA Institute的Páll Thordarson教授团队根据Paul的蓝图，制造了定制mRNA疫苗。注射在Gatton实验室完成，Allavena教授负责。

12月第一针，上个月第二针，下周第三针。

Allavena教授说："It's definitely working. Rosie的癌症已经非常晚期了，但有一个肿瘤缩小了很多——大概缩了一半。"

到这里，故事是真的。而且确实了不起。

## 但推文讲的和原文不太一样

![配图2](/images/illustration-3.png)

好，现在开始fact check。

这件事最大的传播源是X上一个叫@IterIntellectus的账号，17.5万粉，发了条greentext格式的推文，拿了将近8万赞、808万浏览。DeepMind的AGI政策负责人@sebkrier也发了8500赞的版本。

但仔细对比原文（The Australian，记者Natasha Bita，3月13日报道），几个关键差异必须指出来。

**第一，"零生物学背景"——对，但不完全对。**

推文说Paul是"zero background in biology"。生物学背景确实没有。但Paul有**17年的机器学习和数据分析经验**。他是个tech boss，不是路人甲。

这个区别很重要。一个有17年ML经验的人，用ChatGPT辅助分析基因组数据，和一个纯小白从零开始，是两码事。他知道怎么提问，知道怎么验证AI的输出，知道数据分析的基本逻辑。

推文把这个背景抹掉了，故事变得更戏剧化——但也更失真。

**第二，"从头设计疫苗"——他设计的是蓝图，不是疫苗本身。**

推文说"design from scratch"。原文的说法是"create the blueprint"。

实际上，mRNA疫苗是UNSW RNA Institute的Thordarson教授团队制造的。合成、制备、质量控制——这些都是专业实验室的活。Paul做的是上游分析：找突变、预测蛋白结构、设计靶点。

这不是贬低Paul的贡献。但"一个人用AI做了疫苗"和"一个人用AI做了疫苗设计的上游分析，然后找了顶尖大学团队来制造"，是完全不同的叙事。

**第三，"碾压了整个制药行业"——原文没这么说。**

推文里有一句"outperformed the entire pharmaceutical discovery pipeline"。这是推文作者自己的演绎。原文里完全没有这个说法。

Paul自己的原话是："The red tape was actually harder than the vaccine creation."——他说的是*伦理审批流程比疫苗设计更难*，每晚花两小时，折腾了三个月，写了100页文件。

这句话被传播链忽略了。因为"填了三个月表格"不够热血。

**第四，"probably halved"——教授措辞非常谨慎。**

Allavena教授说的是"probably halved"——"大概缩了一半"。这是一个科学家该有的措辞。但到了推文传播链里，你感受到的语气更接近"治愈了"。

Paul自己怎么说的？

"I'm under no illusion that this is a cure, but I do believe this treatment has bought Rosie significantly more time and quality of life."

他很清楚，这不是治愈。他说的是*争取了更多时间和生活质量*。

这句话是整个故事里最重要的一句——但在传播链里几乎没人引用。

## 那这件事到底说明了什么

冷静下来看，这件事真正值得讨论的不是"AI万能"。更加不是“AI马上就要攻克癌症”。

是这么几点：

**AI工具确实在降低某些领域的入门门槛。** 一个没有生物学训练的ML工程师，能够用ChatGPT和AlphaFold完成基因组分析的上游环节——找突变、预测蛋白结构、匹配靶点。这在五年前是不可想象的。

**但"降低门槛"不等于"消除门槛"。** 疫苗还是得专业团队造。伦理审批还是得三个月。Paul能做到这件事，是因为他同时满足了几个条件：17年技术功底、资金能力（测序3000澳元）、知道去找谁合作、以及——说实话——超常的执行力和毅力。

**传播链总是会简化故事。** "一个人用AI救了狗"比"一个有17年经验的ML工程师用AI做了疫苗设计的上游分析，然后找了大学教授团队制造，肿瘤大概缩了一半，他自己说这不是治愈"好传播一百倍。但前者是一个神话，后者是*一个真实的、复杂的、仍然了不起的故事*。

我更喜欢后者。

因为后者告诉你的是：AI不是魔法棒，但如果你有*足够的技术基础、足够的执行力、和足够的运气*——它可以成为一个真正有用的工具。

Paul还在研制第二种疫苗，针对Rosie剩余的肿瘤。

Rosie还活着。

这就够了。

![](/images/Pasted_image_20260315204436.png)
---

感谢观看。
