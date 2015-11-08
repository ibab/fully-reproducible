
import sys
import shelve
import re
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from uncertainties import ufloat

env = Environment(
        loader=FileSystemLoader('.'),
        undefined=StrictUndefined,
)

LATEX_SUBS = (
    (re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r'"'), r"''"),
    (re.compile(r'\.\.\.+'), r'\\ldots'),
)

def escape_tex(value):
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval

def si(value):
    if isinstance(value, tuple):
        value = ufloat(value[0], value[1])
    return "{}".format(value).replace("+/-", "\\pm").replace('(', ' ').replace(')', ' ')

def table_fmt(values, err=None, figures=None):
    before = 0
    after = 0
    if err is None:
        for v in values:
            pre, post = str(round(v), figures).split('.')
            if len(pre) > before:
                before = len(pre)
            if len(post) > after:
                after = len(post)
        return '{}.{}'.format(before, after)
    else:
        error = 0
        for v, e in zip(values, err):
            vv, ee = str(ufloat(v, e)).split('+/-')
            v_pre, v_post = vv.split('.')
            e_pre, e_post = ee.split('.')

            if len(v_pre) > before:
                before = len(v_pre)
            if len(v_post) > after:
                after = len(v_post)
            if len(e_post) > error:
                error = len(e_post)

            return "{}.{}({})".format(before, after, error)

env.block_start_string = '#<'
env.block_end_string = '>#'
env.variable_start_string = '<<'
env.variable_end_string = '>>'
env.comment_start_string = '#='
env.comment_end_string = '=#'
env.filters['escape_tex'] = escape_tex
env.filters['si'] = si
paper = sys.argv[-1]
template = env.get_template(paper)

db = dict()

scripts = sys.argv[1:-1]
for scr in scripts:
    with open(scr) as f:
        code = compile(f.read(), 'test.py', 'exec')
        exec(code, globals(), locals())

db = locals()
db['table_fmt'] = table_fmt
db['map'] = map
db['hex'] = hex

text = template.render(**db)
with open('paper.tmp.tex', 'w') as f:
    f.write(text)

