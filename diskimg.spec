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

