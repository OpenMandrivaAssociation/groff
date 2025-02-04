%define binpair() %{_bindir}/%{1}\
%doc %{_mandir}/man1/%{1}.1*\ %{nil}

%define short_ver %(echo %{version}|cut -d. -f1,2)
%bcond_with crosscompile

# Workaround for the dependency generator
# generating bogus dependencies on local
# perl files (that the provides: generator
# correctly doesn't pick up)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\([^.]*\\.pl\\)

%bcond_without x11

Summary:	Document formatting system
Name:		groff
Version:	1.23.0
Release:	1
License:	GPLv2+
Group:		Text tools
Url:		https://www.gnu.org/software/groff/
Source0:	ftp://ftp.gnu.org/gnu/groff/%{name}-%{version}.tar.gz
Source1:	troff-to-ps.fpi
Source100:	%{name}.rpmlintrc
Patch1:		groff-1.20.1-nroff-convert-encoding.patch
Patch2:		groff-1.23.0-clang.patch

BuildRequires:	ghostscript
BuildRequires:	imake
BuildRequires:	netpbm
BuildRequires:	psutils
BuildRequires:	bison
BuildRequires:	texinfo
Requires:	groff-base

%if %{with x11}
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xmu)
%endif

%if %{cross_compiling}
# When cross-compiling, we can't use the just-built groff...
BuildRequires:	groff-base groff-perl
%endif

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
%{binpair addftinfo}
%{binpair eqn2graph}
%{binpair gdiffmk}
%{binpair grap2graph}
%{binpair grn}
%{binpair grodvi}
%{binpair grolbp}
%{binpair grolj4}
%{binpair hpftodit}
%{binpair indxbib}
%{binpair lkbib}
%{binpair lookbib}
%{binpair neqn}
%{binpair pdfroff}
%{binpair pic}
%{binpair pic2graph}
%{binpair refer}
%{binpair soelim}
%{binpair tfmtodit}
%{_bindir}/post-grohtml
%{_bindir}/pre-grohtml
%if %{with x11}
%{binpair xtotroff}
%{_datadir}/groff/%{version}/font/devX100
%{_datadir}/groff/%{version}/font/devX100-12
%{_datadir}/groff/%{version}/font/devX75
%{_datadir}/groff/%{version}/font/devX75-12
%{_datadir}/groff/%{version}/font/FontMap-X11
%endif
%{_datadir}/groff/%{version}/eign
%{_datadir}/groff/%{version}/font/devcp1047
%{_datadir}/groff/%{version}/font/devdvi
%{_datadir}/groff/%{version}/font/devhtml
%{_datadir}/groff/%{version}/font/devlbp
%{_datadir}/groff/%{version}/font/devlj4
%{_datadir}/groff/%{version}/font/devps
%{_datadir}/groff/%{version}/font/devpdf
%{_datadir}/groff/%{version}/oldfont/devps
%{_datadir}/groff/%{version}/pic/chem.pic

%doc %{_infodir}/groff*
%doc %{_mandir}/man1/grohtml.1*
%doc %{_mandir}/man5/*
%doc %{_mandir}/man7/*

%package base
Summary:	Groff components required for viewing manpages
Group:		Text tools
%rename		groff-for-man
# preconv binary moved from older groff
# pfbtops binary moved from groff to base
# the only bin reqd by font-tools MD 2012/02
Conflicts:	groff < 1.21-4

%description base
The groff-base package contains the parts of the groff text processor
package that are required for viewing manpages.
For a full groff package, install package groff.

%files base
%{binpair eqn}
%{binpair groff}
%{binpair grops}
%{binpair grotty}
%{binpair nroff}
%{binpair pfbtops}
%{binpair preconv}
%{binpair tbl}
%{binpair troff}
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

%package perl
Summary:	Parts of the groff formatting system that require Perl
Group:		Text tools
Requires:	groff-base = %{EVRD}
Conflicts:	groff < 1.22.3-4

%description perl
The groff-perl package contains the parts of the groff text processor
package that require Perl. These include the afmtodit font processor for
creating PostScript font files, the grog utility that can be used to
automatically determine groff command-line options, and the troff-to-ps
print filter.

%files perl
%{binpair afmtodit}
%{binpair chem}
%{binpair glilypond}
%{binpair gperl}
%{binpair gpinyin}
%{binpair grog}
%{binpair gropdf}
%{binpair mmroff}
%{binpair pdfmom}
%{_libdir}/rhs/rhs-printfilters/troff-to-ps.fpi

%package gxditview
Summary:	X previewer for groff text processor output
Group:		Text tools
Requires:	groff-base = %{EVRD}

%description gxditview

Gxditview displays the groff text processor's output on an X Window
System display.

If you are going to use groff as a text processor, you should install
gxditview so that you preview your processed text files in X. You'll
also need to install the groff package and the X Window System.

%if %{with x11}
%files gxditview
%{binpair gxditview}
%{_prefix}/lib/X11/app-defaults/GXditview
%{_prefix}/lib/X11/app-defaults/GXditview-color
%endif

%package doc
Summary:	Documentation for %{name}
Group:		Development/Other
BuildArch:	noarch
Conflicts:	%{name} < 1.22.3-8

%description doc
Documentation for %{name}.

%files doc
%{_docdir}/groff-%{version}

%prep
%autosetup -p1

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
%make_build -j1 \
%if %{cross_compiling}
	GROFFBIN=%{_bindir}/groff \
	GROFF_BIN_PATH=%{_bindir}
%endif

%install
%make_install

mkdir -p %{buildroot}/%{_libdir}/rhs/rhs-printfilters
install -m755 %{SOURCE1} %{buildroot}/%{_libdir}/rhs/rhs-printfilters

# MD fix bad symlink
rm -f %{buildroot}/%{_datadir}/doc/groff-%{version}/pdf/mom-pdf.pdf
ln -s ../examples/mom/mom-pdf.pdf \
	%{buildroot}/%{_datadir}/doc/groff-%{version}/pdf/mom-pdf.pdf
