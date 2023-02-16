from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 6 - Mature',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='ExportWifi',
    version='0.0.3',
    description='Getting Wifi Files of the target',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Fawaz Bashiru',
    author_email='fawazbashiru@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Wifi',
    packages=find_packages(),
    install_requires=["pyautogui", "reportlab"]
)