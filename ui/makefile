init-db:
	python db.py
	
run-ui: init-db
	uvicorn --host 0.0.0.0 --port 8000 main:app --reload
