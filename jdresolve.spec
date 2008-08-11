%define name    jdresolve
%define	version	0.6.1
%define release 1
%define prefix  /usr

Summary: jdresolve resolves IP addresses into hostnames 

Name: %{name}
Version: %{version}
Release: %{release}

Copyright: GPL
Group: Development/Languages
Source: http://www.jdrowell.com/files/%{name}-%{version}.tar.gz
Url: http://www.jdrowell.com/Linux/Projects/jdresolve
Packager: John D. Rowell <me@jdrowell.com>

BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: perl >= 5.004, perl-Net-DNS >= 0.12

%description

%changelog
* Wed Jun 28 2000 John D. Rowell <me@jdrowell.com>
- version 0.6.1
- Fixed "oops" assertion bug
- Improved performance
- New "-p"/"--progress" option

* Sat Jun 17 2000 John D. Rowell <me@jdrowell.com>
- version 0.6.0
- Improved performance (lines/s)
- Better line caching algorithm
- Reduced memory footprint
- The code is now fully commented
- A new ./configure script (locates Perl, Net::DNS, etc)
  ...more... (see CHANGELOG)

* Thu Aug 26 1999 John D. Rowell <me@jdrowell.com>
- version 0.5.2
- fixed memory leak when the --database option was not in use
- fixed warning messages when the --recursive option was not in use

* Mon Aug 16 1999 John D. Rowell <me@jdrowell.com>
- version 0.5.1
- fixed warning messages on FreeBSD
- added jdresolve-mergedb and jdresolve-unresolved utils

* Wed Jul 27 1999 John D. Rowell <me@jdrowell.com>
- version 0.5
- Added database support (--database and jdresolve-dumpdb)

* Wed Jul 14 1999 John D. Rowell <me@jdrowell.com>
- First build (v0.4).

%ifarch noarch

%prep

%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG  COPYING  CREDITS  INSTALL  README  TODO
/usr/bin/jdresolve
/usr/bin/rhost
/usr/man/man1/jdresolve.1.gz
/usr/man/man1/rhost.1.gz

%endif

