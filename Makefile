
target=$(shell git rev-parse HEAD)
branch=$(shell git rev-parse --abbrev-ref HEAD)
message=$(shell git log -n 1 --pretty=format:%s)

paper.pdf: paper.tmp.tex
	docker run -ti --rm -v $${PWD}:/root leodido/texlive bash -c "cd /root; lualatex --jobname=paper paper.tmp.tex"

paper.tmp.tex: paper.tex
	docker run -ti --rm -v ${PWD}:/root python bash -c "cd /root; pip install --user -r requirements.txt; python meta/process.py run.py paper.tex"

clean:
	docker run --ti --rm -v $${PWD}:/root busybox bash -c "cd /root; rm *.pdf *.aux *.log paper.tmp.tex"

publish: paper.pdf
	@git clone -b gh-pages https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git _deploy
	cp paper.pdf _deploy/data/${target}.pdf
	cp  .meta/make_page.py _deploy
	git config --global user.email ""
	git config --global user.name "Automatic travis commit"
	cd _deploy; echo ${target},${message},data/${target}.pdf >> entries.csv
	cd _deploy; python make_page.py
	cd _deploy; git add entries.csv index.html ./data/${target}.pdf
	cd _deploy; git commit -m "Add automatically to gh-pages" || true
	@cd _deploy; git push -fq https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git gh-pages

