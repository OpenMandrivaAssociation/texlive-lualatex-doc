# revision 30473
# category Package
# catalog-ctan /info/luatex/lualatex-doc
# catalog-date 2013-05-14 17:42:28 +0200
# catalog-license fdl
# catalog-version undef
Name:		texlive-lualatex-doc
Version:	20130514
Release:	1
Summary:	A guide to use of LaTeX with LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/luatex/lualatex-doc
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-doc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-doc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-doc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document is a map/guide to the world of LuaLaTeX. Coverage
supports both new users and package developers. Apart from the
introductory material, the document gathers information from
several sources, and offers links to others.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/lualatex/lualatex-doc/News
%doc %{_texmfdistdir}/doc/lualatex/lualatex-doc/README
%doc %{_texmfdistdir}/doc/lualatex/lualatex-doc/lualatex-doc.pdf
#- source
%doc %{_texmfdistdir}/source/lualatex/lualatex-doc/Makefile
%doc %{_texmfdistdir}/source/lualatex/lualatex-doc/lltxdoc.cls
%doc %{_texmfdistdir}/source/lualatex/lualatex-doc/lualatex-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}
