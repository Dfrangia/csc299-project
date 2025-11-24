from setuptools import setup, find_packages

setup(
    name="task-manager-cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'task=tools.task_manager_cli.cli:main',
        ],
    },
)

