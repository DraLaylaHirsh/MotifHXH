3D structures to the domains
============================

We initiate the process using these `sequences <https://github.com/DraLaylaHirsh/MotifHXH/blob/a388a0e05979c92a9891dd03c4be3f1a81c621c2/docs/trimerdata/AndreySEED>`_ as input seed for Hmmer, then, after some
iterations we obtain `this seed <https://github.com/DraLaylaHirsh/MotifHXH/blob/378eed498ed9084f38a9fdd86ed9973d3468981d/docs/trimerdata/SEEDtrimer.afa>`_ .  

.. image:: /images/NterminalDomain.png

The resulting complete sequences from uniprot can be download from here `these sequences <https://github.com/DraLaylaHirsh/MotifHXH/blob/399acd797c20e22a7ac3428ee3f6d53aa031a562/docs/trimerdata/C2C4DF86-4578-11EE-808C-C3E6F8E0C6C4.1-fullseq.fa.gz>`_

The taxonomy of the search results are:

.. image:: /images/taxTrimer.png

The domains of the search results are:

.. image:: /images/domainTrimer.png

.. image:: /images/domtrimer2.png

.. image:: /images/domtrimer3.png

We made the same search but using only PDB databank instead of uniprot, these are the results

.. image:: /images/pdbs.png

The taxonomy of the search results are:

.. image:: /images/taxpdb.png

The domains of the search results are:

.. image:: /images/dompdb.png

Using pymol, we can observe that all the pdbs are trimer, the pdbs are `here <https://github.com/DraLaylaHirsh/MotifHXH/blob/4d1f65a823fcc396ae2573b9b8db98929df3f377/docs/trimerdata/pdbs.tar.gz>`_ 

`1yu0 <https://www.rcsb.org/structure/1yu0>`_ 
`2c3f <https://www.rcsb.org/structure/2c3f>`_ 
`2dp5 <https://www.rcsb.org/structure/2dp5>`_ 
`2iou <https://www.rcsb.org/structure/2iou>`_ 
`2yw0 <https://www.rcsb.org/structure/2yw0>`_ 
`6x3m <https://www.rcsb.org/structure/6x3m>`_ 
`1yu1 <https://www.rcsb.org/structure/1yu1>`_ 
`1yu2 <https://www.rcsb.org/structure/1yu2>`_ 
`1yu3 <https://www.rcsb.org/structure/1yu3>`_ 
`1yu4 <https://www.rcsb.org/structure/1yu4>`_ 
`2yvv <https://www.rcsb.org/structure/2yvv>`_ 
`3eka <https://www.rcsb.org/structure/3eka>`_ 

Considering the species we have:

ARCHEA
------

`Interpro L0KWD4 <https://www.ebi.ac.uk/interpro/protein/UniProt/L0KWD4/alphafold/>`_, the alpha fold model as a trimer is `in this link <https://github.com/DraLaylaHirsh/MotifHXH/blob/c196f9d843f3fa6a72d9de0b6088dcec5d261e6d/docs/pdb/arch_L0KWD4Trimer.pdb>`_ 


.. image:: /images/L0KWD4_trimerDomain.png

.. image:: /images/L0KWD4_trimerbfactor.png

.. image:: /images/L0KWD4_trimer.png


EUKARIOT
--------

`Interpro B9TE92 <https://www.ebi.ac.uk/interpro/protein/UniProt/B9TE92/alphafold/>`_, the alpha fold model as a trimer is in this `link <https://github.com/DraLaylaHirsh/MotifHXH/blob/e3a29b2d6a0dddc5704111fd69cd046d4edf1363/docs/pdb/euk_B9TE92trimer.pdb>`_ 


.. image:: /images/B9TE92_trimerDomain.png

.. image:: /images/B9TE92_trimerbfactor.png

.. image:: /images/B9TE92_trimer.png


BACTERIA
--------
The 128 bacterias present in this cluster have an AF model as a monomer, we took three small sequences and model them as trimers.

A0A0F2JLV1

A0A1H4DFS6.fasta
A0A4S4BSN2.fasta

We also try to observe the amino acids present in all these sequences:

.. image:: /images/bacteriaAA.png



VIRUS
-----
The 212 bacterias present in this cluster do not have an AF model as a monomer nor as trimer. We took two sequences and model them as trimers.

`Interpro C7F4B3 <https://www.ebi.ac.uk/interpro/protein/UniProt/C7F4B3/>`_

.. image:: /images/C7F4B3_trimer.png

.. image:: /images/C7F4B3_trimerDomain.png

.. image:: /images/C7F4B3_trimerbfactor.png

`Interpro B5U373 <https://www.ebi.ac.uk/interpro/protein/UniProt/B5U373/>`_

.. image:: /images/B5U373_trimer.png

.. image:: /images/B5U373_trimerbfactor.png

.. image:: /images/B5U373_trimerDomain.png

We also try to observe the amino acids present in all these sequences:

.. image:: /images/virusAA.png


A SECOND DOMAIN
===============

`Literature <https://europepmc.org/article/MED/30945633#free-full-text>`_


`Seed <https://github.com/DraLaylaHirsh/MotifHXH/blob/2a64a24b30734eca22d79b43c8237c44eddbccfb/docs/trimerdata/SEEDtrimer2.afa>`_

.. image:: /images/Logo2ndDomain.png

.. image:: /images/taxDom2.png

.. image:: /images/Domain2_dom.png

.. image:: /images/Domain2_dom2.png

.. image:: /images/Domain2_dom3.png


K6SYF0
------
Model Seed <
`Monomer AF model AF-K6SYF0-F1-model_v4.pdb <https://github.com/DraLaylaHirsh/MotifHXH/blob/94364ff359133a7ed4f9d31259fb208a972228be/docs/images/AF-K6SYF0-F1-model_v4.pdb>`_
`Pymol Sesion  K6SYF0.pse <https://github.com/DraLaylaHirsh/MotifHXH/blob/94364ff359133a7ed4f9d31259fb208a972228be/docs/images/K6SYF0.pse>`_

.. image:: /images/K6SYF0_bfactor.png

.. image:: /images/K6SYF0.png



A THIRD DOMAIN
===============


`Model Seed <https://github.com/DraLaylaHirsh/MotifHXH/blob/2f32418c8fd0e509cfa23e272e02a20f76b81075/docs/trimerdata/Domain3_2.afa>`_

.. image:: /images/LogoDomain3.png

.. image:: /images/taxDom3.png

.. image:: /images/Domain3_dom.png

.. image:: /images/Domain3_dom2.png

.. image:: /images/Domain3_dom3.png

.. image:: /images/Domain3_dom3.png
