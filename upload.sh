SERVER='dreamarticles'
WEBSITE='articles.chymera.eu'
NAME=$(basename $(pwd))
[[ ! -z "$HOSTNAME" ]] && HOSTNAME="${HOSTNAME}_"

rsync -avP ${1}.pdf ${SERVER}:${WEBSITE}/${HOSTNAME}${NAME}_${1}.pdf &&\
	                echo "Article uploaded to http://${WEBSITE}/${HOSTNAME}${NAME}_${1}.pdf"
