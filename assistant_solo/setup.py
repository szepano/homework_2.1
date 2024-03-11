from setuptools import setup, find_namespace_packages

setup(name='personal_assistant',
      version='0.1',
      description="It is a simple personal assistant that allows you to menage your contacts and perform operations of files using commends.",
      url='https://github.com/szepano/group_project.git',
      author='Bartosz Szczepan, Bartosz Krusiński, Dawid Dziekan, Dawid Dudek',
      author_email='bart.szczepan04@gmail.com, bartoszkrusinski@gmail.com, dziekan.dawid@wp.pl, bervex@gmail.com',
      license='Mit license',
      packages= find_namespace_packages(),
      entry_points={'console_scripts': 
            ['assistant = group_project.personal_assistant:main']},
)