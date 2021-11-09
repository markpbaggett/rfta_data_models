Internal Relationships and RELS-INT
===================================

About
-----

Each Oral History has a bit of RDF serialized as rdf/xml that descibes the duration of the access proxy. It is available
in the :code:`RELS-INT` datastream.

Here is an example:

.. literalinclude:: ../literals/rels_int.xml
    :language: xml

While its serialed as XML, it's arguably easier to understand once the data is converted to ttl:

.. code-block:: turtle

    @prefix ns0: <http://id.loc.gov/ontologies/bibframe/#> .

    <info:fedora/rfta:74/MP4> ns0:duration "00:36:28" .

This is done this way because Fedora 3 doesn't treat files as graphs.  Thus, if you need to make a statement about a
part, you do it here with the subject of the triple being the PID plus the datastream ( :code:`<info:fedora/rfta:74/MP4>` ).

Since this is a video oral history, we can see that its MP4 access proxy has a :code:`bibframe:duration` of "00:36:28".

This is generated on ingest and is used in the outgoing preservation manifest where it is converted to seconds.

.. literalinclude:: ../literals/rfta_video.json
    :language: json
    :lines: 41-46

Since this data is not elsewhere, it may be useful to start with this here rather than regenerate on your ingest.
