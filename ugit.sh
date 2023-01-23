#!/bin/bash

echo Please enter the coment:

read cmt

git add *
git commit -m "$cmt"
git push origin HEAD
