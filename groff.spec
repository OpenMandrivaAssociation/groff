Name:       groff
Version:    1.21
Release:    4

License:    GPLv2+
URL:        http://www.gnu.org/software/groff/

Source0:    ftp://ftp.gnu.org/gnu/groff/%{name}-%{version}.tar.gz
Source1:    troff-to-ps.fpi
Patch1:     groff-1.20.1-nroff-convert-encoding.patch

BuildRequires: netpbm
BuildRequires: libxaw-devel
BuildRequires: libxmu-devel
BuildRequires: psutils
BuildRequires: ghostscript
BuildRequires: imake

#------------------------------------------------------------------------------#

# package groff

Summary: Document formatting system
Group:   Text tools

Requires: groff-for-man
Requires: sed

%description
Groff is a document formatting system. Groff takes standard text and
formatting commands as input and produces formatted output. The created
documents can be shown on a display or printed on a printer. Groff's
formatting commands allow you to specify font type and size, bold type,
italic type, the number and size of columns on a page, and more.

You should install groff if you want to use it as a document formatting
system. Groff can also be used to format man pages. If you are going to
use groff with the X Window System, you'll also need to install the
groff-gxditview package.

%files
%defattr(-,root,root)
%{_bindir}/addftinfo
%{_bindir}/chem
%{_bindir}/eqn2graph
%{_bindir}/gdiffmk
%{_bindir}/grap2graph
%{_bindir}/grn
%{_bindir}/grodvi
%{_bindir}/groffer
%{_bindir}/grolbp
%{_bindir}/grolj4
%{_bindir}/hpftodit
%{_bindir}/indxbib
%{_bindir}/lkbib
%{_bindir}/lookbib
%{_bindir}/neqn
%{_bindir}/pdfroff
%{_bindir}/pfbtops
%{_bindir}/pic
%{_bindir}/pic2graph
%{_bindir}/post-grohtml
%{_bindir}/pre-grohtml
%{_bindir}/roff2dvi
%{_bindir}/roff2html
%{_bindir}/roff2pdf
%{_bindir}/roff2ps
%{_bindir}/roff2text
%{_bindir}/roff2x
%{_bindir}/refer
%{_bindir}/soelim
%{_bindir}/tfmtodit
%{_bindir}/xtotroff
%{_libdir}/groff/groffer
%{_datadir}/groff/%{version}/eign
%{_datadir}/groff/%{version}/font/devX100
%{_datadir}/groff/%{version}/font/devX100-12
%{_datadir}/groff/%{version}/font/devX75
%{_datadir}/groff/%{version}/font/devX75-12
%{_datadir}/groff/%{version}/font/devdvi
%{_datadir}/groff/%{version}/font/devhtml
%{_datadir}/groff/%{version}/font/devlbp
%{_datadir}/groff/%{version}/font/devlj4
%{_datadir}/groff/%{version}/font/devps
%{_datadir}/groff/%{version}/oldfont/devps
%{_datadir}/groff/%{version}/pic/chem.pic
%{_docdir}/groff-%{version}
%{_infodir}/groff*
%{_mandir}/man1/addftinfo.*
%{_mandir}/man1/chem.*
%{_mandir}/man1/eqn2graph.*
%{_mandir}/man1/gdiffmk.*
%{_mandir}/man1/grap2graph.*
%{_mandir}/man1/grn.*
%{_mandir}/man1/grodvi.*
%{_mandir}/man1/groffer.*
%{_mandir}/man1/grohtml.*
%{_mandir}/man1/grolbp.*
%{_mandir}/man1/grolj4.*
%{_mandir}/man1/hpftodit.*
%{_mandir}/man1/indxbib.*
%{_mandir}/man1/lkbib.*
%{_mandir}/man1/lookbib.*
%{_mandir}/man1/neqn.*
%{_mandir}/man1/pdfroff.*
%{_mandir}/man1/pfbtops.*
%{_mandir}/man1/pic.*
%{_mandir}/man1/pic2graph.*
%{_mandir}/man1/refer.*
%{_mandir}/man1/roff2dvi.*
%{_mandir}/man1/roff2html.*
%{_mandir}/man1/roff2ps.*
%{_mandir}/man1/roff2pdf.*
%{_mandir}/man1/roff2text.*
%{_mandir}/man1/roff2x.*
%{_mandir}/man1/soelim.*
%{_mandir}/man1/tfmtodit.*
%{_mandir}/man1/xtotroff.*
%{_mandir}/man5/*
%{_mandir}/man7/*

#------------------------------------------------------------------------------#

%package for-man

Summary: Groff components required for viewing manpages
Group:   Text tools

# preconv binary moved from older groff
Conflicts: groff < 1.20.1-2mdv

%description for-man
The groff-for-man package contains the parts of the groff text processor
package that are required for viewing manpages.
For a full groff package, install package groff.

%files for-man
%defattr(-,root,root)
%{_bindir}/eqn
%{_bindir}/groff
%{_bindir}/grops
%{_bindir}/grotty
%{_bindir}/nroff
%{_bindir}/preconv
%{_bindir}/tbl
%{_bindir}/troff
%{_datadir}/groff/current
%dir %{_datadir}/groff
%dir %{_datadir}/groff/%{version}
%{_datadir}/groff/%{version}/tmac
%dir %{_datadir}/groff/%{version}/font
%{_datadir}/groff/%{version}/font/devascii
%{_datadir}/groff/%{version}/font/devlatin1
%{_datadir}/groff/%{version}/font/devutf8
%dir %{_datadir}/groff/site-tmac
%{_datadir}/groff/site-tmac/man.local
%{_datadir}/groff/site-tmac/mdoc.local
%{_mandir}/man1/eqn.*
%{_mandir}/man1/groff.*
%{_mandir}/man1/grops.*
%{_mandir}/man1/grotty.*
%{_mandir}/man1/preconv.*
%{_mandir}/man1/nroff.*
%{_mandir}/man1/tbl.*
%{_mandir}/man1/troff.*

#------------------------------------------------------------------------------#

%package perl

Summary:  Parts of the groff formatting system that require Perl
Group:    Text tools
Requires: groff-for-man = %{version}-%{release}

%description perl
The groff-perl package contains the parts of the groff text processor
package that require Perl. These include the afmtodit font processor for
creating PostScript font files, the grog utility that can be used to
automatically determine groff command-line options, and the troff-to-ps
print filter.

%files perl
%defattr(-,root,root)
%{_bindir}/afmtodit
%{_bindir}/grog
%{_bindir}/mmroff
%{_libdir}/rhs/rhs-printfilters/troff-to-ps.fpi
%{_mandir}/man1/afmtodit.*
%{_mandir}/man1/grog.*
%{_mandir}/man1/mmroff.*

#------------------------------------------------------------------------------#

%package gxditview

Summary:  X previewer for groff text processor output
Group:    Text tools
Requires: groff-for-man = %{version}-%{release}

%description gxditview

Gxditview displays the groff text processor's output on an X Window
System display.

If you are going to use groff as a text processor, you should install
gxditview so that you preview your processed text files in X. You'll
also need to install the groff package and the X Window System.

%files gxditview
%defattr(-,root,root)
%{_bindir}/gxditview
%{_libdir}/X11/app-defaults/GXditview
%{_libdir}/X11/app-defaults/GXditview-color
%{_mandir}/man1/gxditview.*

#------------------------------------------------------------------------------#

%prep

%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %{buildroot}/%{_libdir}/rhs/rhs-printfilters
install -m755 %{SOURCE1} %{buildroot}/%{_libdir}/rhs/rhs-printfilters


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.21-2mdv2011.0
+ Revision: 664926
- mass rebuild

* Tue Jan 18 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.21-1
+ Revision: 631539
- New version: 1.21

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.20.1-3mdv2011.0
+ Revision: 605499
- rebuild

* Fri Dec 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.20.1-2mdv2010.1
+ Revision: 476536
- Move preconv to groff-for-man (#56264)

* Tue Nov 24 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.20.1-1mdv2010.1
+ Revision: 469749
- New version: 1.20.1
  Moved all the old patches to SOURCES/old-patches
  Added a patch for i18n inside nroff
  Added a a string-format-error patch (already applied upstream)
  Spec file was completly rewritten

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.19.1-15mdv2010.0
+ Revision: 425044
- rebuild

* Sat Mar 28 2009 Funda Wang <fwang@mandriva.org> 1.19.1-14mdv2009.1
+ Revision: 361868
- BR libxp

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1.19.1-13mdv2009.1
+ Revision: 316958
- rediffed fuzzy patches
- fix build with -Werror=format-security (P112)

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.19.1-12mdv2009.0
+ Revision: 264609
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.19.1-11mdv2009.0
+ Revision: 202094
- Fix x86_64 build. Should test for /usr/lib instead of %%{_libdir} for the
  directory that should not be created, neither owned by this package.
- Don't explicitly BuildRequires x11-server-common, rman is long gone,
  and modify/fix versioning Requires(pre) of x11-server-common.
- Install resources file in proper directory and don't try to be owner
  of it. x11-server-common is now the owner package of {some-base}/X11
  shared directories.

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.19.1-8mdv2008.1
+ Revision: 170876
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.19.1-7mdv2008.1
+ Revision: 126307
- kill re-definition of %%buildroot on Pixel's request
- kill file require on info-install
- fix man pages

  + Pixel <pixel@mandriva.com>
    - spec-helper script is no more, use the rpm macro instead

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild for 2008
    - drop unnecessary /usr/X11R6 stuff
    - use Fedora license policy
    - clean dependencies
    - spec clean

  + Oden Eriksson <oeriksson@mandriva.com>
    - fix build deps
    - nuke installed docs

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - add lzma support (P111)

  + Funda Wang <fwang@mandriva.org>
    - bunzip2 the patches

  + Andreas Hasenack <andreas@mandriva.com>
    - Import groff



* Mon Sep 18 2006 Pablo Saratxaga <pablo@mandriva.com> 1.19.1-6mdv2007.0
- better dependencies
- added some "u####" to devutf8 font files

* Sat Sep 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.19.1-5mdv2007.0
- fix update (#25792)

* Wed Sep 12 2006 Pablo Saratxaga <pablo@mandriva.com> 1.19.1-4mdv
- integrated multibyte/utf-8 patch

* Thu Mar 09 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.19.1-3mdk
- patch 109: fix CAN-2004-0969
- use %%mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.19.1-2mdk
- Rebuild

* Mon Jun 13 2005 Götz Waschk <waschk@mandriva.org> 1.19.1-1mdk
- spec cleanup
- replace prereq by new syntax
- drop patch 7
- update patch 5
- New release 1.19.1

* Mon Dec 13 2004 Götz Waschk <waschk@linux-mandrake.com> 1.19-9mdk
- fix buildrequires

* Tue Nov  9 2004 Pixel <pixel@mandrakesoft.com> 1.19-8mdk
- make groff depends on groff-for-man = VERSION-RELEASE
- explict groff-for-man conflict with older groff (because of eqn)

* Tue Nov  9 2004 Pixel <pixel@mandrakesoft.com> 1.19-7mdk
- move eqn to groff-for-man (needed by OpenGL manpages: glBegin...) (bugzilla #4241)

* Tue Aug  3 2004 Stefan van der Eijk <stefan@mandrake.org> 1.19-6mdk
- remove BuildRequires: texinfo < 4.7

* Fri Jun  4 2004  <lmontel@n2.mandrakesoft.com> 1.19-5mdk
- Rebuild

* Wed Jun  2 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.19-4mdk
- merge from amd64-branch: build fixes

* Thu Aug 21 2003 Pablo Saratxaga <pablo@@mandrakesoft.com> 1.19-3mdk
- keep dashes and apostrophes as ascii for man pages in UTF-8 (bug #4212)

* Wed Jul 30 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.19-2mdk
- BuildRequires: netpbm-devel, texinfo >= 4.3

* Wed Jul 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.19-1mdk
- new release
- update patch 3, 107 and 108 (but disable them for now due to build system
  issues)
- fix builrequires

* Thu Feb 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.18.1-5mdk
- patch 108 : fix warnings from pablo fix for utf-8 output

* Fri Jan 31 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 1.18.1-4mdk
- as groff can't handle properly utf-8, the nroff script is modified to
  run groff in the known locale, then convert to utf-8 the output.
- added to files sections a few missing directories

* Mon Jan 20 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.18.1-3mdk
- build release
- add missing info files

* Wed Nov 13 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.18.1-2mdk
- freshen patch 3 (multi byte support)

* Tue Nov 05 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.18.1-1mdk
- new release
- rediff patch 3
- remove patches 110, 111 & 112 (merged upstream)
- simplify %%install
- fix hardcoded version number
- fix url
- add japanese patch link

* Sat Oct 12 2002 Stefan van der Eijk <stefan@eijk.nu> 1.18-4mdk
- BuildRequires: texinfo

* Tue Sep 24 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.18-3mdk
- BuildRequires: libnetpbm9-devel, which grabs libnetpbm9 that
  contains necessary libpnm.so.9 library.
- Patch6: libgroff.a contains C++ code thus we may need to link with
  g++.  That patch was already there but Titi decided to nuke the
  1.17.2-13mdk release when he merged his stuff for 1.18.

* Tue Aug 13 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.18-2mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Tue Aug 13 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.18-1mdk
- new release:
	o colour support (although see below).
	o new macro set, mom, mainly for non-scientific writers. The aim of	these
	  macros is to make groff accessible for ordinary use with a minimum of
	  convoluted syntax.
	o 'eu' and 'Eu' characters available for Euro support.
	o improved support for TeX hyphenation files.
	o new means of setting the line length, which now works for -mdoc manual
	  pages as well as -man. Use man-db >= 2.4.0 to take advantage of this.
	o documentation of the differences between groff and Unix troff is now in
	  groff_diff(7).
	o groff_mwww(1) has been renamed to groff_www(1).
	o groff_ms(7) has been completely rewritten.
	o new scripts: groffer, pic2graph, and eqn2graph.
	o substantial improvements in grohtml (although it's still alpha),
	  including dealing with overstriking properly
- drop patches 5, 6 (merged upstream), 3 (better fix)
- remove useless prefix
- move mdk patches in the 10x area
- patch3: add japanase support
- patch4: fix info name
- patch5: don't build html files
- Prereq: /sbin/install-info
- process texinfo file into info one, and install it
- add %%post and %%postun to install and remove info file
- fix japanese problem: link docj.tmac to doc.tma
- rediff koi8 patch (russian support)
- mmroff.7 is now mmroff.1
- patch110: kill warnings, fix build on non-intel boxes
- patch111: make sure pointsize is initialized properly, thus fixing an
  infinite loop in the ia64 build
- patch112: freeze unbreakable spaces, preventing a failed assertion on
  latin1(7)
- add /usr/share/groff/font/devascii8 to groff-for-man and remove charon fix
- add /usr/share/groff/font/devnippon for japanese support
- add lot of docs

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.17.2-12mdk
- Automated rebuild with gcc3.2

* Sat May 11 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.17.2-11mdk
- gcc-3.1 build

* Wed Apr 17 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.17.2-10mdk
- fix build with gcc-3.1

* Wed Mar 06 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.17.2-9mdk
- fix \' in latin1 (pixel)
- use WANT_AUTOCONF_2_5 with generic autoconf for lord gc

* Mon Feb 25 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.17.2-8mdk
- from Andrej Borsenkow:
	* use configure2_5x
	* require autconf-2.5x due to patch7
	* patch7 - support for koi8-r. Code based on patch in FreeBSD,
	  most credits to Ruslan Ermilov <ru@FreeBSD.org>

* Tue Feb  5 2002 Vincent Danen <vdanen@mandrakesoft.com> 1.17.2-7mdk
- remove patch4 since it breaks html formatting (mkstemp not appropriate in
  this situation... bad snailtalk)

* Wed Jan 30 2002 Vincent Danen <vdanen@mandrakesoft.com> 1.17.2-6mdk
- patch5 for security
- patch6 to fix segfault with pic in some instances

* Tue Oct 30 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.17.2-5mdk
- remove useless %%define

* Wed Oct 10 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.17.2-4mdk
- remove safer patch since it was included in mainstream sources
- Provides:   groff-tools

* Fri Sep 07 2001 Stefan van der Eijk <stefan@eijk.nu> 1.17.2-3mdk
- BuildRequires: byacc
- Removed redundant BuildRequires.

* Mon Aug 06 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.17.2-2mdk
- add LICENSE in %%docdir

* Wed Jul 18 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.17.2-1mdk
- new release

* Wed Jul  4 2001 Pixel <pixel@mandrakesoft.com> 1.17.1-2mdk
- add an-old.tmac to groff-for-man

* Sat Jun 30 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.17.1-1mdk
- 1.17.1 bumped out into cooker.
- Remove the groff safer patch. Seems to have been incorporated into the
  source already.
- src/preproc/html/pre-html.cc: s/mktemp()/mkstemp()/;
- s/Copyright/License/;

* Tue May 15 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.16.1-10mdk
- change default from -Tascii to -Tlatin1 in /usr/bin/nroff (so man pages
  in non-latin1 can still be displayed on screen as previously)
- add /usr/share/groff/font/devutf8 to groff-for-man (we are going utf-8...)

* Mon May  7 2001 Pixel <pixel@mandrakesoft.com> 1.16.1-9mdk
- add /usr/share/groff/tmac/tmac.latin1 to groff-for-man

* Fri May  4 2001 Pixel <pixel@mandrakesoft.com> 1.16.1-8mdk
- add /usr/bin/nroff and tmac.tty-char to groff-for-man so that man works again

* Tue Dec 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.16.1-7mdk
- Don't build grolbp on alpha.

* Thu Nov 09 2000 David BAUDENS <baudens@mandrakesoft.com> 1.16.1-6mdk
- BuildRequires: XFree86

* Fri Nov 03 2000 Florin Grad <florin@mandrakesoft.com> 1.16.1-5mdk
- recompiled with gcc 2.96

* Wed Sep  6 2000 Pixel <pixel@mandrakesoft.com> 1.16.1-4mdk
- add tman.doc and mdoc to groff-for-man for ssh man page

* Sat Sep  2 2000 Pixel <pixel@mandrakesoft.com> 1.16.1-3mdk
- move important stuff for view man pages in groff-for-man

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.16.1-2mdk
- automatically added BuildRequires

* Thu Aug  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.16.1-1mdk
- 1.16.1.

* Thu Jul 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.16-1mdk
- Remove %%{config} for app-default file.
- Merge rh changes.
- Add perl pacakge.
- BM.
- 1.16.

* Sun May 13 2000 David BAUDENS <baudens@mandrakesoft.com> 1.15-4mdk
- Fix build for i486
- Use %%{_tmppath} for BuildRoot

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.15-3mdk
- Fix rpmlint error/warning.

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.15-2mdk
- Add debian patch to display kanji.
- Adjust groups.

* Mon Jan  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.15-1mdk
- 1.15.

* Thu Oct 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix building as user.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- fix handling of RPM_OPT_FLAGS

* Tue Feb 16 1999 Cristian Gafton <gafton@redhat.com>
- glibc 2.1 patch for xditview (#992)

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- fix makefiles to work with bash2

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use g++ for C++ code

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- manhattan and buildroot

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- made xdefaults file a config file

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- split perl components into separate subpackage

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated to 1.11a
- added safe troff-to-ps.fpi

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- removed troff-to-ps.fpi for security reasons.

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc
