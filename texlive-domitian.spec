Name:		texlive-domitian
Version:	55286
Release:	2
Summary:	Drop-in replacement for Palatino
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/domitian
License:	lppl1.3c ofl other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/domitian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/domitian.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Domitian fonts are a free and open-source OpenType font
family, based on the Palatino design by Hermann Zapf
(1918-2015), as implemented in Palladio, the version
distributed as part of URW's free Core 35 PostScript fonts
(2.0). Domitian is meant as a drop-in replacement for Adobe's
version of Palatino. It extends Palladio with small capitals,
old-style figures and scientific inferiors. The metrics have
been adjusted to more closely match Adobe Palatino, and hinting
has been improved.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/domitian
%{_texmfdistdir}/fonts/vf/public/domitian
%{_texmfdistdir}/fonts/type1/public/domitian
%{_texmfdistdir}/fonts/tfm/public/domitian
%{_texmfdistdir}/fonts/opentype/public/domitian
%{_texmfdistdir}/fonts/map/dvips/domitian
%{_texmfdistdir}/fonts/enc/dvips/domitian
%doc %{_texmfdistdir}/doc/fonts/domitian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
