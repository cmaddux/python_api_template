# If container name changes, change variable
CONTAINER=pythonapitemplate_api_1

.PHONY: run-script
run-script:
	docker exec -t $(CONTAINER) pipenv run python $(SCRIPT) $(ARGS)

.PHONY: install-pkg
install-pkg: pipenv-install-pkg pipenv-install-system

.PHONY: pipenv-install-pkg
pipenv-install-pkg:
	docker exec -t $(CONTAINER) pipenv install $(PKG)

.PHONY: pipenv-install-system
pipenv-install-system:
	docker exec -t $(CONTAINER) pipenv install --system

.PHONY: test
test:
	docker exec -t $(CONTAINER) pipenv run python -m pytest tests/
