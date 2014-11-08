%define short_ver %(echo %{version}|cut -d. -f1,2)
%bcond_with	crosscompile

Summary:	Document formatting system
Name:		groff
Version:	1.22.3
Release:	1
License:	GPLv2+
Group:		Text tools
Url:		http://www.gnu.org/software/groff/
Source0:	ftp://ftp.gnu.org/gnu/groff/%{name}-%{version}.tar.gz
Source1:	troff-to-ps.fpi
Source100:	%{name}.rpmlintrc
Patch1:		groff-1.20.1-nroff-convert-encoding.patch

BuildRequires:	ghostscript
BuildRequires:	imake
BuildRequires:	netpbm
BuildRequires:	psutils
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xmu)
Requires:	groff-base

%track
prog %{name} = {
	url = http://ftp.gnu.org/gnu/groff/
	version = %version
	regex = %{name}-(__VER__)\.tar\.gz
}

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
%{_bindir}/gropdf
%{_bindir}/hpftodit
%{_bindir}/indxbib
%{_bindir}/lkbib
%{_bindir}/lookbib
%{_bindir}/neqn
%{_bindir}/pdfroff
%{_bindir}/pdfmom
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
%{_datadir}/groff/%{version}/font/devpdf
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
%{_mandir}/man1/gropdf.*
%{_mandir}/man1/hpftodit.*
%{_mandir}/man1/indxbib.*
%{_mandir}/man1/lkbib.*
%{_mandir}/man1/lookbib.*
%{_mandir}/man1/neqn.*
%{_mandir}/man1/pdfroff.*
%{_mandir}/man1/pdfmom.*
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

%package base
Summary:	Groff components required for viewing manpages
Group:		Text tools
%rename groff-for-man
# preconv binary moved from older groff
# pfbtops binary moved from groff to base
# the only bin reqd by font-tools MD 2012/02
Conflicts:	groff < 1.21-4

%description base
The groff-base package contains the parts of the groff text processor
package that are required for viewing manpages.
For a full groff package, install package groff.

%files base
%{_bindir}/eqn
%{_bindir}/groff
%{_bindir}/grops
%{_bindir}/grotty
%{_bindir}/nroff
%{_bindir}/pfbtops
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
%dir %{_libdir}/groff
%{_libdir}/groff/groff_opts_no_arg.txt
%{_libdir}/groff/groff_opts_with_arg.txt
%{_mandir}/man1/eqn.*
%{_mandir}/man1/groff.*
%{_mandir}/man1/grops.*
%{_mandir}/man1/grotty.*
%{_mandir}/man1/pfbtops.*
%{_mandir}/man1/preconv.*
%{_mandir}/man1/nroff.*
%{_mandir}/man1/tbl.*
%{_mandir}/man1/troff.*

%package perl
Summary:	Parts of the groff formatting system that require Perl
Group:		Text tools
Requires:	groff-base = %{version}-%{release}

%description perl
The groff-perl package contains the parts of the groff text processor
package that require Perl. These include the afmtodit font processor for
creating PostScript font files, the grog utility that can be used to
automatically determine groff command-line options, and the troff-to-ps
print filter.

%files perl
%{_bindir}/gperl
%{_bindir}/gpinyin
%{_bindir}/glilypond
%{_bindir}/afmtodit
%{_bindir}/grog
%{_bindir}/mmroff
%{_libdir}/rhs/rhs-printfilters/troff-to-ps.fpi
%{_libdir}/groff/grog
%{_libdir}/groff/glilypond
%{_libdir}/groff/gpinyin
%{_mandir}/man1/afmtodit.*
%{_mandir}/man1/gperl.1*
%{_mandir}/man1/grog.*
%{_mandir}/man1/mmroff.*
%{_mandir}/man1/gpinyin.1*
%{_mandir}/man1/glilypond.1*

%package gxditview
Summary:	X previewer for groff text processor output
Group:		Text tools
Requires:	groff-base = %{version}-%{release}

%description gxditview

Gxditview displays the groff text processor's output on an X Window
System display.

If you are going to use groff as a text processor, you should install
gxditview so that you preview your processed text files in X. You'll
also need to install the groff package and the X Window System.

%files gxditview
%{_bindir}/gxditview
%{_libdir}/X11/app-defaults/GXditview
%{_libdir}/X11/app-defaults/GXditview-color
%{_mandir}/man1/gxditview.*

%prep
%setup -q
%apply_patches
%if %{with crosscompile}
sed -i \
    -e '/^GROFFBIN=/s:=.*:=%{_bindir}/groff:' \
    -e '/^TROFFBIN=/s:=.*:=%{_bindir}/troff:' \
    -e '/^GROFF_BIN_PATH=/s:=.*:=%{_bindir}:' \
    -e '/^GROFF_BIN_DIR=/s:=.*:=%{_bindir}:' \
    contrib/*/Makefile.sub \
    doc/Makefile.in \
    doc/Makefile.sub
%endif

%build
%configure --with-appresdir=%{_libdir}/X11/app-defaults
# Parallel build is broken as of 1.22.3
make

%install
%makeinstall_std

mkdir -p %{buildroot}/%{_libdir}/rhs/rhs-printfilters
install -m755 %{SOURCE1} %{buildroot}/%{_libdir}/rhs/rhs-printfilters

# MD fix bad symlink
rm -f %{buildroot}/%{_datadir}/doc/groff-%version/pdf/mom-pdf.pdf
ln -s ../examples/mom/mom-pdf.pdf \
	%{buildroot}/%{_datadir}/doc/groff-%version/pdf/mom-pdf.pdf

