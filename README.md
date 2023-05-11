**LOSSLESS VIDEO COMPRESSION**

**SYNOPSIS**

Today there is a growing need for Video Compression in order to reduce
file size on storage requirement. Higher compression ratio can be
achieved using lossy compression technique, but this will lead to loss
of information and may result in errors. Hence there is a need to store
video in lossless format. Traditional lossless compression technique
results in low compression ratio, the goal is to maximize the
compression using a lossless compression tool. HEVC encoding can
effectively exploit the temporal and spatial redundancy observed in
video sequence. This project outlines lossless encoding mode of HEVC. It
is prepared as the newest video coding standard of the ITU-T Video
Coding Experts Group and the ISO/IEC Moving Picture Experts Group.
Lossless compression is useful when it is necessary to minimize the
storage space or transmission bandwidth of data while still maintaining
archival quality. Many applications such as medical imaging,
preservation of artwork, image archiving, remote sensing, and image
analysis require the use of lossless compression, since these
applications cannot allow any distortion in the reconstructed images. As
the HEVC standard requires the video sequence in non-camera capture
format i.e. in YUV format, thus to encode the image sequence for camera
captured format, an internal conversion from RGB to YUV format is
required.

**EXISTING SYSTEM**

Huge software like Adobe Media Encoder is required to convert a video
file format but there may me slight quality reduction. Few existing web
video format converters are not efficient enough to convert without
quality loss under feasible timing.

**PROPOSED SYSTEM**

Lossless video compression is done just by Web UI platform. A video file
can be easily compressed without quality loss under less timing
(according to the Computer/Server's Speed).There are multiple mkv player
for all the Operating platform which makes not only easy to store
efficiently also to access and preview it faster.

**MODULE DESCRIPTION**

**Flask**

-   Flask is a micro web framework written in Python.

-   It is classified as a microframework because it does not require
    particular tools or libraries.

-   It has no database abstraction layer, form validation, or any other
    components where pre-existing third-party libraries provide common
    functions. However, Flask supports extensions that can add
    application features as if they were implemented in Flask itself.

-   Extensions exist for object-relational mappers, form validation,
    upload handling, various open authentication technologies and
    several common framework related tools.

Components

> **Werkzeug** is a utility library for the Python programming language
> for Web Server Gateway Interface (WSGI) applications. Werkzeug can
> instantiate objects for request, response, and utility functions. It
> can be used as the basis for a custom software framework and supports
> Python 2.7 and 3.5 and later.
>
> **Jinja** is a template engine for the Python programming language.
> Similar to the Django web framework, it handles templates in a
> sandbox.
>
> **MarkupSafe** is a string handling library for the Python programming
> language. The eponymous MarkupSafe type extends the Python string type
> and marks its contents as \"safe\"; combining MarkupSafe with regular
> strings automatically escapes the unmarked strings, while avoiding
> double escaping of already marked strings.
>
> **ItsDangerous** is a safe data serialization library for the Python
> programming language. It is used to store the session of a Flask
> application in a cookie without allowing users to tamper with the
> session contents.

**HEVC (.mkv) File Format**

An HEVC file contains a video stored in the High Efficiency Video Coding
(HEVC) format. This format, also known as H.265, improves over the H.264
standard by allowing videos to be stored with a lower file size but with
the same video quality. HEVC helps users store more videos on their
devices and also substantially reduces the file size of high-resolution
videos such as 4K and 8K videos.

It has higher compression compared to other formats which means that a
1-minute 4K video file recorded in the HEVC format will consume
relatively less storage space compared to the same video file recorded
in the regular H.264 format.

HEVC is the next generation compression
standard that offers a number of enhancements over AVC. HEVC compression
is 50% more efficient than AVC, which translates into maintaining the
same video quality at half the bitrate or double the video quality at
the same bitrate. The figure above represents the resolution: bitrate
ratio of different output qualities. In all categories, bandwidth costs
are significantly reduced while resolutions remain identical.

**FFmpeg**

FFmpeg is a collection of libraries and tools to process multimedia
content such as audio, video, subtitles and related metadata.

Convert a video file from one format to HEVC format (mp4 to mkv).

ffmpeg -i yourvideoname.mp4 -c:v libx264 outputfilename.mkv

The command above is an example of when converting a .mp4 file into a
.mkv file.

