%global tl_name domitian
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Drop-in replacement for Palatino
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/domitian
License:	lppl1.3c ofl other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/domitian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/domitian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Domitian fonts are a free and open-source OpenType font family,
based on the Palatino design by Hermann Zapf (1918-2015), as implemented
in Palladio, the version distributed as part of URW's free Core 35
PostScript fonts (2.0). Domitian is meant as a drop-in replacement for
Adobe's version of Palatino. It extends Palladio with small capitals,
old-style figures and scientific inferiors. The metrics have been
adjusted to more closely match Adobe Palatino, and hinting has been
improved.

