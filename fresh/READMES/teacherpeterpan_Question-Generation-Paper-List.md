# Question-Generation-Paper-List
A summary of must-read papers for Neural Question Generation (NQG)

- Contributed by **[Liangming Pan](http://www.liangmingpan.com)**, **[Yuxi Xie](https://yuxixie.github.io/)** and **[Yunxiang Zhang](https://github.com/yunx-z)**

Please follow [this link](./README_by_year.md) to view papers in chronological order. 

## [Content](#content)

<table>
<tr><td colspan="2"><a href="#survey-papers">1. Survey</a></td></tr> 
<tr><td colspan="2"><a href="#models">2. Models</a></td></tr>
<tr>
    <td>&emsp;<a href="#basic-seq2seq-models">2.1 Basic Seq2Seq Models</a></td>
    <td>&ensp;<a href="#encoding-answers">2.2 Encoding Answers</a></td>
</tr>
<tr>
    <td>&emsp;<a href="#linguistic-features">2.3 Linguistic Features</a></td>
    <td>&ensp;<a href="#question-specific-rewards">2.4 Question-specific Rewards</a></td>
</tr>
<tr>
    <td>&emsp;<a href="#content-selection">2.5 Content Selection</a></td>
    <td>&ensp;<a href="#question-type-modeling">2.6 Question Type Modeling</a></td>
</tr>
<tr>
    <td>&emsp;<a href="#encode-wider-contexts">2.7 Encode wider contexts</a></td>
    <td>&ensp;<a href="#qg-with-pretraining">2.8 QG with pretraining</a></td>
</tr>
<tr>
    <td>&emsp;<a href="#other-directions">2.9 Other Directions</a></td>
</tr>
<tr><td colspan="2"><a href="#applications">2. Applications</a></td></tr> 
<tr>
    <td>&emsp;<a href="#difficulty-controllable-QG">2.1 Difficulty Controllable QG</a></td>
    <td>&ensp;<a href="#conversational-QG">2.2 Conversational QG</a></td>
</tr> 
<tr>
    <td>&emsp;<a href="#asking-deep-questions">2.3 Asking Deep Questions</a></td>
    <td>&ensp;<a href="#combining-QA-and-QG">2.4 Combining QA and QG</a></td>
</tr>
<tr>
    <td>&emsp;<a href="#QG-from-knowledge-graphs">2.5 QG from knowledge graphs</a></td>
    <td>&ensp;<a href="#visual-question-generation">2.6 Visual Question Generation</a></td>
</tr> 
<tr>
    <td>&emsp;<a href="#distractor-generation">2.7 Distractor Generation</a></td>
    <td>&ensp;<a href="#cross-lingual-QG">2.8 Cross-lingual QG</a></td>
</tr>
<tr>
    <td>&emsp;<a href="#clarification-question-generation">2.9 Clarification Question Generation</a></td>
</tr>
<tr><td colspan="2"><a href="#evaluation">3. Evaluation</a></td></tr>
<tr><td colspan="2"><a href="#resources">4. Resources</a></td></tr>
</table>

## [Survey papers](#content)
1. **Recent Advances in Neural Question Generation.** arxiv, 2019. [paper](https://arxiv.org/pdf/1905.08949.pdf)
    
    *Liangming Pan, Wenqiang Lei, Tat-Seng Chua, Min-Yen Kan* 

2. **A Systematic Review of Automatic Question Generation for Educational Purposes.** International Journal of Artificial Intelligence in Education, 2020. [paper](https://link.springer.com/content/pdf/10.1007/s40593-019-00186-y.pdf)
    
    *Ghader Kurdi, Jared Leo, Bijan Parsia, Uli Sattler, Salam Al-Emari* 

## [Models](#content)   

### [Basic Seq2Seq Models](#basic-models)

Basic Seq2Seq models with attention to generate questions. 

1. **Learning to ask: Neural question generation for reading comprehension.** ACL, 2017. [paper](https://www.aclweb.org/anthology/P17-1123.pdf)

    *Xinya Du, Junru Shao, Claire Cardie.*

2. **Neural question generation from text: A preliminary study.** NLPCC, 2017. [paper](https://www.researchgate.net/profile/Franco_Scarselli/publication/4202380_A_new_model_for_earning_in_raph_domains/links/0c9605188cd580504f000000.pdf)

    *Qingyu Zhou, Nan Yang, Furu Wei, Chuanqi Tan, Hangbo Bao, Ming Zhou.*

3. **Machine comprehension by text-to-text neural question generation.** Rep4NLP@ACL, 2017. [paper](https://arxiv.org/pdf/1705.02012.pdf)
   
   *Xingdi Yuan, Tong Wang, Çaglar Gülçehre, Alessandro Sordoni, Philip Bachman, Saizheng Zhang, Sandeep Subramanian, Adam Trischler*

### [Encoding Answers](#answer-encoding)

Applying various techniques to encode the answer information thus allowing for better quality answer-focused questions. 

1. **Answer-focused and Position-aware Neural Question Generation.** EMNLP, 2018. [paper](https://www.aclweb.org/anthology/D18-1427)
   
   *Xingwu Sun, Jing Liu, Yajuan Lyu, Wei He, Yanjun Ma, Shi Wang*

2. **Improving Neural Question Generation Using Answer Separation.** AAAI, 2019. [paper](https://arxiv.org/pdf/1809.02393.pdf) [code](https://github.com/yanghoonkim/NQG_ASs2s)

    *Yanghoon Kim, Hwanhee Lee, Joongbo Shin, Kyomin Jung.*

3. **Improving Question Generation with Sentence-level Semantic Matching and Answer Position Inferring.** AAAI, 2020. [paper](https://arxiv.org/pdf/1912.00879.pdf)
   
   *Xiyao Ma, Qile Zhu, Yanlin Zhou, Xiaolin Li, Dapeng Wu*

4. **Answer-driven Deep Question Generation based on Reinforcement Learning.** COLING, 2020. [paper](https://www.aclweb.org/anthology/2020.coling-main.452/)

   *Liuyin Wang, Zihan Xu, Zibo Lin, Hai-Tao Zheng, Ying Shen*

### [Linguistic Features](#linguistic-features)

Improve QG by incorporating various linguistic features into the QG process. 

1. **Neural Generation of Diverse Questions using Answer Focus, Contextual and Linguistic Features.** INLG, 2018. [paper](https://arxiv.org/pdf/1809.02637.pdf)

    *Vrindavan Harrison, Marilyn Walker*

2. **Automatic Question Generation using Relative Pronouns and Adverbs.** ACL, 2018. [paper](https://www.aclweb.org/anthology/P18-3022)
   
   *Payal Khullar, Konigari Rachna, Mukul Hase, Manish Shrivastava* 

3. **Learning to Generate Questions by Learning What not to Generate.** WWW, 2019. [paper](https://arxiv.org/pdf/1902.10418.pdf) [code](https://github.com/BangLiu/QG)

    *Bang Liu, Mingjun Zhao, Di Niu, Kunfeng Lai, Yancheng He, Haojie Wei, Yu Xu.*

4. **Improving Neural Question Generation using World Knowledge.** arXiv, 2019. [paper](https://arxiv.org/pdf/1909.03716.pdf)
   
   *Deepak Gupta, Kaheer Suleman, Mahmoud Adada, Andrew McNamara, Justin Harris*

5. **Syn-QG: Syntactic and Shallow Semantic Rules for Question Generation.** ACL, 2020. [paper](https://arxiv.org/pdf/2004.08694.pdf)
   
   *Kaustubh D. Dhole, Christopher D. Manning*

6. **Automatically Generating Cause-and-Effect Questions from Passages.** EACL Workshop, 2021. [paper](https://www.aclweb.org/anthology/2021.bea-1.17.pdf) [codes](https://github.com/kstats/CausalQG)
    
    *Katherine Stasaski, Manav Rathod, Tony Tu, Yunfang Xiao, Marti A. Hearst*

### [Question-specific Rewards](#RL-rewards)

Improving the training via combining supervised and reinforcement learning to maximize question-specific rewards

1. **Teaching Machines to Ask Questions.** IJCAI, 2018. [paper](https://www.ijcai.org/proceedings/2018/0632.pdf)
   
   *Kaichun Yao, Libo Zhang, Tiejian Luo, Lili Tao, Yanjun Wu*

2. **Natural Question Generation with Reinforcement Learning Based Graph-to-Sequence Model** NeurIPS Workshop, 2019. [paper](https://arxiv.org/pdf/1910.08832.pdf)
   
   *Yu Chen, Lingfei Wu, Mohammed J. Zaki*

3. **Putting the Horse Before the Cart:A Generator-Evaluator Framework for Question Generation from Text** CoNLL, 2019. [paper](https://arxiv.org/pdf/1808.04961.pdf)
   
   *Vishwajeet Kumar, Ganesh Ramakrishnan, Yuan-Fang Li*

4. **Addressing Semantic Drift in Question Generation for Semi-Supervised Question Answering** EMNLP, 2019. [paper](https://arxiv.org/pdf/1909.06356.pdf) [code](https://github.com/ZhangShiyue/QGforQA)
   
   *Shiyue Zhang, Mohit Bansal*

5. **Reinforcement Learning Based Graph-to-Sequence Model for Natural Question Generation** ICLR, 2020. [paper](https://arxiv.org/pdf/1908.04942.pdf) [codes](https://github.com/hugochan/RL-based-Graph2Seq-for-NQG)
   
   *Yu Chen, Lingfei Wu, Mohammed J. Zaki*

12. **Exploring Question-Specific Rewards for Generating Deep Questions.** COLING, 2020. [paper](https://arxiv.org/pdf/2011.01102.pdf) [codes](https://github.com/YuxiXie/RL-for-Question-Generation)
    
    *Yuxi Xie, Liangming Pan, Dongzhe Wang, Min-Yen Kan, Yansong Feng*

13. **Answer-driven Deep Question Generation based on Reinforcement Learning.** COLING, 2020. [paper](https://www.aclweb.org/anthology/2020.coling-main.452/)

    *Liuyin Wang, Zihan Xu, Zibo Lin, Hai-Tao Zheng, Ying Shen*

7. **Cooperative Learning of Zero-Shot Machine Reading Comprehension.** arXiv, 2021. [paper](https://arxiv.org/pdf/2103.07449)
    
    *Hongyin Luo, Shang-Wen Li, Seunghak Yu, James Glass*

7. **Contrastive Multi-document Question Generation.** EACL, 2021. [paper](https://www.aclweb.org/anthology/2021.eacl-main.2.pdf) [codes](https://github.com/woonsangcho/contrast_qgen)
    
    *Woon Sang Cho, Yizhe Zhang, Sudha Rao, Asli Celikyilmaz, Chenyan Xiong, Jianfeng Gao, Mengdi Wang, Bill Dolan*

### [Content Selection](#content-selection)

Improve QG by considering how to select question-worthy contents (content selection) before asking a question. 

1. **Identifying Where to Focus in Reading Comprehension for Neural Question Generation.** EMNLP, 2017. [paper](https://www.aclweb.org/anthology/D17-1219.pdf)
   
   *Xinya Du, Claire Cardie*

2. **Neural Models for Key Phrase Extraction and Question Generation.** ACL Workshop, 2018. [paper](https://www.aclweb.org/anthology/W18-2609.pdf)
   
   *Sandeep Subramanian, Tong Wang, Xingdi Yuan, Saizheng Zhang, Adam Trischler, Yoshua Bengio*

3. **A Comparative Study on Question-Worthy Sentence Selection Strategies for Educational Question Generation.** AIED, 2019. [paper](https://link.springer.com/chapter/10.1007/978-3-030-23204-7_6)
   
   *Guanliang Chen, Jie Yang, Dragan Gasevic*

4. **Learning to Generate Questions by Learning What not to Generate.** WWW, 2019. [paper](https://arxiv.org/pdf/1902.10418.pdf) [code](https://github.com/BangLiu/QG)

    *Bang Liu, Mingjun Zhao, Di Niu, Kunfeng Lai, Yancheng He, Haojie Wei, Yu Xu.*

5. **Improving Question Generation With to the Point Context.** EMNLP, 2019. [paper](https://arxiv.org/pdf/1910.06036.pdf)

    *Jingjing Li, Yifan Gao, Lidong Bing, Irwin King, Michael R. Lyu.*

6. **Weak Supervision Enhanced Generative Network for Question Generation.** IJCAI, 2019. [paper](https://arxiv.org/pdf/1907.00607v1)
   
   *Yutong Wang, Jiyuan Zheng, Qijiong Liu, Zhou Zhao, Jun Xiao, Yueting Zhuang*

7. **A Multi-Agent Communication Framework for Question-Worthy Phrase Extraction and Question Generation.** AAAI, 2019. [paper](https://www.aaai.org/ojs/index.php/AAAI/article/view/4700/4578)
   
   *Siyuan Wang, Zhongyu Wei, Zhihao Fan, Yang Liu, Xuanjing Huang*

8. **Self-Attention Architectures for Answer-Agnostic Neural Question Generation.** ACL, 2019. [paper](https://www.aclweb.org/anthology/P19-1604.pdf)
   
   *Thomas Scialom, Benjamin Piwowarski, Jacopo Staiano.*

9. **Mixture Content Selection for Diverse Sequence Generation.** EMNLP, 2019. [paper](https://arxiv.org/pdf/1909.01953.pdf) [code](https://github.com/clovaai/FocusSeq2Seq)
   
   *Jaemin Cho, Minjoon Seo, Hannaneh Hajishirzi*

10. **Asking Questions the Human Way: Scalable Question-Answer Generation from Text Corpus.** WWW, 2020. [paper](https://arxiv.org/pdf/2002.00748.pdf)
    
    *Bang Liu, Haojie Wei, Di Niu, Haolan Chen, Yancheng He*

### [Question Type Modeling](#question-type-modeling)

Improve QG by explicitly modeling question types or interrogative words. 

1. **Question Generation for Question Answering.** EMNLP,2017. [paper](https://www.aclweb.org/anthology/D17-1090)
   
   *Nan Duan, Duyu Tang, Peng Chen, Ming Zhou*

2. **Answer-focused and Position-aware Neural Question Generation.** EMNLP, 2018. [paper](https://www.aclweb.org/anthology/D18-1427)
   
   *Xingwu Sun, Jing Liu, Yajuan Lyu, Wei He, Yanjun Ma, Shi Wang*

3. **Let Me Know What to Ask: Interrogative-Word-Aware Question Generation** EMNLP Workshop, 2019. [paper](https://arxiv.org/pdf/1910.13794.pdf)
   
   *Junmo Kang, Haritz Puerto San Roman, Sung-Hyon Myaeng*

4. **Question-type Driven Question Generation** EMNLP, 2019. [paper](https://arxiv.org/pdf/1909.00140.pdf)
   
   *Wenjie Zhou, Minghua Zhang, Yunfang Wu*

5. **Expanding, Retrieving and Infilling: Diversifying Cross-Domain Question Generation with Flexible Templates.** EACL, 2021. [paper](https://www.aclweb.org/anthology/2021.eacl-main.279.pdf) [codes](https://github.com/xiaojingyu92/ERIQG)
    
    *Xiaojing Yu, Anxiao Jiang*

### [Encode Wider Contexts](#encode-wider-contexts)

Improve QG by incorporating wider contexts in the input passage. 

1. **Harvesting paragraph-level question-answer pairs from wikipedia.** ACL, 2018. [paper](https://arxiv.org/pdf/1805.05942.pdf) [code&dataset](https://github.com/xinyadu/HarvestingQA)
    
    *Xinya Du, Claire Cardie*

2. **Leveraging Context Information for Natural Question Generation** ACL, 2018. [paper](https://www.aclweb.org/anthology/N18-2090) [code](https://github.com/freesunshine0316/MPQG)
   
   *Linfeng Song, Zhiguo Wang, Wael Hamza, Yue Zhang, Daniel Gildea*

3. **Paragraph-level Neural Question Generation with Maxout Pointer and Gated Self-attention Networks.** EMNLP, 2018. [paper](https://www.aclweb.org/anthology/D18-1424.pdf)
   
   *Yao Zhao, Xiaochuan Ni, Yuanyuan Ding, Qifa Ke*

4. **Capturing Greater Context for Question Generation** AAAI, 2020. [paper](https://arxiv.org/pdf/1910.10274.pdf)
   
   *Luu Anh Tuan, Darsh J Shah, Regina Barzilay*

5. **How to Ask Good Questions? Try to Leverage Paraphrases** ACL, 2020. [paper](https://www.aclweb.org/anthology/2020.acl-main.545.pdf)
   
   *Xin Jia, Wenjie Zhou, Xu SUN, Yunfang Wu*

6. **PathQG: Neural Question Generation from Facts** EMNLP, 2020. [paper](http://www.sdspeople.fudan.edu.cn/zywei/paper/2020/wangsy-emnlp-2020.pdf) [code](https://github.com/WangsyGit/PathQG)
   
   *Siyuan Wang, Zhongyu Wei, Zhihao Fan, Zengfeng Huang, Weijian Sun, Qi Zhang, Xuanjing Huang*

7. **AnswerQuest: A System for Generating Question-Answer Items from Multi-Paragraph Documents.** EACL Demo, 2021. [paper](https://arxiv.org/pdf/2103.03820.pdf) [codes](https://github.com/roemmele/answerquest)
    
    *Melissa Roemmele, Deep Sidhpura, Steve DeNeefe, Ling Tsou*

8. **OneStop QAMaker: Extract Question-Answer Pairs from Text in a One-Stop Approach.** arXiv, 2021. [paper](https://arxiv.org/pdf/2102.12128)
    
    *Shaobo Cui, Xintong Bao, Xinxing Zu, Yangyang Guo, Zhongzhou Zhao, Ji Zhang, Haiqing Chen*

9. **ASQ: Automatically Generating Question-Answer Pairs using AMRs.** arXiv, 2021. [paper](https://arxiv.org/pdf/2105.10023)
    
    *Geetanjali Rakshit, Jeffrey Flanigan*

10. **Zero-shot Fact Verification by Claim Generation.** ACL, 2021. [paper](https://arxiv.org/pdf/2105.14682) [codes](https://github.com/teacherpeterpan/Zero-shot-Fact-Verification)
    
    *Liangming Pan, Wenhu Chen, Wenhan Xiong, Min-Yen Kan, William Yang Wang*

### [QG with pretraining](#qg-with-pretraining)

Improve QG ultilizing NLP pretraining models. 

1. **Unified Language Model Pre-training for Natural Language Understanding and Generation.** NeurIPS, 2019. [paper](https://arxiv.org/pdf/1905.03197.pdf) [code](https://github.com/microsoft/unilm)
   
   *Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jianfeng Gao, Ming Zhou, Hsiao-Wuen Hon*

2. **A Recurrent BERT-based Model for Question Generation.** MRQA Workshop, 2019. [paper](https://www.aclweb.org/anthology/D19-5821.pdf)

   *Ying-Hong Chan, Yao-Chung Fan*

3. **CopyBERT: A Unified Approach to Question Generation with Self-Attention.** ACL Workshop, 2020. [paper](https://www.aclweb.org/anthology/2020.nlp4convai-1.3.pdf) [code](https://github.com/StalVars/CopyBERT)

   *Stalin Varanasi, Saadullah Amin, Guenter Neumann*

4. **QURIOUS: Question Generation Pretraining for Text Generation.** arXiv, 2020. [paper](https://arxiv.org/pdf/2004.11026.pdf)
   
   *Shashi Narayan, Gonçalo Simoes, Ji Ma, Hannah Craighead, Ryan Mcdonald*

5. **UniLMv2: Pseudo-Masked Language Models for Unified Language Model Pre-Training.** arXiv, 2020. [paper](https://arxiv.org/pdf/2002.12804.pdf) [code](https://github.com/microsoft/unilm/tree/master/unilm)
   
   *Hangbo Bao, Li Dong, Furu Wei, Wenhui Wang, Nan Yang, Xiaodong Liu, Yu Wang, Songhao Piao, Jianfeng Gao, Ming Zhou, Hsiao-Wuen Hon*

### [Other Directions](#other-model)

1. **Generating Question-Answer Hierarchies.** ACL, 2019. [paper](https://arxiv.org/pdf/1906.02622.pdf) [code](http://squash.cs.umass.edu/)
   
   *Kalpesh Krishna and Mohit Iyyer.*

2. **Can You Unpack That? Learning to Rewrite Questions-in-Context.** EMNLP, 2019. [paper](https://www.aclweb.org/anthology/D19-1605.pdf)
   
   *Ahmed Elgohary, Denis Peskov, Jordan L. Boyd-Graber*

3. **Sequential Copying Networks.** AAAI, 2018. [paper](https://arxiv.org/pdf/1807.02301.pdf)
   
   *Qingyu Zhou, Nan Yang, Furu Wei, Ming Zhou*

4. **Let's Ask Again: Refine Network for Automatic Question Generation.** EMNLP, 2019. [paper](https://www.aclweb.org/anthology/D19-1326.pdf)
   
   *Preksha Nema, Akash Kumar Mohankumar, Mitesh M. Khapra, Balaji Vasan Srinivasan, Balaraman Ravindran*

## [Applications](#applications)

### [Difficulty Controllable QG](#difficulty-controllable-QG)

Endowing the model with the ability to control the difficulty of the generated questions. 

1. **Easy-to-Hard: Leveraging Simple Questions for Complex Question Generation.** arxiv, 2019. [paper](https://arxiv.org/pdf/1912.02367.pdf)

    *Jie Zhao, Xiang Deng, Huan Sun.*

2. **Difficulty Controllable Generation of Reading Comprehension Questions.** IJCAI, 2019. [paper](https://www.ijcai.org/proceedings/2019/0690.pdf)
   
   *Yifan Gao, Lidong Bing, Wang Chen, Michael R. Lyu, Irwin King* 

3. **Difficulty-controllable Multi-hop Question Generation From Knowledge Graphs.** ISWC, 2019. [paper](https://arxiv.org/pdf/1807.03586.pdf)  [code&dataset](https://github.com/liyuanfang/mhqg)
   
   *Vishwajeet Kumar, Yuncheng Hua, Ganesh Ramakrishnan, Guilin Qi, Lianli Gao, Yuan-Fang Li*

4. **Guiding the Growth: Difficulty-Controllable Question Generation through Step-by-Step Rewriting.** ACL, 2021. [paper](https://arxiv.org/pdf/2105.11698) [codes](https://tinyurl.com/19esunzz)
    
    *Yi Cheng, Siyao Li, Bang Liu, Ruihui Zhao, Sujian Li, Chenghua Lin, Yefeng Zheng*

### [Conversational QG](#conversational-QG)

Learning to generate a series of coherent questions grounded in a question answering style conversation. 

1. **Learning to Ask Questions in Open-domain Conversational Systems with Typed Decoders.** ACL, 2018. [paper](https://arxiv.org/pdf/1805.04843.pdf) [code](https://github.com/victorywys/Learning2Ask_TypedDecoder) [dataset]( http://coai.cs.tsinghua.edu.cn/hml/dataset/)
   
   *Yansen Wang, Chenyi Liu, Minlie Huang, Liqiang Nie*

2. **Answerer in Questioner's Mind: Information Theoretic Approach to Goal-Oriented Visual Dialog.** NIPS, 2018. [paper](https://arxiv.org/pdf/1802.03881.pdf)

   *Sang-Woo Lee, Yu-Jung Heo, Byoung-Tak Zhang*

3. **Interconnected Question Generation with Coreference Alignment and Conversation Flow Modeling.** ACL, 2019. [paper](https://arxiv.org/pdf/1906.06893.pdf) [code](https://github.com/Evan-Gao/conversational-QG)
   
   *Yifan Gao, Piji Li, Irwin King, Michael R. Lyu*

4. **Reinforced Dynamic Reasoning for Conversational Question Generation.** ACL, 2019. [paper](https://www.aclweb.org/anthology/P19-1203) [code](https://github.com/ZJULearning/ReDR) [dataset](https://stanfordnlp.github.io/coqa/)
   
   *Boyuan Pan, Hao Li, Ziyu Yao, Deng Cai, Huan Sun*

5. **Towards Answer-unaware Conversational Question Generation.** ACL Workshop, 2019. [paper](https://www.aclweb.org/anthology/D19-5809.pdf)
   
   *Mao Nakanishi, Tetsunori Kobayashi, Yoshihiko Hayashi*

6. **What Should I Ask? Using Conversationally Informative Rewards for Goal-oriented Visual Dialog.** ACL, 2019. [paper](https://www.aclweb.org/anthology/P19-1646.pdf)
   
   *Pushkar Shukla, Carlos Elmadjian, Richika Sharan, Vivek Kulkarni, Matthew Turk, William Yang Wang*

7. **Visual Dialogue State Tracking for Question Generation.** AAAI, 2020. [paper](https://arxiv.org/pdf/1911.07928.pdf)
   
   *Wei Pang, Xiaojie Wang*

7. **Interactive Classification by Asking Informative Questions.** ACL, 2020. [paper](https://arxiv.org/pdf/1911.03598.pdf)
   
   *Lili Yu, Howard Chen, Sida Wang, Tao Lei, Yoav Artzi*

7. **Learning to Ask More: Semi-Autoregressive Sequential Question Generation under Dual-Graph Interaction.** ACL, 2020. [paper](https://www.aclweb.org/anthology/2020.acl-main.21.pdf) [dataset](https://github.com/ChaiZ-pku/Sequential-QG)
   
   *Zi Chai, Xiaojun Wan*

8. **Stay Hungry, Stay Focused: Generating Informative and Specific Questions in Information-Seeking Conversations.** EMNLP, 2020. [paper](https://arxiv.org/pdf/2004.14530.pdf) [codes](https://github.com/qipeng/stay-hungry-stay-focused)
   
   *Peng Qi, Yuhao Zhang, Christopher D. Manning*

7. **ChainCQG: Flow-Aware Conversational Question Generation.** EACL, 2021. [paper](https://arxiv.org/pdf/2102.02864.pdf) [codes](https://github.com/searchableai/ChainCQG)
    
    *Jing Gu, Mostafa Mirshekari, Zhou Yu, Aaron Sisto*

### [Asking Deep Questions](#asking-deep-questions)

This direction focuses on exploring how to ask deep questions that require high cognitive levels, such as multi-hop reasoning questions, mathematical questions, open-ended questions, and non-factoid questions. 

1. **Automatic Opinion Question Generation.** ICNLG, 2018. [paper](https://www.aclweb.org/anthology/W18-6518.pdf)
   
   *Yllias Chali, Tina Baghaee* 

3. **A Multi-language Platform for Generating Algebraic Mathematical Word Problems.** arxiv, 2019. [paper](https://arxiv.org/pdf/1912.01110.pdf)
   
   *Vijini Liyanage, Surangika Ranathunga*

6. **Asking the Crowd: Question Analysis, Evaluation and Generation for Open Discussion on Online Forums.** ACL, 2019. [paper](https://www.aclweb.org/anthology/P19-1497.pdf)
   
   *Zi Chai, Xinyu Xing, Xiaojun Wan, Bo Huang*

7. **Learning to Ask Unanswerable Questions for Machine Reading Comprehension.** ACL, 2019. [paper](https://www.aclweb.org/anthology/P19-1415.pdf)
   
   *Haichao Zhu, Li Dong, Furu Wei, Wenhui Wang, Bing Qin, Ting Liu*

8. **Distant Supervised Why-Question Generation with Passage Self-Matching Attention.** IJCNN, 2019. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8851781)
   
   *Jiaxin Hu, Zhixu Li, Renshou Wu, Hongling Wang, An Liu, Jiajie Xu, Pengpeng Zhao, Lei Zhao*

9. **Conclusion-Supplement Answer Generation for Non-Factoid Questions.** AAAI, 2020. [paper](https://arxiv.org/pdf/1912.00864.pdf)
   
   *Makoto Nakatsuji, Sohei Okui*

9. **Generating Multi-hop Reasoning Questions to Improve Machine Reading Comprehension.** WWW, 2020. [paper](https://dl.acm.org/doi/pdf/10.1145/3366423.3380114)
   
   *Jianxing Yu, Xiaojun Quan, Qinliang Su, Jian Yin*

10. **Low-Resource Generation of Multi-hop Reasoning Questions.** ACL, 2020. [paper](https://www.aclweb.org/anthology/2020.acl-main.601.pdf)
    
    *Jianxing Yu, Wei Liu, Shuang Qiu, Qinliang Su, Kai Wang, Xiaojun Quan, Jian Yin*

11. **Semantic Graphs for Generating Deep Questions.** ACL, 2020. [paper](https://arxiv.org/pdf/2004.12704.pdf) [code](https://github.com/YuxiXie/SG-Deep-Question-Generation)
    
    *Liangming Pan, Yuxi Xie, Yansong Feng, Tat-Seng Chua, Min-Yen Kan*

12. **Review-based Question Generation with Adaptive Instance Transfer and Augmentation.** ACL, 2020. [paper](https://www.aclweb.org/anthology/2020.acl-main.26.pdf)
    
    *Qian Yu, Lidong Bing, Qiong Zhang, Wai Lam, Luo Si*

12. **Inquisitive Question Generation for High Level Text Comprehension.** EMNLP, 2020. [paper](https://arxiv.org/pdf/2010.01657.pdf) [dataset](https://github.com/wjko2/INQUISITIVE)
    
    *Wei-Jen Ko, Te-Yuan Chen, Yiyan Huang, Greg Durrett, Junyi Jessy Li*

12. **Stronger Transformers for Neural Multi-Hop Question Generation.** ArXiv, 2020. [paper](https://arxiv.org/pdf/2010.11374.pdf)
    
    *Devendra Singh Sachan, Lingfei Wu, Mrinmaya Sachan, William Hamilton*

12. **Mathematical Word Problem Generation from Commonsense Knowledge Graph and Equations.** ArXiv, 2020. [paper](https://arxiv.org/pdf/2010.06196.pdf)
    
    *Tianqiao Liu, Qian Fang, Wenbiao Ding, Zhongqin Wu, Zitao Liu*

12. **Reinforced Multi-task Approach for Multi-hop Question Generation.** COLING, 2020. [paper](https://arxiv.org/pdf/2004.02143.pdf)
    
    *Deepak Gupta, Hardik Chauhan, Akella Ravi Tej, Asif Ekbal, Pushpak Bhattacharyya*

12. **Exploring Question-Specific Rewards for Generating Deep Questions.** COLING, 2020. [paper](https://arxiv.org/pdf/2011.01102.pdf) [codes](https://github.com/YuxiXie/RL-for-Question-Generation)
    
    *Yuxi Xie, Liangming Pan, Dongzhe Wang, Min-Yen Kan, Yansong Feng*

12. **Ask to Learn: A Study on Curiosity-driven Question Generation.** COLING, 2020. [paper](https://arxiv.org/pdf/1911.03350.pdf) [codes](https://github.com/YuxiXie/RL-for-Question-Generation)
    
    *Thomas Scialom, Jacopo Staiano*

12. **EQG-RACE: Examination-Type Question Generation.** AAAI, 2021. [paper](https://arxiv.org/pdf/2012.06106.pdf)
    
    *Xin Jia, Wenjie Zhou, Xu Sun, Yunfang Wu*

12. **CliniQG4QA: Generating Diverse Questions for Domain Adaptation of Clinical Question Answering.** NeurIPS Workshop, 2021. [paper](https://arxiv.org/pdf/2010.16021.pdf) [codes](https://github.com/sunlab-osu/CliniQG4QA)
    
    *Xiang Yue, Xinliang Frederick Zhang, Ziyu Yao, Simon Lin, Huan Sun*

7. **Quiz-Style Question Generation for News Stories.** WWW, 2021. [paper](https://arxiv.org/pdf/2102.09094.pdf) [codes](https://github.com/google-research-datasets/NewsQuizQA)
    
    *Adam D. Lelkes, Vinh Q. Tran, Cong Yu*

7. **Back-Training excels Self-Training at Unsupervised Domain Adaptation of Question Generation and Passage Retrieval.** arXiv, 2021. [paper](https://arxiv.org/pdf/2104.08801)
    
    *Devang Kulshreshtha, Robert Belfer, Iulian Vlad Serban, Siva Reddy*

7. **Contrastive Multi-document Question Generation.** EACL, 2021. [paper](https://www.aclweb.org/anthology/2021.eacl-main.2.pdf) [codes](https://github.com/woonsangcho/contrast_qgen)
    
    *Woon Sang Cho, Yizhe Zhang, Sudha Rao, Asli Celikyilmaz, Chenyan Xiong, Jianfeng Gao, Mengdi Wang, Bill Dolan*

### [Combining QA and QG](#Combining-QA-and-QG)

This direction investigate how to combine the task of QA and QG by multi-task learning or joint training. 

1. **Question Generation for Question Answering.** EMNLP,2017. [paper](https://www.aclweb.org/anthology/D17-1090)
   
   *Nan Duan, Duyu Tang, Peng Chen, Ming Zhou*

2. **Learning to Collaborate for Question Answering and Asking.** NAACL, 2018. [paper](https://www.aclweb.org/anthology/N18-1141)
   
   *Duyu Tang, Nan Duan, Zhao Yan, Zhirui Zhang, Yibo Sun, Shujie Liu, Yuanhua Lv, Ming Zhou*

3. **Generating Highly Relevant Questions.** EMNLP, 2019. [paper](https://arxiv.org/abs/1910.03401)
   
   *Jiazuo Qiu, Deyi Xiong*

4. **Learning to Answer by Learning to Ask: Getting the Best of GPT-2 and BERT Worlds.** arxiv, 2019. [paper](https://arxiv.org/pdf/1911.02365.pdf)
   
   *Tassilo Klein, Moin Nabi*

5. **Triple-Joint Modeling for Question Generation Using Cross-Task Autoencoder.** NLPCC, 2019. [paper](https://link.springer.com/chapter/10.1007/978-3-030-32236-6_26)
   
   *Hongling Wang, Renshou Wu, Zhixu Li, Zhongqing Wang, Zhigang Chen, Guodong Zhou*

6. **Addressing Semantic Drift in Question Generation for Semi-Supervised Question Answering** EMNLP, 2019. [paper](https://arxiv.org/pdf/1909.06356.pdf) [code](https://github.com/ZhangShiyue/QGforQA)
   
   *Shiyue Zhang, Mohit Bansal*

7. **Synthetic QA Corpora Generation with Roundtrip Consistency** ACL, 2019. [paper](https://arxiv.org/pdf/1906.05416.pdf)
   
   *Chris Alberti, Daniel Andor, Emily Pitler, Jacob Devlin, Michael Collins*

7. **Unsupervised Question Answering by Cloze Translation** ACL, 2019. [paper](https://www.aclweb.org/anthology/P19-1484.pdf)
   
   *Patrick Lewis, Ludovic Denoyer, Sebastian Riedel*

9. **Generating Multi-hop Reasoning Questions to Improve Machine Reading Comprehension.** WWW, 2020. [paper](https://dl.acm.org/doi/pdf/10.1145/3366423.3380114)
   
   *Jianxing Yu, Xiaojun Quan, Qinliang Su, Jian Yin*

9. **Template-Based Question Generation from Retrieved Sentences for Improved Unsupervised Question Answering.** ACL, 2020. [paper](https://arxiv.org/pdf/2004.11892.pdf)
   
   *Alexander R. Fabbri, Patrick Ng, Zhiguo Wang, Ramesh Nallapati, Bing Xiang*

9. **On the Importance of Diversity in Question Generation for QA.** ACL, 2020. [paper](https://www.aclweb.org/anthology/2020.acl-main.500.pdf)
   
   *Md Arafat Sultan, Shubham Chandel, Ramón Fernandez Astudillo, Vittorio Castelli*

9. **End-to-End Synthetic Data Generation for Domain Adaptation of Question Answering Systems.** EMNLP, 2020. [paper](https://arxiv.org/pdf/2010.06028.pdf)
   
   *Siamak Shakeri, Cicero Nogueira dos Santos, Henry Zhu, Patrick Ng, Feng Nan, Zhiguo Wang, Ramesh Nallapati, Bing Xiang*

9. **Tell Me How to Ask Again: Question Data Augmentation with Controllable Rewriting in Continuous Space.** EMNLP, 2020. [paper](https://arxiv.org/pdf/2010.01475.pdf)
   
   *Dayiheng Liu, Yeyun Gong, Jie Fu, Yu Yan, Jiusheng Chen, Jiancheng Lv, Nan Duan, Ming Zhou*

9. **Training Question Answering Models From Synthetic Data.** EMNLP, 2020. [paper](https://arxiv.org/pdf/2002.09599.pdf)
   
   *Raul Puri, Ryan Spring, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro*

7. **Unsupervised Multi-hop Question Answering by Question Generation.** NAACL, 2021. [paper](https://arxiv.org/pdf/2010.12623.pdf)
    
    *Liangming Pan, Wenhu Chen, Wenhan Xiong, Min-Yen Kan, William Yang Wang*

7. **Data-QuestEval: A Referenceless Metric for Data to Text Semantic Evaluation.** arXiv, 2021. [paper](https://arxiv.org/pdf/2104.07555)
    
    *Clément Rebuffel, Thomas Scialom, Laure Soulier, Benjamin Piwowarski, Sylvain Lamprier, Jacopo Staiano, Geoffrey Scoutheeten, Patrick Gallinari*

7. **Q2: Evaluating Factual Consistency in Knowledge-Grounded Dialogues via Question Generation and Question Answering** arXiv, 2021. [paper](https://arxiv.org/pdf/2104.08202)
    
    *Or Honovich, Leshem Choshen, Roee Aharoni, Ella Neeman, Idan Szpektor, Omri Abend*

7. **Improving Question Answering Model Robustness with Synthetic Adversarial Data Generation** arXiv, 2021. [paper](https://arxiv.org/pdf/2104.08678)
    
    *Max Bartolo, Tristan Thrush, Robin Jia, Sebastian Riedel, Pontus Stenetorp, Douwe Kiela*

7. **Cooperative Learning of Zero-Shot Machine Reading Comprehension.** arXiv, 2021. [paper](https://arxiv.org/pdf/2103.07449)
    
    *Hongyin Luo, Shang-Wen Li, Seunghak Yu, James Glass*

7. **Progressively Pretrained Dense Corpus Index for Open-Domain Question Answering.** EACL, 2021. [paper](https://www.aclweb.org/anthology/2021.eacl-main.244.pdf) [codes](https://github.com/xwhan/ProQA.git)
    
    *Wenhan Xiong, Hong Wang, William Yang Wang*

7. **Text Modular Networks: Learning to Decompose Tasks in the Language of Existing Models.** NAACL, 2021. [paper](https://www.aclweb.org/anthology/2021.naacl-main.99.pdf) [codes](https://github.com/allenai/modularqa)
    
    *Tushar Khot, Daniel Khashabi, Kyle Richardson, Peter Clark, Ashish Sabharwal*

### [QG from knowledge graphs](#QG-from-knowledge-graphs)

This direction is about generating questions from a knowledge graph. 

1. **Generating Factoid Questions With Recurrent Neural Networks: The 30M Factoid Question-Answer Corpus.** ACL, 2016. [paper](https://arxiv.org/pdf/1603.06807.pdf) [dataset](https://www.agarciaduran.org)
   
   *Iulian Vlad Serban, Alberto García-Durán, Çaglar Gülçehre, Sungjin Ahn, Sarath Chandar, Aaron C. Courville, Yoshua Bengio*

2. **Generating Natural Language Question-Answer Pairs from a Knowledge Graph Using a RNN Based Question Generation Model.** ACL, 2017. [paper](https://www.aclweb.org/anthology/E17-1036/)
   
   *Mitesh M. Khapra, Dinesh Raghu, Sachindra Joshi, Sathish Reddy*

3. **Knowledge Questions from Knowledge Graphs.** ICTIR, 2017. [paper](https://arxiv.org/pdf/1610.09935.pdf)
   
   *Dominic Seyler, Mohamed Yahya, Klaus Berberich.*

4. **Zero-Shot Question Generation from Knowledge Graphs for Unseen Predicates and Entity Types.** NAACL, 2018. [paper](https://arxiv.org/pdf/1802.06842.pdf) [code](https://github.com/NAACL2018Anonymous/submission)
   
   *Hady Elsahar, Christophe Gravier, Frederique Laforest.*

5. **A Neural Question Generation System Based on Knowledge Base** NLPCC, 2018. [paper](https://link.springer.com/chapter/10.1007/978-3-319-99495-6_12)
   
   *Hao Wang, Xiaodong Zhang, Houfeng Wang*

6. **Formal Query Generation for Question Answering over Knowledge Bases.** ESWC, 2018. [paper](https://link.springer.com/chapter/10.1007/978-3-319-93417-4_46)
   
   *Hamid Zafar, Giulio Napolitano, Jens Lehmann*

7. **Generating Questions for Knowledge Bases via Incorporating Diversified Contexts and Answer-Aware Loss.** EMNLP, 2019. [paper](https://www.aclweb.org/anthology/D19-1247.pdf)
   
   *Cao Liu, Kang Liu, Shizhu He, Zaiqing Nie, Jun Zhao*

8. **Difficulty-controllable Multi-hop Question Generation From Knowledge Graphs.** ISWC, 2019. [paper](https://arxiv.org/pdf/1807.03586.pdf)  [code&dataset](https://github.com/liyuanfang/mhqg)
   
   *Vishwajeet Kumar, Yuncheng Hua, Ganesh Ramakrishnan, Guilin Qi, Lianli Gao, Yuan-Fang Li*

9.  **How Question Generation Can Help Question Answering over Knowledge Base.** NLPCC, 2019. [paper](http://tcci.ccf.org.cn/conference/2019/papers/183.pdf)
    
    *Sen Hu, Lei Zou, Zhanxing Zhu*

10.  **Toward Subgraph Guided Knowledge Graph Question Generation with Graph Neural Networks.** arXiv, 2020. [paper](https://arxiv.org/pdf/2004.06015.pdf)

      *Yu Chen, Lingfei Wu, Mohammed J. Zaki*

11.  **Generating Semantically Valid Adversarial Questions for TableQA.** arXiv, 2020. [paper](https://arxiv.org/pdf/2005.12696.pdf)

      *Yi Zhu, Menglin Xia, Yiwei Zhou*

12. **Knowledge-enriched, Type-constrained and Grammar-guided Question Generation over Knowledge Bases.** COLING, 2020. [paper](https://arxiv.org/pdf/2010.03157.pdf)
    
    *Sheng Bi, Xiya Cheng, Yuan-Fang Li, Yongzhen Wang, Guilin Qi*


### [Visual Question Generation](#visual-question-generation)

Asking questions based on visual inputs (usually an image). 

1. **Generating Natural Questions About an Image** ACL, 2016. [paper](https://arxiv.org/pdf/1603.06059.pdf)
   
   *Nasrin Mostafazadeh, Ishan Misra, Jacob Devlin, Margaret Mitchell, Xiaodong He, Lucy Vanderwende*

2. **Creativity: Generating Diverse Questions Using Variational Autoencoders** CVPR,2017. [paper](https://arxiv.org/pdf/1704.03493.pdf)
   
   *Unnat Jain, Ziyu Zhang, Alexander G. Schwing*

3. **Automatic Generation of Grounded Visual Questions** IJCAI, 2017. [paper](https://www.ijcai.org/proceedings/2017/0592.pdf)
   
   *Shijie Zhang, Lizhen Qu, Shaodi You, Zhenglu Yang, Jiawan Zhang*

4. **A Reinforcement Learning Framework for Natural Question Generation using Bi-discriminators** COLING, 2018. [paper](https://www.aclweb.org/anthology/C18-1150.pdf)
   
   *Zhihao Fan, Zhongyu Wei, Siyuan Wang, Yang Liu, Xuanjing Huang*

5. **Customized Image Narrative Generation via Interactive Visual Question Generation and Answering** CVPR, 2018. [paper](https://arxiv.org/pdf/1805.00460.pdf)
   
   *Andrew Shin, Yoshitaka Ushiku, Tatsuya Harada*

6. **Multimodal Differential Network for Visual Question Generation** EMNLP, 2018. [paper](https://www.aclweb.org/anthology/D18-1434.pdf)
   
   *Badri Narayana Patro, Sandeep Kumar, Vinod Kumar Kurmi, Vinay P. Namboodiri*

7. **A Question Type Driven Framework to Diversify Visual Question Generation** IJCAI, 2018. [paper](http://www.sdspeople.fudan.edu.cn/zywei/paper/fan-ijcai2018.pdf)
   
   *Zhihao Fan, Zhongyu Wei, Piji Li, Yanyan Lan, Xuanjing Huang*

8. **Visual Question Generation as Dual Task of Visual Question Answering.** CVPR, 2018. [paper](http://openaccess.thecvf.com/content_cvpr_2018/papers/Li_Visual_Question_Generation_CVPR_2018_paper.pdf)
   
   *Yikang Li, Nan Duan, Bolei Zhou, Xiao Chu, Wanli Ouyang, Xiaogang Wang, Ming Zhou* 

9. **Two can play this Game: Visual Dialog with Discriminative Question Generation and Answering.** CVPR, 2018. [paper](https://arxiv.org/pdf/1803.11186.pdf)
   
   *Unnat Jain, Svetlana Lazebnik, Alexander Schwing*

10. **Information Maximizing Visual Question Generation.** CVPR, 2019. [paper](https://arxiv.org/pdf/1903.11207.pdf)
    
    *Ranjay Krishna, Michael Bernstein, Li Fei-Fei*

11. **What Should I Ask? Using Conversationally Informative Rewards for Goal-oriented Visual Dialog.** ACL, 2019. [paper](https://www.aclweb.org/anthology/P19-1646.pdf)
    
    *Pushkar Shukla, Carlos Elmadjian, Richika Sharan, Vivek Kulkarni, Matthew Turk, William Yang Wang*

### [Distractor Generation](#distractor-generation)

Learning to generate distractors for multi-choice questions. 

1. **Generating Questions and Multiple-Choice Answers using Semantic Analysis of Texts.** COLING, 2016. [paper](https://www.aclweb.org/anthology/C16-1107.pdf)

   *Jun Araki, Dheeraj Rajagopal, Sreecharan Sankaranarayanan, Susan Holm, Yukari Yamakawa, Teruko Mitamura*

2. **Distractor Generation for Multiple Choice Questions Using Learning to Rank.** NAACL Workshop, 2018. [paper](https://www.aclweb.org/anthology/W18-0533.pdf) [code](https://github.com/harrylclc/LTR-DG)

   *Chen Liang, Xiao Yang, Neisarg Dave, Drew Wham, Bart Pursel, C. Lee Giles*

3. **Generating Distractors for Reading Comprehension Questions from Real Examinations.** AAAI, 2019. [paper](https://arxiv.org/pdf/1809.02768.pdf)

   *Yifan Gao, Lidong Bing, Piji Li, Irwin King, Michael R. Lyu*

4. **Knowledge-Driven Distractor Generation for Cloze-style Multiple Choice Questions.** AAAI, 2021. [paper](https://arxiv.org/pdf/2004.09853.pdf)
    
    *Siyu Ren, Kenny Q. Zhu*

### [Cross-lingual QG](#cross-lingual-QG)

Building cross-lingual models to generate questions in low-resource languages. 

1. **Cross-Lingual Training for Automatic Question Generation.** ACL, 2019. [paper](https://arxiv.org/pdf/1906.02525.pdf) [dataset](https://www.cse.iitb.ac.in/~ganesh/HiQuAD/clqg/)
   
   *Vishwajeet Kumar, Nitish Joshi, Arijit Mukherjee, Ganesh Ramakrishnan, Preethi Jyothi*

2. **Cross-Lingual Natural Language Generation via Pre-Training.** AAAI, 2020. [paper](https://arxiv.org/pdf/1909.10481.pdf)

   *Zewen Chi, Li Dong, Furu Wei, Wenhui Wang, Xian-Ling Mao, Heyan Huang*

7. **Quinductor: a multilingual data-driven method for generating reading-comprehension questions using Universal Dependencies.** arXiv, 2021. [paper](https://arxiv.org/pdf/2103.10121) [codes](https://github.com/dkalpakchi/quinductor)
    
    *Dmytro Kalpakchi, Johan Boye*

### [Clarification Question Generation](#clarification-question-generation)

Learning to ask clarification questions to better understand user intents in conversation, recommendation system, or search engine. 

1. **Are You Asking the Right Questions? Teaching Machines to Ask Clarification Questions.** ACL Workshop, 2017. [paper](https://www.aclweb.org/anthology/P17-3006.pdf)
   
   *Sudha Rao*

2. **Learning to Ask Good Questions: Ranking Clarification Questions using Neural Expected Value of Perfect Information.** ACL, 2018. [paper](https://arxiv.org/pdf/1805.04655.pdf) [code](https://github.com/raosudha89/ranking_clarification_questions)
   
   *Sudha Rao, Hal Daumé III*

1. **Interpretation of Natural Language Rules in Conversational Machine Reading.** EMNLP, 2018. [paper](https://arxiv.org/pdf/1809.01494.pdf) [dataset](https://sharc-data.github.io/)
   
   *Marzieh Saeidi, Max Bartolo, Patrick Lewis, Sameer Singh, Tim Rocktäschel, Mike Sheldon, Guillaume Bouchard, Sebastian Riedel*

1. **Answer-based Adversarial Training for Generating Clarification Questions.** NAACL, 2019. [paper](https://arxiv.org/pdf/1904.02281.pdf) [code](https://github.com/raosudha89/clarification_question_generation_pytorch)
   
   *Rao S, Daumé III H.*

2. **Asking Clarifying Questions in Open-Domain Information-Seeking Conversations.** SIGIR, 2019. [paper](https://dl.acm.org/doi/pdf/10.1145/3331184.3331265) [dataset](https://github.com/aliannejadi/qulac)
   
   *Mohammad Aliannejadi, Hamed Zamani, Fabio Crestani, W. Bruce Croft*


2. **Asking Clarification Questions in Knowledge-Based Question Answering.** EMNLP, 2019. [paper](https://www.aclweb.org/anthology/D19-1172.pdf) [dataset](https://github.com/msra-nlc/MSParS_V2.0)
   
   *Jingjing Xu, Yuechen Wang, Duyu Tang, Nan Duan, Pengcheng Yang, Qi Zeng, Ming Zhou, Xu Sun*


1. **ClarQ: A large-scale and diverse dataset for Clarification Question Generation.** ACL, 2020. [paper](https://www.aclweb.org/anthology/2020.acl-main.651.pdf) [dataset](https://github.com/vaibhav4595/ClarQ)
   
   *Vaibhav Kumar, Alan W. black.*

2. **Interactive Classification by Asking Informative Questions.** ACL, 2020. [paper](https://arxiv.org/pdf/1911.03598.pdf)
   
   *Lili Yu, Howard Chen, Sida Wang, Tao Lei, Yoav Artzi*

2. **Towards Question-based Recommender Systems.** SIGIR, 2020. [paper](https://arxiv.org/pdf/2005.14255.pdf)
   
   *Jie Zou, Yifan Chen, Evangelos Kanoulas*

2. **Generating Clarifying Questions for Information Retrieval.** WWW, 2020. [paper](http://hamedz.ir/assets/pub/zamani-www2020.pdf)
   
   *Hamed Zamani, Susan T. Dumais, Nick Craswell, Paul N. Bennett, and Gord Lueck*

7. **Diverse and Specific Clarification Question Generation with Keywords** WWW, 2021. [paper](https://arxiv.org/pdf/2104.10317) [codes](https://github.com/blmoistawinde/KPCNet)
    
    *Zhiling Zhang, Kenny Q. Zhu*

7. **Data Augmentation with Hierarchical SQL-to-Question Generation for Cross-domain Text-to-SQL Parsing** arXiv, 2021. [paper](https://arxiv.org/pdf/2103.02227)
    
    *Ao Zhang, Kun Wu, Lijie Wang, Zhenghua Li, Xinyan Xiao, Hua Wu, Min Zhang, Haifeng Wang*

7. **Learning to Ask Appropriate Questions in Conversational Recommendation** SIGIR, 2021. [paper](https://arxiv.org/pdf/2105.04774) [codes](https://github.com/XuhuiRen/KBQG)
    
    *Xuhui Ren, Hongzhi Yin, Tong Chen, Hao Wang, Zi Huang, Kai Zheng*

7. **Ask whats missing and whats useful: Improving Clarification Question Generation using Global Knowledge.** NAACL, 2021. [paper](https://www.aclweb.org/anthology/2021.naacl-main.340.pdf) [codes](https://github.com/microsoft/clarification-qgen-globalinfo)
    
    *Bodhisattwa Prasad Majumder, Sudha Rao, Michel Galley, Julian McAuley*

## [Evaluation](#evaluation)

This direction investigates the mechanism behind question asking, and how to evaluate the quality of generated questions. 

1. **Question Asking as Program Generation.** NeurIPS, 2017. [paper](https://arxiv.org/pdf/1711.06351.pdf)
   
   *Anselm Rothe, Brenden M. Lake, Todd M. Gureckis.*

2. **Towards a Better Metric for Evaluating Question Generation Systems.** EMNLP, 2018. [paper](https://www.aclweb.org/anthology/D18-1429/)
   
   *Preksha Nema, Mitesh M. Khapra.*

3. **Evaluating Rewards for Question Generation Models.** NAACL, 2019. [paper](https://arxiv.org/pdf/1902.11049.pdf)
   
   *Tom Hosking and Sebastian Riedel.*

## [Resources](#resources)

QG-specific datasets and toolkits. 

1. **LearningQ: A Large-Scale Dataset for Educational Question Generation.** ICWSM, 2018. [paper](https://yangjiera.github.io/works/icwsm2018.pdf)
   
   *Guanliang Chen, Jie Yang, Claudia Hauff, Geert-Jan Houben.*

2. **ParaQG: A System for Generating Questions and Answers from Paragraphs.** EMNLP Demo, 2019. [paper](https://arxiv.org/pdf/1909.01642.pdf)
   
   *Vishwajeet Kumar, Sivaanandh Muneeswaran, Ganesh Ramakrishnan, Yuan-Fang Li.*

3. **How to Ask Better Questions? A Large-Scale Multi-Domain Dataset for Rewriting Ill-Formed Questions.** AAAI, 2020. [paper](https://arxiv.org/pdf/1911.09247.pdf) [code](https://github.com/ZeweiChu/MQR)
   
   *Zewei Chu, Mingda Chen, Jing Chen, Miaosen Wang, Kevin Gimpel, Manaal Faruqui, Xiance Si.*

3. **ClarQ: A large-scale and diverse dataset for Clarification Question Generation.** ACL, 2020. [paper](https://www.aclweb.org/anthology/2020.acl-main.651.pdf) [dataset](https://github.com/vaibhav4595/ClarQ)
   
   *Vaibhav Kumar, Alan W. black.*

3. [Toolkit] **Question Generation using transformers** . [github link](https://github.com/patil-suraj/question_generation)
   
   *Suraj Patil*

12. **Inquisitive Question Generation for High Level Text Comprehension.** EMNLP, 2020. [paper](https://arxiv.org/pdf/2010.01657.pdf) [dataset](https://github.com/wjko2/INQUISITIVE)
    
    *Wei-Jen Ko, Te-Yuan Chen, Yiyan Huang, Greg Durrett, Junyi Jessy Li*

7. **Quiz-Style Question Generation for News Stories.** WWW, 2021. [paper](https://arxiv.org/pdf/2102.09094.pdf) [codes](https://github.com/google-research-datasets/NewsQuizQA)
    
    *Adam D. Lelkes, Vinh Q. Tran, Cong Yu*

7. **Back-Training excels Self-Training at Unsupervised Domain Adaptation of Question Generation and Passage Retrieval.** arXiv, 2021. [paper](https://arxiv.org/pdf/2104.08801)
    
    *Devang Kulshreshtha, Robert Belfer, Iulian Vlad Serban, Siva Reddy*

6. **Automatically Generating Cause-and-Effect Questions from Passages.** EACL Workshop, 2021. [paper](https://www.aclweb.org/anthology/2021.bea-1.17.pdf) [codes](https://github.com/kstats/CausalQG)
    
    *Katherine Stasaski, Manav Rathod, Tony Tu, Yunfang Xiao, Marti A. Hearst*

