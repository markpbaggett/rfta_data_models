Understanding the Fedora Object
===============================

About
-----

All objects related to RFTA are managed in a Fedora 3.8.1 repository with Islandora 7.

This page describes the content model of an RFTA oral history and the unique datastreams related to each Fedora object.
If the datastream is more than a binary and needs further explanation, it is hyperlinked and described in future pages.

Unique Datastreams
------------------

Each Fedora object may have these unique datastreams.

* `RELS-EXT <2_rels_ext.html>`__: includes information about the object and its external relationships including the colleciton it belongs to, its content model, and any current permissions.
* `MODS <3_understanding_the_mods.html>`__: this is our source of descriptive metadata and includes information to navigate to specific portions of video.
* DC:  this datastream is generated automatically but is not needed for migration. We do not need this in the new system.
* OBJ: this is the preservation object regardless of its content model / work type.  We add to Fedora for preservation activities and its synced to DuraCloud.
* `POLICY <4_policy.html>`__: this is typically the file that we use to describe read and write permissions. Unlike the RELS-EXT, it's where the magic actually happens.
* TECHMD:  This is a xml document that includes technical metadata about the OBJ datastream specifically.  It is not useful for migration as Islandora only cares about capturing this for the OBJ.
* MP4: If the content model (work type) is video, this is the access proxy.  It originates from the preservation OBJ, but includes human edited content that the preservation object does not have.  In other words, we can't generate from OBJ directly.
* `TRANSCRIPT <5_transcripts.html>`__: All audio and videos have an attached webVTT file in English that serves as a captioning document. The intent is to allow close captioning in English and a searchable transcript.
* `RELS-INT <6_rels_int.html>`__: Each audio and video oral history has a RELS-INT file that states the duration of the oral history's access proxy (MP4 or Proxy_MP3).
* BIOFORM: Each oral history has a bioform.  This is important for preservation but should not be accessible to the public.
* RELEASE: Each oral history that is public has a signed release form.  This is important for preservation but should not be accessible to the public.
* TN: Each oral history has a machine generated thumbnail.  This is not needed.
* PROXY_MP3: If the content model (work type) is audio, this is the access proxy.
* `TRANSCRIPT-ES <5_transcripts.html>`__: Oral histories conducted in Spanish have an English and a Spanish vtt file that is relevant for closed captioning and a searchable transcript.


