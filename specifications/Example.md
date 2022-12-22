# PyEED Data Model

PyEED is a Python-encoded data model of an Enzyme Engineering Database. It supports the scalable and reproducible analysis of sequence and structure data of protein families, and makes data and processes findable, accessible, interoperable, and reusable according to the FAIR data principles.

### ProteinSequence

- __protein_sequence_id__
  - Type: string
  - Description: Presented protein sequence  
- __name__
  - Type: string
  - Description: Systematic name of the protein.
- __amino_acid_sequence__
  - Type: string
  - Description: The amino acid sequence of the protein sequence object.
- __database_id__
  - Type: [Database](#Database)
  - Description: Data base ID
- __pdb_id__
  - Type: string
  - Description: Identifier for the PDB database
  - Multiple: True
- __database_entry__
  - Type: string
  - Description: Identifier for the database
- __organism_id__
  - Type: [Organism](#Organism)
  - Description: Corresponding organism 


### DNASequence

- __dna_sequence_id__
  - Type: string
  - Description: Reference to the Translated DNA from the matching Protein sequence
- __protein_sequence_id*__
  - Type: [ProteinSequence](#ProteinSequence)
  - Description: Presented protein sequence
- __database_id__
  - Type: [Database](#Database)
  - Description: Data base ID
- __database_entry__
  - Type: string
  - Description: Identifier for the database
- __organism_id__
  - Type: [Organism](#Organism)
  - Description: NCBI Taxonomy ID to identify the organism
  - 
### Organism

- __organism_id__
  - Type: string
  - Description: NCBI Taxonomy ID to identify the organism
- __organism_name__
  - Type: string
  - Description: Organism name
- __ncbi_taxonomy_id__
  - Type: string
  - Description: NCBI Taxonomy ID to identify the organism

### Database

- __database_id__
  - Type: string
  - Description: Name of the annotated domain
- __database__
  - Type: integer
  - Description: Position in the sequence where the domain starts
- __link_to_database__
  - Type: integer
  - Description: Position in the sequence where the domain ends

### Standard Numbering Scheme

- __standard_numering_scheme_id__
  - Type: integer
  - Description: Equivalent position in the reference sequence
- __standard_numering_scheme_name__
  - Type: integer
  - Description: Position that is equivalent to the reference sequence position that is also given
- __protein_sequence_id__
  - Type: string
  - Description: Presented protein sequence

### Position

- __position_id__
  - Type: integer
  - Description: Equivalent position in the reference sequence
- __protein_sequence_id__
  - Type: [ProteinSequence](#ProteinSequence)
  - Description: Position that is equivalent to the reference sequence position that is also given
- __standard_numbering_scheme_id__
  - Type: integer
  - Description: Position that is equivalent to the reference sequence position that is also given
- __annotation_id__
  - Type: [Annotation](#Annotation)
  - Description: Function that is found in the annotated amino acid or sub-sequence

  
### Annotation

- __protein_sequence_id__
  - Type: integer
  - Description: Start position of the annotation. A single start position without an end corresponds to a single amino acid
- __start_position__
  - Type: integer
  - Description: Optional end position if the annoation contains more than a single amino acid.
- __end_position__
  - Type: integer
  - Description: Optional end position if the annoation contains more than a single amino acid.
- __function__
  - Type: string
  - Description: Function that is found in the annotated amino acid or sub-sequence

 
