Name:		texlive-makecookbook
Version:	49311
Release:	1
Summary:	Make a Cookbook
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makecookbook
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecookbook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecookbook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The makecookbook bundle contains the files needed to create a
nice quality family cookbook in a form ready to submit to most
print-on-demand companies. Modifiable choices have been made
regarding standard book features such as trim size, margins,
headers/footers, chapter heading formatting, front matter
(copyright page, table of contents, etc.) and back matter
(index). Commands and environments have been created to format
the food stories and recipes. The user will need to: supply
their own food stories and recipes(!), and install the needed
fonts. We assume a LuaTeX compile. Please note that no new
document class or package is included here. Rather, we provide
a modifiable preamble and a small number of other files that,
together, fully support creation of all of the internal pages
of a cookbook (i.e., everything except the cover art).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/lualatex/makecookbook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
