#!/bin/sh

# - generate a current gnumed.pot file from GnuMed source
# - merge with existing translations
# - first arg should be ISO language code

# $Source: /home/ncq/Projekte/cvs2git/vcs-mirror/gnumed/gnumed/test-area/blobs_hilbert/locale/Attic/create-gnumed_po.sh,v $
# $Revision: 1.1 $

# what language are we working on
LANGNAME="$1"
if [ "${LANGNAME}" == "" ]; then
	echo "You must give an ISO language code as the first argument."
	exit
fi

# where to look for files
BASE="dist/"
# what to call the result
POTNAME="gnumed-archiv.pot"

echo "harvesting python source files in ${BASE} into the file ${POTNAME}"
find ${BASE} -follow -name '*.py' -print0 | xargs -0 pygettext.py -v -o ${POTNAME} "-"

echo "merging current source strings with old translations for language ${LANGNAME}"
if [ -f "${LANGNAME}.po" ]; then
	msgmerge -v -o gnumed-archiv-${LANGNAME}.po ${LANGNAME}.po ${POTNAME}
	mv -vf gnumed-archiv-${LANGNAME}.po ${LANGNAME}.po
	#rm -vf ${POTNAME}
else
	cp -vf ${POTNAME} ${LANGNAME}.po
fi;

echo "you can now translate messages in ${LANGNAME}.po"
