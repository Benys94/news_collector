# Makefile for news_collector project

doc:
	cd ./docs/ && make html

run-pylint:
	pylint src/

.PHONY:
	docs
	run-pylint
