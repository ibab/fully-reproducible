
target=$(shell git rev-parse HEAD)
branch=$(shell git rev-parse --abbrev-ref HEAD)
message=$(shell git log -n 1 --pretty=format:%s)

paper.pdf: paper.tmp.tex
	lualatex --jobname=paper paper.tmp.tex

paper.tmp.tex: paper.tex
	python process.py run.py paper.tex

clean:
	rm *.pdf *.aux *.log paper.tmp.tex

add_pages: paper.pdf
	mkdir -p ./data
	mv paper.pdf data/${target}.pdf
	git checkout -f origin/gh-pages
	git checkout master -- make_page.py
	echo ${target},${message},data/${target}.pdf >> entries.csv
	python make_page.py
	git add entries.csv index.html ./data/${target}.pdf
	git commit -m "Add automatically to gh-pages" || true
	git checkout ${branch}

publish: add_pages
	git checkout origin/gh-pages
	@git push -fq https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git gh-pages

