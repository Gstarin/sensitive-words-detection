from flask import render_template, request, redirect, url_for, flash, jsonify
from . import admin_bp
from ..models import Word
from ..extensions import db
from .forms import WordForm


@admin_bp.route('/')
def index():
    addForm = WordForm()
    updateForm = WordForm()
    words = Word.query.all()
    return render_template("admin.html", words=words, addForm=addForm, updateForm=updateForm)


@admin_bp.route('add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":

        new_word = Word(
            word=request.form.get('word'),
            regex=request.form.get('regex'),
            type=request.form.get('type'),
        )
        # 根据 word 生成两个新的正则表达式
        regex1 = f"\\b{new_word.word}\\b"  # 匹配完整单词
        regex2 = f"{new_word.word}.*"  # 匹配以 word 开头的字符串


        new_regex = regex1 + '|' + regex2


        if(new_word.regex == ""):
            new_word.regex = genRegex(new_regex)

        # add to db.session
        db.session.add(new_word)
        try:
            db.session.commit()
            flash('敏感词添加成功！', 'success')
        except Exception as e:
            db.session.rollback()
            flash('敏感词添加失败。', 'danger')
    return redirect(url_for('admin.index'))


@admin_bp.route('update/<word_id>', methods=['POST'])
def update(word_id):
    data = request.get_json()  # 从请求中获取 JSON 数据
    print(data.get('type'))
    word = Word.query.get_or_404(word_id)
    if not data:
        return jsonify({'success': False, 'message': '没有收到数据'}), 400

    try:
        # 更新敏感词的属性
        word.word = data.get('word', word.word)
        word.regex = data.get('regex', word.regex)
        word.type = data.get('type', word.type)

        # 提交到数据库
        db.session.commit()
        return jsonify({'success': True, 'message': '敏感词更新成功！'})

    except Exception as e:
        db.session.rollback()  # 如果更新失败，回滚数据库事务
        return jsonify({'success': False, 'message': str(e)}), 500


@admin_bp.route('delete/<word_id>', methods=['DELETE'])
def delete(word_id):
    delete_word = Word.query.get_or_404(word_id)
    try:
        db.session.delete(delete_word)
        db.session.commit()
        return {"status": "success", "message": "敏感词删除成功"}
    except:
        db.session.rollback()

    return {"status": "error", "message": "敏感词删除失败"}


@admin_bp.route('/search/<word_id>', methods=['GET', 'POST'])
def search(word_id):
    pass

def genRegex(word):
    return word
