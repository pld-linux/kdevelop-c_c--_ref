%define name kdevelop-c_c++_ref
%define version 0.1
%define release 1
%define prefix /opt/kde

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: KDevelop-specific C and C++ reference HTML files
Name: %{name}
Version: %{version}
Release: %{release}
Group: X11/KDE/Development
Copyright: GPL
Vendor: Sandy Meier <smeier@rz.uni-potsdam.de>
Packager: Troy Engel <tengel@sonic.net>
Source: %{name}-%{version}.tar.gz
URL: http://www.cs.uni-potsdam.de/~smeier/kdevelop/
Requires: kdevelop
BuildRoot: /tmp/build-%{name}-%{version}

%description
KDevelop is an easy to use IDE (Intergrated Development Enviroment) for
KDE/Unix/X11. At the moment there are only unstable alpha-versions.

This package provides a C (v1.08) and C++ (0.1) reference from within
kdevelop, as written by Martin Leslie. The original files have been
rearranged to meet our needs.

%prep
%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
./mkinstalldirs $RPM_BUILD_ROOT%{prefix}
cp -R * $RPM_BUILD_ROOT%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%defattr(-,root,root)
%{prefix}/share/doc/HTML/en/kdevelop/*
