下载后修改app下的cofig.py文件SQLALCHEMY_DATABASE_URI
```pycon
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL', 'mysql+pymysql://root:yourpassword@localhost:3306/sensitive_word_system')
    SQLALCHEMY_ECHO = True
```
## 一
将sensitive_words_from_lvchunli.txt里的敏感词都加进来<br>
<em><b>格式</b></em><br>
<em><b>原数据</b></em><br>
[1,"“两学一做”学习教育","/[^“]两学一做[^“]|“两学一做”学习教育活动/u"]
<em><b>添加的数据格式</b></em><br>
[1,"“两学一做”学习教育","[^“]两学一做[^“]|“两学一做”学习教育活动"]
## 二
写一下admin模块里routes.py文件里的genRegex函数
## 三
对后台数据表分页显示
## 四