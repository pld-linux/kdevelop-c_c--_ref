Summary:	KDevelop-specific C and C++ reference HTML files
Summary(pl):	Dokumentacja C i C++ w HTML dla KDevelopa
Name:		kdevelop-c_c++_ref
Version:	2.0.2
Release:	1
Epoch:		0
License:	GPL
Group:		Documentation
Source0:	ftp://ftp.ee.fhm.edu/pub/unix/ide/KDevelop/c_cpp_reference-%{version}.tar.bz2
# Source0-md5:	3b9c51d73d2622ab51ae9d109c38bd61
Source1:	%{name}-snip_ex_index.html
Source2:	%{name}-c++_ex_index.html
Source3:	%{name}-OR_PRACTICAL_C_index.html
Source4:	%{name}-OR_USING_C_index.html
Patch0:		%{name}-broken_links.patch
URL:		http://www.kdevelop.org
BuildRequires:	code2html >= 0.9.1
Requires:	kdevelop
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_destinationdir	%{_docdir}/kde/HTML/en/kdevelop
%define	__code2html	"/usr/bin/code2html -v --fallback=plain"

%description
KDevelop is an easy to use IDE (Intergrated Development Enviroment)
for KDE/Unix/X11. At the moment there are only unstable
alpha-versions.

This package provides a C (v1.08) and C++ (0.1) reference from within
kdevelop, as written by Martin Leslie. The original files have been
rearranged to meet our needs.

%description -l pl
KDevelop jest prostym w u¿yciu IDE (zintegrownym ¶rodowiskiem
programistycznym) dla KDE/Unix/X11.

Ten pakiet dostarcza dokumentacjê C (w wersji 1.08) oraz C++ (0.1) do
u¿ywania z kdevelopem, napisan± przez Martina Leslie. Oryginalne pliki
zosta³y dostosowane do u¿ytku z kdevelopem.

%prep
%setup -q -n c_cpp_reference-%{version}
%patch0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_destinationdir}/
find $RPM_BUILD_DIR/c_cpp_reference-%{version}/reference -name "Makefile.*" \
	| xargs rm -f
cp -Rf $RPM_BUILD_DIR/c_cpp_reference-%{version}/reference \
		$RPM_BUILD_ROOT%{_destinationdir}/

# "htmlization":
cd $RPM_BUILD_ROOT%{_destinationdir}/reference
for a in `find . -type f -name "*.htm*"`
do
%{__perl} -pi -e 's/(href=.+\.c)(\"|>)/$1\.html$2/i;'	"$a"
%{__perl} -pi -e 's/(href=.+\.C)(\"|>)/$1\.html$2/i;'	"$a"
%{__perl} -pi -e 's/(href=.+\.cc)(\"|>)/$1\.html$2/i;'	"$a"
%{__perl} -pi -e 's/(href=.+\.cpp)(\"|>)/$1\.html$2/i;'	"$a"
%{__perl} -pi -e 's/(href=.+\.CC)(\"|>)/$1\.html$2/i;'	"$a"
%{__perl} -pi -e 's/(href=.+\.h)(\"|>)/$1\.html$2/i;'	"$a"
%{__perl} -pi -e 's/(href=.+\.asm)(\"|>)/$1\.html$2/i;'	"$a"
done

for a in `find . -type f	\
	-name "*.c"		\
	-or -name "*.cc"	\
	-or -name "*.C"		\
	-or -name "*.CC"	\
	-or -name "*.asm"	\
	-or -name "*.h"		`
do
	"%{__code2html}" "$a" "$a.html"
done

# adds html indexes for "htmlized" examples:
install %{SOURCE1} \
	$RPM_BUILD_ROOT%{_destinationdir}/reference/C/CONTRIB/SNIP/index.html
install %{SOURCE2} \
	$RPM_BUILD_ROOT%{_destinationdir}/reference/CPLUSPLUS/EXAMPLES/index.html
install %{SOURCE3} \
	$RPM_BUILD_ROOT%{_destinationdir}/reference/C/CONTRIB/OR_PRACTICAL_C/index.html
install %{SOURCE4} \
	$RPM_BUILD_ROOT%{_destinationdir}/reference/C/CONTRIB/OR_USING_C/index.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%{_docdir}/kde/HTML/en/kdevelop/reference/C/*
%{_docdir}/kde/HTML/en/kdevelop/reference/CPLUSPLUS
%{_docdir}/kde/HTML/en/kdevelop/reference/GRAPHICS
