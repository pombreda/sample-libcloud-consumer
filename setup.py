from setuptools import setup

setup(
    name = 'sample-libcloud-consumer',
    packages = ['sample_libcloud_consumer'],
    version = '0.0.1',
    description = 'Sample library that uses apache-libcloud',
    author = 'Quinn Slack',
    author_email = 'sqs@sourcegraph.com',
    url = 'https://github.com/sourcegraph/sample-libcloud-consumer',
    install_requires = ['apache-libcloud'],
)
