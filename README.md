# A Whole-Brain Map and Assay Parameter Analysis of Mouse VTA Dopaminergic Activation

These are the content files used to generate scientific communication materials for the project originally titled “Opto-fMRI of the VTA” (opfvta).

## Dependencies

A full list of unambiguously identified dependency constraints is specified [here](.gentoo/sci-publications/opfvta/opfvta-99999.ebuild) (following the [Package Manager Specification format](https://dev.gentoo.org/~ulm/pms/head/pms.html#x1-690008.2)).
On a Gentoo Linux system, dependencies can be automatically managed with the included install script:

```
su -
cd /path/to/opfvta
cd .gentoo
./install.sh
```

### Manual Data Download (only if automated Gentoo dependency management is unavailable)

While other dependencies will very likely be available from your distribution's own package manager, the data package of this publication is probably not.
You can manually install it via the following commands:

```
wget chymera.eu/distfiles/opfvta_bidsdata-2.0.tar.xz
tar xf opfvta_bidsdata-2.0.tar.xz
mv opfvta_bidsdata-2.0 /usr/share/opfvta_bidsdata
```

The latter command may require superuser access.
Total install time will take upwards of an hour on personal computers with no prior neuroimaging software deployment.

## Compilation Instructions

This is a [RepSeP](https://github.com/TheChymera/RepSeP)-style document.
The data processing step is run asynchronously from the document compilation, and you may choose to reproduce either the top-level statistics (“demo” reproduction) or the entire analysis starting from the raw data (“full analysis stack” reproduction).

The data processing for the full analysis stack will by default take place in `~/.scratch`.
The analysis requires just under 200GB available storage space.
If this is unavailable in the home partition we suggest creating a symlink to a volume which meets this requirement:

```
mkdir /mnt/largevolume/.scratch
ln -s /mnt/largevolume/.scratch ~/.scratch
```

### Top-Level Analysis

```
cd /path/to/opfvta
./compile.sh
```

This analysis may take up to 20 minutes on personal computers.

### Full Analysis Stack

```
cd /path/to/opfvta
./produce.sh
```

This analysis may take over 24 hours on personal computers.
