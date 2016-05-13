# layer-dokuwiki

DokuWiki charm layer for Juju.

## Usage

To build the charm:

`charm build`

To deploy it:

`juju deploy $JUJU_REPOSITORY/trusty/dokuwiki --series trusty`
`juju expose dokuwiki`

Once the dokuwiki service is in the `active` state, you should be able to access it by pointing a browser at the public address for dokuwiki/0. Hurray!

## Considerations

Currently, this charm won't scale out - DokuWiki uses local flat-file storage instead of an external database. In theory, it might be possible to store DokuWiki data on NFS and support scaling that way; I haven't tried.
