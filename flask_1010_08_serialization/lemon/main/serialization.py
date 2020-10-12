from marshmallow import post_load, fields, ValidationError, validates

from lemon.extensions import ma
from lemon.main import models

# class UserSchema(ma.Schema):
#     username = fields.str()


class EnvsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # 和那个 ORM 模型绑定
        model = models.Envs
        # 是否包含外键
        include_fk = True


class ProjectsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Projects
        include_fk = True

    name = fields.String()

    @validates("name")
    def unique(self, data):
        project = models.Projects.query.filter_by(name=data).first()
        if project:
            raise ValidationError('project name must be unique')

    @post_load
    def to_orm(self, json, **kw):
        project = models.Projects(**json)
        project.save()
        return project


class InterfacesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Interfaces
        include_fk = True


class ConfiguresSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Configures
        include_fk = True


class DebugTalksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.DebugTalks
        include_fk = True


class ReportsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Reports
        include_fk = True


class SummarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Summary
        include_fk = True


class TestcasesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Testcases
        include_fk = True


class TestsuitsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Testsuits
        include_fk = True







