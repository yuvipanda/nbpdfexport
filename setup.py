from setuptools import setup, find_packages

setup(
    name='nbpdfexport',
    version='0.1',
    install_requires=[
        'nbconvert',
        'pyppeteer',
    ],
    python_requires='>=3.6',
    description='Convert Jupyter Notebooks to PDF without LaTeX',
    url='http://github.com/yuvipanda/nbpdfexport',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='BSD',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['jupyter-pdfexport=nbpdfexport:main']
    }
)
