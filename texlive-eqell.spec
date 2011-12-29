# revision 22931
# category Package
# catalog-ctan /macros/latex/contrib/eqell
# catalog-date 2011-05-29 19:51:14 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-eqell
Version:	20110529
Release:	1
Summary:	Sympathetically spaced ellipsis after punctuation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eqell
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqell.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqell.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands that give a well-spaced ellipsis
after !, ?, !? or ?!.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eqell/eqell.sty
%doc %{_texmfdistdir}/doc/latex/eqell/README
%doc %{_texmfdistdir}/doc/latex/eqell/eqell.pdf
%doc %{_texmfdistdir}/doc/latex/eqell/eqell.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
