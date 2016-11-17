"""
Convert CIDR to list of IPs
"""
from setuptools import find_packages, setup


setup(
    name='cidr-list',
    version='0.1.0',
    url='https://github.com/mpicard/python-cidr-list',
    license='MIT',
    author='Martin Picard',
    author_email='map@cix.ie',
    description='Convert CIDR to list of IPs',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['click', 'netaddr'],
    entry_points={
        'console_scripts': [
            'cidr-list = cidr_list.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
