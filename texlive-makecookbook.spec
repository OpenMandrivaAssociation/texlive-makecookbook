%global tl_name makecookbook
%global tl_revision 49311

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.85
Release:	%{tl_revision}.1
Summary:	Make a Cookbook
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/makecookbook
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecookbook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makecookbook.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The makecookbook bundle contains the files needed to create a nice
quality family cookbook in a form ready to submit to most print-on-
demand companies. Modifiable choices have been made regarding standard
book features such as trim size, margins, headers/footers, chapter
heading formatting, front matter (copyright page, table of contents,
etc.) and back matter (index). Commands and environments have been
created to format the food stories and recipes. The user will need to:
supply their own food stories and recipes(!), and install the needed
fonts. We assume a LuaTeX compile. Please note that no new document
class or package is included here. Rather, we provide a modifiable
preamble and a small number of other files that, together, fully support
creation of all of the internal pages of a cookbook (i.e., everything
except the cover art).

