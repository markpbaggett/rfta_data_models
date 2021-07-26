Understanding XACML Policies
============================

About
-----

Each oral history an attached :code:`POLICY` binary.  This file is based on the
`XACML 1.0 <https://www.oasis-open.org/committees/download.php/2406/oasis-xacml-1.0.pdf>`_ specification.  This section
describes how to interpret our :code:`POLICY` binaries and what information is meaningful for migration.

Deny Management Functions
-------------------------

Each XACML policy includes a "deny-management-functions" section that includes who can perform what Fedora actions.  It
includes roles and people.

For this project, this is not important to migration.

In the sample below, this section is present on lines 14 - 187.

Deny Access Functions
---------------------

Each XACML policy includes a "deny-access-functions" section that includes who can read the Fedora object.  It
includes roles and people.

For this project, this may be useful for migration as we have some objects that will need to be restricted for the
foreseeable future.

In the sample below, this section is present on lines 14 - 187.

.. literalinclude:: ../literals/policy.xml
    :language: xml
    :lines: 188-241

Relationship to the RELS-EXT
----------------------------

The RELS-EXT may include information regarding access or management, but due to some bugs with replacement, it should
not be relied on.

This is further influenced by the fact that the XACML policy is actually what is used -- not the triples in the RELS-EXT
datastream.

Full Sample
-----------

In case it's useful, a full XACML record can be found here:

.. literalinclude:: ../literals/policy.xml
    :language: xml
    :linenos:
