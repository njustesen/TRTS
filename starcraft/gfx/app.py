import yaml
from flask import Flask, render_template
app = Flask(__name__, template_folder='static')


def img(name):
    return name.replace("Level 1", "").replace("Level 2", "").replace("Level 3", "").replace(" ", "") + ".png"


def num_products(item):
    produces = len(item['Produces']) if 'Produces' in item else 0
    upgrades = len(item['Upgrades']) if 'Upgrades' in item else 0
    stats = 0
    if 'Stats' in item:
        if 'Ground Damage' in item['Stats']:
            stats += 1
        if 'Air Damage' in item['Stats']:
            stats += 1
        if 'Range' in item['Stats']:
            stats += 1
        if 'Speed' in item['Stats']:
            stats += 1
    return produces + upgrades + stats


@app.route('/protoss', methods=['GET', 'POST'])
def my_form_post():
    parsed_yaml_file = yaml.load(open('data/starcraft.yaml', 'r'), Loader=yaml.FullLoader)
    return render_template('templates/index.html',
                           race='Protoss',
                           data=parsed_yaml_file,
                           img=img,
                           num_products=num_products)


if __name__ == '__main__':
    app.debug = True
    app.run()
