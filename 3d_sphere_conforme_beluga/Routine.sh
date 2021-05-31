#!/bin/bash

for Re in $(seq 20 5 25)	#Re $(min pas max)

do	

	vis=$(echo "scale=5; 1/$Re" | bc)

	sed -i '14s/set output name=sphere-.*/set output name=sphere-'$Re'/' sphere_adapt.prm #modification du nom output
	sed -i '54s/set kinematic viscosity=.*/set kinematic viscosity='$vis'/' sphere_adapt.prm #modication de la viscosité cinématique
	echo $vis

	./gls_navier_stokes_3d sphere_adapt.prm #execution de la simulation au rang courant Re
	mkdir Re=$Re
	mv *.pvd *.vtu *.pvtu *.dat Re\=$Re/

	#sed -n 14p sphere_adapt.prm
done
