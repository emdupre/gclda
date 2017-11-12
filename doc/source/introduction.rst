Introduction
============

The gcLDA model is a generalization of the correspondence-LDA model (Blei & Jordan, 2003, "Modeling annotated data"), which is an unsupervised learning model used for modeling multiple data-types, where one data-type describes the other. The gcLDA model was introduced in the following paper:

[Generalized Correspondence-LDA Models (GC-LDA) for Identifying Functional Regions in the Brain](https://timothyrubin.github.io/Files/GCLDA_NIPS_2016_Final_Plus_Supplement.pdf)

where the model was applied for modeling the [Neurosynth](http://neurosynth.org/) corpus of fMRI publications. Each publication in this corpus consists of a set of word tokens and a set of reported peak activation coordinates (x, y and z spatial coordinates corresponding to brain locations).

When applied to fMRI publication data, the gcLDA model identifies a set of T topics, where each topic captures a 'functional region' of the brain. More formally: each topic is associated with (1) a spatial probability distribution that captures the extent of a functional neural region, and (2) a probability distribution over linguistic features that captures the cognitive function of the region.

The gcLDA model can additionally be directly applied to other types of data. For example, Blei & Jordan presented correspondence-LDA for modeling annotated images, where pre-segmented images were represented by vectors of real-valued image features. The code provided here should be directly applicable to these types of data, provided that they are appropriately formatted. Note however that this package has only been tested on the Neurosynth dataset; some modifications may be needed for use with other datasets.
