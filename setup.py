from setuptools import setup, find_packages

setup(
    name='cowgirl-ai-file-manager',
    version='0.1.0',
    description='Interacting with the Open AI API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Cowgirl-AI/file-management',
    author='Tera Earlywine',
    author_email='dev@teraearlywine.com',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.10',
    # entry_points={
    #     'console_scripts': [
    #         'your_command=your_module:main_function',
    #     ],
    # },
    include_package_data=True,
    zip_safe=False
)
