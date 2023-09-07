How we got the sequences
========================
We visit PFAM entry for Phage tail repeat like `here <https://www.ebi.ac.uk/interpro/entry/pfam/PF12789/entry_alignments/?type=seed/>`_
From this page we obtain the SEED and curate it, obtaining `this new SEED <https://github.com/DraLaylaHirsh/MotifHXH/blob/0a919053e5ccf16bca6110c5f9ed3a03f696efd4/docs/best85817344-35C1.afa/>`_

.. image:: /images/SEEDHxH.png

This SEED gave us diferent architecture domains


.. image:: /images/domains1.png
.. image:: /images/domains2.png
.. image:: /images/domains3.png
.. image:: /images/domains4.png
.. image:: /images/domains5.png

The taxonomy distribution is shown here:

.. image:: /images/taxonomi.png

We obtained all `1071 complete sequences <https://github.com/DraLaylaHirsh/MotifHXH/blob/6e6c74142624eb4bf96832738d80269f43623d95/docs/bestCompleteSeq.fa/>`_ gathered using the previous profile and eliminate 80% redundancy `sequences (162 sequences) <https://github.com/DraLaylaHirsh/MotifHXH/blob/6e6c74142624eb4bf96832738d80269f43623d95/docs/bestCompleteSeqNoRed.fa/>`_. 

Then this 162 sequences where analized and was confirmed that only 149 contain the Motif. 
The following table shows how they are represented in average :

.. image:: /images/averagecount.png

The patters of the presence of the motifs in quantity are shown in the following table:

.. image:: /images/table.png 
.. image:: /images/table2.png
.. image:: /images/table3.png
.. image:: /images/table4.png

