run:
	.\venv\Scripts\python.exe app.py

format:
	cd templates && prettier -w *.html
	cd static/css && prettier -w *.css 
	cd static/js && prettier -w *.js
	autopep8 --in-place --aggressive --aggressive *.py