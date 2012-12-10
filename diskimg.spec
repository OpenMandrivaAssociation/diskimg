%define name diskimg 
%define version 1.1.1
%define release %mkrel 9

Summary: A tools to make disks/partitions image
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar.bz2
License: GPL
Group: Archiving/Backup
Url: http://www.scylla-charybdis.com/tools.html#diskimg
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
DiskImg is a small command-line utility that dumps the contents
of a drive or partition to standard out. Because it is based on 
large file support, it is able to skip over read errors and log
them to a log file. It can start reading at an offset and writes
its progress to stderr.

%prep
%setup -q

%build
%make "CFLAGS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -s -D %name %buildroot/%_bindir/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc VERSION README
%_bindir/%name



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-9mdv2011.0
+ Revision: 617787
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-8mdv2010.0
+ Revision: 428278
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-7mdv2009.0
+ Revision: 244339
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1.1-5mdv2008.1
+ Revision: 136365
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 1.1.1-5mdv2008.0
+ Revision: 68457
- rebuild


* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 13:26:34 (53252)
- rebuild

* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 13:20:45 (53251)
Import diskimg

* Sat Dec 31 2005 Olivier Thauvin <nanardon@mandriva.org> 1.1.1-3mdk
- Rebuild && %%mkrel

* Fri Dec 24 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.1-2mdk
- Birthday rebuild && Merry Xmas, especially for my Queen

* Tue Oct 28 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.1-1mdk
- 1.1.1

* Thu Oct 23 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0.1-1mdk
- 1st mdk spec

