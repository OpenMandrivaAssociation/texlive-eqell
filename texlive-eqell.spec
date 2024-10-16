Name:		texlive-eqell
Version:	22931
Release:	2
Summary:	Sympathetically spaced ellipsis after punctuation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eqell
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqell.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eqell.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
