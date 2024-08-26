source .venv/Scripts/activate #activar entorno virtual
pip install --upgrade pip #actualizar
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate

#bash build.sh (lanzar script con la terminal Bash)