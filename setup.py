from setuptools import setup, find_packages
import os


def requirements_txt_to_install_requires_array():
    __curr_location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    requirements_txt_file_as_str = f"{__curr_location__}/requirements.txt"
    with open(requirements_txt_file_as_str, 'r') as reqfile:
        libs = reqfile.readlines()
        for i in range(len(libs)):
            libs[i] = libs[i].replace('\n', '')
    return libs


setup(
    name='webapp_workflow_automator',
    author='',
    author_email='',
    version='0.0.1',
    url='https://www.foobar.com',
    description='Webapp automator (with REST API)',
    packages=find_packages(include=['webapp_workflow_automator', 'webapp_workflow_automator.*']),
    # include_package_data=True,
    # package_data={'webapp_workflow_automator': ['config/*', ]},
    python_requires='>=3.7',
    install_requires=requirements_txt_to_install_requires_array(),
    extras_require={
        'HttpServer': ['flask>=1.1.2', 'werkzeug>=1.0.1'],
    },
    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
        'Framework :: Jupyter',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Engineering :: Frameworks',
        'Topic :: Software Development :: Libraries'
    ]
)
