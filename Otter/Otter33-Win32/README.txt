        ------------------
        Otter, Version 3.3    Search for Proofs
        ------------------
        ------------------
        Mace,  Version 2.2    Search for Countermodels
        ------------------

     *****************************************
     * This version is for Microsoft Windows *
     *  For more information see index.html  *
     *****************************************

(Also see index.html in this directory.)

----------------
OTTER HIGHLIGHTS
----------------

Over the years we've added many experimental features to Otter,
but the basic functions haven't changed much in the past
ten years.

The Otter package now includes Mace 2 (as a separate program).

----------------
MACE2 HIGHLIGHTS
----------------

Mace2 is now an independent program.  It no longer calls Otter
to parse the input.  It still accepts the same inputs as Otter.
Performance is sometimes better than in previous versions
(see mace2/README.22).

----------------
DOCUMENTS
----------------

The documents directory contains a (newly updated) Otter 3.3
manual and a Mace 2.0 manual.  See documents/README.

----------------
FETCHING
----------------

Download Otter 3.3 and Mace 2.2 from the Otter Web page:

  http://www.mcs.anl.gov/AR/otter/

----------------
INSTALLING AND TESTING (for MS Windows)
----------------

Unzip the package.  This should produce a directory called Otter-Win32.
The binaries

    otter.exe*
    mace2.exe*
    anldp.exe*

should be in the directory Otter33-Win32\bin.

There is no GUI (yet?) for Otter, so it must be run from a command prompt.
Assuming you are in the directory Otter33-Win32, try the following.

    bin\otter < examples\auto\steam.in > temp1.out
    bin\mace2 -N6 -p < examples-mace2/basic/noncommutative_group.in > temp2.out

For normal use we recommend setting your PATH variable to include
the bin directory and runing the programs from the same directory as the
input files.  That way, the programs can be run, for example, as

    otter < p1.in > p1.out
    mace2 -N6 -p < p1.in > p1.out

The whole set of test problems is available via Otter33-Win32\index.html.

----------------
DISCLAIMER
----------------

I am not a MS Windows user, so I cannot provide much help on running
these programs in Windows.  For assistance, one can subscribe to the
otter-help mailing list (see the Otter Web page) and ask questions
there.

----------------

The Otter Web page is http://www.mcs.anl.gov/AR/otter/

  W. McCune
  Argonne National Laboratory
  August, 2003
