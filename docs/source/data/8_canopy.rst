Canopy
======

About
-----

Digital Initiatives maintains a standalone Jamstack application that reads in and indexes IIIF presentation v3 manifests
for audio and video objects and serves them with an in house built viewer. The application is called
`canopy <https://github.com/utkdigitalinitiatives/canopy>`_.

The name is derived from a departmental mantra where we see IIIF as our "trunk" for serving data from our repository to
many frontends. This idea originates from a presentation given at CNI in Fall 2020 by Esme Cowles and Mark Matienzo. In
`A Tree’s Strength Is Its Trunk: IIIF as Central Operational Infrastructure <https://www.cni.org/topics/standards/a-trees-strength-is-its-trunk-iiif-as-central-operational-infrastructure>`_,
Cowles and Matienzo discuss what they describe as a trunk and branches model with IIIF. The `trunk` are the many IIIF API
specifications. Connected to a repository platform at its roots, information about the objects in the repository can be
published as IIIF and served to and embedded in many `branch` frontend applications for discovery and dissemination.

Using the many IIIF specifications, we felt we could serve our content to a variety of applications. Until we were able
to launch a new digital collections platform, this meant we needed a `branch` application for the audio and video oral histories
in this collection. To solve this problem, we developed a new application called `canopy` to serve our content to the
outside world.

This section describes this application and its relationship to the Rising from the Ashes project specifically.

Canopy and its Relationship to our Repository
---------------------------------------------

Canopy and its relationship to our repository can be understood in the `IIIF as a Trunk` model.

.. image:: ../images/roots_trunk_branch.png

In this model, our Fedora 3.8 repository stores the oral history objects and its associated binary files and metadata.
I like to think about this as the `roots` of our tree.

IIIF Presentation and Image built by iiif_assemble are the `trunk` of the tree and feeds our frontend application.

Canopy is the `branch` and presents our objects to the outside world.

The Canopy Stack
----------------

Canopy is a `Jamstack <https://jamstack.org/>`_ built with Gatsby, React, HTML 5, GraphQL, Lunr, and IIIF presentation v3.
The application has a config file that generates a site from `IIIF Presentation v3 collection manifest
<https://github.com/utkdigitalinitiatives/canopy/blob/f44316878c27436d209b7c118b1f7a92d8691cfc/gatsby-node.js#L13>`_.

When the site is `"built"`, each manifest mentioned in that manifest is indexed in the stacks GraphQL and Lunr index.
Static HTML pages are created and cached from the build process for performance reasons.

Canopy defines many components that leverage aspects from these manifests. These are described below:
