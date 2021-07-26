Transcript and Transcript-ES
============================

About
-----

This document includes information about the TRANSCRIPT and TRANSCRIPT-ES datastreams.

Every oral history should have a TRANSCRIPT in English that should be used for closed captioning and a searchable index.
If the oral history was conducted in Spanish, it will also have a TRANSCRIPT-ES.

Expectations for Delivery
-------------------------

Since the beginning, we intended to do this project in `IIIF presentation v3 <https://iiif.io/api/presentation/3.0/>`_.
To understand expectations for delivery, here is `one of our sample manifests for RFTA in Mirador <https://projectmirador.org/embed/?iiif-content=https://raw.githubusercontent.com/markpbaggett/utk_iiif_recipes/main/raw_manifests/rfta_video.json>`_.

It only has a transcript in English, so you do not see Spanish as an option when you click the captioning button.
Furthermore, since captions should be optional, you have to click it to turn that on.

This is being done currently following the IIIF specification. A full sample of the manifest is below.  The important
bit here though is on lines 66-82:

.. literalinclude:: ../literals/rfta_video.json
    :lines: 66-82
    :language: json
    :emphasize-lines: 4, 6, 11

You can see that the canvas has a `W3C Web Annotation <https://www.w3.org/TR/annotation-model/>`_ with a label of
captions in English targetting the canvas. It has a motivation of supplmenting to suggest that it can be optionally
rendered by the viewer.

This is unlike the Annotation that paints the actual audio or video to the viewer since it should always be displayed.

.. literalinclude:: ../literals/rfta_video.json
    :lines: 51-65
    :emphasize-lines: 4, 6, 14
    :language: json

If this also had a Spanish transcript, we'd have another W3C Web Annotation with the motivation of :code:`supplementing`,
a different label, and a different language. The target is the same.

Full Sample
-----------

If useful, a full sample can be found here:

.. literalinclude:: ../literals/rfta_video.json
    :language: json

