Summary:	KDevelop-specific C and C++ reference HTML files
Summary(pl):	Dokumentacja C i C++ w HTML dla KDevelopa
Name:		kdevelop-c_c++_ref
Version:	2.0.2
Release:	1
License:	GPL
Group:		Documentation
Vendor:		Sandy Meier <smeier@rz.uni-potsdam.de>
Source0:	ftp://ftp.ee.fhm.edu/pub/unix/ide/KDevelop/c_cpp_reference-%{version}.tar.gz
URL:		http://www.cs.uni-potsdam.de/~smeier/kdevelop/
Requires:	kdevelop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

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
kde_htmldir="%{_htmldir}"; export kde_htmldir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_htmldir}/en/kdevelop/*
