SERVER='dreamarticles'
WEBSITE='articles.chymera.eu'
[[ ! -z "$HOSTNAME" ]] && HOSTNAME="${HOSTNAME}_"
rsync -avP article.pdf ${SERVER}:${WEBSITE}/${HOSTNAME}opfvta.pdf &&\
	echo "Article uploaded to http://${WEBSITE}/${HOSTNAME}irsabi.pdf"
