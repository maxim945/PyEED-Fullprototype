<h2 align="center">
  Markdown Example for sdRDM
</h2>

<p align="center"> 
This is an example of how to set up a data model using the Software-Driven Research Data Management (sdRDM) library which is based on abstract object models. Furthermore, the sdRDM library supports the conversion of data models defined in the Markdown format.</p>
 

Data models defined in the Markdown format follow these conventions:

- **Modules** are denoted by a heading level 1 ```#```
- **Objects** are started with a heading level 3 ```###``` 
- Each object contains **fields** in bold as a list &rarr; ```- __name__```
- **Required fields** are denoted with an asterix &rarr; ```- __name*__```
- Each field has **options** as a list of name to value mapping &rarr; ```- Type: string```

**Field options**

Each field in an object can hold options relevant for mapping to another data model (e.g. a standardized format) and general information such as its type and description. In the following is a collection of all native and required fields:

- **Type** - Required option to denote the data type. Please note, this can also contain other objects defined in this document.
- **Multiple** - Whether or not this field can contain multiple values. Setting to ```True```will result in a ```List[dtype]``` annoatation in the software.
- **Description** - Required option to describe the field. This should be a brief description that explains what the attribute is about.

**Inheritance**

In order to inherit attributes to another object, the object definition additionally includes the name of the parent object in italic wrapped with brackets:

&rarr; ```## Child [_Parent_]```

In the following an example data model is defined using above rules. Feel free to use this example also as a template for your own application.

---------
# Dataset

This is the place where you can describe the complete module/dataset and give information about all the details. Markdown offers a convenient way to enable as much space as needed to elucidate purpose and capabilities of your data model.

# Dataset

This is a Test dataset.

### ProteinSequence

- __name*__
  - Type: string
  - Description: Systematic name of the protein.
- __amino_acid_sequence*__
  - Type: string
  - Description: The amino acid sequence of the protein sequence object.

### Organism

- __ncbi_taxonomy_id*__
  - Type: string
  - Description: NCBI Taxonomy ID to identify the organism
- __name*__
  - Type: string
  - Description: Name of the annotated domain
  
### Annotation

- __start_position*__
  - Type: integer
  - Description: Start position of the annotation. A single start position without an end corresponds to a single amino acid
- __end_position__
  - Type: integer
  - Description: Optional end position if the annoation contains more than a single amino acid.
- __function*__
  - Type: string
  - Description: Function that is found in the annotated amino acid or sub-sequence
