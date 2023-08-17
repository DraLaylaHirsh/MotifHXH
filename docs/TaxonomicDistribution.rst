Eukaryotic Taxonomic Distribution
=================================


.. image:: /images/taxonomic.png

With the results of Hmmer, we divided the analisis in 3, Eukaryot 808 sequences, Virus 178 sequences and Bacteria 85 sequences, in this section we work on the 808 Eukaryotic sequences.

.. image:: /images/eukaryot.png

We can observe the domains architectures for this sequences, and we will see 3 "big" clusters

.. image:: /images/domainseuka.png


This SEED gave us diferent architecture domains and we analized each of them by getting all the complete sequences of the cluster, align them and eliminate the redundacy considering a 75% .
The results are the following:

Cluster 379
-----------
After aligning and cleaning the redundancy we had 16 complete sequences that were trimmed 

.. image:: /images/RightPartali379.png

.. image:: /images/LeftPartali379.png

The motif HxH is present in 3 different sections

Position 330 of the alignment HTH or HIH in position 148 of ost of the sequences. 
There are some particular cases:
-A2H129 has the motif in position 17 of the sequence.
-Four of the sequences ( A2Fw47,A2E7R7, A2GBQ3,A2H129)present a second motif after aprox 20 amino acids (HTH).


.. image:: /images/pos330HxH_379.png

Position 480 of the alignment HTH or HKH in position 170-190 of the sequences. 
There are some particular cases:
-A2GLX5 has the motif in position 8 of the sequence.
-Again in some cases we can find a second Motif HXH and even a third and fourth motif in a 20 amino acid distance each all HTH motifs.
-Some sequences have more motifs in them, but there is no conservation with the others.

.. image:: /images/Pos480HxH379.png

Position 890 of the alignment HTH or HSH in the tail of the sequences. 
There are some particular cases:
-After 11 amino acids there is a second motif HSH or HKH in almost all of the sequences.
-After 36 amino acids there is a third motif HSH or HTH or HQH or HIH or HAH or HVH in almost all of the sequences.

.. image:: /images/Pos820HxH379.png

Considering the 16 complete sequences, we evaluate the type and quantity of amino acids present in the sequence: the amino acids more present in the sequence are marked in red.

.. image:: /images/379aa.png

Considering the 16 complete sequences, we evaluate the type and quantity of the motif HxH present in the sequence and their relative positions: 

.. image:: /images/379motiv.png


Considering the 16 complete sequences, we evaluate the type and order of the motif HxH present in the sequence and their relative positions: 

.. image:: /images/379motifPosition.png

.. image:: /images/375motiforder.png

All the complete sequences as trimmers were sent to AlphaFold Cluster, only A2DGZ2, A2FEE1, A2GLX5 and A2H129 retrive an output.

For A2FEE1, position 14 of the list, the spectrum: range is 21.94000 to 96.58000.

.. image:: /images/A2FEE1_sumary.png

.. image:: /images/A2FEE1_trimerbfactor.png

.. image:: /images/A2FEE1_trimer.png 


For A2DGZ2, position 7 of the list, the spectrum: range is 31.46000 to 98.06000.

 .. image:: /images/A2DGZ2_sumary.png

.. image:: /images/A2DGZ2_trimerbfactor.png

.. image:: /images/A2DGZ2_trimer.png 

For A2GLX5, position 5 of the list, the spectrum: range is  

 .. image:: /images/A2GLX5_sumary.png

.. image:: /images/A2GLX5_trimerbfactor.png

.. image:: /images/A2GLX5_trimer.png 

For A2H129, position 9 of the list, the spectrum: range is 

 .. image:: /images/A2H129_sumary.png

.. image:: /images/A2H129_trimerbfactor.png

.. image:: /images/A2H129_trimer.png 
