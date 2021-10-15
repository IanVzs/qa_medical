# qa_medical

## 项目介绍
此前在一家医疗AI公司工作辞职后也心心念念里面的一些功能想去使用,在Github上看见[QASystemOnMedicalKG](https://github.com/liuhuanyong/QASystemOnMedicalKG)很感兴趣.于是开始学习.很有启发.

不过该项目年久失修,研读后实现方式也较为原始,所以准备重写一遍，使之可以工具化,予众人以便利.

在项目初期,为了使功能可用,我会保持原作者的代码. 预计功能迭代五次之后会将原作者代码全部摒弃.这也是为什么新开一个仓库的原因.
再次表示感谢.

## 项目运行方式
详参`Makefile`

### docker
TODO
### python
需要自行配置`Neo4j`图数据库.
复制`config.json.template`为`config.json`再根据自身需求修改`config.json`文件内容.
#### 第一次运行
```bash
make init
make run
```
#### 后续
只`make run`即可