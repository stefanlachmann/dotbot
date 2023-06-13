.PHONY: all install run test report

all: install run test report

install:
    pip install -r requirements.txt

run:
    python3 dotbot.py

test:
    python -m unittest discover tests/

report:
    python generate_report.py
