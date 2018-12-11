from invoke import task


def generate_type_hierarchy(ctx):
    """
    Generate a document containing the available variable types.
    """
    ctx.run('./env/bin/python -m puresnmp.types > docs/typetree.rst')


@task
def doc(ctx):
    generate_type_hierarchy(ctx)
    ctx.run('sphinx-apidoc '
            '-o docs/developer_guide/api '
            '-f '
            '-e '
            'puresnmp '
            'puresnmp/test')
    with ctx.cd('docs'):
        ctx.run('make html')


@task
def publish(ctx):
    ctx.run('rm -rf dist')
    ctx.run('python3 setup.py bdist_wheel --universal')
    ctx.run('python3 setup.py sdist')
    ctx.run('twine upload dist/*')
