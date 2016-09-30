from setuptools import setup, find_packages


def load_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip().split('==')[0] for line in f]

# console-script means the CLI takes weather
# as the argument and points to the main function as the entry point
setup(
    name='weather',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements(),
    entry_points={
        'console_scripts': [
            'weather = weather.main:main',
        ]
    },
)
