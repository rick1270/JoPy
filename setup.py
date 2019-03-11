from distutils.core import setup

setup(
    name='JoPy',
    version='0.1dev',
    packages=['pandas, matplotlib.pyplot', 'urllib.request.urlopen',
              'PIL.Image', 'geopy.geocoders.Nominatim',
              'geopy.distance.geodesic', 'math', 'colorsys'],
    license='MIT',
    long_description=open('README.txt').read(),
)
