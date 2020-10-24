[[ ! -z "$HOSTNAME" ]] && HOSTNAME="${HOSTNAME}_"
rsync -avP article.pdf dreamarticles:articles.chymera.eu/${HOSTNAME}opfvta.pdf
