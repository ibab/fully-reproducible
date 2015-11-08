
target=$(shell git rev-parse HEAD)
branch=$(shell git rev-parse --abbrev-ref HEAD)
message=$(shell git log -n 1 --pretty=format:%s)

paper.pdf: paper.tmp.tex
	lualatex --jobname=paper paper.tmp.tex

paper.tmp.tex: paper.tex
	python process.py run.py paper.tex

clean:
	rm *.pdf *.aux *.log paper.tmp.tex

publish: paper.pdf
	@git clone -b gh-pages https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git _deploy
	cp paper.pdf _deploy/data/${target}.pdf
	cp make_page.py _deploy
	cd _deploy
	ls -R
	echo ${target},${message},data/${target}.pdf >> entries.csv
	python make_page.py
	git add entries.csv index.html ./data/${target}.pdf
	git commit -m "Add automatically to gh-pages" || true
	@git push -fq https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git gh-pages

