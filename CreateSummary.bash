#!/bin/bash

#Run main.py python script with bash
echo "Running main.py"
python3 main.py

filename=$(cat folderName.txt)
echo $filename;
my_filename=$filename
path=Downloads/$my_filename/output.txt
echo $path;
read -p "Enter the pattern:" pattern
echo $pattern" is registered";
cat $path | xargs -0 | fabric --model codegemma:latest -sp $pattern | save $my_filename"_AI_Summary"
