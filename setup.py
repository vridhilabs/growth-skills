from setuptools import setup, find_packages

setup(
    name='growth-skills',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={
        'growth_skills': ['templates/*.json'],
    },
    install_requires=[
        # No heavy dependencies yet—standard lib only for CLI
    ],
    entry_points={
        'console_scripts': [
            'growth-skills=growth_skills.cli:main',
        ],
    },
    author='Sai Rahul',
    description='Open-source high-engagement templates for social, email, and DM outreach.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vridhilabs/growth-skills',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
