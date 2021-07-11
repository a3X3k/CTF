#!/bin/bash

i=1000

while [ $i -ge 1 ]
do
        tar xf $i.tar
        rm $i.tar
        ((i--))
done

