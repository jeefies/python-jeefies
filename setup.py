from setuptools import setup

# from blog.csdn.net/tcy23456/article/details/91886555

with open('README.md') as f:
    long_des=f.read()

setup(
        name = 'jeefies',
        author = 'Jeef',
        version = '0.0.3',
        packages = ['jeefies', "jeefies/jeefies_sec"],
        author_email = 'jeefy163@163.com',
        description = 'A package made by jeefy and it\'s use for self',
        maintainer = 'Jeef',
        maintainer_email = 'jeefy163@163.com',
        python_requires = '>=3.4',
        package_data = {'': ['*txt']},
        url = 'https://www.baidu.com',
        long_description = long_des,
        long_description_content_type = 'text/markdown'
        )
