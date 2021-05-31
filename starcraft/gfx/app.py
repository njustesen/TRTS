import yaml
from flask import Flask, render_template
app = Flask(__name__, template_folder='static')


def img(name):
    return name.replace(" ", "") + ".png"


def num_products(building):
    produces = len(building['Produces']) if 'Produces' in building else 0
    upgrades = len(building['Upgrades']) if 'Upgrades' in building else 0
    return produces + upgrades


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
