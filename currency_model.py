from tortoise import Model, fields


class Currency(Model):
    id = fields.IntField(pk=True)
    currency = fields.TextField()
    price = fields.FloatField()
