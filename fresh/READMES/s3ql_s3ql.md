..
  NOTE: We cannot use sophisticated ReST syntax here because this
  file is rendered by GitHub.

======
 S3QL
======

S3QL is a file system that stores all its data online using storage
services like `Google Storage`_, `Amazon S3`_, or OpenStack_. S3QL
effectively provides a virtual drive of dynamic, infinite capacity that
can be accessed from any computer with internet access.

S3QL is a standard conforming, full featured UNIX file system that is
conceptually indistinguishable from any local file system.
Furthermore, S3QL has additional features like compression,
encryption, data de-duplication, immutable trees and snapshotting
which make it especially suitable for online backup and archival.

S3QL is designed to favor simplicity and elegance over performance and
feature-creep. Care has been taken to make the source code as
readable and serviceable as possible. Solid error detection and error
handling have been included from the very first line, and S3QL comes
with extensive automated test cases for all its components.

.. _`Google Storage`: https://cloud.google.com/storage/docs
.. _`Amazon S3`: https://aws.amazon.com/s3/
.. _OpenStack: https://www.openstack.org/software/


Features
========

* **Transparency.** Conceptually, S3QL is indistinguishable from a
  local file system. For example, it supports hardlinks, symlinks,
  standard unix permissions, extended attributes and file
  sizes up to 2 TB.

* **Dynamic Size.** The size of an S3QL file system grows and shrinks
  dynamically as required.

* **Compression.** Before storage, all data may be compressed with the
  LZMA, bzip2 or deflate (gzip) algorithm.

* **Encryption.** After compression (but before upload), all data can be
  AES encrypted with a 256 bit key. An additional SHA256 HMAC checksum
  is used to protect the data against manipulation.

* **Data De-duplication.** If several files have identical contents,
  the redundant data will be stored only once. This works across all
  files stored in the file system, and also if only some parts of the
  files are identical while other parts differ.

* **Immutable Trees.** Directory trees can be made immutable, so that
  their contents can no longer be changed in any way whatsoever. This
  can be used to ensure that backups can not be modified after they
  have been made.

* **Copy-on-Write/Snapshotting.** S3QL can replicate entire directory
  trees without using any additional storage space. Only if one of the
  copies is modified, the part of the data that has been modified will
  take up additional storage space. This can be used to create
  intelligent snapshots that preserve the state of a directory at
  different points in time using a minimum amount of space.

* **High Performance independent of network latency.** All operations
  that do not write or read file contents (like creating directories
  or moving, renaming, and changing permissions of files and
  directories) are very fast because they are carried out without any
  network transactions.

  S3QL achieves this by saving the entire file and directory structure
  in a database. This database is locally cached and the remote
  copy updated asynchronously.

* **Support for low bandwidth connections.** S3QL splits file contents
  into smaller blocks and caches blocks locally. This minimizes both
  the number of network transactions required for reading and writing
  data, and the amount of data that has to be transferred when only
  parts of a file are read or written.


Development Status
==================

S3QL is considered stable and suitable for production use.  Starting
with version 2.17.1, S3QL uses semantic versioning. This means that
backwards-incompatible versions (e.g., versions that require an
upgrade of the file system revision) will be reflected in an increase
of the major version number.


Supported Platforms
===================

S3QL is developed and tested under Linux. Users have also reported
running S3QL successfully on OS-X, FreeBSD and NetBSD. We try to
maintain compatibility with these systems, but (due to lack of
pre-release testers) we cannot guarantee that every release will run
on all non-Linux systems. Please report any bugs you find, and we will
try to fix them.


Typical Usage
=============

Before a file system can be mounted, the backend which will hold the
data has to be initialized. This is done with the *mkfs.s3ql*
command. Here we are using the Amazon S3 backend, and
*nikratio-s3ql-bucket* is the S3 bucket in which the file system will
be stored. ::

  mkfs.s3ql s3://ap-south-1/nikratio-s3ql-bucket

To mount the S3QL file system stored in the S3 bucket
*nikratio_s3ql_bucket* in the directory ``/mnt/s3ql``, enter::

  mount.s3ql s3://ap-south-1/nikratio-s3ql-bucket /mnt/s3ql

Now you can instruct your favorite backup program to run a backup into
the directory ``/mnt/s3ql`` and the data will be stored on Amazon
S3. When you are done, the file system has to be unmounted with ::

   umount.s3ql /mnt/s3ql


Need Help?
==========

The following resources are available:

* The `S3QL User's Guide`_.
* The `S3QL Wiki`_
* The `S3QL Mailing List`_. You
  can subscribe by sending a mail to
  `s3ql+subscribe@googlegroups.com <mailto:s3ql+subscribe@googlegroups.com>`_.

Please report any bugs you may encounter in the `GitHub Issue Tracker`_.

Contributing
============

The S3QL source code is available on GitHub_.

.. _`S3QL User's Guide`: https://www.rath.org/s3ql-docs/
.. _`S3QL Wiki`: https://github.com/s3ql/s3ql/wiki
.. _`S3QL Mailing List`: https://groups.google.com/g/s3ql
.. _`GitHub Issue Tracker`: https://github.com/s3ql/s3ql/issues
.. _GitHub: https://github.com/s3ql/main
