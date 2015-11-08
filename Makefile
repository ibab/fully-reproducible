
target=$(shell git rev-parse HEAD).pdf
branch=$(shell git rev-parse --abbrev-ref HEAD)

paper.pdf: paper.tmp.tex
	texfot lualatex --jobname=paper paper.tmp.tex

paper.tmp.tex: paper.tex
	python process.py run.py paper.tex

clean:
	rm *.pdf *.aux *.log paper.tmp.tex

add_pages: paper.pdf
	mkdir -p ./data
	mv paper.pdf data/${target}
	python make_page.py
	git checkout -f gh-pages
	git add index.html ./data/${target}
	git commit -m "Add automatically to gh-pages" || true
	git checkout ${branch}

publish: add_pages
	git checkout gh-pages
	git push origin gh-pages
	git checkout ${branch}

