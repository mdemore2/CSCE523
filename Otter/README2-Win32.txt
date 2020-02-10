        ------------------
        Otter, Version 3.3    Search for Proofs
        ------------------
        ------------------
        Mace,  Version 2.2    Search for Countermodels
        ------------------

(Also see index.html in this directory.)

Here is a quickstart guide contributed by a Windows-Otter user.

1.  Extract the files using the stored path information; notice where
otter.exe is stored.

2.  Get a command prompt by choosing "Command prompt" from Start |
Programs or from Start | Programs | Accessories (depending on the
version of Windows), and navigate to the folder containing otter.exe
If you do not know how to navigate to a specified folder from the
command prompt, then you can run Otter from Start | Run by browsing to
the desired folder.

3.  Otter expects input.  Normally one supplies this input in a file,
so the command to run Otter needs to mention this file, as in

    otter  <  myfile.in

Input files by convention end in ".in".  If you are running Otter from
Start | Run, then after browsing to otter.exe you will have to type in
"< myfile.in" at the end (without the quotes).  Windows is not
case-sensitive so you can capitalize "Otter" if you wish.

4.  Check that everything is working by running otter on one of the
test files supplied with Otter:

    otter <  cn19.in

You should see some output flashing by, then hear two beeps in quick
succession (That's Otter telling you it found a proof.)  Then you
should see a proof on your screen followed by some statistics about
the Otter run.

5.  The output of otter is usually too long to fit conveniently on one
screen, so it is often directed to an output file:

    otter < myfile.in > myfile.out

Try this by giving the command

    otter < cn19.in > cn19.out

Edit the file cn19.out to see Otter's complete output.

6.  You can edit the input and output files with any text editor.
However, when doing so be careful to save them as file type "all
files" to avoid accidentally saving your changes as myfile.in.txt
instead of myfile.in

7.  OK, you've installed Otter correctly.  The manuals and
test problems for Otter and Mace2 can be found via the file
index.html in the main Otter directory.
