init-cache:
	mkdir -p /app/.cache
	
run-model: init-cache
	uvicorn --host 0.0.0.0 --port 8000 main:app --reload
