import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()

setuptools.setup(
    name='sketchkh',
    version='0.1',
    description='sketchkh: Distribution-informed single-cell sketching with kernel herding.',
    long_description=long_description,
    url='https://github.com/CompCy-lab/SketchKH',
    license='MIT',
    python_requires='>=3',
    install_requires=['numpy', 'tqdm', 'anndata'],
    packages=setuptools.find_packages()
)
