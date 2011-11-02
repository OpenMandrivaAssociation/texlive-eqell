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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides commands that give a well-spaced ellipsis
after !, ?, !? or ?!.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
