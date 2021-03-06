###  Learn-Pytorch-And-Become-A-Data-Scientist
### 《学好Pytorch成为数据科学家》书籍代码
###  请扫描关注，图书微信公众号。
![avatar](gongzhonghao.jpg)
### 图书目录
```
第1章  初识Pytorch	11
```
- 1.1  AI发展简史	12
    - 1.1.1  神经网络的前世今生	12
    - 1.1.2  深度学习框架对比	13
- 1.2  环境安装	16
    - 1.2.1 Python版本选择及安装	16
    - 1.2.2 安装Pytorch1.2稳定版	18
    - 1.2.3 开发环境IDE	19
- 1.3  Pytorch核心概念	20
    - 1.3.1基本概念	20
    - 1.3.2自动微分	24
    - 1.3.3 Pytorch核心模块	26
- 1.4 实验室小试牛刀	27
    - 1.4.1塔珀自指公式	27
    - 1.4.2看看你毕业了能拿多少	28
- 1.5 课后加油站高等数学知识回顾	43
    - 1.5.1 函数与导数	43
    - 1.5.2 偏导数及梯度	47
```
第2章 机器学习基础及常见概念	50
```
- 2.1 机器学习的分类	51
    - 2.1.1 监督学习	51
    - 2.1.2 半监督学习	52
    - 2.1.3 无监督学习	52
    - 2.1.4 强化学习	53
- 2.2 机器学习常见概念	54
    - 2.2.1 缺失值处理	54
    - 2.2.2 数据标准化与正则化	56
    - 2.2.3 交叉验证	58
    - 2.2.4 过拟合和欠拟合	60
- 2.3 神经网络	61
    - 2.3.1 神经网络的生理学发现与编程模拟	61
    - 2.3.2 人工神经网络的核心思想	67
    - 2.3.3 人工神经网络与逻辑斯蒂之间的关联	68
- 2.4实现线性回归和逻辑回归	68
     - 2.4.1 Pytorch实现线性回归	68
     - 2.4.2 Pytorch实现多项式回归	70
     - 2.4.3 Pytorch实现类逻辑回归	73
- 2.5 加油站高等数学知识回顾	77
    - 2.5.1 方向导数和梯度	77
    - 2.5.2 微分及积分	79
    - 2.5.3 牛顿-莱布尼兹公式	82
```
第3章 Pytorch与科学计算	83
```
- 3.1 算子字典	83
    - 3.1.1 基本方法	83
    - 3.1.2 索引·切片·连接·换位	85
    - 3.1.3 随机抽样	89
    - 3.1.4 数据持久化与高并发	90
    - 3.1.5 元素级别数学计算	91
    - 3.1.6 规约计算	94
    - 3.1.7 数值比较运算	96
    - 3.1.8 矩阵运算	98
- 3.2 广播机制	101
    - 3.2.1 自动广播规则	101
    - 3.2.2 广播结果结算规则	102
- 3.3 GPU及并行编程	103
    - 3.3.1 device和cuda基本用法	103
    - 3.3.2 CPU到GPU	104
    - 3.3.3 固定缓冲区	106
    - 3.3.4 自动设备感知	107
    - 3.3.5 并发编程	108
- 3.4 实验室小试牛刀之轻松搞定图片分类	110
    - 3.4.1 Softmax分类简介	113
    - 3.4.2 定义网络结构	115
- 3.5 加油站高等数学知识回顾	120
    - 3.5.1 泰勒公式及思想	121
    - 3.5.2 拉格朗日乘子法及思想	124
```
第4章 激活函数、损失函数、优化器及数据加载	125
```    
- 4.1 激活函数	126
    - 4.1.1 Sigmoid	126
    - 4.1.2 Tanh	128
    - 4.1.3 Relu及其变形	129
    - 4.1.4 MaxOut	132
- 4.2 损失函数	133
    - 4.2.1 L1范数损失	134
    - 4.2.2 MSE均方误差损失	134
    - 4.2.3 BCE二分类交叉熵损失	135 
    - 4.2.4 CrossEntropyLoss和NLLLoss计算交叉熵损失	135
    - 4.2.5 KL散度损失	136
    - 4.2.6 余弦相似度损失	137
    - 4.2.7 多分类多标签损失	138
- 4.3 优化器	139
    - 4.3.1 BGD	139
    - 4.3.2 SGD	139
    - 4.3.3 MBGD	140
    - 4.3.4 Momentum	141
    - 4.3.5 NAG	142
    - 4.3.6 Adagrad	143
    - 4.3.7 Adadelta	143
    - 4.3.8 Adam	144
- 4.4 数据加载	145
    - 4.4.1 Dataset数据集	145
    - 4.4.2 DataLoader数据加载	148
- 4.5 初探卷积神经网络	149
    - 4.5.1 知识科普：卷积过程及物理意义	149
    - 4.5.2 卷积神经网络CNN	153
    - 4.5.3 stride和padding	158
    - 4.5.4 膨胀卷积神经网络	159
    - 4.5.5 Pooling池化	161
- 4.6 实验室小试牛刀	164
    - 4.6.1 设计卷积神经网络	164
    - 4.6.2 定义卷积网络	164
    - 4.6.3 训练模型	165
    - 4.6.4 理解CNN在学什么	168
```
第5章 Pytorch深度神经网络	177
```
- 5.1 计算机视觉工具包	177
- 5.2 训练过程的可视化	179
    - 5.2.1 Tensorboard	179
    - 5.2.2 Visdom	184
- 5.3 深度神经网络	186
    - 5.3.1 LeNet	187 
    - 5.3.2 AlexNet	188
    - 5.3.3 ZF-Net	190
    - 5.3.4 VGG-Nets	191
    - 5.3.5 GoogLeNet	194
    - 5.3.6 ResNet	196
    - 5.3.7 DenseNet	197
- 5.4 RNN循环神经网络	199
    - 5.4.1 RNN	199
    - 5.4.2 LSTM	203
    - 5.4.3 GRU	207
- 5.5 实验室小试牛刀	209
    - 5.5.1 数据准备	209
    - 5.5.2 GRU网络设计	211
    - 5.5.3 训练模型	212
    - 5.5.4 模型预测	213
- 5.6 加油站之概率论基础知识回顾	214
    - 5.6.1 离散型随机变量和连续型随机变量	214
    - 5.6.2 概率论常用概念	219
    - 5.6.3 二维随机变量	220
    - 5.6.4 边缘分布	223
    - 5.6.5 期望和方差	224
    - 5.6.6 大数定理	225
    - 5.6.7 马尔科夫不等式及切比雪夫不等式	226
    - 5.6.8 中心极限定理	227
```
第6章 自然语言处理	227
```
- 6.1 自然语言基础	227
    - 6.1.1 自然语言发展史	228
    - 6.1.2 自然语言处理中的常见任务	230
    - 6.1.3 统计自然语言理论	232
    - 6.1.4 隐马尔可夫模型实现中文分词	240
- 6.2 关键字提取	242
    - 6.2.1 TF-IDF	243
    - 6.2.2 TextRank	244
    - 6.2.3 主题模型	245
- 6.3 Word2vec和词嵌入	246
    - 6.3.1 N-Gram模型	246
    - 6.3.2 词袋模型	247
    - 6.3.3 Word2vec词向量的密集表示	248
    - 6.3.4 使用Word2vec生成词向量	255
    - 6.3.5 Word2vec源码调试	256
    - 6.3.6 Pytorch中使用词向量	256
- 6.4 变长序列处理	258
    - 6.4.1 pack_padded_sequence压缩	259
    - 6.4.2 pad_packed_sequence解压缩	261
- 6.5 Encoder-Decoder框架和注意力机制	262
    - 6.5.1 Encoder-Decoder框架	262
    - 6.5.2 Attention Mechanism注意力机制	263
- 6.6 实验室小试牛刀对话机器人	266
    - 6.6.1 中文对话语料	266
    - 6.6.2 构建问答词典	267
    - 6.6.3 DataLoader数据加载	268
    - 6.6.4 Encoder双向多层GRU	271
    - 6.6.5 Attention注意力机制	272
    - 6.6.6 Decoder多层GRU	273
    - 6.6.7 模型训练	274
    - 6.6.8 答案搜索及效果展示	276
- 6.7 加油站之常见的几种概率分布	277
    - 6.7.1 二项分布	277
    - 6.7.2 正态分布	278
    - 6.7.3 均匀分布	279
    - 6.7.4 泊松分布	280
    - 6.7.5 卡方分布	282
    - 6.7.6 Beta分布	283
```
第7章 自然语言的曙光预训练模型	284
```
- 7.1 预训练模型的应用	285
- 7.2 从Word Embedding到ELMO	286
    - 7.2.1 Word Embedding头上的乌云	286
    - 7.2.2 ELMO	286
- 7.3 从ELMO到GPT	288
    - 7.3.1 GPT模型	288
    - 7.3.2 使用GPT模型	289
- 7.4 从GPT到BERT	291
```
第8章 自然语言处理利器AllenNLP	295
```
- 8.1 中文词性标注	295
    - 8.1.1 DatasetReader数据读取	295
    - 8.1.2 定义Model模型	297
    - 8.1.3 训练模型	298
    - 8.1.4 模型预测	300
    - 8.1.5 保存和加载模型	300
- 8.2 AllenNLP 使用Config Files	301
    - 8.2.1 参数解析	301
    - 8.2.2 注册数据读取器和模型	301
    - 8.2.3 定义Jsonnet配置文件	302
    - 8.2.4 命令行工具	303
    - 8.2.5 特征融合	304
    - 8.2.6 制作在线Demo	306
```
第9章 FastAI高层深度学习框架	307
```
- 9.1 FastAI框架中的原语	307
- 9.2 FastAI框架中使用BERT完成中文分类	308
    - 9.2.1 分词器	308
    - 9.2.2 定义字典	309
    - 9.2.3 数据准备	310
    - 9.2.4 构建Databunch和Learner	311
    - 9.2.5 开始训练	312
    - 9.2.6 模型保存和加载	313
    - 9.2.7 模型预测	313
    - 9.2.8 制作Rest接口提供服务	313
```
第10章 Pytorch Big Graph大型图嵌入	314
```
- 10.1 Pytorch Big Graph简介	315
    - 10.1.1 PBG模型	315
    - 10.1.2 模型的表示	316
    - 10.1.3 正负样本及损失函数	317
    - 10.1.4 分布式训练	317
    - 10.1.5 批量负采样	318
- 10.2 PBG实践应用	319
    - 10.2.1 模型配置文件	320
    - 10.2.2 划分训练集和测试集	321
    - 10.2.3 模型训练和验证	322
    - 10.2.4 图嵌入向量及应用	323


