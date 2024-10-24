from .extensions import db


# 定义 Word 模型类，映射到数据库中的 'words' 表
class Word(db.Model):
    __tablename__ = 'words'  # 定义表名为 'words'

    # 定义表的字段
    id = db.Column(db.Integer, primary_key=True)  # id 字段，主键，自增整数
    word = db.Column(db.String(250), nullable=False)  # word 字段，存储敏感词，最大长度为 250，不能为空
    regex = db.Column(db.UnicodeText, nullable=False)  # regex 字段，存储正则表达式，不能为空
    type = db.Column(db.Integer, nullable=False)  # type 字段，存储敏感词的类型，用整数表示，不能为空

    # 定义对象的字符串表示，用于调试和日志输出
    def __repr__(self):
        return '<Word %r>' % self.word  # 返回 Word 对象的字符串形式，显示 word 的值