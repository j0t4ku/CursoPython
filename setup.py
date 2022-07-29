#Crear e instalar un paquete 
#python setup.py sdist #Crea el Paquete
#pip3 o pip install y el paquete.tar.gz nombre_paquete
#pip3 o pip uninstall el nombre del paquete



from setuptools import setup

setup(
    name="paquetecalculos",
    version="1.0",
    description="Paquete de calculos basicos",
    author="Joel",
    author_email="j.ismar00@gmail.com",
    url="j0t4ku.github.io",
    packages=["Paquetes","Paquetes.Basicos"]
    )