PLATFORM = $(shell uname)
ifeq ($(PLATFORM), Darwin)
PYBIN = Python
else
PYBIN = python
endif
PROJ = dreamstack


version:
	@python -c "from $(PROJ) import meta;print meta.version;"


setup:
	git init
	touch README.rst
	git add README.rst
	-git commit -m "Added README placeholder."
	git remote add origin git@github.com:dreamhost/dreamstack-deploy.git
	git push -u origin master


clean:
	find ./ -name "*~" -exec rm {} \;
	find ./ -name "*.pyc" -exec rm {} \;
	find ./ -name "*.pyo" -exec rm {} \;
	find . -name "*.sw[op]" -exec rm {} \;
	rm -rf _trial_temp/ build/ dist/ MANIFEST *.egg-info


check-testcase-names:
	@echo "Checking for (possibly) badly named test cases..."
	@find ./$(PROJ)|xargs grep Test|grep class|grep -v 'TestCase('


virtual-dir-setup: VERSION ?= 2.7
virtual-dir-setup:
	-@test -d .venv-$(VERSION) || virtualenv -p $(PYBIN)$(VERSION) .venv-$(VERSION)
	-. .venv-$(VERSION)/bin/activate && pip install pep8
	-. .venv-$(VERSION)/bin/activate && pip install pyflakes
	-. .venv-$(VERSION)/bin/activate && pip install fabric

virtual-builds:
	-@test -e "`which $(PYBIN)2.6`" && VERSION=2.6 make virtual-dir-setup || echo "Couldn't find $(PYBIN)2.6"
	-@test -e "`which $(PYBIN)2.7`" && VERSION=2.7 make virtual-dir-setup || echo "Couldn't find $(PYBIN)2.7"


virtual-runner: VERSION ?= 2.7
virtual-runner: MOD ?= $(PROJ)
virtual-runner:
ifeq ($(strip $(MOD)),)
	-. .venv-$(VERSION)/bin/activate && .venv-$(VERSION)/bin/python $(PROJ)/testing/runner.py
else
	-. .venv-$(VERSION)/bin/activate && .venv-$(VERSION)/bin/python $(PROJ)/testing/runner.py --test-specific=$(MOD)
endif


virtual-pep8: VERSION ?= 2.7
virtual-pep8:
	-. .venv-$(VERSION)/bin/activate && pep8 --repeat ./$(PROJ)


virtual-pyflakes: VERSION ?= 2.7
virtual-pyflakes:
	-. .venv-$(VERSION)/bin/activate && pyflakes ./$(PROJ)


virtual-check: VERSION ?= 2.7
virtual-check:
	-VERSION=$(VERSION) make virtual-runner
	-VERSION=$(VERSION) make virtual-pep8
	-VERSION=$(VERSION) make virtual-pyflakes


virtual-checks: clean virtual-builds
	-@test -e "`which python2.6`" && VERSION=2.6 make virtual-check
	-@test -e "`which python2.7`" && VERSION=2.7 make virtual-check
	make check-testcase-names


virtual-uninstall: VERSION ?= 2.7
virtual-uninstall: PACKAGE ?= ""
virtual-uninstall:
	-. .venv-$(VERSION)/bin/activate && pip uninstall $(PACKAGE)


virtual-uninstalls: PACKAGE ?= ""
virtual-uninstalls:
	-@test -e "`which python2.6`" && VERSION=2.6 PACKAGE=$(PACKAGE) make virtual-uninstall
	-@test -e "`which python2.7`" && VERSION=2.7 PACKAGE=$(PACKAGE) make virtual-uninstall


virtual-dir-remove: VERSION ?= 2.7
virtual-dir-remove:
	rm -rfv .venv-$(VERSION)


clean-virtual-builds: clean
	@VERSION=2.6 make virtual-dir-remove
	@VERSION=2.7 make virtual-dir-remove


virtual-build-clean: clean-virtual-builds build virtual-builds
.PHONY: virtual-build-clean


check: MOD ?= $(PROJ)
check:
ifeq ($(strip $(MOD)),)
	python $(PROJ)/testing/runner.py
else
	python $(PROJ)/testing/runner.py --test-specific=$(MOD)
endif
