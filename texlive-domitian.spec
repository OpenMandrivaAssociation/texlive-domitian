%global tl_name domitian
%global tl_revision 77682
%global tl_version 1.0.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Drop-in replacement for Palatino
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/domitian
License:	lppl1.3c ofl other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/domitian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/domitian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The Domitian fonts are a free and open-source OpenType font family,
based on the Palatino design by Hermann Zapf (1918-2015), as implemented
in Palladio, the version distributed as part of URW's free Core 35
PostScript fonts (2.0). Domitian is meant as a drop-in replacement for
Adobe's version of Palatino. It extends Palladio with small capitals,
old-style figures and scientific inferiors. The metrics have been
adjusted to more closely match Adobe Palatino, and hinting has been
improved.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from domitian:
Map Domitian.map
TL_DROPIN_EOF
