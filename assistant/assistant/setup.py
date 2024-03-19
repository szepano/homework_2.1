from setuptools import setup, find_namespace_packages

setup(name='assistant_project',
      version='0.1',
      description="It is a simple personal assistant that allows you to menage your contacts and perform operations of files using commends.",
      url='https://github.com/szepano/group_project.git',
      author='Bartosz Szczepan, Bartosz Krusiński, Dawid Dziekan, Dawid Dudek',
      author_email='bart.szczepan04@gmail.com',
      license='Mit license',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': 
            ['assistant = assistant.interaction:main']},
)