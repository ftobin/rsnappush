rsnappush(1) - rsync-based pushed incremental snapshot
============================

## SYNOPSIS

<code>**rsnappush** [**-h**] [**-r RSYNC_OPT**] [**-q**] *SOURCE_PATH* [*ACCOUNT:*]*DEST_PATH*</code>

## DESCRIPTION

**rsnappush** is a wrapper around rsync(1) to assist in file-level
incremental snapshots that are pushed to a destination.
Unchanged files are hard-linked.  Files are plainly laid
out in a directory for each snapshot: *DEST_PATH*/*backup-YYYYmmdd-HHMM*/
for easy access and restoration.

*SOURCE_PATH* is any local path.

*DEST_PATH* is a path, local or remote.  If remote, *ACCOUNT* specifies
an ssh(1)-compatible account description, such as *USER*@*HOST*.

Additionally, under *DEST_PATH* there is a *permissions*/ directory
created that has compressed output from getfacl(1).  setfacl(1) can be used
to restore permissions from this file once it is uncompressed.

## EXAMPLE

    rsnappush --rsync-opt=--partial-dir=/home/user2/rsync-partial \
              /home/user user2@remotehost:backups/


## OPTIONS

<code>**-h**, **--help**</code>
: display a help message

<code>**-r**, **--rsync-opt=RSYNC_OPT**</code>
: pass-thru options to rsync(1). Use the '=' syntax to pass through options,
and include prefixing dashes.  See [EXAMPLE][] for details.

<code>**-q**, **--quiet**</code>
: emit less output


## AUTHORS
rsnappush is written by Frank Tobin: <ftobin@neverending.org>, <https://www.neverending.org/>

rsnappush is released under the Mozilla Public License 2.0 <https://opensource.org/licenses/MPL-2.0>.

## SEE ALSO

rsync(1), ssh(1)
