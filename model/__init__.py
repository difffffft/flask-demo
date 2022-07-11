import json
from typing import Union
from flask import jsonify
from db import db


# 基础模型
class Base(db.Model):
    __abstract__ = True

    """
    作用:
        每张表都应该有一个跟业务无关的主键自增
    名称:
        id
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    """
    作用:
        将模型对象映射成字典
    """

    @classmethod
    def to_dict(cls, obj):
        d = dict()
        for c in cls.__table__.columns:
            v = getattr(obj, c.name)
            d[c.name] = v
        return d

    # 新增一条数据
    @classmethod
    def insert(cls, data):
        obj = cls(**data)
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
        return cls.to_dict(obj)

    # 物理删除一条数据
    @classmethod
    def delete_by_id(cls, id: Union[int, str] = None):
        res = True
        try:
            db.session.query(cls).filter(cls.id == id).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
        return res

    # 修改一条数据
    def update(self):
        # res = True
        try:
            obj = db.session.query(self.__class__).get(self.id)
            for k in obj:
                obj[k] = self[k]

            # obj.update(cls.to_dict(obj))
            # db.session.commit()
        except Exception as e:
            # db.session.rollback()
            raise e
        finally:
            pass
            # db.session.close()
        return "res"

    # 根据id查询
    @classmethod
    def find_by_id(cls, id: Union[int, str] = None):
        try:
            obj = db.session.query(cls).get(id)
        except Exception as e:
            raise e
        finally:
            db.session.close()
        return cls.to_dict(obj)


# 用户表
class User(Base):
    __tablename__ = 'user'
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    boy = db.Column(db.Boolean, default=True)


#
# db.drop_all()
db.create_all()
