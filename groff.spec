# rh-1.18-3
# deb-1.18-4

Summary:	Document formatting system
Name:		groff
Version:	1.19.1
Release:	%mkrel 10
License:	GPLv2+
Group:		Text tools
BuildRequires:	autoconf
BuildRequires:	byacc
BuildRequires:	imake
BuildRequires:	gccmakedep
BuildRequires:	netpbm
BuildRequires:	netpbm-devel
BuildRequires:	texinfo >= 4.3
BuildRequires:	xpm-devel
BuildRequires:	libxaw-devel
BuildRequires:	perl-devel
BuildRequires:	ghostscript
# For psselect:
BuildRequires:	psutils
# for rman:
BuildRequires:	x11-server-common
URL:		http://www.gnu.org/directory/GNU/groff.html
Source0:	ftp://prep.ai.mit.edu/pub/gnu/groff/%name-%version.tar.bz2
Source1:	troff-to-ps.fpi
Source2:	README.A4
# nippon/multi-byte support from http://people.debian.org/~ukai/groff/
Patch3:		groff-1.19.1-mb.patch
Patch4:		groff-1.18-info.patch
Patch5:		groff-1.19.1-nohtml.patch
Patch6:		groff-1.17.2-libsupc++.patch
Patch7:		groff-1.19.1-nops.patch
Patch8:		groff-1.19.1-fonts.patch
Patch102:	groff-1.16.1-no-lbp-on-alpha.patch
# improved (i18n) nroff script
Patch108:	groff-1.19-nroff.patch
# keeps apostrophes and dashes as ascii, but only for man pages
# -- pablo
Patch109:	groff-1.19-dashes.patch
Patch110:	groff-1.19.1-CAN-2004-0969.patch
Patch111:	groff-1.19.1-lzma-support.patch

Requires:	mktemp 
Requires:	groff-for-man = %{version}-%{release}
Buildroot:	%_tmppath/%name-root
Obsoletes:	groff-tools
Provides:	groff-tools
Requires(post,preun):	info-install

%description
Groff is a document formatting system.  Groff takes standard text and
formatting commands as input and produces formatted output.  The
created documents can be shown on a display or printed on a printer. 
Groff's formatting commands allow you to specify font type and size, bold
type, italic type, the number and size of columns on a page, and more.

You should install groff if you want to use it as a document formatting
system.  Groff can also be used to format man pages. If you are going
to use groff with the X Window System, you'll also need to install the
groff-gxditview package.

%package for-man
Summary: Required for viewing manpages
Group: Text tools
Conflicts: groff < 1.19.1-5

%description for-man
The groff-for-man package contains the parts of the groff text processor
package that are required for viewing manpages.
For a full groff package, install package groff.

%package perl
Summary: Parts of the groff formatting system that require Perl
Group: Text tools
Requires: groff-for-man = %{version}-%{release}

%description perl
The groff-perl package contains the parts of the groff text processor
package that require Perl. These include the afmtodit font processor
for creating PostScript font files, the grog utility that can be used
to automatically determine groff command-line options, and the
troff-to-ps print filter.

%package gxditview
Summary:	X previewer for groff text processor output
Group:		Text tools
Requires: groff-for-man = %{version}-%{release}
# Avoid problems with symlinks during transition - groff-gxditview used
# to think it owned /usr/lib/X11 directory (that now is a symlink to /etc/X11).
Requires(pre): x11-server-common >= 1.4.0.90-13mdv

%description gxditview
Gxditview displays the groff text processor's output on an X Window
System display.

If you are going to use groff as a text processor, you should install
gxditview so that you preview your processed text files in X.  You'll also
need to install the groff package and the X Window System.

%prep

%setup -q
%patch3 -p1 -b ._utf8
%patch4 -p1
%patch5 -p1 -b .nohtml
%patch6 -p1 -b .libsupc++
%patch7 -p1 -b .nops
%patch8 -p1 -b ._fonts
%ifarch alpha
%patch102 -p1 -b .alpha
%endif
%patch108 -p1 -b ._nroff
%patch109 -p1 -b ._dashes
%patch110 -p1 -b .can-2004-0969
%patch111 -p1 -b .lzma_support

cp -f %SOURCE2 ./

autoconf

%build
export MAKEINFO=$HOME/cvs/texinfo/makeinfo/makeinfo
%configure2_5x --enable-multibyte
make top_builddir=$PWD top_srcdir=$PWD
cd doc
makeinfo groff.texinfo
cd ../src/xditview
xmkmf
perl -p -i -e "s|CXXDEBUGFLAGS = .*|CXXDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile
perl -p -i -e "s|CDEBUGFLAGS = .*|CDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile
perl -p -i -e "s|XAPPLOADDIR = .*|XAPPLOADDIR = %{_datadir}/X11/app-defaults|" Makefile
make depend
%make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%_prefix,%_infodir,%_bindir,%_docdir/%name/%version/html/momdoc}
%makeinstall manroot=%buildroot/%_mandir top_builddir=$PWD top_srcdir=$PWD common_words_file=$RPM_BUILD_ROOT%_datadir/%name/%version mkinstalldirs=mkdir
install -m 644 doc/groff.info* $RPM_BUILD_ROOT/%_infodir
pushd src/xditview
%makeinstall DESTDIR=$RPM_BUILD_ROOT

# A link to ../../../etc/X11/app-defaults is made
APPDEF=%{buildroot}%{_libdir}/X11/app-defaults
if   [ -L $APPDEF ]; then rm    $APPDEF
elif [ -d $APPDEF ]; then rmdir $APPDEF
fi

popd
for i in s.tmac mse.tmac m.tmac; do
	ln -s $i $RPM_BUILD_ROOT%_datadir/groff/%version/tmac/g$i
done
for i in troff tbl pic eqn neqn refer lookbib indxbib soelim nroff; do
	ln -s $i $RPM_BUILD_ROOT/%_bindir/g$i
done

# Build system is compressing man-pages
for i in eqn.1 indxbib.1 lookbib.1 nroff.1 pic.1 refer.1 soelim.1 tbl.1 troff.1; do
		ln -s $i%{_extension} $RPM_BUILD_ROOT/%_mandir/man1/g$i%{_extension}
done

mkdir -p $RPM_BUILD_ROOT/%_libdir/rhs/rhs-printfilters
install -m755 %{SOURCE1} $RPM_BUILD_ROOT/%_libdir/rhs/rhs-printfilters

# call spec-helper before creating the file list
%{?__spec_helper_post}

cat <<EOF > groff.list
/%_datadir/groff/%version/eign
/%_datadir/groff/%version/font/devX100
/%_datadir/groff/%version/font/devX100-12
/%_datadir/groff/%version/font/devX75
/%_datadir/groff/%version/font/devX75-12
/%_datadir/groff/%version/font/devdvi
/%_datadir/groff/%version/font/devhtml
/%_datadir/groff/%version/font/devlbp
/%_datadir/groff/%version/font/devlj4
/%_datadir/groff/%version/font/devps
EOF

cat <<EOF > groff-for-man.list
%_bindir/eqn
%_bindir/troff
%_bindir/nroff
%_bindir/tbl
%_bindir/geqn
%_bindir/gtbl
%_bindir/gnroff
%_bindir/grotty
%_bindir/groff
%_bindir/gtroff
%dir %_datadir/groff
%dir %_datadir/groff/%version
%_datadir/groff/%version/tmac
%dir %_datadir/groff/%version/font
%_datadir/groff/%version/font/devascii
%_datadir/groff/%version/font/devascii8
%_datadir/groff/%version/font/devlatin1
%_datadir/groff/%version/font/devnippon
%_datadir/groff/%version/font/devutf8
%dir %_datadir/groff/site-tmac
%_datadir/groff/site-tmac/man.local
%_datadir/groff/site-tmac/mdoc.local
EOF

cat <<EOF > groff-perl.list
%_bindir/grog
%_bindir/mmroff
%_bindir/afmtodit
%_mandir/man1/afmtodit.*
%_mandir/man1/grog.*
%_mandir/man1/mmroff.*
EOF

dirs=usr/share/man/*
(cd $RPM_BUILD_ROOT ; find usr/bin usr/share/man usr/share/groff/%version/tmac ! -type d -printf "/%%p\n" | grep -v gxditview) >> %name.list
(cd $RPM_BUILD_ROOT ; find usr/share/groff/%version/tmac/* -type d -printf "%%%%dir /%%p\n") >> %name.list

perl -ni -e 'BEGIN { open F, "%{name}-for-man.list"; $s{$_} = 1 foreach <F>; } print unless $s{$_}' %name.list
perl -ni -e 'BEGIN { open F, "%{name}-perl.list"; $s{$_} = 1 foreach <F>; } print unless $s{$_}' %name.list
# japanese environment is crazy; doc.tmac seems superior than docj.tmac
ln -sf doc.tmac $RPM_BUILD_ROOT/usr/share/groff/%version/tmac/docj.tmac

for i in $(find $RPM_BUILD_ROOT -empty -type f); do echo " ">> $i;done

# cleanup
rm -rf %{buildroot}%{_docdir}/groff

%files -f groff.list
%defattr(-,root,root)
%doc BUG-REPORT NEWS PROBLEMS README README.A4 TODO VERSION
%_infodir/groff*

%files for-man -f groff-for-man.list
%defattr(-,root,root)

%files perl -f groff-perl.list
%defattr(-,root,root)
%_libdir/rhs/*/*

%files gxditview
%defattr(-,root,root)
%doc VERSION
%_bindir/gxditview
%{_datadir}/X11/app-defaults/GXditview

%post
%_install_info %name

%preun
%_remove_install_info %name


%clean
rm -rf $RPM_BUILD_ROOT
