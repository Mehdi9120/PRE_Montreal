#!/bin/bash

for Re in $(seq 5 5 30)	#Re $(min pas max)

do	

	vis=$(echo "scale=5; 1/$Re" | bc)

	sed -i '11s/set output name=sphere-.*/set output name=sphere-'$Re'/' sphere_IB.prm #modification du nom output
	sed -i '45s/set kinematic viscosity=.*/set kinematic viscosity='$vis'/' sphere_IB.prm #modication de la viscosité cinématique
	echo $vis

	./gls_sharp_navier_stokes_3d sphere_IB.prm #execution de la simulation au rang courant Re
	mkdir Re=$Re
	mv *.pvd *.vtu *.pvtu *.dat Re\=$Re/

	#sed -n 14p sphere_IB.prm
done
