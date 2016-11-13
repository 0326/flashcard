# FlashCard+
初衷：编程需要软技能，也需要硬知识，计算机基础/算法/编程语言/快捷键 很多东西不仅需要理解，还需要记忆。FlashCard+ 以FlashCard + 卡牌游戏的形式记录和学习编程相关知识, 帮助巩固学习这些硬知识。

## 前端上手
[Vue.js 2](https://cn.vuejs.org/v2/api/) + [vue-material](https://marcosmoura.github.io/vue-material/#/).

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

## 后端上手
Python 2.7 + [Flask 0.11](http://docs.jinkan.org/docs/flask) + mysql
### 本地开发
```bash
# install dependencies
cd server
virtualenv venv
pip install Flask

# start server
python src/start.py
```

### 服务部署
部署到AWS Elastic Beanstalk：参考：[Deploying a Flask Application to AWS Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)

```bash
cd server/flask-server
# Initialize your EB CLI repository with the eb init command:
eb init -p python2.7 flask-flashcard
# Configure a default keypair so that you can connect to the EC2 instance
eb init
# Create an environment and deploy your application to it with eb create:
eb create flask-env
# Open your web site，like http://flask-env.nmnkpedtwk.us-west-2.elasticbeanstalk.com/
eb open
# Terminate your Elastic Beanstalk environment
eb terminate flask-env
```
初始化部署之后，后面再有代码变更，直接`eb deploy`部署即可。

## Change Log
