from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
        name='ssbio-edbr',
        version='0.9.9.7',
        author='Xiaofan Li',
        author_email='xli@edbr.uk',
        license='MIT',
        url='http://github.com/i386uk/ssbio',
        download_url='https://github.com/i386uk/ssbio/archive/v0.9.9.7.tar.gz',
        description='Tools to enable structural systems biology, forked from SBRG/ssbio',
        packages=find_packages(),
        package_dir={'ssbio': 'ssbio'},
        # scripts=['ssbio/protein/structure/utils/cleanpdb.py',
        #          'ssbio/protein/structure/utils/mutatepdb.py',
        #          'ssbio/protein/structure/utils/tleap.py'],
        #          'ssbio/protein/structure/properties/msms.py'],
        long_description=open('README.rst').read(),
        install_requires=required
)
