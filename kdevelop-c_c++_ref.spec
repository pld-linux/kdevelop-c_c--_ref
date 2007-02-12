Summary:	KDevelop-specific C and C++ reference HTML files
Summary(pl.UTF-8):   Dokumentacja C i C++ w HTML dla KDevelopa
Name:		kdevelop-c_c++_ref
Version:	0.1
Release:	1
License:	GPL
Group:		Documentation
Vendor:		Sandy Meier <smeier@rz.uni-potsdam.de>
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.cs.uni-potsdam.de/~smeier/kdevelop/
Requires:	kdevelop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDevelop is an easy to use IDE (Intergrated Development Enviroment)
for KDE/Unix/X11. At the moment there are only unstable
alpha-versions.

This package provides a C (v1.08) and C++ (0.1) reference from within
kdevelop, as written by Martin Leslie. The original files have been
rearranged to meet our needs.

%description -l pl.UTF-8
KDevelop jest prostym w użyciu IDE (zintegrownym środowiskiem
programistycznym) dla KDE/Unix/X11.

Ten pakiet dostarcza dokumentację C (w wersji 1.08) oraz C++ (0.1) do
używania z kdevelopem, napisaną przez Martina Leslie. Oryginalne pliki
zostały dostosowane do użytku z kdevelopem.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
./mkinstalldirs $RPM_BUILD_ROOT%{_prefix}
cp -R * $RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/HTML/en/kdevelop/*
