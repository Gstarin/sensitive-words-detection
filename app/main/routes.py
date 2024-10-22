from flask import render_template, request, redirect, url_for, flash, jsonify
from . import main_bp
from ..models import Word
from ..extensions import db

@main_bp.route('/')
def index():
    return render_template('index.html')