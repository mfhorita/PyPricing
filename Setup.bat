REM Criar pasta do pacote PyPI 
REM Configurar setup.py
REM Criar README.rst e licence.txt
REM Criar Setup.cfg
REM Instalar twine: pip3 install twine

REM python setup.py register
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*