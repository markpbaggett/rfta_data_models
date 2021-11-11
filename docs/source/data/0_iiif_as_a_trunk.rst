RFTA and IIIF as a Trunk
========================

About
-----

This section provides an overview of this system, how it functions, and how we apply the concept of IIIF as a trunk to
the system.

What is IIIF as a Trunk
-----------------------

"IIIF as a Trunk" is and idea that originates from a presentation given at CNI in Fall 2020 by Esme Cowles and Mark
Matienzo. In `A Tree’s Strength Is Its Trunk: IIIF as Central Operational Infrastructure <https://www.cni.org/topics/standards/a-trees-strength-is-its-trunk-iiif-as-central-operational-infrastructure>`_,
Cowles and Matienzo discuss describe as a trunk and branches model with IIIF where digital objects are served by the
many IIIF API specifications to consuming applications. The `trunk` refers to IIIF and the `branch` is a consuming
application. Connected to a repository platform at its roots, information about the objects in the repository can be
published as IIIF and served to or embedded in many `branch` frontend applications for discovery and dissemination.

Our System in this Model
------------------------

"IIIF as a trunk" is applied to RFTA in this manner.

.. figure:: ../images/roots_trunk_branch.png
    :alt: Tree depicting RFTA as IIIF as a Trunk

    Apply IIIF as a Trunk to RFTA

=========
The Roots
=========

The `roots` of our system is our Fedora repository. All objects are stored here with all their related binaries. The
following sections describe how things are stored and how they relate to the rest of the project.

=========
The Trunk
=========

The `trunk` of our system is IIIF by way of `iiif_assemble <https://github.com/utkdigitalinitiatives/iiif_assemble>`_.
This application builds IIIF presenation manifests with links to IIIF image responses where necessary. The application
and how it consumes information from the repository is discussed later in a later chapter.

==========
The Branch
==========

The primary `branch` in this system is `canopy <https://github.com/utkdigitalinitiatives/canopy>`_.  Canopy is a Jamstack
that consumes IIIF presentation manifests, indexes metadata about them, and makes their content available through a viewer.
The application is discussed in the final chapter of this document.
