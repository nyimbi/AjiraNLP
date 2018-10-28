#!/bin/bash
# File              : aligner.sh
# Date              : 20.10.2018
# Last Modified Date: 20.10.2018

function dotxt(){
    rm -Rf dataln
    mkdir dataln
    for f in *.txt; do
    cat ${f}| tr '\n' ' ' | gsed -e  's@\([[:digit:]]\+\)@\n\1  @g;G'| sed -n '/^[1-9]/p'| gsed '/^$/d;G' > dataln/${f}'.al.txt'
    # echo "${f}"
    done
    rm dataln/*INTRO*
    # echo "REMOVED INTRO FILES"
    ls dataln/*.al.txt | cut -d . -f 1,2 | sort > dataln//chaplist.lst
    # echo "GENERATED CHAPTER LIST"
}

function align(){
for dir in */; do
  dir=${dir%*/}
  echo ${dir##*/}
  (pushd `pwd` >/dev/null && cd $dir && dotxt && popd >/dev/null)
 done
}

