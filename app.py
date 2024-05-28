import os

from flask import Flask, render_template
from mongoengine import fields, Document, connect, DynamicDocument

app = Flask(__name__, template_folder="templates")

app.config["MONGODB_SETTINGS"] = {
    "db": "association_prod",
    "host": os.getenv("MONGODB_HOST"),
}
connect(**app.config["MONGODB_SETTINGS"])


class Rules(Document):
    store_id = fields.IntField()
    store_description_en = fields.StringField()
    area = fields.IntField()
    segment_en = fields.StringField()
    antecedent = fields.ListField(fields.StringField())
    consequent = fields.ListField(fields.StringField())
    confidence = fields.FloatField()
    lift = fields.FloatField()
    support = fields.FloatField()


class ItemSets(Document):
    store_id = fields.IntField()
    store_description_en = fields.StringField()
    area = fields.IntField()
    segment_en = fields.StringField()
    items = fields.ListField(fields.StringField())
    freq = fields.ListField(fields.IntField())


@app.route("/")
def home():
    return render_template(
        'home.html',
        title="Home"
    )


@app.route('/rules')
def rules():
    rules = Rules.objects()
    return render_template(
        'rules.html',
        title='Rules Table',
        rules=rules
    )


@app.route('/item-sets')
def item_sets():
    item_sets = ItemSets.objects()
    return render_template(
        'item_sets.html',
        title='Item Sets Table',
        item_sets=item_sets
    )


if __name__ == '__main__':
    app.run(debug=True, port=5050)
