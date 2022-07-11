from uuid import uuid4
from flask import Blueprint, request
from model import User
from common import R

url_prefix = 'user'
bp = Blueprint(url_prefix, __name__, url_prefix=f'/{url_prefix}')


@bp.route('/find', methods=['POST'])
def find():
    user = User.find_by_id(id=request.json["id"])
    return R.success("查询成功", user)


@bp.route('/insert', methods=['POST'])
def insert():
    user = User.insert(request.json)
    return R.success("新增成功", user)


@bp.route('/delete', methods=['POST'])
def delete():
    res = User.delete_by_id(id=request.json["id"])
    return R.success("删除成功", res)


@bp.route('/update', methods=['POST'])
def update():
    user = User(**request.json)
    res = user.update()
    return R.success("修改成功", res)


@bp.route('/register', methods=['POST'])
def register():
    user = User(**request.json)
    # b, err = user.insert()
    # print(b)

    user1 = User().find_by_id(user.id)
    print(user1)

    # username = request.json['username']
    # password = request.json['password']

    # if not username:
    #     return R.error("username is required")
    # if not password:
    #     return R.error("password is required")
    return R.success("注册成功", request.json)


@bp.route('/upload', methods=['POST'])
def upload():
    support_file_types = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    f = request.files['file']
    file_type = f.filename.split('.')[-1]
    if file_type in support_file_types:
        file_name = str(uuid4())
        file_name = file_name + "." + file_type
        file_path = f'/static/images/{file_name}'
        f.save("." + file_path)
        return R.success("文件上传成功", file_path)
    else:
        return R.error("未知的文件类型")
