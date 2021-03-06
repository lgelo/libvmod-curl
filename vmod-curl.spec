Summary: CURL support for Varnish VCL
Name: vmod-curl
Version: 0.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0: libvmod-curl.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish >= 4.0
BuildRequires: make, python-docutils, curl-devel > 7.19.0

%description
CURL support for Varnish VCL

%prep
%setup -n libvmod-curl

%build
./configure --prefix=/usr/ --docdir='${datarootdir}/doc/%{name}'
make
make check

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnis*/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Tue Nov 14 2012 Lasse Karstensen <lasse@varnish-software.com> - 0.1-0.20121114
- Initial version.
