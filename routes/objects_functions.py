import json
import os
import settings
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()


def get_classes_views_formats():
    """
    Caches the graph_classes JSON file in memory
    :return: a Python object parsed from the classes_views_formats.json file
    """
    cvf = cache.get('classes_views_formats')
    if cvf is None:
        cvf = json.load(open(os.path.join(settings.HOME_DIR, 'routes', 'classes_views_formats.json')))
        # times out never (i.e. on app startup/shutdown)
        cache.set('classes_views_formats', cvf)
    return cvf


def get_classes():
    cvf = get_classes_views_formats()
    classes = []
    for c in list(cvf.keys()):
        if not c.startswith('_'):
            classes.append(c.split('#')[1])

    return classes


def get_class_uris():
    cvf = get_classes_views_formats()
    classes = []
    for c in list(cvf.keys()):
        if not c.startswith('_'):
            classes.append(c)
    return classes
