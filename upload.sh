[[ ! -z "$HOSTNAME" ]] && HOSTNAME = "${HOSTNAME}_"
rsync -avP article.pdf dreamhost:chymera.eu/articles/${HOSTNAME}opfvta.pdf
