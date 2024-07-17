from setuptools import find_packages
from setuptools import setup

install_requires = [
    'numpy',
    'scipy',
    'autorom[accept-rom-license]',
    'gymnasium[accept-rom-license,atari]',
    ]

test_requires = [
    'pytest',
    'attrs<19.2.0',  # pytest does not run with attrs==19.2.0 (https://github.com/pytest-dev/pytest/issues/3280)  # NOQA
]

setup(
    name='ale_utils',
    version='0.0.0',
    description='Arcade Learning Environment Utils',
    keywords='ALE, Arcade, DQN',
    author='Prabhat Nagarajan',
    author_email='nagarajan@ualberta.ca',
    packages=find_packages(),
    install_requires=install_requires,
    test_requires=test_requires
)
