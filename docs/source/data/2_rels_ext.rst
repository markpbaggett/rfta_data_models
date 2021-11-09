External Relationships & RELS-EXT
=================================

About
-----

The RELS-EXT datastream describes each oral history and its relationship to other objects in our repository. It is
serialized as rdf/xml and looks like something like this:

.. code-block:: xml

    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:fedora="info:fedora/fedora-system:def/relations-external#" xmlns:fedora-model="info:fedora/fedora-system:def/model#" xmlns:islandora="http://islandora.ca/ontology/relsext#">
      <rdf:Description rdf:about="info:fedora/rfta:8">
        <fedora:isMemberOfCollection rdf:resource="info:fedora/collections:rfta"></fedora:isMemberOfCollection>
        <fedora-model:hasModel rdf:resource="info:fedora/islandora:sp_videoCModel"></fedora-model:hasModel>
        <islandora:inheritXacmlFrom rdf:resource="info:fedora/collections:rfta"></islandora:inheritXacmlFrom>
        <islandora:isViewableByUser>bdysonsm</islandora:isViewableByUser>
        <islandora:isViewableByUser>comyn7</islandora:isViewableByUser>
        <islandora:isViewableByUser>epatric1</islandora:isViewableByUser>
        <islandora:isViewableByUser>ltrott1</islandora:isViewableByUser>
        <islandora:isViewableByUser>mbagget1</islandora:isViewableByUser>
        <islandora:isViewableByUser>mhale16</islandora:isViewableByUser>
        <islandora:isViewableByUser>mjorda</islandora:isViewableByUser>
        <islandora:isViewableByUser>fedoraAdmin</islandora:isViewableByUser>
        <islandora:isViewableByUser>islandora</islandora:isViewableByUser>
        <islandora:isViewableByRole>administrator</islandora:isViewableByRole>
        <islandora:isManageableByUser>bdysonsm</islandora:isManageableByUser>
        <islandora:isManageableByUser>comyn7</islandora:isManageableByUser>
        <islandora:isManageableByUser>epatric1</islandora:isManageableByUser>
        <islandora:isManageableByUser>islandora</islandora:isManageableByUser>
        <islandora:isManageableByUser>ltrott1</islandora:isManageableByUser>
        <islandora:isManageableByUser>mbagget1</islandora:isManageableByUser>
        <islandora:isManageableByUser>mhale16</islandora:isManageableByUser>
        <islandora:isManageableByUser>mjorda</islandora:isManageableByUser>
        <islandora:isManageableByUser>fedoraAdmin</islandora:isManageableByUser>
        <islandora:isManageableByRole>administrator</islandora:isManageableByRole>
      </rdf:Description>
    </rdf:RDF>

In order to talk about this more concisely and clearly, I have converted the above to ttl:

.. code-block:: turtle

    @prefix ns0: <info:fedora/fedora-system:def/relations-external#> .
    @prefix ns1: <info:fedora/fedora-system:def/model#> .
    @prefix ns2: <http://islandora.ca/ontology/relsext#> .

    <info:fedora/rfta:8>
      ns0:isMemberOfCollection <info:fedora/collections:rfta> ;
      ns1:hasModel <info:fedora/islandora:sp_videoCModel> ;
      ns2:inheritXacmlFrom <info:fedora/collections:rfta> ;
      ns2:isViewableByUser "bdysonsm", "comyn7", "epatric1", "ltrott1", "mbagget1", "mhale16", "mjorda", "fedoraAdmin", "islandora" ;
      ns2:isViewableByRole "administrator" ;
      ns2:isManageableByUser "bdysonsm", "comyn7", "epatric1", "islandora", "ltrott1", "mbagget1", "mhale16", "mjorda", "fedoraAdmin" ;
      ns2:isManageableByRole "administrator" .

The following sections will break this down so that we can share what's important here.

Understanding Content Model
---------------------------

.. code-block:: turtle
    :linenos:
    :emphasize-lines: 7

    @prefix ns0: <info:fedora/fedora-system:def/relations-external#> .
    @prefix ns1: <info:fedora/fedora-system:def/model#> .
    @prefix ns2: <http://islandora.ca/ontology/relsext#> .

    <info:fedora/rfta:8>
      ns0:isMemberOfCollection <info:fedora/collections:rfta> ;
      ns1:hasModel <info:fedora/islandora:sp_videoCModel> ;
      ns2:inheritXacmlFrom <info:fedora/collections:rfta> ;
      ns2:isViewableByUser "bdysonsm", "comyn7", "epatric1", "ltrott1", "mbagget1", "mhale16", "mjorda", "fedoraAdmin", "islandora" ;
      ns2:isViewableByRole "administrator" ;
      ns2:isManageableByUser "bdysonsm", "comyn7", "epatric1", "islandora", "ltrott1", "mbagget1", "mhale16", "mjorda", "fedoraAdmin" ;
      ns2:isManageableByRole "administrator" .

First, the `ns1:hasModel` value has one of two values as its object:

1. info:fedora/islandora:sp-audioCModel
2. info:fedora/islandora:sp_videoCModel

info:fedora/islandora:sp-audioCModel means it should be treated as an audio work type, and info:fedora/islandora:sp_videoCModel means
it should be treated as a video work type.

Understanding Relationship to its Collection
--------------------------------------------

All Rising from the Ashes objects are available in one collection for discovery.

This is handled by the RELS-EXT in line six and interpreted by our web application:

.. code-block:: turtle
    :linenos:
    :emphasize-lines: 6

    @prefix ns0: <info:fedora/fedora-system:def/relations-external#> .
    @prefix ns1: <info:fedora/fedora-system:def/model#> .
    @prefix ns2: <http://islandora.ca/ontology/relsext#> .

    <info:fedora/rfta:8>
      ns0:isMemberOfCollection <info:fedora/collections:rfta> ;
      ns1:hasModel <info:fedora/islandora:sp_videoCModel> ;
      ns2:inheritXacmlFrom <info:fedora/collections:rfta> ;
      ns2:isViewableByUser "bdysonsm", "comyn7", "epatric1", "ltrott1", "mbagget1", "mhale16", "mjorda", "fedoraAdmin", "islandora" ;
      ns2:isViewableByRole "administrator" ;
      ns2:isManageableByUser "bdysonsm", "comyn7", "epatric1", "islandora", "ltrott1", "mbagget1", "mhale16", "mjorda", "fedoraAdmin" ;
      ns2:isManageableByRole "administrator" .

Parts that Should Not Matter for Migration
------------------------------------------

While we currently have the objects, we are restricting them from access.  This is done with the POLICY datastream.
Unfortunately, Islandora, our current respository, adds triples that describe the policy when its created but it doesn't
modify these when the POLICY is changed or removed.  Because of this, we consider these triples inaccurate and misleading.

.. code-block:: turtle
    :linenos:
    :emphasize-lines: 8-12

    @prefix ns0: <info:fedora/fedora-system:def/relations-external#> .
    @prefix ns1: <info:fedora/fedora-system:def/model#> .
    @prefix ns2: <http://islandora.ca/ontology/relsext#> .

    <info:fedora/rfta:8>
      ns0:isMemberOfCollection <info:fedora/collections:rfta> ;
      ns1:hasModel <info:fedora/islandora:sp_videoCModel> ;
      ns2:inheritXacmlFrom <info:fedora/collections:rfta> ;
      ns2:isViewableByUser "bdysonsm", "comyn7", "epatric1", "ltrott1", "mbagget1", "mhale16", "mjorda", "fedoraAdmin", "islandora" ;
      ns2:isViewableByRole "administrator" ;
      ns2:isManageableByUser "bdysonsm", "comyn7", "epatric1", "islandora", "ltrott1", "mbagget1", "mhale16", "mjorda", "fedoraAdmin" ;
      ns2:isManageableByRole "administrator" .