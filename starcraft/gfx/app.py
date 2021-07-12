import yaml
from flask import Flask, render_template
app = Flask(__name__, template_folder='static')


def img(name):
    return name.replace("Level 1", "").replace("Level 2", "").replace("Level 3", "").replace(" ", "") + ".png"


def font(text):
    if len(text) < 100:
        return 12
    if len(text) < 200:
        return 12
    return 11


def header(item_type):
    if item_type == 'Buildings' or item_type == 'Units':
        return 22
    return 18


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


def num_health_stats(item):
    c = 0
    if 'Stats' in item:
        if 'Health' in item['Stats']:
            c+=1
        if 'Shield' in item['Stats']:
            c += 1
        if 'Armor' in item['Stats']:
            c += 1
    return c

@app.route('/protoss', methods=['GET', 'POST'])
def protoss():
    parsed_yaml_file = yaml.load(open('data/starcraft.yaml', 'r'), Loader=yaml.FullLoader)
    return render_template('templates/index.html',
                           race='Protoss',
                           data=parsed_yaml_file,
                           img=img,
                           num_products=num_products,
                           level_requirements=level_requirements,
                           font=font,
                           header=header,
                           num_health_stats=num_health_stats,
                           float=float)


@app.route('/terran', methods=['GET', 'POST'])
def terran():
    parsed_yaml_file = yaml.load(open('data/starcraft.yaml', 'r'), Loader=yaml.FullLoader)
    return render_template('templates/index.html',
                           race='Terran',
                           data=parsed_yaml_file,
                           img=img,
                           num_products=num_products,
                           level_requirements=level_requirements,
                           font=font,
                           header=header,
                           num_health_stats=num_health_stats,
                           float=float)


@app.route('/zerg', methods=['GET', 'POST'])
def zerg():
    parsed_yaml_file = yaml.load(open('data/starcraft.yaml', 'r'), Loader=yaml.FullLoader)
    return render_template('templates/index.html',
                           race='Zerg',
                           data=parsed_yaml_file,
                           img=img,
                           num_products=num_products,
                           level_requirements=level_requirements,
                           font=font,
                           header=header,
                           num_health_stats=num_health_stats,
                           float=float)

@app.route('/rules', methods=['GET', 'POST'])
def rules():
    return render_template('templates/rules.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
