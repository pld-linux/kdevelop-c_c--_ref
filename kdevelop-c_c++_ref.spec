Summary:	KDevelop-specific C and C++ reference HTML files
Name:		kdevelop-c_c++_ref
Version:	0.1
Release:	1
Copyright:	GPL
Group:		X11/KDE/Development
Vendor:		Sandy Meier <smeier@rz.uni-potsdam.de>
Source:		%{name}-%{version}.tar.gz
URL:		http://www.cs.uni-potsdam.de/~smeier/kdevelop/
Requires:	kdevelop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDevelop is an easy to use IDE (Intergrated Development Enviroment) for
KDE/Unix/X11. At the moment there are only unstable alpha-versions.

This package provides a C (v1.08) and C++ (0.1) reference from within
kdevelop, as written by Martin Leslie. The original files have been
rearranged to meet our needs.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
./mkinstalldirs $RPM_BUILD_ROOT%{prefix}
cp -R * $RPM_BUILD_ROOT%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/share/doc/HTML/en/kdevelop/*
