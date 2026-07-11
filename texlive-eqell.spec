%global tl_name eqell
%global tl_revision 22931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Sympathetically spaced ellipsis after punctuation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eqell
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqell.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqell.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands that give a well-spaced ellipsis after !,
?, !? or ?!.

