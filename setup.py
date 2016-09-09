from distutils.core import setup

install_requires = [
    'Pillow',
]

test_requires = [
    'pytest',
    'mock',
]

setup(
    name='image2tiled',
    version='0.1.0',
    packages=['image2tiled'],
    url='https://github.com/henriquegemignani/image2tiled',
    license='GPL v3',
    author='Henrique Gemignani',
    author_email='henrique@gemignani.org',
    description='Tool that creates a tiled map based on an image',
    install_requires=install_requires,
    test_requires=test_requires,
    extras_require={
        'tests': test_requires,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'image2tiled = image2tiled.cli:main'
        ],
    }
)
