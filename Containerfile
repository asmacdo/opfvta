# name the portage image
FROM gentoo/portage:latest as portage

# based on stage3 image
# FROM gentoo/stage3:amd64-hardened-20200905
FROM gentoo/stage3:latest

# copy the entire portage volume in
COPY --from=portage /var/db/repos/gentoo /var/db/repos/gentoo

RUN emerge --noreplace dev-vcs/git

COPY .[^opfvta_bids]* /opfvta

RUN rm -f /opfvta/.gentoo/metadata/layout.conf
RUN rm -f /opfvta/.gentoo/overlays/science
RUN rm -f /etc/portage/repos.conf/science.conf

COPY reproduce/science.conf /etc/portage/repos.conf/science.conf
COPY reproduce/make.conf /etc/make.conf
COPY .gentoo/package.accept_keywords/gen /etc/portage/package.accept_keywords

RUN emerge --sync science

COPY opfvta_bidsdata-2.0/* /usr/share/opfvta_bidsdata/

RUN sed -i -e "s/sci-biology\/ants//g" /var/db/repos/science/profiles/package.mask
RUN sed -i -e "s/sci-biology\/samri//g" /var/db/repos/science/profiles/package.mask
RUN echo "sci-biology/opfvta_bidsdata-2.0" > /etc/portage/profile/package.provided
RUN echo ">=media-libs/harfbuzz-7.1.0 icu" > /etc/portage/package.use

RUN FEATURES="-ipc-sandbox -mount-sandbox -network-sandbox -pid-sandbox" \
  emerge texlive-latexextra --autounmask-write &&
  /asmacdo/.gentoo/install.sh

# latex errors, files not found RETURN to proceed
