from distutils.core import setup

setup(
    name='tbapiv3',
    version='1.2.1',
    packages=['tbapiv3'],
    url='https://github.com/WardBenjamin/TBAPIv3',
    license='MIT',
    author='Benjamin Ward',
    author_email='ward.programm3r@gmail.com',
    description='Bindings to get data from The Blue Alliance API (v3). Uses structured (instead of generated) data classes.',
    requires=['requests']
)
