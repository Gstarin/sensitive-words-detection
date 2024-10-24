from flask import render_template, request, redirect, url_for, flash, jsonify
from . import admin_bp  # 从 app/admin/__init__.py 中导入 admin_bp
from ..models import Word#引用models.py中的Word函数
from ..extensions import db
from .forms import WordForm
from ..trie import Trie, TrieNode

trie = Trie()
# 管理员首页路由
@admin_bp.route('/')
def index():
    # 创建用于添加和更新敏感词的表单实例
    addForm = WordForm()  # 用于添加新敏感词的表单
    updateForm = WordForm()  # 用于更新已有敏感词的表单
    words = Word.query.all()  # 查询所有敏感词
    # 将数据库中的敏感词插入到Trie中
    trie.root = TrieNode()  # 重新初始化Trie，避免重复插入
    for word in words:
        trie.insert(word.word)  # 将每个敏感词插入到Trie中
    return render_template("admin.html", words=words, addForm=addForm, updateForm=updateForm)  # 渲染模板，将敏感词数据和表单传递给前端

# 添加敏感词的路由
@admin_bp.route('add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # 创建一个新敏感词实例，使用表单中的数据
        new_word = Word(
            word=request.form.get('word'),  # 从表单获取敏感词文本
            regex=request.form.get('regex'),  # 从表单获取正则表达式
            type=request.form.get('type'),  # 从表单获取敏感词的类型
        )
        # 将新词添加到数据库会话中
        db.session.add(new_word)
        try:
            db.session.commit()  # 提交数据库会话，将新词保存到数据库中
            flash('敏感词添加成功！', 'success')  # 如果成功，显示提示信息
        except Exception as e:
            db.session.rollback()  # 如果出现错误，回滚事务
            flash('敏感词添加失败，请重试。', 'danger')  # 显示错误提示信息
    return redirect(url_for('admin.index'))  # 重定向到管理员首页

# 更新敏感词的路由
@admin_bp.route('update/<word_id>', methods=['POST'])
def update(word_id):
    data = request.get_json()  # 从请求中获取 JSON 数据
    print(data.get('type'))  # 打印获取的数据类型字段，用于调试
    word = Word.query.get_or_404(word_id)  # 根据 ID 获取敏感词对象，如果找不到则返回 404 错误
    if not data:
        return jsonify({'success': False, 'message': '没有收到数据'}), 400  # 如果数据为空，返回错误响应

    try:
        # 更新敏感词的属性，如果数据中未提供新值则保留原值
        word.word = data.get('word', word.word)
        word.regex = data.get('regex', word.regex)
        word.type = data.get('type', word.type)

        # 提交到数据库，保存更新
        db.session.commit()
        return jsonify({'success': True, 'message': '敏感词更新成功！'})  # 返回成功响应

    except Exception as e:
        db.session.rollback()  # 如果更新失败，回滚数据库事务
        return jsonify({'success': False, 'message': str(e)}), 500  # 返回错误响应，包含错误信息

# 删除敏感词的路由
@admin_bp.route('delete/<word_id>', methods=['DELETE'])
def delete(word_id):
    delete_word = Word.query.get_or_404(word_id)  # 根据 ID 获取敏感词对象，如果找不到则返回 404 错误
    try:
        db.session.delete(delete_word)  # 从数据库会话中删除敏感词对象
        db.session.commit()  # 提交删除操作到数据库
        return {"status": "success", "message": "敏感词删除成功"}  # 返回成功消息
    except:
        db.session.rollback()  # 如果删除失败，回滚事务
    return {"status": "error", "message": "敏感词删除失败"}  # 返回错误消息

# 搜索敏感词的路由（尚未实现）
@admin_bp.route('/search', methods=['GET', 'POST'])
def search():
    # 创建表单实例
    addForm = WordForm()
    updateForm = WordForm()

    # 用于存储查询结果
    words = []

    if request.method == 'POST':
        # 从表单中获取输入的文本
        text = request.form.get('text')
        if not text:
            flash('没有收到搜索文本', 'danger')
            return redirect(url_for('admin.index'))

        # 假设存在 trie 的敏感词查找功能（如未提供具体实现）
        found_words = trie.search(text) if trie else []
        if found_words:
            flash('发现敏感词！', 'success')
        else:
            flash('未发现敏感词', 'info')
    elif request.method == 'GET':
        # 从导航栏中获取查询参数
        query = request.args.get('query')
        if query:
            # 查询数据库中与敏感词或正则表达式匹配的条目
            words = Word.query.filter(
                (Word.word.ilike(f"%{query}%")) |
                (Word.regex.ilike(f"%{query}%"))
            ).all()

            if words:
                flash('搜索到相关敏感词', 'success')
            else:
                flash('没有找到相关敏感词', 'info')

    # 渲染模板，确保传递 addForm、updateForm 和查询结果 words
    return render_template("admin.html", words=words, addForm=addForm, updateForm=updateForm)