#!/bin/sh

[ "${TRAVIS_PULL_REQUEST}" = "false" ] && ghp-import -n ./_site && git push -fq https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git gh-pages > /dev/null 2>&1 || true


