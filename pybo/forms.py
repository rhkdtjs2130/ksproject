from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired("제목은 필수로 입력 해주셔야 합니다.")])
    content = TextAreaField('내용', validators=[DataRequired("내용은 필수로 입력 해주셔야 합니다.")])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired("내용은 필수 항목 입니다.")])

class UserCreateForm(FlaskForm):
    username = StringField('사용자 이름', validators=[DataRequired("사용자 이름을 입력하세요."), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired("비밀번호를 입력하세요."), EqualTo('password2','비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired("비밀번호 확인을 입력 하세요.")])
    email = EmailField('이메일', validators=[DataRequired("이메일주소를 입력 하세요."), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])