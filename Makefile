.PHONY: all clean lint type

CMD:=poetry run
PYMODULE:=monzo_webhook
EXTRACODE:=

all: type lint

lint:
	$(CMD) flake8 $(PYMODULE) $(TESTS) $(EXTRACODE)

type:
	$(CMD) mypy $(PYMODULE) $(TESTS) $(EXTRACODE)

isort:
	$(CMD) isort $(PYMODULE) $(TESTS) $(EXTRACODE)

clean:
	git clean -Xdf # Delete all files in .gitignore