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
URL:		http://www.kdevelop.org
BuildRequires:	autoconf, automake, code2html
Requires:	kdevelop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	__code2html	/usr/bin/code2html

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

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/kde
mv $RPM_BUILD_ROOT%{_docdir}/HTML $RPM_BUILD_ROOT%{_docdir}/kde/

cd $RPM_BUILD_ROOT%{_docdir}/kde/HTML/en/kdevelop/reference
 for a in `find . -type f -name "*.htm*"`
 do 
	%{__perl} -pi -e 's/(href=\".*\.c)\"/$1\.html\"/i;' $a
 	%{__perl} -pi -e 's/(href=\".*\.cc)\"/$1\.html\"/i;' $a
 done
 for a in `find . -type f -name "*.c"`
 do
 	%{__code2html} $a $a.html
	rm -f $a
 done
 for a in `find . -type f -name "*.cc"`
 do
	%{__code2html} $a $a.html
	rm -f $a
 done

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc AUTHORS INSTALL
%{_docdir}/kde/HTML/en/kdevelop/reference/C/*
%{_docdir}/kde/HTML/en/kdevelop/reference/CPLUSPLUS
%{_docdir}/kde/HTML/en/kdevelop/reference/GRAPHICS
