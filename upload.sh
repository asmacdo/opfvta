[[ ! -z "$HOSTNAME" ]] && HOSTNAME="${HOSTNAME}_"
rsync -avP article.pdf dreamhost:chymera.eu/articles/${HOSTNAME}opfvta.pdf
rsync -avP article_mp.pdf dreamhost:chymera.eu/articles/${HOSTNAME}opfvta_mp.pdf
