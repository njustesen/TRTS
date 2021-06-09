import yaml
from flask import Flask, render_template
app = Flask(__name__, template_folder='static')


def img(name):
    return name.replace("Level 1", "").replace("Level 2", "").replace("Level 3", "").replace(" ", "") + ".png"


def level_requirements(requirements):
    reqs = {}
    for level, level_reqs in requirements.items():
        existing_key = None
        for l, r in reqs.items():
            if level_reqs == r:
                existing_key = l
        if existing_key is None:
            reqs[str(level)] = level_reqs
        else:
            reqs[l + '+' + str(level)] = level_reqs
            del reqs[existing_key]
    return reqs


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
def protoss():
    parsed_yaml_file = yaml.load(open('data/starcraft.yaml', 'r'), Loader=yaml.FullLoader)
    return render_template('templates/index.html',
                           race='Protoss',
                           data=parsed_yaml_file,
                           img=img,
                           num_products=num_products,
                           level_requirements=level_requirements)


@app.route('/terran', methods=['GET', 'POST'])
def terran():
    parsed_yaml_file = yaml.load(open('data/starcraft.yaml', 'r'), Loader=yaml.FullLoader)
    return render_template('templates/index.html',
                           race='Terran',
                           data=parsed_yaml_file,
                           img=img,
                           num_products=num_products,
                           level_requirements=level_requirements)


@app.route('/zerg', methods=['GET', 'POST'])
def zerg():
    parsed_yaml_file = yaml.load(open('data/starcraft.yaml', 'r'), Loader=yaml.FullLoader)
    return render_template('templates/index.html',
                           race='Zerg',
                           data=parsed_yaml_file,
                           img=img,
                           num_products=num_products,
                           level_requirements=level_requirements)


if __name__ == '__main__':
    app.debug = True
    app.run()
