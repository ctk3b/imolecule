"""
Visualize a molecule, specified as a JSON string, in a browser.
Uses viewer.html as a template. The JSON
"""
import shutil
import webbrowser
import time
import os
import tempfile
from tornado import template

def visualize(mol_json, title="imolecule"):

    PATH = os.path.dirname(os.path.realpath(__file__))
    print PATH
    t = template.Loader(PATH).load('viewer.template')

    html = t.generate(title=title, mol_json=mol_json)

    tempdir = tempfile.mkdtemp(prefix='imolecule_' + str(int(time.time())) + '_')

    html_filename = os.path.join(tempdir,'index.html')
    with open(html_filename, 'w') as f:
        f.write(html)

    shutil.copy(os.path.join(PATH, os.path.join('server/css', 'chosen.css')), tempdir)
    shutil.copy(os.path.join(PATH, os.path.join('server/css', 'server.css')), tempdir)
    shutil.copy(os.path.join(PATH, os.path.join('js', 'jquery-1.11.1.min.js')), tempdir)
    shutil.copy(os.path.join(PATH, os.path.join('server/js', 'chosen.jquery.min.js')), tempdir)
    shutil.copy(os.path.join(PATH, os.path.join('js/build', 'imolecule.min.js')), tempdir)

    webbrowser.open(html_filename)

if __name__ == '__main__':

    mol_json = """
    {
        "atoms": [
            { "element": "O", "location": [ -3.206572, 0.149643, -0.030451 ] },
            { "element": "C", "location": [ -1.974803, 0.072639, -0.018629 ] },
            { "element": "N", "location": [ -1.172329, 1.214313, -0.010788 ] },
            { "element": "C", "location": [ -1.770043, 2.537593, -0.017626 ] },
            { "element": "C", "location": [ 0.195123, 1.078518, 0.002544 ] },
            { "element": "C", "location": [ 0.802543, -0.142774, 0.008489 ] },
            { "element": "N", "location": [ 2.140595, 0.133599, 0.021646 ] },
            { "element": "C", "location": [ 3.251708, -0.783226, 0.032763 ] },
            { "element": "C", "location": [ 2.267755, 1.500567, 0.022590 ] },
            { "element": "N", "location": [ 1.095482, 2.099785, 0.011110 ] },
            { "element": "N", "location": [ -1.316891, -1.171982, -0.012672 ] },
            { "element": "C", "location": [ -2.123078, -2.377546, -0.022140 ] },
            { "element": "C", "location": [ 0.070621, -1.362729, 0.000940 ] },
            { "element": "O", "location": [ 0.600598, -2.470613, 0.005597 ] },
            { "element": "H", "location": [ -1.450297, 3.078914, 0.878468 ] },
            { "element": "H", "location": [ -1.435940, 3.075797, -0.910364 ] },
            { "element": "H", "location": [ -2.862191, 2.492974, -0.026344 ] },
            { "element": "H", "location": [ 3.857542, -0.598300, -0.858326 ] },
            { "element": "H", "location": [ 3.840617, -0.597062, 0.934879 ] },
            { "element": "H", "location": [ 2.906763, -1.816272, 0.030287 ] },
            { "element": "H", "location": [ 3.229531, 1.998273, 0.031787 ] },
            { "element": "H", "location": [ -1.867519, -2.967420, -0.908701 ] },
            { "element": "H", "location": [ -1.883060, -2.971435, 0.866064 ] },
            { "element": "H", "location": [ -3.196156, -2.173257, -0.031123 ] }
        ],
        "bonds": [
            { "atoms": [ 0, 1 ], "order": 2 },
            { "atoms": [ 1, 2 ], "order": 1 },
            { "atoms": [ 2, 3 ], "order": 1 },
            { "atoms": [ 2, 4 ], "order": 1 },
            { "atoms": [ 4, 5 ], "order": 2 },
            { "atoms": [ 5, 6 ], "order": 1 },
            { "atoms": [ 6, 7 ], "order": 1 },
            { "atoms": [ 6, 8 ], "order": 1 },
            { "atoms": [ 8, 9 ], "order": 2 },
            { "atoms": [ 4, 9 ], "order": 1 },
            { "atoms": [ 1, 10 ], "order": 1 },
            { "atoms": [ 10, 11 ], "order": 1 },
            { "atoms": [ 10, 12 ], "order": 1 },
            { "atoms": [ 5, 12 ], "order": 1 },
            { "atoms": [ 12, 13 ], "order": 2 },
            { "atoms": [ 3, 14 ], "order": 1 },
            { "atoms": [ 3, 15 ], "order": 1 },
            { "atoms": [ 3, 16 ], "order": 1 },
            { "atoms": [ 7, 17 ], "order": 1 },
            { "atoms": [ 7, 18 ], "order": 1 },
            { "atoms": [ 7, 19 ], "order": 1 },
            { "atoms": [ 8, 20 ], "order": 1 },
            { "atoms": [ 11, 21 ], "order": 1 },
            { "atoms": [ 11, 22 ], "order": 1 },
            { "atoms": [ 11, 23 ], "order": 1 }
        ]
    }
    """

    visualize(mol_json, title='caffeine')