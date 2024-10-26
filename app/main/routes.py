from flask import render_template, request, redirect, url_for, flash, jsonify
from . import main_bp
from ..models import Word
from ..extensions import db


@main_bp.route('/')
def index():
    words = Word.query.all()
    regex_patterns = [word.regex for word in words]  # 提取所有正则表达式
    return render_template('index.html',regex_patterns=regex_patterns)

