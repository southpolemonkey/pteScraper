#!/usr/bin/env bash

#for file in *;
#if [[ $file == Bar ]]
#then
#    do mv "$file" "Bar/${file}";
#elif [[ $file == Flow ]]; then
#    do mv "$file" "Flow/${file}";
#elif [[ $file == Line ]]; then
#    do mv "$file" "Line/${file}";
#elif [[ $file == Map ]]; then
#    do mv "$file" "Map/${file}";
#elif [[ $file == Mix ]]; then
#    do mv "$file" "Mix/${file}";
#elif [[ $file == Picture ]]; then
#    do mv "$file" "Picture/${file}.jpg";
#fi
#done

find . -type d -print0 | while read -d '' -r dir; do
    files=("$dir"/*)
    printf "%5d files in directory %s\n" "${#files[@]}/2" "$dir"
done | sort -r
