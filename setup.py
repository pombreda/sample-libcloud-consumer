from setuptools import setup

requires=[
    'apache-libcloud'
]
install_requires = []
for package in requires:
    try:
        import package
    except ImportError:
        install_requires.append(package)

setup(
    name = 'sample-libcloud-consumer',
    packages = ['sample_libcloud_consumer'],
    version = '0.0.1',
    description = 'Sample library that uses apache-libcloud',
    author = 'Quinn Slack',
    author_email = 'sqs@sourcegraph.com',
    url = 'https://github.com/sourcegraph/sample-libcloud-consumer',
    install_requires = install_requires,
)
