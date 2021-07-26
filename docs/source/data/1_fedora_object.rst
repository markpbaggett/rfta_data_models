Understanding the Fedora Object
===============================

About
-----

This page describes the unique datastreams related to a Fedora object.

Unique Datastreams
------------------

Each Fedora object may have these unique datastreams.

* `RELS-EXT <2_rels_ext.html>`__: includes information about the object and its external relationships including the colleciton it belongs to, its content model, and any current permissions.
* `MODS <3_understanding_the_mods.html>`__: this is our source of descriptive metadata and includes information to navigate to specific portions of video.
* DC:  this datastream is generated automatically but is not needed for migration. We do not need this in the new system.
* OBJ: this is the preservation object regardless of its content model / work type.  We add to Fedora for preservation activities and its synced to DuraCloud.
* POLICY
* TECHMD
* MP4: If the content model (work type) is video, this is the access proxy.  It originates from the preservation OBJ, but includes human edited content that the preservation object does not have.  In other words, we can't generate from OBJ directly.
* TRANSCRIPT
* RELS-INT
* BIOFORM
* RELEASE
* TN
* PROXY_MP3: If the content model (work type) is audio, this is the access proxy.
* TRANSCRIPT-ES


